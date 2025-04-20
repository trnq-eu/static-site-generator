from enum import Enum

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "`Code text`"
    LINK = "url of the link"
    IMAGE = "link to an image"

class TextNode():
    def __init__(self, text,text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        TEXT = self.text
        TEXT_TYPE = self.text_type
        URL = self.url
        return f"TextNode({TEXT}, {TEXT_TYPE}, {URL})"

