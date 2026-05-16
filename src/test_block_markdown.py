import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
    markdown_to_html_node,
)


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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
