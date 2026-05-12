import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is node one", TextType.TEXT)
        node2 = TextNode("This is node two", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is the url", TextType.ITALIC, "https://priyanshoon")
        self.assertEqual(first="https://priyanshoon", second=node.url)

    def test_urlNone(self):
        node = TextNode("the url is none", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_text_type(self):
        node = TextNode("This is the bold type", TextType.ITALIC, None)
        self.assertEqual(first=TextType.ITALIC, second=node.text_type)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("click me", TextType.LINK, "https://priyanshoon.me/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://priyanshoon.me/"})

    def test_image(self):
        node = TextNode("bhalu", TextType.IMAGE, "./bhalu.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "./bhalu.png", "alt": "bhalu"})


if __name__ == "__main__":
    unittest.main()
