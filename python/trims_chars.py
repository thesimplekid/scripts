"""
Trims <chars_to_trim> from end of <line> for each file in folder
"""

import os

path = "./mlvd/"
line = 10
chars_to_trim = 6
for files in os.listdir(path):
    if os.path.isfile(os.path.join(path, files)):
        print(files)

        with open("./mlvd/" + files, 'r+') as fd:
            contents = fd.readlines()
            print (contents)
            contents[line] = contents[line][:-chars_to_trim] + "\n"
            # print(contents[10])
            print(contents)
            fd.seek(0)
            fd.writelines(contents)
