from os import listdir, path


result = []
if __name__ == '__main__':
    files = [f for f in listdir() if f[-4:] == '.txt' and path.isfile(f)]
    for file in files:
        with open(file, 'r') as filename:
            for line in filename:
                result.append(line)

    with open('result.txt', 'w') as filename:
        filename.writelines(result)
