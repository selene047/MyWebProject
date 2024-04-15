from gencontent import generate_page
from textnode import TextNode
import os

# Function to generate pages recursively
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                markdown_path = os.path.join(root, file)
                relative_path = os.path.relpath(markdown_path, dir_path_content)
                output_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
                generate_page(markdown_path, template_path, output_path)

# Update main function to include generating pages recursively
def main():
    # Define paths
    dir_path_content = "content"  # Update the content directory path
    template_path = "template.html"
    dest_dir_path = "public"

    # Generate pages recursively
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)

    # Start a simple web server
    os.system(f"python server.py --dir {dest_dir_path}")

# Run main function
if __name__ == "__main__":
    main()
