from asyncio import create_task, gather, run, Semaphore
from textwrap import dedent

from dominate import tags
from dominate.dom_tag import async_context_id


def test_child_task_does_not_inherit_parent_dom_context():
    async def build_child():
        with tags.div(id='child') as child:
            tags.span('child content')
        return str(child)

    async def build_parent():
        with tags.div(id='parent') as parent:
            child = await create_task(build_child())
        return str(parent), child

    token = async_context_id.set(None)
    try:
        parent, child = run(build_parent())
    finally:
        async_context_id.reset(token)

    assert parent == '<div id="parent"></div>'
    assert child == '<div id="child"><span>child content</span></div>'


# To simulate sleep without making the tests take a hella long time to complete
# lets use a pair of semaphores to explicitly control when our coroutines run.
# The order of execution will be marked as comments below:
def test_async_bleed():
    async def tag_routine_1(sem_1, sem_2):
        root = tags.div(id = 1) # [1]
        with root: # [2]
            sem_2.release() # [3]
            await sem_1.acquire() # [4]
            tags.div(id = 2) # [11]
        return str(root) # [12]

    async def tag_routine_2(sem_1, sem_2):
        await sem_2.acquire() # [5]
        root = tags.div(id = 3) # [6]
        with root: # [7]
            tags.div(id = 4) # [8]
        sem_1.release() # [9]
        return str(root) # [10]

    async def merge():
        sem_1 = Semaphore(0)
        sem_2 = Semaphore(0)
        return await gather(
            tag_routine_1(sem_1, sem_2),
            tag_routine_2(sem_1, sem_2)
        )

    # An ID initialized by a parent task is copied into each child's context.
    # Task identity must still keep the two DOM contexts independent.
    async_context_id.set(0)
    tag_1, tag_2 = run(merge())

    assert tag_1 == dedent("""\
        <div id="1">
          <div id="2"></div>
        </div>
    """).strip()

    assert tag_2 == dedent("""\
        <div id="3">
          <div id="4"></div>
        </div>
    """).strip()

    # Also verify tasks starting with an uninitialized context.
    async_context_id.set(None)
    tag_1, tag_2 = run(merge())

    # Ah, much better...
    assert tag_1 == dedent("""\
        <div id="1">
          <div id="2"></div>
        </div>
    """).strip()

    assert tag_2 == dedent("""\
        <div id="3">
          <div id="4"></div>
        </div>
    """).strip()
