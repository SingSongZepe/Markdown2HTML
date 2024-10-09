

import unittest

from object.text import Text, TextModifier
from object.tag import Tag, TagName

class TextTest(unittest.TestCase):
    def test_text(self):
        text = Text('A B', TextModifier.Italic)
        print(text.into_string())
        outer_text = Text('C{}D', TextModifier.Bold, [text])
        print(outer_text.into_string())
        oouter_text = Text('E{}F G{}H', TextModifier.Bold, [outer_text, text])
        print(oouter_text.into_string())

    def test_read_str(self):
        str = '`A**B**C _DEF_ GHI`'
        text = Text.read_str(str)
        print(text.into_string())


    def test_tag(self):
        text = Text('A B', TextModifier.Italic)
        outer_text = Text('C{}D', TextModifier.Bold, [text])
        oouter_text = Text('E{}F G{}H', TextModifier.Bold, [outer_text, text])

        tag = Tag()
        tag.set_tag(TagName.P)
        tag.set_text(oouter_text)
        tag.set_sub_tags([Tag(TagName.Strong, outer_text)])

        print(tag.into_string())


    def test_tag_simple(self):
        text = Text('A B{}', TextModifier.NoModifier, [Text('C D', TextModifier.Italic)])
        tag = Tag(TagName.H1, text)
        print(tag.into_string())

if __name__ == '__main__':
    unittest.main()
