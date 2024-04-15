from textnode import TextNode

import os
import shutil

# Function to recursively copy contents of a directory to another directory
def copy_directory_contents(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            copy_directory_contents(source_path, destination_path)
        else:
            shutil.copy2(source_path, destination_path)

# Update main function to include copying
def main():
    # Define source and destination directories
    source_dir = "static"
    destination_dir = "public"

    # Delete contents of destination directory if it exists
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

    # Copy contents from source to destination directory
    copy_directory_contents(source_dir, destination_dir)

    # Run the test functions
    test_split_nodes_image()
    test_extract_markdown_images()
    print("All tests passed!")


