# CSC645 Computer Networks:  P2P BitTorrent App Template 

## General
This template contains all the necesary classes and signature methods to get you started with this assignment. This
template is optional. So, you can also use your own design for this assignment. However, it is highly recomeneded to 
use this template for the assignment because methods in classes come with comments about how to implement them at
the high level. Note that you still will need to create your own methods or helper classes to provide some of 
the services and functionalities required for this assignments. For example, this template do not provide methods
to log in screen all the progresses when pieces and blocks are downloaded or uploaded by a peer,

## Compatibility
This template has been created with python 3.8, using PyCharm IDE. It has not been tested for Python versions below 3.0

## Cloning or Downloading 
You can download or clone this template in your local environment and then commit it to your class repository. Note that
this template. after commited to your repository, must be located in ~/applications/peer-to-peer-app/. 

## Notes about the template
* Methods that need to be implemented have a TODO comment like in the following example: 
  ```python
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
        Please don't forget to check for exceptions (try-catch) in this
        method because you'll be connecting to many peers at the same time.
        :param swarm: Swarm object returned from the tracker
        :return: True if the connection was succesfull. Otherwise, return False
        """
        return False
  ```
* The methods that have 'pass' instead of return are void methods. Remove the 'pass' keyword after you implement the method
All the other methods that return something are set as 'return None'. Please, once implemented set them to return the 
appropiates values or objects. Here is an example of a VOID method with 'pass' keyword 
   ```python
   def add_peer(self, peer):
        """
        TODO: implement this method
        :param peer: add the peer object
        :return: VOID
        """
        pass
   ```
* In this template, the Message class is also 'half' inplemented. The comments added there explain clearly
the services or functionality that every one of those fields provide to the protocol. Here is how it looks like:
```python
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

```

