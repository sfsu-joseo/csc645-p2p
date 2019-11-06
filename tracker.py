# -*- coding: utf-8 -*-
""" The tracker
This file implements the Tracker class. The tracker has two main functionalities
 (1) A client connects to a tracker, and a tracker sends
all the peers ip addresses and ports connected to the swarm that are sharing
the same resource. Since a tracker can handle more than one swarm, then the
swarm needs to be identified with a id (i.e the file id that is being shared
in the swarm)
 (2) When a peers change status (become leechers or seeders) they must inform
 the tracker, so the tracker can update that info in the swarm where they are
 sharing the resource

"""
from server import Server

class Tracker(Server):

    IP_ADDRESS = ""
    PORT = 0000

    def __init__(self):
        """
        Inherits from class Server
        """
        Server.__init__(self)
        # the list of swarms that this tracker keeps
        self.swarms = []

    def add_swarm(self, swarm):
        """
        Add a Swarm object to the swarms list of the tracker
        :param swarm:
        :return:
        """
        self.swarms.append(swarm)

    def remove_swarm(self, resource_id):
        """
        Given a resource id, remove the swarm from the tracker
        that is sharing this resource id.
        This happens normally when there is no seeder sharing
        this resource.
        :param resource_id:
        :return:
        """
        return None

    def add_peer_to_swarm(self, peer, resource_id):
        """
        Based on the resource_id provided, iterate over the
        swarms list, and when resource_id matchs, add the
        new peer to the swarm.
        :param peer:
        :param resource_id:
        :return:
        """
    def change_peer_status(self, resource_id):
        """
        When a peers in a swarm report a change of status
        (leecher or seeder) then, get the swarm object from
        the swarm list, and update the status in the swarm of
        such peer.
        :param resource_id:
        :return:
        """

    def send_peers(self, requester_peer, resource_id):
        """
        Iterate the swarms list, and find the one which match with
        the resource id provided as a parameter. Then, extract the
        peers sharing this file in the swarm, and send their connection
        info (ip adresses and port) to the requested_peer.
        :param requester_peer: the peer that is requesting the info
        :param resource_id: the resource id to identify the swarm
               sharing this resource
        :return:
        """
        return None


