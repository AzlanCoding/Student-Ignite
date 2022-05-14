import os
os.system("proxy")


'''import socket, sys
from threading import *
max_conn = 5
buffer_size = 8192
def start():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 9106))
    s.listen(max_conn)
  except Exception as error:
    print("An error occured")
    print(error)
  while True:
    try:
      conn, addr = s.accept()
      print("acceptted connection")
      data = conn.recv(buffer_size)
      #print(str(conn) +"\n"+ str(data) +"\n"+ str(addr))
      #threading.Thread(target=conn_string, args=(conn,data,addr)).start()
      conn_string(conn,data,addr)
    except KeyboardInterrupt:
      s.close()
      print("closed")
      sys.exit(1)
def conn_string(conn,data,addr):
  conn = conn
  #data = data.encode()
  addr = addr
  print(type(data))
  #Client Browser Request Appear here
  try:
    first_line = data.split(b'\n')[0]

    url = first_line.split(b' ')[1]

    http_pos = url.find(b"://")
    if (http_pos == -1):
      temp = url
    else:
      temp = url[(http_pos + 3):]#get rest of url

    port_pos = temp.find(b":")
    webserver_pos = temp.find(b"/")
    if webserver_pos == -1:
      webserver_pos = len(temp)
    webserver = ""
    port = -1
    if (port_pos == -1 or webserver_pos < port_pos):
      port = 80
      webserver = temp[:webserver_pos]
    else:
      port = int((temp[(port_pos + 1):])[:webserver_pos - port_pos - 1])
      webserver = temp[:port_pos]
    print(url)
    print(temp)
    print(webserver)
    proxy_server(webserver, port, conn, addr, data)
  except Exception as Error:
    print(Error)
    raise

def proxy_server(webserver, port, conn, addr, data):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((webserver,port))
    print(data)
    s.send(data)
    reply = s.recv(buffer_size)
    count = 0
    while True:

      if (len(reply) > 0 and count <= len(reply)):
          print(len(reply))
          print(reply[count])
          conn.send(reply)#send back data
          dar = float(len(reply))
          dar = float(dar / 1024)
          dar = "%.3s" % (str(dar))
          dar = "%s KB" % (dar)
          print("Request Completed: %s => %s <=" % (str(addr[0]),str(dar)))
          print("\n\n\n")
          count += 1
      else:
          print("err no reply")
          #break failed connection
          break
    s.close()
    conn.close()
  except Exception as E:
    s.close()
    conn.close()
    print("an err occured")
    print(E)
    raise
    sys.exit(1)
start()
'''
