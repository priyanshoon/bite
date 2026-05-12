import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
