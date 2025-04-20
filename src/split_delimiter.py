from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # if a node is not TEXT, we add it to the new list
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Look for a delimiters pair
        text = old_node.text
        if delimiter not in text:
            new_nodes.append(old_node)
            continue

        start_index = text.find(delimiter)
        end_index = text.find(delimiter, start_index + len(delimiter))

        if end_index == -1:
            # Raise an exception if there is no closing delimiter
            raise ValueError(f"Non closing delimiter found for {delimiter}")
        
        # Split into three parts
        before_text  = text[:start_index]
        delimited_text = text[start_index + len(delimiter):end_index]
        after_text = text[end_index + len(delimiter):]

        # Create new nodes
        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
        new_nodes.append(TextNode(delimited_text, text_type))
        if after_text:
            temp_node = TextNode(after_text, TextType.TEXT)
            new_nodes.extend(split_nodes_delimiter([temp_node], delimiter, text_type))

    print(new_nodes)
    return new_nodes


# nodes = [TextNode("I am a **grassetto** text and I am _italic_ text.", TextType.TEXT)]
# split_nodes_delimiter(nodes, '**', TextType.BOLD)
