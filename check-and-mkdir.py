import os

def checkAndMkdir(src):
    if not os.path.exists(src):
        os.mkdirs(src)