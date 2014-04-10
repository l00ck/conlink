import serverhash
import conlinkserverclass


def u_input():
    user_input = input('>: ')
    user_input = user_input.split(' ')
    server = None

    for word in user_input:
        if word in serverhash.serverdic:
            server = conlinkserverclass.Server(serverhash.serverdic[word], word)
        else:
            pass

    if user_input[0] == 'scan':
        try:
            if user_input[1] == 'network':
                for k in serverhash.serverdic:
                    print(k)

            if user_input[1] == 'ports' and server is not None:
                pass
                server.ports()
            else:
                print('Server not found')
        except IndexError:
            print('scan what?')
            #test