"""
Script to delete lines that are listed in the set from each file in directory
"""
import os 


path = "./mlvd/"
lines_to_delete = [11,12]

for files in os.listdir(path):
    if os.path.isfile(os.path.join(path, files)):
        print(files)

        with open(path + files, 'r+') as fd:
            contents = fd.readlines()
            fd.seek(0)
            for i, line in enumerate(contents):
                if i not in lines_to_delete:
                    fd.write(line)
            fd.truncate()


