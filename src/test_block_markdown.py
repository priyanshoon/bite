import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_markdown_to_blocks(self):
        md = """"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )

    def test_markdown_to_blocks_with_multiple_newline(self):
        md = """


This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items




>something"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                ">something",
            ],
        )

    def test_block_to_block_type_paragraph(self):
        paragraph = "this is paragraph"
        block_type_paragraph = block_to_block_type(paragraph)
        self.assertEqual(block_type_paragraph, BlockType.PARAGRAPH)

    def test_block_to_block_type_headings(self):

        headings = [
                "# this is heading",
                "## this is heading",
                "### this is heading",
                "#### this is heading",
                "##### this is heading",
                "###### this is heading",
                ]

        for heading in headings:
            with self.subTest(heading=heading):
                self.assertEqual(block_to_block_type(heading), BlockType.HEADING)


    def test_block_to_block_type_code(self):
        code = """```
this is code
```"""
        block_type_code = block_to_block_type(code)
        self.assertEqual(block_type_code, BlockType.CODE)

    def test_block_to_block_type_code_empty(self):
        code = "```\n```"
        block_type_code = block_to_block_type(code)
        self.assertEqual(block_type_code, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        quote = """>still\n>quoted"""
        block_type_quote = block_to_block_type(quote)
        self.assertEqual(block_type_quote, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        unordered_list = """- something
- something else
- something way too big"""
        block_type_unordered_list = block_to_block_type(unordered_list)
        self.assertEqual(block_type_unordered_list, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        ordered_list = """1. Hello
2. World
3. Robot"""

        block_type_ordered_list = block_to_block_type(ordered_list)
        self.assertEqual(block_type_ordered_list, BlockType.ORDERED_LIST)
