from dominate.tags import *
from dominate.svg import *
from htmldiffer import utils as diff_utils
import pytest
from dominate import svg as m_svg


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
      <path d="M10,110 A120,120 -45 0,1 110 10 A120,120 -45 0,1 10,110" fill="none" id="theMotionPath" stroke="lightgrey" stroke-width="2"></path>
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
        circle(cx=10, cy=110, r=3, fill="lightgrey")
        circle(cx=110, cy=10, r=3, fill="lightgrey")
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
        with circle(cx=50, cy=60, r=30, fill="black"):
            desc("I am a circle")
    assert html_equals(result.render(), expected)


def test_clip_path():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <clipPath id="MyClip">
        <circle cx="20" cy="30" r="40"></circle>
      </clipPath>
      <path d="M10,30 A20,20,0,0,1,50,30 A20,20,0,0,1,90,30 Q90,60,50,90 Q10,60,10,30 Z" id="heart"></path>
      <use clip-path="url(#MyClip)" fill="red" xlink:href="#heart"></use>
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
            circle(cx=50, cy=60, r=30, fill="black")
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


filter_names = ['feBlend', 'feColorMatrix', 'feComponentTransfer', 'feComposite', 'feConvolveMatrix', 'feDiffuseLighting',
           'feDisplacementMap', 'feFlood', 'feGaussianBlur', 'feImage', 'feMerge', 'feMorphology', 'feOffset',
           'feSpecularLighting', 'feTile', 'feTurbulence', 'feDistantLight', 'fePointLight', 'feSpotLight']


def test_filters():
    for name in filter_names:
        attr = getattr(m_svg, name)
        with filter() as f:
            attr()
        expected = """
        <filter>
            <{}></{}>
        </filter>
        """.format(name, name)
        assert html_equals(f.render(), expected)

def test_g():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <g fill="white" stroke="green" stroke-width="5">
        <circle r="25" rx="40" ry="40"></circle>
        <circle r="25" rx="60" ry="60"></circle>
      </g>
    </svg>
    """
    with base() as result:
        with g(fill="white", stroke="green", stroke_width="5"):
            circle(rx=40, ry=40, r=25)
            circle(rx=60, ry=60, r=25)

    assert html_equals(result.render(), expected)


def test_line():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <line stroke="red" x0="0" x1="50" y0="0" y1="50"></line>
    </svg>
    """
    with base() as result:
        line(x0='0', x1='50', y0='0', y1='50', stroke='red')
    assert html_equals(result.render(), expected)


def test_linear_gradient():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <linearGradient gradientTransform="rotate(90)" id="myGradient">
          <stop offset="5%" stop-color="gold"></stop>
          <stop offset="95%" stop-color="red"></stop>
        </linearGradient>
      </defs>
      <circle fill="url('#myGradient')" r="40" rx="50" ry="50"></circle>
    </svg>
    """
    with base() as result:
        with defs():
            with linearGradient(id="myGradient", gradientTransform="rotate(90)"):
                stop(offset="5%", stop_color="gold")
                stop(offset="95%", stop_color="red")

        circle(rx=50, ry=50, r=40, fill="url('#myGradient')")

    assert html_equals(result.render(), expected)


def test_marker():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <marker id="arrow" markerHeight="6" markerWidth="6" orient="auto-start-reverse" refX="5" refY="5" viewBox="0 0 10 10">
          <path d="M 0 0 L 10 5 L 0 10 z"></path>
        </marker>
      </defs>
      <polyline fill="none" marker-end="url(#arrow)" marker-start="url(#arrow)" points="10,10 10,90 90,90" stroke="black"></polyline>
    </svg>"""
    with base() as result:
        with defs():
            with marker(id="arrow", viewBox="0 0 10 10", refX="5", refY="5",
                        markerWidth="6", markerHeight="6", orient="auto-start-reverse"):
                path(d="M 0 0 L 10 5 L 0 10 z")

        polyline(points="10,10 10,90 90,90", fill="none", stroke="black", marker_start="url(#arrow)",
                      marker_end="url(#arrow)" )

    assert html_equals(result.render(), expected)


def test_mask():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <mask id="myMask">
            <rect fill="white" height="100" width="100" x="0" y="0"></rect>
            <path d="M10,35 A20,20,0,0,1,50,35 A20,20,0,0,1,90,35 Q90,65,50,95 Q10,65,10,35 Z" fill="black"></path>
        </mask>
    <polygon fill="orange" points="-10,110 110,110 110,-10"></polygon>
    <circle cx="50" cy="50" mask="url(#myMask)" r="50"></circle>
    </svg>"""
    with base() as result:
        with mask(id="myMask"):
            rect(x="0", y="0", width="100", height="100", fill="white")
            path(d="M10,35 A20,20,0,0,1,50,35 A20,20,0,0,1,90,35 Q90,65,50,95 Q10,65,10,35 Z", fill="black" )
        polygon(points="-10,110 110,110 110,-10", fill="orange")
        circle(cx=50, cy=50, r=50, mask="url(#myMask)")
    assert html_equals(result.render(), expected)


def test_pattern():
    expected = """
    <svg viewBox="0 0 230 100">
      <defs>
        <pattern height="10%" id="star" viewBox="0 0 10 10" width="10%">
          <polygon points="0,0 2,5 0,10 5,8 10,10 8,5 10,0 5,2"></polygon>
        </pattern>
      </defs>
      <circle cx="50" cy="50" fill="url(#star)" r="50"></circle>
      <circle cx="180" cy="50" fill="none" r="50" stroke="url(#star)" stroke-width="20"></circle>
    </svg>
    """
    with svg(viewBox="0 0 230 100") as result:
        with defs():
            with pattern(id="star", viewBox="0 0 10 10", width="10%", height="10%"):
                polygon(points="0,0 2,5 0,10 5,8 10,10 8,5 10,0 5,2")
        circle(cx=50, cy=50, r=50, fill="url(#star)")
        circle(cx=180, cy=50, r=50, fill="none", stroke_width=20, stroke="url(#star)")
    assert html_equals(result.render(), expected)


def test_radial_gradient():
    expected = """
    <svg height="120" version="1.1" viewBox="0 0 120 120" width="120" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <radialGradient id="myGradient">
          <stop offset="10%" stop-color="gold"></stop>
          <stop offset="95%" stop-color="red"></stop>
        </radialGradient>
      </defs>
      <circle cx="50" cy="5" fill="url(#myGradient)" r="50"></circle>
    </svg>
    """
    with base() as result:
        with defs():
            with radialGradient(id="myGradient"):
                stop(offset="10%", stop_color="gold")
                stop(offset="95%", stop_color="red")
        circle(cx=50, cy=5, r=50, fill="url(#myGradient)")
    assert html_equals(result.render(), expected)






