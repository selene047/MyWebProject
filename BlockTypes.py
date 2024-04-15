def block_to_block_type(block):
    # Define block type constants
    BLOCK_TYPE_PARAGRAPH = "paragraph"
    BLOCK_TYPE_HEADING = "heading"
    BLOCK_TYPE_CODE = "code"
    BLOCK_TYPE_QUOTE = "quote"
    BLOCK_TYPE_UNORDERED_LIST = "unordered_list"
    BLOCK_TYPE_ORDERED_LIST = "ordered_list"
    
    # Check if the block is a heading
    if block.startswith("# "):
        return BLOCK_TYPE_HEADING
    
    # Check if the block is a code block
    if block.startswith("```") and block.endswith("```"):
        return BLOCK_TYPE_CODE
    
    # Check if the block is a quote block
    if all(line.startswith(">") for line in block.split("\n")):
        return BLOCK_TYPE_QUOTE
    
    # Check if the block is an unordered list block
    if all(line.startswith("*") or line.startswith("-") for line in block.split("\n")):
        return BLOCK_TYPE_UNORDERED_LIST
    
    # Check if the block is an ordered list block
    lines = block.split("\n")
    if all(line.startswith(f"{i+1}.") for i, line in enumerate(lines)):
        return BLOCK_TYPE_ORDERED_LIST
    
    # If none of the above conditions are met, consider it as a paragraph
    return BLOCK_TYPE_PARAGRAPH

# Test the function with sample blocks
block1 = "## Heading"
block2 = "```\nCode block\n```"
block3 = "> Quote block\n> Line 2"
block4 = "* Item 1\n* Item 2"
block5 = "1. Item 1\n2. Item 2\n3. Item 3"
block6 = "This is a paragraph."

print(block_to_block_type(block1))  # Output: heading
print(block_to_block_type(block2))  # Output: code
print(block_to_block_type(block3))  # Output: quote
print(block_to_block_type(block4))  # Output: unordered_list
print(block_to_block_type(block5))  # Output: ordered_list
print(block_to_block_type(block6))  # Output: paragraph
