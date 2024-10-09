
# test cases here

import unittest

from utils.file import File
from markdown2html import Markdown2HTML


class Test(unittest.TestCase):
    def test1(self):
        md = File.read_file('./file/test/test1.md')
        html = Markdown2HTML.compile(md)
        File.write_file(html, './file/output/test1.html')






if __name__ == '__main__':
    unittest.main()