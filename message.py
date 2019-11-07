# -*- coding: utf-8 -*-
""" The message
This file implements a message class for P2P BitTorrent Message Protocol used by the Peer protocol.
"""

class Message(object):
    """
    Note that for this assignment you are only required to create a basic implementation of the message protocol
    like the one described above. More complicated options of this protocol are out of the scope of csc645.
    """
    def __init__(self):

        # 1 chocked, 0 unchocked.
        # When a peer is chocking another peer means that the peer requesting the data is not
        # allowed to download data from the chocked peer. Chocked status is set automatically for multiple causes
        # such as congestion in the network, low uploads from the requester, no seeds in the swarm...
        self.chocked = 0

        # 1 interested, 0 not interested
        # When a peer is connected to a swarm, in order to start downloading data, the sender must be unchocked and the
        # receiver must be interested.
        self.interesed = 0

        # number of pieces downloaded so far. This is optional and dangerious because a malicious peer may use this
        # info to create a security treat in the swarm.
        self.have = 0

        # Only sent after the handshake. A list of bits representing the pieces already downloaded
        # bit set to 1 means that the piece is complete. Bit set to 0 means that the piece is missing or incompleted.
        # [1,0,1,0,1] means that the peer sending this message is missing piece with index 1, and 3. Indexes start at 0
        self.bitfield = []

        # request to the sender
        # index: integer specifying the zero-based piece index
        # begin: integer specifying the zero-based byte offset within the piece
        # length: integer specifying the requested length.
        self.request = {"index": 0, "begin": 0, "length": 0}

        # send block to another peer/s in the swarm
        # index: integer specifying the zero-based piece index
        # begin: integer specifying the zero-based byte offset within the piece
        # block: block of data, which is a subset of the piece specified by index.
        self.piece = {"index": 0, "begin": 0, "block": []}

        # Payload is similar to the request but is send to request the last block from a peer to complete a piece.
        self.cancel = {"index": 0, "begin": 0, "length": 0}

        # A keep alive message must be sent in order to keep the connection alive. If keep_alive is set to 0, and the
        # message contains payload, the reciever will accept the payload (if not chocked) and inmediatly will close
        # the connection with the sender (similar to HTTP:1.0/TCP non-persistent connections)
        self.keep_alive = 0




