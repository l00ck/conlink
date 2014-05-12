import serverhash
import server_class

if __name__ == "__main__":
    localhost = server_class.Localhost(serverhash.serverdic['localhost'], 'localhost')
    localhost.interface()

    while True:
        localhost.interface()
else:
    print('this does nothing')