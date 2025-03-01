from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        if delimiter not in text:
            new_nodes.append(old_node)
            continue
        
        # use helper funciton to find delimiter indices
        start_index, end_index = find_delimiter_indices(text, delimiter)
        
        before_text = text[:start_index]
        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))

        between_text = text[start_index + len(delimiter):end_index]
        new_nodes.append(TextNode(between_text, text_type))

        after_text = text[end_index + len(delimiter):]
        if after_text:
            new_nodes.append(TextNode(after_text, TextType.TEXT))
        
    
    return new_nodes


def find_delimiter_indices(text, delimiter):
    """
    Find the indices of the first pair of delimiters in the text.
    Returns (start_index, end_index) or raises an exception if no pair is found.
    """

    start_index = text.find(delimiter)
    if start_index == -1:
        return None, None  # no starting delimiter found

    end_index = text.find(delimiter, start_index + len(delimiter))
    if end_index == -1:
        raise Exception(f"No closing delimiter found for {delimiter}")

    return start_index, end_index