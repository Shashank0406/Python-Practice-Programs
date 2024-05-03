import os.path,time


print("%s" %time.ctime(os.path.getmtime('18.os.envi.py')))


print("%s" %time.ctime(os.path.getctime('18.os.envi.py')))


print("%s" %time.ctime(os.path.getatime('18.os.envi.py')))