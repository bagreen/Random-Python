from itertools import chain
import os
import subprocess

filetypes = ('.bmp', '.gif', '.ico', '.jpg', '.log', '.md5', '.nfo', '.png', '.raw', '.txt')
folders = ('Movies', 'TV-Shows')

for root, directories, files in chain.from_iterable(os.walk(folder) for folder in folders):
    # for directory in directories:
    #     subprocess.run(['rmdir', directory])

    for file in files:
        if 'sample' in file.lower():
            print('Do you want to remove ' + file + '?')
            entered = input()

            if entered.lower() in ('yes', 'y'):
                os.remove(root + '/' + file)

        elif file == 'ETRG.mp4' or file == 'RARBG.com.mp4' or file[-5:].lower() == '.jpeg' or file[-4:].lower() in filetypes:
            path = root + '/' + file
            print(path)
            os.remove(path)
