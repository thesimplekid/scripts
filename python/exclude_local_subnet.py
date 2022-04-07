"""
Scripts take mullvad config files and motifies so selected subnet is excluded.
"""

import os

line_one = "PostUp = ip route add <subnet to route to>/24 via <ip of router>;\n"
line_two =  "PreDown = ip route delete <subnet to route to>;\n"


path = "./mlvd/"

for files in os.listdir(path):
    if os.path.isfile(os.path.join(path, files)):
        print(files)

        with open("./mlvd/" + files, 'r+') as fd:
            contents = fd.readlines()
            contents.insert(6, line_one)
            contents.insert(7, line_two)
            fd.seek(0)
            fd.writelines(contents)

