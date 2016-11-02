from jinja2 import Template


def render_page(taglines_filename):
    with open(taglines_filename, 'r') as f:
        taglines = f.readlines()

    with open('template.html', 'r') as f:
        template_string = f.read()

    template = Template(template_string)
    return template.render(taglines = taglines)
