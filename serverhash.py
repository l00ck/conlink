import os

serverdic = {}


scriptpath = os.path.abspath(__file__)
serverpath = os.path.dirname(scriptpath)+"\servers"
serverdirs = os.listdir(serverpath)


def info_parser(server_folder):
    server_attributes_list = server_folder.read().split("\n")
    return server_attributes_list
    

for folder in serverdirs:
    info = open(serverpath + "\\" + folder + "\info.txt")
    x = info_parser(info)
    serverdic[folder] = x
    info.close()



#print serverdic