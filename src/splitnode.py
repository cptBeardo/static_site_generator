import re
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes


"""          Functions for splitting nodes          """
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

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text

        images = extract_markdown_images(text)
        if not images:
            new_nodes.append(old_node)
            continue # don't forget to add the continue

        remaining_text = text

        for alt_text, image_url in images:
            image_pattern = f"![{alt_text}]({image_url})" # don't forget the ! at the beginning of image markdown
            parts = remaining_text.split(image_pattern, 1)

            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url)) # must match what was defined in this for loop (for alt_text, image_url in images:)

            remaining_text = parts[1] if len(parts) > 1 else ""
    
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        # Extract all links with re.finditer to get positions
        
        """The followin commented out block is if I didn't have the extract_markdown_links() function already defined"""
        # ALT METHOD: pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
        # ALT METHOD: matches = list(re.finditer(pattern, old_node.text))

        # ALT METHOD: if not matches:
        # ALT METHOD:     new_nodes.append(old_node)
        # ALT METHOD:     continue
               
        links = extract_markdown_links(text) # Helper function created below
        if not links:
            new_nodes.append(old_node)
            continue

        # Splitting logic here
        remaining_text = text

        for link_text, link_url in links:
            # find position of this link in remaining text
            link_pattern = f"[{link_text}]({link_url})"
            parts = remaining_text.split(link_pattern, 1)

            # Add the text before the link
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # Add the link
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            # Update remaining text
            remaining_text = parts[1] if len(parts) > 1 else ""

        # Add any remaining text after the last link
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

        


"""          Helper Functions for splitting nodes          """

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

def extract_markdown_links(text):
    """    find the [anchor text] and (url) in the text string    """
    links_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links_matches    
    
def extract_markdown_images(text):
    """    find the ![alt text] and (url) in the text string    """
    images_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images_matches

