import os
path=os.getcwd()
print("current working directory is:",path)
print("content of current directory:",os.listdir(path))
path=os.chdir('mysub')
print("content of 'mysub' directory :",os.listdir(path))