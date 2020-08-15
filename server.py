import socket
import json
import os
import random


class UserData:
    def __init__(self):
        if not os.path.isfile("data.json"):
            with open("data.json", "w") as data_file:
                data_file.write("{}")

        with open("default_data.json", "r") as default:
            self.default_data = json.load(default)

        with open("data.json", "r") as data:
            self.data = json.load(data)

    def save(self):
        with open("data.json", "w") as data_file:
            json.dump(self.data, data_file, indent=4)

    def set_profile(self, user, key, value):
        self.data[user]["profile"][key] = value

    def get_profile(self, user, key):
        return self.data[user]['profile'].get(key)

    def is_user(self, user):
        return bool(self.data.get(user))


    def create_coder(self):
        firstname = input('First Name: ')
        lastname = input('Last name: ')
        age = int(input('Age: '))
        user = f'{firstname}_{lastname}@{random.randint(100000, 900000)}'
        if not self.is_user(user):
            self.data[user] = self.default_data
            self.set_profile(user, 'name', f'{firstname} {lastname}')
            self.set_profile(user, 'age', age)
            self.save()

            print('User has been created')
            print('Now starting server')
        else:
            print('Coder Already exist')




ud = UserData()
server = input('server or input')
if server == 'ser':
    print('awww yeay')
else:
    ud.create_coder()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
sock.bind((ip, 8888))

sock.listen(1)
while True:
    c, a = sock.accept()
    print(a)
    msg = (c.recv(1024)).decode()
    print(msg)
    if msg == 'Hello':
        print('hello')

    elif 'login' in msg:
        log_det = c.recv(1024).decode()
        log_det = log_det.replace('login', '')
        log_det = log_det.splitlines()
        print(log_det)


    elif 'refresh' in msg:
        print('Getting Current Info...')
        stuff1 = c.recv(1024).decode().replace('refresh', '')
        stuff = ud.get_profile('Samuel_Scott@544464', 'Belt')

        print(stuff)

    else:
        print('Error no commands found')


