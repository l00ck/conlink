import os

serverdic = {}

scriptpath = os.path.abspath(__file__)
serverpath = os.path.dirname(scriptpath) + "\servers"
serverdirs = os.listdir(serverpath)


def info_parser(server_folder):
    server_attributes_list = server_folder.read().split("\n")
    return server_attributes_list


def read_files(folder):
    files = os.listdir(folder)
    l = []

    if len(files) is not 0:
        for f in files:
            content = open(folder + '\\' + f, 'r')
            a = content.read()
            content.close()
            f = [f, a]
            l.append(f)
        return l

    else:
        return ['empty']


for folder in serverdirs:
    info = open(serverpath + "\\" + folder + "\info.txt")
    x = info_parser(info)
    f = read_files(serverpath + "\\" + folder + "\\files")
    x.append(f)
    #print(f)
    serverdic[folder] = x
    info.close()

print(serverdic)