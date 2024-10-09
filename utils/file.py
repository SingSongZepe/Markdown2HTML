

import os

from utils.log import Log

class File:
    @staticmethod
    def read_file(filename: str) -> str:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")

        with open(filename, 'r') as file:
            content = file.read()
            Log.ln(f'Read file ${filename} successfully')
            return content

    # option 'f' is force cover
    @staticmethod
    def write_file(filename, content: str, option='f') -> bool:
        if os.path.exists(filename):
            Log.ln(f'File {filename} already exists, overwriting...')
            if option == 'f':
                Log.lw(f'Force to cover the existing file ${filename}')
            else:
                Log.ln(f'Because option is false, then do not cover file ${filename}')
                return False

        with open(filename, 'w') as file:
            file.write(content)

        Log.ln(f'Write file ${filename} successfully')
        return True

