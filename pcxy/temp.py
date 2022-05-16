import proxy_server
from proxy_server import Server
import socket
import threading
import signal
import sys
import pdb
import logging
import logging.config
import pthread
import config
logging.config.fileConfig('logging.conf')
proxy_logger = logging.getLogger('proxy')
server = Server(config)
server.listenForClient()
