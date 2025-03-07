import os
import shutil
from textnode import TextNode, TextType
from markdownblock import markdown_to_blocks, markdown_to_html_node

"""navigate to ../public and run python3 -m http.server 8888"""

script_dir = os.path.dirname(os.path.abspath(__file__))
root_directory = os.path.dirname(script_dir)
#root_directory = os.path.abspath("./")
public_directory = os.path.join(root_directory,"public")
static_directory = os.path.join(root_directory, "static")
static_image_directory = os.path.join(static_directory, "images")

class SiteGenerator:
    def __init__(self, output_directory):
        self.output_directory = output_directory

    def generate_page(self, from_path, template_path, dest_path):
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")
        with open(from_path, 'r') as md_file:
            md_content = md_file.read()
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
        html_string = markdown_to_html_node(md_content).to_html()
        doc_title = extract_title(md_content)
        new_html_content = template_content.replace("{{ Title }}", doc_title)
        new_html_content = new_html_content.replace("{{ Content }}", html_string)
        with open(dest_path, 'w') as dest_file:
            dest_file.write(new_html_content)
        with open(dest_path, 'r') as dest_file:
            if new_html_content != dest_file.read():
                raise Exception(f"Content mismatch in {dest_path}")

    def create_dest_path(self, directory, file_name):
        dest_path = os.path.join(directory, file_name)
        create_dir(directory)
        return dest_path

"""end of SiteGenerator Class"""

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

def extract_title(markdown):
    h1_blocks = list(filter(lambda block: block.startswith("# "), markdown_to_blocks(markdown)))
    if not h1_blocks:
        raise Exception("No h1 header found in markdown")
    return h1_blocks[0][2:].strip()

"""don't write functions below this main() function"""
def main(from_path, template_path, dest_path):

    empty_dir(public_directory)

    copy_static(static_directory, public_directory)

    site_generator = SiteGenerator(public_directory)

    site_generator.generate_page(
        os.path.join(root_directory, from_path),
        os.path.join(root_directory, template_path),
        os.path.join(root_directory, dest_path)
    )
 
if __name__ == "__main__":
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    main(from_path, template_path, dest_path)
