from pathlib import Path
from collections import Counter
import shutil
from src.data import dir_path
import json
import sys
from src.data.utiles import read_json



class orgnizer:

    def __init__(self):

        self.ext_json = read_json("ext.json")
        
        self.category = {}
        for folder_cat , sufs in self.ext_json.items():
            for suf in sufs:
                self.category[suf] = folder_cat


    def cleaner(self, directory_path = "/home/bahram/Downloads"):
        ext =[]
        for files in Path(directory_path).iterdir():
            #ignores dirs
            if files.is_dir():
                continue

            #ignores hidden files
            if files.name.startswith('.'):
                continue

            #moves files
            if files.suffix not in self.category:
                folder_path = Path(directory_path)/'others'
            else:
                folder_path = Path(directory_path)/self.category[files.suffix]

            folder_path.mkdir(exist_ok = True)
            shutil.move(str(files) , str(folder_path))
            print(f'{files.suffix:10}{folder_path}')
            ext.append(files.suffix)
        print('done')

if __name__ == "__main__":
    c1 = orgnizer()
    c1.cleaner(sys.argv[1])