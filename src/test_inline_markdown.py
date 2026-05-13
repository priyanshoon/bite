import unittest

from inline_markdown import split_nodes_delimiter
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

    def test_ignore_non_text_nodes(self):
        node = TextNode("`someone`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        equals = [
                TextNode("`someone`", TextType.CODE),
        ]

        self.assertEqual(new_nodes, equals)


