import json
import downloads
import private

downloadDir = private.downloadDir

list = json.loads(private.listStr)

fileListAll = []
fileNameListAll = []
for file in list:
    fileName = file.split('.zip')[0]
    file = ''.join(filter(str.isalpha, fileName))
    fileListAll.append(file)
    fileNameListAll.append(fileName)


res = [item for item in fileListAll if item not in downloads.getFileList(downloadDir)]
res.sort()
print(res)
print(len(res))
