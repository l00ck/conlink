import serverhash
import server_class



def scan_func(user_input, server):
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


def try_to_connect(user_input, server):
    if len(user_input) > 1 and server is not None:
        print('connected to ' + server.name)
        server.global_commands()
    elif len(user_input) == 1:
        print('Server not specified')
    else:
        print('Server not found')


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
        try_to_connect(user_input, server)
