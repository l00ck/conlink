import serverhash
import server_class


def scan_func(user_input, server):
    if user_input[1] == 'network':
        for k in serverhash.serverdic:
            print(k)

    elif server is not None:
        if user_input[1] == server.name:
            server.server_info()

        elif user_input[1] == 'ports' and user_input[2] == server.name:
            server.ports()
    else:
        print('scan what?')


def global_func(user_input, server):
    if user_input[1] == server.name:
        print('connected to ' + server.name)
        connected = True
        while connected is True:
            connected_input = input('>: ')
            connected_input = connected_input.split(' ')
            if connected_input[0] == 'ls':
                server.print_files()

            elif connected_input[0] == 'disconnect':
                connected = False
                print('disconnected from ' + server.name)

            elif connected_input[0] == 'cat':
                server.print_file_content(connected_input[1])

            else:
                print('still connected')


def u_input():
    user_input = input('>: ')
    user_input = user_input.split(' ')
    server = None

    for word in user_input:
        if word in serverhash.serverdic:
            server = server_class.Server(serverhash.serverdic[word], word)
        else:
            pass

    if user_input[0] == 'scan':
        scan_func(user_input, server)

    if user_input[0] == 'connect':
        global_func(user_input, server)


