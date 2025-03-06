import sys
import os
import posixpath
import shutil
from textnode import TextNode, TextType

"""navigate to ../public and run python3 -m http.server 8888"""

script_dir = os.path.dirname(os.path.abspath(__file__))
root_directory = os.path.dirname(script_dir)
#root_directory = os.path.abspath("./")
public_directory = os.path.join(root_directory,"public")
static_directory = os.path.join(root_directory, "static")
static_image_directory = os.path.join(static_directory, "images")

def create_dir(directory: str):
    target_directory = os.path.exists(directory)
    if not target_directory:
        os.mkdir(directory)

def empty_dir(directory: str):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    create_dir(directory)

def copy_static(source, destination):
    create_dir(destination)

    items = os.listdir(source)
    for item in items:
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} to {dest_path}")
        else:
            create_dir(dest_path)
            copy_static(source_path, dest_path)
            print(f"Copied directory: {source_path} to {dest_path}")


"""don't write functions below this main() function"""
def main():
    empty_dir(public_directory)

    copy_static(static_directory, public_directory)




if __name__ == "__main__":
    main()
