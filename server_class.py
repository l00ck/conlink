import serverhash


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
        self.files = serverattributes[-1]
        #security: 0=completely open 1= ApachePW

    def print_name(self):
        print(self.name)

    def server_info(self):
        print(self.cpu)
        print(self.ram)
        print(self.location)

    def ports(self):
        print(self.port)

    def print_files(self):
        if self.files != ['empty']:
            for file in self.files:
                print(file[0])
        else:
            print('no files')

    def print_file_content(self, filename):
        for file in self.files:
            if file[0] == filename:
                print(file[1])
            else:
                pass

    def server_commands(self, command):
        if command == 'disconnect':
            localhost = Localhost(serverhash.serverdic['localhost'], 'localhost')
            print('disconnected from ' + self.name)
            localhost.interface()
        else:
            pass

    def global_commands(self, command):
        if command == 'ls':
            self.print_files()
        elif command == 'cat':
            self.print_file_content(command)
        else:
            pass

    def interface(self):
        client_connected = True
        while client_connected is True:
            commands = input('>: ')
            commands = commands.split(' ')
            self.server_commands(commands[0])
            self.global_commands(commands[0])


class Localhost(Server):

    def get_server(self, user_input):
        for word in user_input:
            if word in serverhash.serverdic:
                server = Server(serverhash.serverdic[word], word)
                return server
        else:
            None

    def scan(self, user_input, server):
        if len(user_input) > 1 and user_input[1] == 'network':
            for k in serverhash.serverdic:
                print(k)
        elif server is not None:
            if user_input[1] == server.name:
                server.server_info()
            elif user_input[1] == 'ports' and user_input[2] == server.name:
                server.ports()
        else:
            print('scan what?')

    def try_to_connect(self, user_input, server):
        if len(user_input) > 1 and server is not None:
            print('connected to ' + server.name)
            server.interface()
        elif len(user_input) == 1:
            print('Server not specified')
        else:
            print('Server not found')


    def localhost_commands(self, user_input):
        server = self.get_server(user_input)
#        print(server.name)

        if user_input[0] == 'scan':
            self.scan(user_input, server)
        if user_input[0] == 'connect':
            self.try_to_connect(user_input, server)




    def interface(self):
        client_connected = True
        while client_connected is True:
            commands = input('>: ')
            commands = commands.split(' ')
            self.localhost_commands(commands)
