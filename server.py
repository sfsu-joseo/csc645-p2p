# -*- coding: utf-8 -*-
""" The server
This file has the class client that implements a server socket.
Note that you can replace this server file by your server from
assignment #1.
"""
import socket
import pickle
import threading

class Server(object):

    def __init__(self):
        """
        TODO: implement this constructor
        Class contructor
        """
        self.server_socket = None  # create here your client tcp socket

    def listen(self):
        """
        TODO: implement this method
        Listen for new connections
        :return: VOID
        """
        pass

    def accept(self):
        """
        TODO: implement this method
        Accept new clients
        :return:
        """
        return None

    def recieve(self, memory_allocation_size):
        """
        TODO: implement this method
        Receives data from clients socket
        :param memory_allocation_size:
        :return: deserialized data
        """
        return None

    def send(self, data):
        """
        TODO: implement this method
        Implements send socket send method
        :param data: raw_data. This data needs to be
                     serialized inside this method
                     with pickle before being sent.
                     You can also serialize objects
                     with pickle
        :return: VOID
        """
        pass

    def threaded_client(self, conn, client_addr):
        """
        TODO: implement this method
        :param conn:
        :param client_addr:
        :return: a threaded client.
        """
        return None



