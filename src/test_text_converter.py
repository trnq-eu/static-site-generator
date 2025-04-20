from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode
from text_converter import text_node_to_html_node
import unittest

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("strong me!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "strong me!")

    def test_italic(self):
        node = TextNode("italo me", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "italo me")

    def test_code(self):
        node = TextNode("if this than that", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "if this than that")

    def test_link(self):
        node = TextNode("link me", TextType.LINK, "http:www.gazzetta.it")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "link me")
        self.assertEqual(html_node.props["href"], "http:www.gazzetta.it")

if __name__ == "__main__":
    unittest.main()