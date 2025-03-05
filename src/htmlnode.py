

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
        if value is None:
            raise ValueError("Leaf node must have a value")

        super().__init__(tag, value, children=None, props=props)
        self.tag = tag
        self.value = value

    def add_child(self, child):
        raise ValueError("LeafNode cannot have children")

    def to_html(self):
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children=None, props=None):
        if tag is None:
            raise ValueError("Parent node must have a tag")
        if not children:
            raise ValueError("Parent node must have children")

        super().__init__(tag, None, children, props=props)
        self.value = None
        self.children = children
        self.tag = tag


    def to_html(self):          
        # See below for previous code and debugging process
        return f"<{self.tag}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
        # DEBUGGING: print(f"Processing ParentNode with tag {self.tag} and children: {self.children}")
        
        # DEBUGGING: children_html = ""   # code prior to the one-line code below
        # DEBUGGING: for child in self.children:
        # DEBUGGING:     print(f"Calling to_html on child: {child}")
        # DEBUGGING:     child_html = child.to_html()
        # DEBUGGING:     print(f"Generated HTML from child: {child_html}")
        # DEBUGGING:     children_html += child_html

        # DEBUGGING: children_html = "".join(child.to_html() for child in self.children)

        # DEBUGGING: return f"<{self.tag}>{children_html}</{self.tag}>"
        