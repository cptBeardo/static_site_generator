import sys
from textnode import TextNode, TextType

"""navigate to ../public and run python3 -m http.server 8888"""

#  print("# hello world")  # only used to test that ./main.sh was working properly

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node, flush=True)  # use flush=True to have result printed immediately (must import sys)

if __name__ == "__main__":
    main()
