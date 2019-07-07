
from dominate.svg import svg, animate, animateMotion, mpath, animateTransform, polygon, circle
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


def test_animate():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <animate attributeName="x" attributeType="XML" dur="10s" from="-100" repeatCount="indefinate" to="120">
        </animate>
    </svg>"""
    with base() as result:
        animate(attributeType="XML", attributeName="x", _from="-100", to="120", dur="10s", repeatCount="indefinate")
    assert html_equals(result.render(), expected)


def test_animate_motion():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <animateMotion dur="6s" repeatCount="indefinate">
            <mpath xlink:href="#theMotionPath"></mpath>
        </animateMotion>
    </svg>
    """

    with base() as result:
        with animateMotion(dur="6s", repeatCount="indefinate"):
            mpath(xlink_href="#theMotionPath")

    assert html_equals(result.render(), expected)


def test_animate_transform():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <polygon points="60,30 90,90, 30,90">
        <animateTransform attibuteName="transform" attributeType="XML" dur="10s" from="0, 60, 70" repeatCount="indefinate" to="360 60 70" type="rotate">
      </polygon>
    </svg>
    """
    with base() as result:
        with polygon(points="60,30 90,90, 30,90"):
            animateTransform(attibuteName="transform", attributeType="XML", type="rotate", _from="0, 60, 70",
                             to="360 60 70", dur="10s", repeatCount="indefinate")

    assert html_equals(result.render(), expected)


def test_circle():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <circle cx="50" cy="50" r="50">
    </svg>
    """
    with base() as result:
        circle(cx = "50", cy = "50", r = "50")
    assert html_equals(result.render(), expected)

