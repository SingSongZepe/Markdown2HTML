
import os

from markdown2html import Markdown2HTML






def main() -> None:
    test_dir = './file/test'
    for file in os.listdir(test_dir):
        m2h = Markdown2HTML("test.md")




if __name__ == '__main__':
    main()

