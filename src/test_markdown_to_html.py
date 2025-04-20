import unittest
from markdown_to_html import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images_empty(self):
        text = "This text has no images."
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_images_single(self):
        text = "This text has one image ![](/path/to/image.png)."
        self.assertEqual(extract_markdown_images(text), [('', '/path/to/image.png')])

    def test_extract_markdown_images_with_alt_text(self):
        text = "This text has an image ![alt text](/image.jpg)."
        self.assertEqual(extract_markdown_images(text), [('alt text', '/image.jpg')])

    def test_extract_markdown_images_multiple(self):
        text = "Here are two images: ![image1](/img1.gif) and ![image two](url/img2.jpeg)."
        self.assertEqual(extract_markdown_images(text), [('image1', '/img1.gif'), ('image two', 'url/img2.jpeg')])

    def test_extract_markdown_images_mixed_content(self):
        text = "Text ![img](link) more text [link](url) and ![another](path)."
        self.assertEqual(extract_markdown_images(text), [('img', 'link'), ('another', 'path')])

    def test_extract_markdown_images_malformed(self):
        text = "![alt text](/image.jpg](extra)"
        self.assertEqual(extract_markdown_images(text), [('alt text', '/image.jpg')]), "Should still capture the valid part"

    def test_extract_markdown_links_empty(self):
        text = "This text has no links."
        self.assertEqual(extract_markdown_links(text), [])

    def test_extract_markdown_links_single(self):
        text = "This text has one link [boot dev](https://www.boot.dev)."
        self.assertEqual(extract_markdown_links(text), [('boot dev', 'https://www.boot.dev')])

    def test_extract_markdown_links_multiple(self):
        text = "Here are two links: [link one](http://example.com) and [second link](/another/page)."
        self.assertEqual(extract_markdown_links(text), [('link one', 'http://example.com'), ('second link', '/another/page')])

    def test_extract_markdown_links_with_title(self):
        text = "This link has a title [Example](https://example.com 'Optional title')."
        # La tua regex attuale non gestisce i titoli, quindi cattura tutto fino alla fine delle parentesi
        self.assertEqual(extract_markdown_links(text), [('Example', "https://example.com 'Optional title'")])

    def test_extract_markdown_links_mixed_content(self):
        text = "Text ![img](link) more text [link](url) and ![another](path)."
        self.assertEqual(extract_markdown_links(text), [('link', 'url')])

    def test_extract_markdown_links_malformed(self):
        text = "[link](url) (extra)"
        self.assertEqual(extract_markdown_links(text), [('link', 'url')])

    def test_extract_markdown_links_empty_alt_text(self):
        text = "[](https://emptylink.com)"
        self.assertEqual(extract_markdown_links(text), [('', 'https://emptylink.com')])

if __name__ == '__main__':
    unittest.main()