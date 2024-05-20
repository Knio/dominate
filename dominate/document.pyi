from typing import Any, Literal
from dominate.tags import html, head, body
from dominate.dom_tag import dom_tag
from dominate.util import container

class document(html):
    head: head
    body: body
    doctype: str
    header: container
    main: container
    footer: container

    def __init__(
        self,
        title: str = ...,
        doctype: str = ...,
        *a: dom_tag | str,
        __inline: bool = ...,
        __pretty: bool = ...,
        **kw: str | Literal[True],
    ) -> None: ...
