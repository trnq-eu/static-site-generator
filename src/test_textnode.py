import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text_type(self):
        node1 = TextNode("Same Text", TextType.BOLD)
        node2 = TextNode("Same Text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_different_url(self):
        node1 = TextNode("Same Text", TextType.BOLD, "http://www.repubblica.it")
        node2 = TextNode("Same Text", TextType.ITALIC, "http://www.gazzetta.it")
        self.assertNotEqual(node1, node2)

    



if __name__ == "__main__":
    unittest.main()