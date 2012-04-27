from collections import namedtuple
import warnings

try:
    import zmqrpc as rpc
except ImportError:
    warnings.warn("WARNING: Using pure Python socket RPC implementation instead of zmq. This will not affect you if your not running locust in distributed mode, but if you are, we recommend you to install the python packages: pyzmq and gevent-zeromq")
    import socketrpc as rpc

class Message:
        def __init__(self, type, data, node_id):
                self.type=type
                self.data=data
                self.node_id=node_id
