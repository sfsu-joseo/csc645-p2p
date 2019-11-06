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
        Class contructor
        """
        self.server_socket = None  # create here your client tcp socket

    def listen(self):
        """
        Listen for new connections
        :return: VOID
        """
        return None

    def accept(self):
        """
        Accept new clients
        :return:
        """
        return None

    def recieve(self, memory_allocation_size):
        """
        Receives data from clients socket
        :param memory_allocation_size:
        :return: deserialized data
        """
        return None

    def send(self, data):
        """
        Implements send socket send method
        :param data: raw_data. This data needs to be
                     serialized inside this method
                     with pickle before being sent.
                     You can also serialize objects
                     with pickle
        :return: VOID
        """
        return None  # remove this after implemented

    def threaded_client(self, conn, client_addr):
        """
        I made this method for you. It is already completed and no need to modify it.
        This already creates the threads for the proxy is up to you to find out where to put it.
        Hint: since we are using only  non-persistent connections. Then, when a clients connects,
        it also means that it already has a request to be made. Think about the difference
        between this and assign#1 when you created a new thread.
        :param conn:
        :param client_addr:
        :return:
        """
        #proxy_thread = ProxyThread(conn, client_addr)
        #proxy_thread.init_thread()
        return None



