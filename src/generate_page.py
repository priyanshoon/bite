from block_markdown import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            title = block[1:].strip()
            return title

    raise Exception("No title")
