import glob
import os

def getFileList(dir):
    list_of_files = [os.path.basename(x) for x in glob.glob(dir +'/*')]

    fileList = []
    fileNameList = []
    for file in list_of_files:
        fileName = file.split('.')[0]
        #fileName = fileName.replace('_', '-')
        file = ''.join(filter(str.isalpha, fileName))
        fileList.append(file)
        fileNameList.append(fileName)
    return fileList

    # latest_file = max(list_of_files, key=os.path.getctime)
    # print(fileList)
    # print(len(fileList))
