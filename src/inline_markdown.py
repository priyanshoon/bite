from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        delimiter_split = node.text.split(delimiter)
        if len(delimiter_split) % 2 == 0:
            raise Exception("delimiter not closed")

        for i in range(len(delimiter_split)):
            if delimiter_split[i] == "":
                continue

            if i % 2 == 0:
                node = TextNode(delimiter_split[i], TextType.TEXT)
                result.append(node)
            else:
                node = TextNode(delimiter_split[i], text_type)
                result.append(node)

    return result
