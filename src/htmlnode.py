

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("need to add markdown text")

    def props_to_html(self):
        in_line_string = ""
        for key in self.props:
            in_line_string += f' {key}="{self.props[key]}"'
        return in_line_string

    def __repr__(self):
        return (f"HTMLNode contains: "
                f"tag={self.tag or 'None'}, "
                f"value={self.value or 'None'}, "
                f"{len(self.children) if self.children else 0} children, "
                f"{len(self.props) if self.props else 0} props")  # useful for debugging later
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def add_child(self, child):
        raise ValueError("LeafNode cannot have children")

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return self.value

        props_html = self.props_to_html()
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'