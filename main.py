from collections.abc import Iterable
import markdown
import os
from sys import argv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = dict(enumerate(argv))
    input_dir: str = args.get(1, 'test')
    output_dir: str = args.get(2, 'public')
    includes_dir: str = 'includes'

    # header file
    header_file: str = os.path.join(includes_dir, "header.htm")
    footer_file: str = os.path.join(includes_dir, "footer.htm")
    if os.path.exists(header_file):
        header: str = open(header_file, "r").read()
    else:
        header: str = ""
    if os.path.exists(footer_file):
        footer: str = open(footer_file, "r").read()
    else:
        footer: str = ""
    file_list: Iterable = os.listdir(input_dir)
    for element in file_list:
        assert isinstance(element, str)
        md_file = os.path.join(input_dir, element)
        html: str = markdown.markdown(open(md_file, "r").read())
        page = element[0:element.find('.')] + ".htm"
        with open(os.path.join(output_dir, page), "w") as f:
            f.write(header)
            f.write(html)
            f.write(footer)
            f.close()
