# -*- coding: utf-8 -*-
""" The peer """
from server import Server
from client import Client

class Peer(Client, Server):

    def __init__(self):
        """
        TODO: implement the class constructor
        """
        Server.__init__(self) # inherites methods from Server class
        Client.__init__(self) # inherites methods from Client class

    def connect_to_tracker(self, ip_address, port):
        """
        TODO: implement this method
        Connect to the tracker. Note that a tracker in this assignment
        is similar to the server in assignment #1. So, you already know
        how to implement this connection
        Note that ip address and port comes from the announce in
        the torrent file. So you need to parse it firt at some point
        :param ip_address:
        :param port:
        :return: VOID
        """
        return None

    def get_metainfo(self, torrent_path):
        """
        TODO: implement this method
        (1) Create a empty resource object
        (2) call the method parse_metainfo from that object
        (3) return the resource object, so all the metainfo
        from that file can be accessed by getters and setters.
        :param torrent_path:
        :return:
        """