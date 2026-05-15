import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        delimiter_split = node.text.split(delimiter)
        if len(delimiter_split) % 2 == 0:
            raise Exception("delimiter not closed")

        for i in range(len(delimiter_split)):
            if delimiter_split[i] == "":
                continue

            if i % 2 == 0:
                node = TextNode(delimiter_split[i], TextType.TEXT)
                result.append(node)
            else:
                node = TextNode(delimiter_split[i], text_type)
                result.append(node)

    return result


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    result = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        extract = extract_markdown_images(old_node.text)
        if len(extract) == 0:
            result.append(old_node)
            continue

        text = old_node.text
        for alt, url in extract:
            image_markdown = f"![{alt}]({url})"

            sections = text.split(image_markdown, 1)

            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))

            result.append(TextNode(alt, TextType.IMAGE, url))

            text = sections[1]

        if text != "":
            result.append(TextNode(text, TextType.TEXT))

    return result


def split_nodes_link(old_nodes):
    result = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        extract = extract_markdown_links(old_node.text)
        if len(extract) == 0:
            result.append(old_node)
            continue

        text = old_node.text
        for link, url in extract:
            image_markdown = f"[{link}]({url})"

            sections = text.split(image_markdown, 1)

            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))

            result.append(TextNode(link, TextType.LINK, url))

            text = sections[1]

        if text != "":
            result.append(TextNode(text, TextType.TEXT))

    return result


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)

    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
