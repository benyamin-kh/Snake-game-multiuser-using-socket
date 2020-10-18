import socket, json


class Network:

    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.data = {}

    def start(self):
        self.s.connect((self.host, self.port))
        json_data = self.s.recv(4096).decode('ascii')
        self.data = json.loads(json_data)
        with open('config.json', 'w') as f:
            f.write(json_data)

    def send_data(self, keys):
        message = 'snake_' + str(self.data['id']) + '_'
        if len(keys) == 0:
            message += 'no_key'
        else:
            message += keys[0]
        data = {
            'keys': [message],
            'dead': False
        }
        self.s.sendall(str(json.dumps(data)).encode('ascii'))

    def get_data(self):
        data = self.s.recv(4096).decode('ascii').replace("'", '"')
        data = json.loads(data)
        return data
