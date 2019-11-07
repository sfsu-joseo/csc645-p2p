# -*- coding: utf-8 -*-
""" The tracker
This file has the class swarm that represents a swarm
where peers can share a resource.
"""
class Swarm(object):

    def __init__(self, resource_id):
        """
        Class constructor
        """
        self.peers = [] # the peers connected to this swarm
        self.resource_id = resource_id

    def add_peer(self, peer):
        """
        TODO: implement this method
        :param peer: add the peer object
        :return: VOID
        """
        pass

    def delete_peer(self, peer):
        """
         TODO: implement this method
        :param peer_id: the client id of the peer
        :return: VOID
        """
        pass

    def peers(self):
        """
        TODO: implement this method
        :return: the list of peers connected to the swarm
        """
        return None

    def resource_id(self):
        """
        TODO: implement this method
        :return: the file id of the file that is being
                 shared by this swarm
        """
        return None