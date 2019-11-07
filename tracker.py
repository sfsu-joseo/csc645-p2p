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

    PORT = 12000
    IP_ADDRESS = "127.0.0.1"

    def __init__(self, ip_address = None, port = 0):
        """
        TODO: finish constructor implementation (if needed)
        If parameters ip_address and port are not set at the object creation time,
        you need to use the default IP address and the default port set in the class constants.
        :param ip_address:
        :param port:
        """
        Server.__init__(self)
        self.port = port
        self.ip = ip_address
        # the list of swarms that this tracker keeps
        self.swarms = []

    def add_swarm(self, swarm):
        """
        Already implemented
        Add a Swarm object to the swarms list of the tracker
        :param swarm:
        :return:
        """
        self.swarms.append(swarm)

    def remove_swarm(self, resource_id):
        """
        TODO: implement this method
        Given a resource id, remove the swarm from the tracker
        that is sharing this resource id.
        This happens normally when there is no seeder sharing
        this resource.
        :param resource_id:
        :return: VOID
        """
        pass

    def add_peer_to_swarm(self, peer, resource_id):
        """
        TODO: implement this method
        Based on the resource_id provided, iterate over the
        swarms list, and when resource_id matchs, add the
        new peer to the swarm.
        :param peer:
        :param resource_id:
        :return: VOID
        """
        pass

    def change_peer_status(self, resource_id):
        """
        TODO: implement this method
        When a peers in a swarm report a change of status
        (leecher or seeder) then, get the swarm object from
        the swarm list, and update the status in the swarm of
        such peer.
        :param resource_id:
        :return: VOID
        """
        pass

    def send_peers(self, peer_socket, resource_id):
        """
        TODO: implement this method
        Iterate the swarms list, and find the one which match with
        the resource id provided as a parameter. Then, serialize the
        swarm and send the swarm object to the peer requesting it.
        :param peer_socket: the peer socket that is requesting the info
        :param resource_id: the resource id to identify the swarm
               sharing this resource
        :return: VOID
        """
        pass


