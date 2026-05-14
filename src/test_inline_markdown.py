import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_text_with_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        equals = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, equals)

    def test_split_text_with_multiple_code_delimiter(self):
        node = TextNode("This `code` is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        equals = [
            TextNode("This ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, equals)

    def test_non_closing_delimiter(self):
        node = TextNode("This is `code but fuck off", TextType.TEXT)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(str(context.exception), "delimiter not closed")

    def test_empty_delimiter(self):
        node = TextNode("text is **** something", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        equals = [
            TextNode("text is ", TextType.TEXT),
            TextNode(" something", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, equals)

    def test_start_with_delimiter(self):
        node = TextNode("**bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        equals = [TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)]

        self.assertEqual(new_nodes, equals)

    def test_ignore_non_text_nodes(self):
        node = TextNode("`someone`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        equals = [
            TextNode("`someone`", TextType.CODE),
        ]

        self.assertEqual(new_nodes, equals)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is the text with an [link](https://priyanshoon.me/)"
        )

        self.assertEqual([("link", "https://priyanshoon.me/")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "![cat](https://cat.com/img.png) and ![dog](https://dog.com/img.jpg)"
        )
        self.assertListEqual(
            [("cat", "https://cat.com/img.png"), ("dog", "https://dog.com/img.jpg")],
            matches,
        )

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "[google](https://google.com) and [github](https://github.com)"
        )
        self.assertEqual(
            [("google", "https://google.com"), ("github", "https://github.com")],
            matches,
        )
