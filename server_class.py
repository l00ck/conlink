class Server(object):
    def __init__(self, serverattributes, servername):
        self.serverattributes = serverattributes
        self.name = servername
        self.ip = serverattributes[0]
        self.port = serverattributes[1]
        self.cpu = serverattributes[2]
        self.storage = serverattributes[3]
        self.ram = serverattributes[4]
        self.location = serverattributes[5]
        #security: 0=completely open 1= ApachePW

    def print_name(self):
        print(self.name)

    def server_info(self):
        print(self.cpu)
        print(self.ram)
        print(self.location)

    def ports(self):
        print(self.port)