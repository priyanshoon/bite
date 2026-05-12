import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode("p", "Some paragraph")
        self.assertEqual("p", node.tag)

    def test_props_to_html(self):
        node = HTMLNode(
            None, None, None, {"href": "https://priyanshoon.me", "target": "_blank"}
        )
        equal = ' href="https://priyanshoon.me" target="_blank"'

        self.assertEqual(node.props_to_html(), equal)

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a", "Click me!", {"href": "https://priyanshoon.me", "target": "_blank"}
        )
        equals_to = '<a href="https://priyanshoon.me" target="_blank">Click me!</a>'

        self.assertEqual(node.to_html(), equals_to)
