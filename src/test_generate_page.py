import unittest
from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        title = "Hello"
        extract = extract_title("# Hello")

        self.assertEqual(title, extract)

    def test_extract_title_with_multiple_lines(self):
        title = "Hello"
        md = """something is not right, right?

# Hello

fucking ninja"""

        extract = extract_title(md)

        self.assertEqual(title, extract)

    def test_extract_title_with_no_title(self):
        title = "something is here but not heading"

        with self.assertRaises(Exception):
            extract_title(title)

    def test_extract_title_on_second_block(self):
        md = """## Not h1

# Yes"""
        
        extract = extract_title(md)
        self.assertEqual("Yes", extract)
