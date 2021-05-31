import os
import glob
import re
import private

dir_path = private.downloadDir
list_of_files = [os.path.basename(x) for x in glob.glob(dir_path+'*')]
print(list_of_files)
for file_name in list_of_files:
    match = re.match("^(.*)\s\([\d]*\)(\..*)$", file_name)
    file_path = dir_path+file_name
    if match:
        origin = match.group(1)+match.group(2)
        if origin in list_of_files:
            os.chmod(file_path, 0o777)
            os.remove(file_path)
            print(file_name+' removed!!!!')
        else:
            print(file_name+' (kept)')

print(len(list_of_files))
