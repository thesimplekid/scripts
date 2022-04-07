## Script to make sure file name is safe and replace ' | ' with '-'
## Used this to rename photo file names  
## files in a directory or folder
## Takes two arguments the first --root_folder is required 
## --root_folder is the root folder files will rename from
## -r=True will also include files is subdirectories
## -r defaults to False

import os
import re
import argparse
import shutil

from werkzeug.utils import secure_filename 

def clean_filename(root: str, filename: str):
    src = f"{root}/{filename}"
    filename = filename.replace(' | ','-')
    filename =  secure_filename(filename)
    dst = f"{root}/{filename}" 
    shutil.move(src, dst)

# Function to rename multiple files
def main():
    parser = argparse.ArgumentParser(description='Renames files')
    parser.add_argument('--root-folder', metavar='root_folder', required=True, help='Root folder to rename from')
    parser.add_argument('--recursive','-r', metavar='recursive', required=False, default=False, choices={'True', 'False'}, help='Rename also goes to subdirectory')
    args = parser.parse_args()
    
    recursive = args.recursive
    folder = args.root_folder

    if not recursive:
        for count, filename in enumerate(os.listdir(folder)):
            clean_filename(folder, filename)
    else:
        for root, subdirectories, files in os.walk(folder):
            for file in files:
                clean_filename(root, file)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()
