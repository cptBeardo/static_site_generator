import os
import re
import posixpath

from htmlnode import *
from textnode import *
from splitnode import *
from main import *

# Sanity Check 1: Default attributes
# DEBUGGING: node1 = HTMLNode()  # Everything should default
# DEBUGGING: print(node1)

# Sanity Check 2: With attributes
# DEBUGGING: node2 = HTMLNode(tag="div", value="Hello", children=[HTMLNode(tag="span")], props={"class": "test"})
# DEBUGGING: print(node2)
# DEBUGGING: print(node2.props_to_html())

# Sanity Check 3: Just props
# DEBUGGING: node3 = HTMLNode(props={"id": "unique"})
# DEBUGGING: print(node3.props_to_html())

# Sanity Check 4: no children left in LeafNode
# DEBUGGING: node4 = LeafNode(tag="span", value="example text")
# DEBUGGING: print(node4)

# DEBUGGING:node5 = ParentNode(
# DEBUGGING:    "p",
# DEBUGGING:    [
# DEBUGGING:        LeafNode("b", "Bold Text"),
# DEBUGGING:        LeafNode(None, "Normal text"),
# DEBUGGING:        LeafNode("i", "italic text"),
# DEBUGGING:        LeafNode(None, "Normal text"),
# DEBUGGING:    ],
# DEBUGGING:)
# DEBUGGING:print(node5.to_html())  # Circle back to this

# DEBUGGING: leaf = LeafNode("b", "Bold Text")
# DEBUGGING: print(leaf.to_html())  # Should print: <b>Bold Text</b>

# DEBUGGING: node6 = split_nodes_delimiter(["This is **bold** text"], "**", TextType.TEXT)
# DEBUGGING: print(split_nodes_delimiter.new_nodes)

# Create a sample old_nodes list
# DEBUGGING: old_nodes = [
# DEBUGGING:     TextNode("This is text with a **bold word** in it", TextType.TEXT),
# DEBUGGING:     TextNode("This is already bold", TextType.BOLD)
# DEBUGGING: ]

# Print out the old_nodes to see their structure
# DEBUGGING: print("Old Nodes:")
# DEBUGGING: for node in old_nodes:
# DEBUGGING:     print(f"Text: '{node.text}', Type: {node.text_type}")

# Let's imagine how split_nodes_delimiter would work with "**" delimiter
# DEBUGGING: print("\nIf we split with '**' delimiter for BOLD type, we would get:")
# DEBUGGING: print("1. TextNode('This is text with a ', TEXT)")
# DEBUGGING: print("2. TextNode('bold word', BOLD)")
# DEBUGGING: print("3. TextNode(' in it', TEXT)")
# DEBUGGING: print("4. TextNode('This is already bold', BOLD) - unchanged because it's not TEXT type")

# DEBUGGING: test = "This is my website [Cameron Sager Music](https://cmmusic.com), and this is my reference [john smith](http://johnsmithmusic.com)"
# DEBUGGING: matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", test)
# DEBUGGING: print(matches)
# DEBUGGING: print(len(matches[1][0]))
# DEBUGGING: for match in matches:
# DEBUGGING:     for item in match:
# DEBUGGING:         print(len(item), test.find(item) - 1)

# DEBUGGING: test2 = "This is the image I want to use ![Empty Image](https://../static_site_generator/srd/empty_image.jpg)"
# DEBUGGING: new_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", test2)
# DEBUGGING: print(new_matches)
# DEBUGGING: print(len(new_matches[0][0]))

# TESTING posixpath commands: print(os.path.abspath("sandbox.py"))
# TESTING posixpath commands: print(os.path.basename("/home/cmsager/workspace/github.com/cptBeardo/static_site_generator/src/sandbox.py"))
# TESTING posixpath commands: print(os.path.abspath("sandbox.py")) # returns full path of file or directory"""
# TESTING posixpath commands: print(os.path.exists("/public/"))
print(os.path.exists("../public/")) # USE THIS ONE
print(os.path.abspath(".")) # USE THIS ONE => Returns the full parent directory path to current file (does NOT return current file itself)
current_directory = os.path.abspath(".")
print(os.path.splitroot(current_directory))
public_directory = os.path.abspath("../public")
print(os.listdir(public_directory))
static_directory = os.path.abspath("../static")
print(os.listdir(static_directory))
static_image_directory = os.path.abspath("../static/images")
print(os.listdir(static_image_directory))
print(if os.path.exists(current_directory))






