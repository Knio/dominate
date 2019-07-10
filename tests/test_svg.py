from dominate.tags import *
from dominate.svg import *
from htmldiffer import utils as diff_utils
import pytest


def html_equals(html1, html2):
    lines1 = [line.strip() for line in diff_utils.html2list(html1)]
    lines1 = [line for line in lines1 if len(line) > 0]
    lines2 = [line.strip() for line in diff_utils.html2list(html2)]
    lines2 = [line for line in lines2 if len(line) > 0]
    diffs = [(line[0], line[1]) for line in zip(lines1, lines2) if line[0] != line[1]]
    return lines1 == lines2

def base():
    return svg(width=120, height=120, viewBox="0 0 120 120", version="1.1",
              xmlns="http://www.w3.org/2000/svg", xmlns_xlink="http://www.w3.org/1999/xlink")


def make_circle(cx: int = 50, cy: int=60, r: int=30, fill: str = "black"):
    return circle(cx=str(cx), cy=str(cy), r=str(r), fill=fill)


# Note, all tests produce working examples. The expected results can be pasted into https://jsfiddle.net/api/mdn/


def test_animate():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <rect height="100" width="100" x="10" y="10">
        <animate attributeName="x" attributeType="XML" dur="10s" from="-100" repeatCount="indefinite" to="120"></animate>
      </rect>
    </svg>
    """
    with base() as result:
        with rect(x="10", y="10", width="100", height="100"):
            animate(attributeType="XML", attributeName="x", _from="-100", to="120", dur="10s", repeatCount="indefinite")

    assert html_equals(result.render(), expected)


def test_animate_motion():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <path d="M10,110 A120,120 -45 0,1 110 10 A120,120 -45 0,1 10,110" fill="none" id="theMotionPath" stroke="lightgrey" stroke_width="2"></path>
      <circle cx="10" cy="110" fill="lightgrey" r="3"></circle>
      <circle cx="110" cy="10" fill="lightgrey" r="3"></circle>
      <circle cx="" cy="" fill="red" r="5">
        <animateMotion dur="6s" repeatCount="indefinite">
          <mpath xlink:href="#theMotionPath"></mpath>
        </animateMotion>
      </circle>
    </svg>
    """
    with base() as result:
        path(d="M10,110 A120,120 -45 0,1 110 10 A120,120 -45 0,1 10,110", stroke="lightgrey", stroke_width="2",
             fill="none", id="theMotionPath")
        make_circle(10, 110, 3, fill="lightgrey")
        make_circle(110, 10, 3, "lightgrey")
        with circle(cx="", cy="", r="5", fill="red"):
            with animateMotion(dur="6s", repeatCount="indefinite"):
                mpath(xlink_href="#theMotionPath")
    assert html_equals(result.render(), expected)


def test_animate_transform():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <polygon points="60,30 90,90, 30,90">
        <animateTransform attributeName="transform" attributeType="XML" dur="10s" from="0 60 70" repeatCount="indefinite" to="360 60 70" type="rotate">
      </polygon>
    </svg>
    """
    with base() as result:
        with polygon(points="60,30 90,90, 30,90"):
            animateTransform(attributeName="transform", attributeType="XML", type="rotate", _from="0 60 70",
                             to="360 60 70", dur="10s", repeatCount="indefinite")

    assert html_equals(result.render(), expected)


def test_circle():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <circle cx="50" cy="60" fill="black" r="30">
        <desc>I am a circle</desc>
      </circle>
    </svg>        
    """
    with base() as result:
        with make_circle():
            desc("I am a circle")
    assert html_equals(result.render(), expected)


def test_clip_path():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <clipPath id="MyClip">
        <circle cx="20" cy="30" r="40"></circle>
      </clipPath>
      <path d="M10,30 A20,20,0,0,1,50,30 A20,20,0,0,1,90,30 Q90,60,50,90 Q10,60,10,30 Z" id="heart"></path>
      <use clip_path="url(#MyClip)" fill="red" xlink:href="#heart"></use>
    </svg>
    """
    with base() as result:
        with clipPath(id="MyClip"):
            circle(cx="20", cy="30", r="40")
        path(id="heart", d="M10,30 A20,20,0,0,1,50,30 A20,20,0,0,1,90,30 Q90,60,50,90 Q10,60,10,30 Z")
        use(clip_path="url(#MyClip)", xlink_href="#heart", fill="red")

    assert html_equals(result.render(), expected)


def test_defs():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <circle cx="50" cy="60" fill="black" r="30"></circle>
      </defs>
      <use x="5" xlink:href="#myCircle" y="5"></use>
    </svg>
    """
    with base() as result:
        with defs():
            make_circle()
        use(x="5", y="5", xlink_href="#myCircle")
    assert html_equals(result.render(), expected)


def test_ellipse():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <ellipse cx="100" cy="50" rx="100" ry="50"></ellipse>
    </svg>
    """
    with base() as result:
        ellipse(cx="100", cy="50", rx="100", ry="50" )
    assert html_equals(result.render(), expected)



