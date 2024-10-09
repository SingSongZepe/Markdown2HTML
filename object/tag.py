
from typing import List, Dict
from enum import Enum, auto

from object.text import Text

# class TagType(Enum):
#     Single = auto()
#     Wrap = auto()

class TagName(Enum):
    # title tags
    H1 = auto()
    H2 = auto()
    H3 = auto()
    H4 = auto()
    H5 = auto()
    H6 = auto()

    # paragraph tags
    P = auto()

    # image tags
    Img = auto()
    A = auto() # used for links, e.g. <a href="https://www.google.com">Google</a>

    Strong = auto()
    Em = auto()
    Del = auto()
    Code = auto()

    # list tags
    Ul = auto()
    Ol = auto()
    Li = auto()

    Br = auto() # line break

    Blockquote = auto() # same as > in markdown

    Caption = auto() # for table caption
    Table = auto()
    Thead = auto()
    Tbody = auto()
    Tfoot = auto()
    Tr = auto()
    th = auto()
    Td = auto()

    def into_format(self) -> str:
        match self:
            case TagName.H1:
                return '<h1>{}</h1>'
            case TagName.H2:
                return '<h2>{}</h2>'
            case TagName.H3:
                return '<h3>{}</h3>'
            case TagName.H4:
                return '<h4>{}</h4>'
            case TagName.H5:
                return '<h5>{}</h5>'
            case TagName.H6:
                return '<h6>{}</h6>'
            case TagName.P:
                return '<p>{}</p>'
            case TagName.Img:
                return '<img src="{}" alt="{}">'
            case TagName.A:
                return '<a href="{}">{}</a>'
            case TagName.Strong:
                return '<strong>{}</strong>'
            case TagName.Em:
                return '<em>{}</em>'
            case TagName.Del:
                return '<del>{}</del>'
            case TagName.Code:
                return '<code>{}</code>'
            case TagName.Ul:
                return '<ul>{}</ul>'
            case TagName.Ol:
                return '<ol>{}</ol>'
            case TagName.Li:
                return '<li>{}</li>'
            case TagName.Br:
                return '<br>'
            case TagName.Blockquote:
                return '<blockquote>{}</blockquote>'
            case TagName.Caption:
                return '<caption>{}</caption>'
            case TagName.Table:
                return '<table>{}</table>'
            case TagName.Thead:
                return '<thead>{}</thead>'
            case TagName.Tbody:
                return '<tbody>{}</tbody>'
            case TagName.Tfoot:
                return '<tfoot>{}</tfoot>'
            case TagName.Tr:
                return '<tr>{}</tr>'
            case TagName.th:
                return '<th>{}</th>'
            case TagName.Td:
                return '<td>{}</td>'
            case _:
                return '{}'



# a tree-like element of markdown to HTML
# markdown:
# # Heading 1
# html:
# <h1>Heading 1</h1>

# # Heading *1*
# <h1>Hello<em>Wo</em>uld</h1>

class Tag:
    def __init__(self,
                 tag: TagName = TagName.P,
                 text: Text = '',
                 sub_tags: List['Tag'] = None,
                 attrs: Dict[str, str] = None):
        self.tag = tag        # h1, p, img, etc.

        # Heading 1 and its modifiers
        # or in a text, there is some word has other modifiers
        # <h3>New<strong>Hello</strong>World</h3>
        self.text: Text = text
        self.sub_tags: List[Tag] = sub_tags
        self.attrs = attrs


    def into_string(self) -> str:
        sub_tag_str = ''
        if self.sub_tags:
            sub_tag_str += ''.join([tag.into_string() for tag in self.sub_tags])

        return self.tag.into_format().format(self.text.into_string() + sub_tag_str)

    def set_tag(self, tag: TagName):
        self.tag = tag

    def set_text(self, text: Text):
        self.text = text

    def set_sub_tags(self, sub_tags: List['Tag']):
        self.sub_tags = sub_tags

    def set_attrs(self, attrs: Dict[str, str]):
        self.attrs = attrs


