from glob import glob
import html5lib


def test_html5():
    parser = html5lib.HTMLParser(strict=True)
    for page in glob('public/*.htm'):
        with open(page, "rb") as f:
            parser.parse(f)
