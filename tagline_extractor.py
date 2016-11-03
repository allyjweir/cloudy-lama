import requests
from bs4 import BeautifulSoup


def _extract_tagline():
    page = requests.get('http://www.theverge.com')
    soup = BeautifulSoup(page.content, 'html.parser')
    taglines = soup.findAll('div', {'class': 'c-masthead__tagline'})
    tagline = taglines[0]
    return _clean_text(tagline)


def _clean_text(tagline):
    return tagline.prettify() \
                  .replace('\n', '') \
                  .lstrip() \
                  .rstrip()


def _is_unique_tagline(filename, new_tagline):
    with open(filename, 'r') as taglines:
        for tagline in taglines:
            if tagline == new_tagline:
                return False
    return True


def _append_saved_taglines(filename, new_tagline):
    with open(filename, 'w') as taglines:
        taglines.write(str(new_tagline))


def check_for_new_tagline(output_file):
    current_tagline = _extract_tagline()
    if _is_unique_tagline(output_file, current_tagline):
        _append_saved_taglines(output_file, current_tagline)
