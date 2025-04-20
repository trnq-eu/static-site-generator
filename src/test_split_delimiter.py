import unittest
from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter  # Assuming your function is in 'your_module.py'

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiter(self):
        # Test that text without delimiters remains unchanged
        node = TextNode("No delimiter here", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "No delimiter here")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_bold_delimiter(self):
        # Test that text with bold delimiters is split correctly
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_italic_delimiter(self):
        # Test that text with italic delimiters is split correctly
        node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)