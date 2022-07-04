import os

def rename_files(path):
    for index, dirname in enumerate(os.listdir(path),1):
        os.rename(path+"/"+dirname, path+"/"+"cat_" + syn_index(index)+".jpg")

def syn_index(index):
    len = 5
    temp = index
    result = ""
    while (temp//10>=1):
        len -= 1
        temp = temp//10
    len-=1
    for _ in range(len):
        result += "0"
    return result + str(index)

if __name__=="__main__":
    path = "../dataset/train/Cat"
    rename_files(path)
