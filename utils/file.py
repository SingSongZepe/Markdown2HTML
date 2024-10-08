

import os


class File:
    @staticmethod
    def read_file(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")

        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        if os.path.exists(file_path):
            print(f"File {file_path} already exists, overwriting...")

        with open(file_path, 'w') as file:
            file.write(content)


