def markdown_to_blocks(markdown):
    if len(markdown) == 0:
        return []
    
    blocks = markdown.split("\n\n")
    
    result = []
    for block in blocks:
        block_strip = block.strip()

        if len(block_strip) != 0:
            result.append(block_strip)

    return result
