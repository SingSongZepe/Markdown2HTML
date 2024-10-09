
from enum import Enum, auto
from typing import List, Tuple

# Bold
# Italic
# delete
# code

class TextModifier(Enum):
    NoModifier = auto()
    Bold = auto()
    Italic = auto()
    Delete = auto()
    Code = auto()

    def into_format(self) -> str:
        match self:
            case TextModifier.NoModifier:
                return "{}"
            case TextModifier.Bold:
                return "<strong>{}</strong>"
            case TextModifier.Italic:
                return "<em>{}</em>"
            case TextModifier.Delete:
                return "<del>{}</del>"
            case TextModifier.Code:
                return "<code>{}</code>"

# use for constructing a string with modifiers
# into tag string view

class Text:
    def __init__(self, content: str = '',
                 modifier: TextModifier = TextModifier.NoModifier,
                 sub_texts: List['Text'] = None):
        self.content: str = content
        self.modifier: TextModifier = modifier
        self.sub_texts: List[Text] = sub_texts

    # read **Hel*lo Wor*ld**
    # into Text object
    # outer Text object.content = "He{}lo", modifer = TextModifier.Bold
    # inner Text object.content = "llo Wor", modifier = TextModifier.Italic
    # recursively add sub_texts to inner Text object

    # this string can only consist of following indicators:
    # **A**
    # __A__
    # *B*
    # _B_
    # ~~C~~
    # `D` in code block, do not recognize other indicators inside it
    # **Bo _It`a`l~~i~~c_ ld**

    # TODO!
    @staticmethod
    def read_str(raw_str: str) -> 'Text':
        # the most outer Text object
        text = Text()

        if raw_str.startswith('**') or raw_str.startswith('__'):
            text.modifier = TextModifier.Bold
            raw_str = raw_str[2:-2]
        elif raw_str.startswith('*') or raw_str.startswith('_'):
            text.modifier = TextModifier.Italic
            raw_str = raw_str[1:-1]
        elif raw_str.startswith('~~'):
            text.modifier = TextModifier.Delete
            raw_str = raw_str[2:-2]
        elif raw_str.startswith('`'): # special case for code block
            text.modifier = TextModifier.Code
            raw_str = raw_str[1:-1]
            text.sub_texts = []
            text.content = raw_str
            return text
        else:
            text.modifier = TextModifier.NoModifier

        # when occurs italic, sub_str can be like _It`a`l~~i~~c_ ld**
        # return
        def read(sub_str: str) -> Tuple[str, Text]:
            pass

        curr_content = ''
        last_char = ''
        for c in raw_str:
            if c == '*':
                if last_char == '*':
                    last_char = ''


        return Text()


    def into_string(self) -> str:
        content = self.content
        if self.sub_texts:
            # for easy-understanding, I don't put v directly into content format function
            v = [sub_text.into_string() for sub_text in self.sub_texts]
            content = content.format(*v)

        return self.modifier.into_format().format(content)

    def set_content(self, content: str) -> None:
        self.content = content

    def set_sub_texts(self, sub_texts: List['Text']) -> None:
        self.sub_texts = sub_texts

    def set_modifier(self, modifier: TextModifier) -> None:
        self.modifier = modifier

