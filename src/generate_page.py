import os
import pathlib

from block_markdown import markdown_to_html_node
from block_markdown import markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            title = block[1:].strip()
            return title

    raise Exception("No title")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path, "r")
    template_file = open(template_path, "r")

    markdown = markdown_file.read()
    template = template_file.read()

    markdown_file.close()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    path = os.path.dirname(dest_path)
    os.makedirs(path, exist_ok=True)

    with open(dest_path, "w") as index:
        index.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        from_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(from_path):
            generate_page(
                from_path,
                template_path,
                pathlib.Path(os.path.join(dest_dir_path, entry)).with_suffix(".html"),
            )
        else:
            generate_pages_recursive(
                from_path, template_path, os.path.join(dest_dir_path, entry)
            )
