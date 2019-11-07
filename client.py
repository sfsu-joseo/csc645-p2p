# -*- coding: utf-8 -*-
""" The client
This file has the class client that implements a client socket.
Note that you can replace this client file by your client from
assignment #1.
"""
import socket
import pickle

class Client(object):

    def __init__(self):
        """
        TODO: implement this contructor
        Class contructor
        """
        self.client_socket = None # create here your client tcp socket

    def connect(self, ip_adress, port):
        """
        TODO: Implement connection to server sockets
        :param ip_adress:
        :param port:
        :return: VOID
        """
        pass

    def send(self, data):
        """
        TODO: Implement client socket send method
        :param data: raw_data. This data needs to be
                     serialized inside this method
                     with pickle before being sent.
                     You can also serialize objects
                     with pickle
        :return: VOID
        """
        pass

    def recieve(self, memory_allocation_size):
        """
        TODO: implement receives data from server socket
        :param memory_allocation_size:
        :return: deserialized data
        """
        return None

    def close(self):
        """
        TODO: implement the close mechanish of a client socket
        :return: VOID
        """
        pass
