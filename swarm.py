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

        :param peer: add the peer object
        :return: VOID
        """
        self.peers.append(peer)

    def delete_peer(self, peer_id):
        """

        :param peer_id: the client id of the peer
        :return: VOID
        """
        self.peers.remove(peer)

    def resource_id(self):
        """

        :return: the file id that is being
                 shared by this swarm
        """
        if self.resource_id:
            return self.resource_id