import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link  # Assuming your functions are in 'your_module.py'


class TestNodeSplitting(unittest.TestCase):

    def test_split_nodes_image_single_image(self):
        node = TextNode("This is text with ![alt](url).", TextType.TEXT)
        expected_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "url"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertListEqual(split_nodes_image([node]), expected_nodes)

    def test_split_nodes_image_no_image(self):
        node = TextNode("This text has no images.", TextType.TEXT)
        expected_nodes = [node]
        self.assertListEqual(split_nodes_image([node]), expected_nodes)

    def test_split_nodes_image_multiple_images(self):
        node = TextNode("One ![alt1](url1) and two ![alt2](url2).", TextType.TEXT)
        expected_nodes = [
            TextNode("One ", TextType.TEXT),
            TextNode("alt1", TextType.IMAGE, "url1"),
            TextNode(" and two ", TextType.TEXT),
            TextNode("alt2", TextType.IMAGE, "url2"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertListEqual(split_nodes_image([node]), expected_nodes)

    def test_split_nodes_image_image_at_start_and_end(self):
        node = TextNode("![start](start_url) middle text ![end](end_url)", TextType.TEXT)
        expected_nodes = [
            TextNode("start", TextType.IMAGE, "start_url"),
            TextNode(" middle text ", TextType.TEXT),
            TextNode("end", TextType.IMAGE, "end_url"),
        ]
        self.assertListEqual(split_nodes_image([node]), expected_nodes)

    def test_split_nodes_link_single_link(self):
        node = TextNode("Click [here](https://example.com).", TextType.TEXT)
        expected_nodes = [
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertListEqual(split_nodes_link([node]), expected_nodes)

    def test_split_nodes_link_no_link(self):
        node = TextNode("This text has no links.", TextType.TEXT)
        expected_nodes = [node]
        self.assertListEqual(split_nodes_link([node]), expected_nodes)

    def test_split_nodes_link_multiple_links(self):
        node = TextNode("Go to [site1](url1) or [site2](url2).", TextType.TEXT)
        expected_nodes = [
            TextNode("Go to ", TextType.TEXT),
            TextNode("site1", TextType.LINK, "url1"),
            TextNode(" or ", TextType.TEXT),
            TextNode("site2", TextType.LINK, "url2"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertListEqual(split_nodes_link([node]), expected_nodes)

    def test_split_nodes_link_link_at_start_and_end(self):
        node = TextNode("[first](link1) some text [last](link2)", TextType.TEXT)
        expected_nodes = [
            TextNode("first", TextType.LINK, "link1"),
            TextNode(" some text ", TextType.TEXT),
            TextNode("last", TextType.LINK, "link2"),
        ]
        self.assertListEqual(split_nodes_link([node]), expected_nodes)

    # def test_split_nodes_image_empty_alt_text(self):
    #     node = TextNode("Image with ![ ](image.png).", TextType.TEXT)
    #     expected_nodes = [
    #         TextNode("Image with ", TextType.TEXT),
    #         TextNode(" ", TextType.IMAGE, "image.png"),
    #         TextNode(".", TextType.TEXT),
    #     ]
    #     self.assertListEqual(split_nodes_image([node]), expected_nodes)

    # def test_split_nodes_link_empty_alt_text(self):
    #     node = TextNode("Link with [](empty.com).", TextType.TEXT)
    #     expected_nodes = [
    #         TextNode("Link with ", TextType.TEXT),
    #         TextNode(" ", TextType.LINK, "empty.com"),
    #         TextNode(".", TextType.TEXT),
    #     ]
    #     self.assertListEqual(split_nodes_link([node]), expected_nodes)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)