from htmlnode import HTMLNode, LeafNode

def block_to_html_node(block, block_type):
    if block_type == "heading":
        # Determine the heading level based on the number of '#' characters
        level = block.count("#")
        tag = f"h{level}"
        value = block.replace("#", "").strip()
        return HTMLNode(tag=tag, value=value)
    elif block_type == "code":
        return HTMLNode(tag="pre", children=[LeafNode(tag=None, value=block.strip())])
    elif block_type == "quote":
        return HTMLNode(tag="blockquote", value=block.strip())
    elif block_type == "unordered_list":
        items = [HTMLNode(tag="li", value=item.strip()) for item in block.split("\n")]
        return HTMLNode(tag="ul", children=items)
    elif block_type == "ordered_list":
        items = [HTMLNode(tag="li", value=item.split(".", 1)[1].strip()) for item in block.split("\n")]
        return HTMLNode(tag="ol", children=items)
    else:  # Paragraph block
        return HTMLNode(tag="p", value=block.strip())

def markdown_to_html_node(markdown):
    blocks = markdown.split("\n\n")
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        block_nodes.append(block_node)
    return HTMLNode(tag="div", children=block_nodes)

def block_to_block_type(block):
    if block.startswith("#"):
        return f"heading_{block.count('#')}"
    elif block.startswith("```"):
        return "code"
    elif block.startswith(">"):
        return "quote"
    elif block.startswith("*") or block.startswith("-"):
        return "unordered_list"
    elif block[0].isdigit() and block[1] == ".":
        return "ordered_list"
    else:
        return "paragraph"
    
    # Convert each block into an HTMLNode
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = block_to_html_node(block, block_type)
        block_nodes.append(block_node)
    
    # Create a top-level HTMLNode with a <div> tag and add the block nodes as children
    return HTMLNode(tag="div", children=block_nodes)

# Test the markdown_to_html_node function

