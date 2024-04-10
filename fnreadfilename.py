import os
def readfilesname(path):
    dir_list = os.listdir(path)
    # print("Files and directories in '", path, "' :")
    # prints all files
    # print(dir_list)

    i=0
    temp=[]
    while i <len(dir_list):
        if str(dir_list[i])[-6:] == '_2.csv':
            temp.append(dir_list[i])
        i=i+1
    return temp
