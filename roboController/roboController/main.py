import sys
from socketIO_client import SocketIO, LoggingNamespace

def on_connect():
  print('connected to ECE183')
  sys.stdout.flush()
  socketIO.emit('uplink', 'roboController')

def on_reconnect():
  print('reconnected to ECE183')
  sys.stdout.flush()
  socketIO.emit('uplink', 'roboController')

def on_up():
  pass

def on_down():
  pass

def on_left():
  pass

def on_right():
  pass

URL = "egorv1.herokuapp.com"
with SocketIO(URL, 80) as socketIO:
    socketIO.on('connect', on_connect)
    socketIO.on('reconnect', on_reconnect)
    socketIO.on('up', on_up)
    socketIO.on('down', on_down)
    socketIO.on('left', on_left)
    socketIO.on('right', on_right)
    #socketIO.off('disconnect')
    socketIO.wait()
