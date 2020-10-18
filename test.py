import unittest, time, os

from network import Network
from socket import socket
from threading import Thread
from server_tester import *
import server_tester

class Tests(unittest.TestCase):

    def test_network_init(self):
        network = Network("127.0.0.1", 5555)
        self.assertEqual(network.host, "127.0.0.1")
        self.assertEqual(network.port, 5555)
        self.assertEqual(True, isinstance(network.s, socket.socket))

    def test_network_start(self):

        server = Server(1, 5556)

        Thread(target=server.start).start()

        network = Network("127.0.0.1", 5556)

        network.start()

        self.assertEqual(server_tester.connected, 1)

        with open('config.json', 'r') as f:
            loaded_data = json.load(f)
            self.assertEqual(loaded_data, server_tester.config_sent[0])

        try:
            server.finish()
        except:
            pass


    def test_network_send_and_get_data(self):
        server = Server(1, 5555)

        Thread(target=server.start).start()

        network = Network("127.0.0.1", 5555)

        network.start()

        try:
            server.s.close()
        except:
            pass

        self.assertEqual(server_tester.connected, 1)

        with open('config.json', 'r') as f:
            loaded_data = json.load(f)
            self.assertEqual(loaded_data, config_sent[0])

        Thread(target=server.pass_cycle).start()

        network.send_data(['1111'])

        self.assertEqual(network.get_data(), server_tester.data_sent)

        self.assertEqual(server_tester.send_data_is_ok, True)

        server.finish()

