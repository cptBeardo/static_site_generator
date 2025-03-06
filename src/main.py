import sys
import os
import posixpath
from textnode import TextNode, TextType

"""navigate to ../public and run python3 -m http.server 8888"""

#  print("# hello world")  # only used to test that ./main.sh was working properly
root_directory = os.path.abspath("../")
public_directory = os.path.join(root_directory,"public")
static_directory = os.path.join(root_directory, "static")
static_image_directory = os.path.join(static_directory, "images")

def create_dir(directory: str):
    target_directory = os.path.exists(directory)
    if not target_directory:
        os.mkdir(directory)

def empty_dir(directory: str):
    target_directory = os.path.exists(directory)
    if not target_directory:
        create_dir(directory)
    else:
        pass

def main():
    # original code to test main.py works: node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # original code to test main.py works: print(node, flush=True)  # use flush=True to have result printed immediately (must import sys)




if __name__ == "__main__":
    main()
