import serverhash
import server_class


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
        try:
            if user_input[1] == 'network':
                for k in serverhash.serverdic:
                    print(k)

            elif user_input[1] == server.name:
                server.server_info()

            elif user_input[1] == 'ports' and server is not None:
                server.ports()
        except IndexError:
            print('scan what?')

    if user_input[0] == 'connect':
        if user_input[1] == server.name:
            print('connected to ' + server.name)
            connected = True
            while connected is True:
                connected_input = input('>: ')
                if connected_input == 'disconnect':
                    connected = False
                    print('disconnected from ' + server.name)
                else:
                    print('still connected')

