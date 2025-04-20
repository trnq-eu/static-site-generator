from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest

class TestHtmlNode(unittest.TestCase):
    def test_base(self):
        node = HTMLNode(tag='p', value='prova prova', props={"class": "message"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "prova prova")
        self.assertEqual(node.props, {"class": "message"})
        self.assertEqual(node.children, None)

    def test_html_output(self):
        node = HTMLNode(tag = "p", value = "test", props = {"class": "test-class"})
        self.assertEqual(node.__repr__(), "p test None {'class': 'test-class'}")


    def test_node_no_value(self):
        node = HTMLNode(tag = "br")
        self.assertEqual(node.tag, "br")
        self.assertEqual(node.value, None)
        self.assertEqual(node.props, None)
        self.assertEqual(node.children, None)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "clicca qui!", {"href": 'http://www.repubblica.it'})
        self.assertEqual(node.to_html(), '<a href="http://www.repubblica.it">clicca qui!</a>')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()