import os
import markdown

# Extract title function
def extract_title(markdown_text):
    lines = markdown_text.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("No h1 header found in the markdown file")

# Generate page function
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Extract title
    title = extract_title(markdown_content)

    # Read template file
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Replace placeholders with generated content
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_content)

    # Create necessary directories if they don't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write new HTML to destination file
    with open(dest_path, 'w') as f:
        f.write(template_content)

# Example usage
generate_page("example.md", "template.html", "output/index.html")
