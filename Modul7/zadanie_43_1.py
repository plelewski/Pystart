from os import path, remove


class File:
    def __init__(self, filename: str):
        self.filename = filename

    @staticmethod
    def exists(filename: str):
        return path.exists(filename)

    @staticmethod
    def delete(filename: str):
        remove(filename)

    @staticmethod
    def readfile(filename: str):
        with open(filename) as file:
            return file.readlines()


if __name__ == '__main__':
    print('Start')
    print(File.exists('pole_bitwy.py'))
    print('Teraz usuwam plik')
    File.delete('dupa.txt')
