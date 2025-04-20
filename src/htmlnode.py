class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_list = []
        for k,v in self.props.items():
            props_list.append(f'{k}="{v}"')
        return " ".join(props_list)
    
    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"
    
   
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        else:
            props_html = self.props_to_html()
            if props_html:
                return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Children value is mandatory")
        else:
            child_html = "".join(child.to_html() for child in self.children)
            props_html = self.props_to_html()
            if props_html:
                return f"<{self.tag} {props_html}>{child_html}</{self.tag}>"
            else:
                return f"<{self.tag}>{child_html}</{self.tag}>"
    

# node = HTMLNode(tag = "p", value = "test", props = {"class": "test-class"})
# node.__repr__()
