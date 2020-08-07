import os
import re
old = 'ngk'
new = 'eosio'
pattern = re.compile(old, re.IGNORECASE)
for dirpath,dirnames,files in os.walk('/home/sjf/Desktop/test/',topdown=False):
    if pattern.sub(new,dirpath.split('/')[-1]):
        new_folder = dirpath.rsplit('/',maxsplit=1)[0] +'/'+ pattern.sub(new,dirpath.split('/')[-1]) + '/'
        if new_folder != dirpath+'/':
           os.rename(dirpath,new_folder)
           dirpath = new_folder
    for item in files:
        if dirpath.endswith('/'):
            used_name = dirpath + item
            new_name = dirpath  + pattern.sub(new, item)
            os.rename(used_name, new_name)
        else:
            used_name = dirpath + '/' + item
            new_name = dirpath + '/' + pattern.sub(new, item)
            os.rename(used_name, new_name)