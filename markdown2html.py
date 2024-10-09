

from typing import List

class Markdown2HTML:


    @staticmethod
    def compile(markdown_test: str) -> str:
        markdown_lines = markdown_test.split('\n')

        belonging = ''
        for line in markdown_lines:

            # indent
            if line.startswith('    '):
                pass









# recv a markdown string and return a html string
# e.g.
#
# ### This is h3
# - This is a list item
# - This is another list item
#
# **Bold text**
# *Italic text*
#
# `Code`
#
# [Link](https://www.google.com)
# ![Image](https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png)
#
# #### Following are tables
# | Column 1 | Column 2 |
# |----------|----------|
# | Value 1  | Value 2  |
# | Value 3  | Value 4  |
#