#Get file size , print it , process it...
#Os.stat will provide the file size in (.st_size) property. 
#The file size will be shown in bytes.

import os

fsize=os.stat('filepath')
print('size:' + fsize.st_size.__str__())

#check if the file size is less than 10 MB

if fsize.st_size < 10000000:
    processing is: