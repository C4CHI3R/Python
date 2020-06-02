#!/usr/bin/python
import zipfile
import re
from zipfile import ZipFile

password = 'pass'
def main():
    zip_file = '/file/name/here' 

    with zipfile.ZipFile(zip_file, 'r') as zf:
        for name in zf.namelist():
            password = re.sub('.zip', '', name)
        print ('password = ' + password)
        zf.extractall(pwd=bytes(password,'utf-8'))
        next_name = zf.namelist()[0]
        zf.close()
        
    while True:
        if zipfile.is_zipfile(next_name):
            with zipfile.ZipFile(next_name, 'r') as child_file:
                for name in child_file.namelist():
                    password = re.sub('.zip','', name)
                print ('password = ' + password)
                child_file.extractall(pwd=bytes(password, 'utf-8'))
                next_name = child_file.namelist()[0]

        else:
            break
if __name__ == '__main__': 
    main()