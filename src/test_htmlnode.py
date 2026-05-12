import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_a_children(self):
        child_a = LeafNode(
            "a", "Click me!", {"href": "https://priyanshoon.me/", "target": "_blank"}
        )
        parent_node = ParentNode("div", [child_a])
        self.assertEqual(
            parent_node.to_html(),
            '<div><a href="https://priyanshoon.me/" target="_blank">Click me!</a></div>',
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
