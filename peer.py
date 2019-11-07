# -*- coding: utf-8 -*-
""" The peer """
from server import Server
from client import Client

class Peer(Client, Server):

    # status
    PEER = 0
    SEEDER = 1
    LEECHER = 2

    def __init__(self, max_upload_rate, max_download_rate):
        """
        TODO: implement the class constructor
        """
        Server.__init__(self) # inherites methods from Server class
        Client.__init__(self) # inherites methods from Client class
        self.status = self.PEER
        self.chocked = False
        self.interested = False
        self.max_download_rate = max_download_rate
        self.max_upload_rate = max_upload_rate

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
        :return: the swarm object with all the info from the peers connected to the swarm
        """
        return None

    def connect_to_swarm(self, swarm):
        """
        TODO: implement this method
        This method will create a socket (TCP) connection
        with all the peers in the swarm sharing the requested
        resource.
        Take into consideration that even if you are connected
        to the swarm. You do not become a leecher until you set
        your status to interested, and at least one of the leechers
        or seeders in the swarm is not chocked.
        :param swarm: Swarm object returned from the tracker
        :return: VOID
        """
        pass

    def upload_rate(self):
        """
        TODO: implement this method
        Compute the actual upload rate using the formule from assignment docs
        This needs to be re-evaluated every 30 seconds approximatly
        :return: the new upload_rate
        """
        return None

    def download_rate(self):
        """
        TODO: implement this method
        Compute the actual download rate using the formule from assignment docs
        This needs to be re-evaluated every 30 seconds approximatly
        :return: the new download rate
        """
        return None


    def get_metainfo(self, torrent_path):
        """
        TODO: implement this method
        (1) Create an empty resource object
        (2) call the method parse_metainfo() from that object
            which must return all the fields and values from
            the metainfo file, including the hashes from the
            file pieces.
        :param torrent_path:
        :return: the metainfo
        """
        return None

    def change_role(self, new_role):
        """
        TODO: implement this method
        When a peer is interested in downloading a pieces of
        a resource, and the seeder or leecher sharing the resource
        is not chocked, then the peer becomes a leecher. When the
        leecher already have all the completed files from the file
        it becomes a seeder.
        :param new_role: use class constants: PEER, SEEDER or LEECHER
        :return: VOID
        """
        pass

    def send_message(self, block, start_index = -1, end_index = -1):
        """
        TODO: implement this method
        (1) Create a message object from the message class
        (2) Set all the properties of the message object
        (3) If the start index and end_index are not negative
            then, that means that the block needs to be sent
            in parts. implement that situations too.
        (4) Don't forget to check for exceptions with try-catch
            before sending messages. Also, don't forget to
            serialize the message object before being sent
        :param block: a block object from the Block class
        :param start_index: the start index (if any) of the data being sent
        :param end_index: the end index of the data being sent
        :return: VOID
        """
        pass

    def recieve_message(self):
        """
        TODO: implement this method
        (1) recieve the message
        (2) inspect the message (i.e does it have payload)
        (4) If this was the last block of a piece, then you need
            to compare the piece with the sha1 from the torrent file
            if is the same hash, then you have a complete piece. So, set
            the piece object related to that piece to completed.
        (5) Save the piece data in the downloads file.
        (6) Start sharing the piece with other peers.
        :return: VOID
        """
        pass

    def get_top_four_peers(self):
        """
        TODO: implement this method
        Since we are implementing the 'tit-for-tat' algorithm
        which upload data to the top 4 peers in the swarm (max rate upload peers)
        then this method will inspect the swarm object returned by the tracker
        and will get the 4 top peers with highest upload rates. This method needs to
        be re-evaluated every 30 seconds.
        :return: a list of the 4 top peers in the swarm
        """
        self.top_four = []
        # your implementation here
        return self.top_four

    def verify_piece_downloaded(self, piece):
        """
        TODO: implement this method
        :param piece: the piece object of this piece
        :return: true if the piece is verified and is not corrupted, otherwisem, return false
        """
        return False

    def is_chocked(self):
        """
        Already implemented
        :return:
        """
        return self.chocked

    def is_interested(self):
        """
        Already implemented
        :return:
        """
        return self.interested

    def chocked(self):
        """
        Already implemented
        :return: VOID
        """
        self.chocked = True

    def unchocked(self):
        """
        Already implemented
        :return: VOID
        """
        self.chocked = False

    def interested(self):
        """
        Already implemented
        :return: VOID
        """
        self.interested = True

    def not_interested(self):
        """

        Already implemented
        :return: VOID
        """
        self.interested = False

