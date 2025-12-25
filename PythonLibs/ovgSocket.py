import socket
from threading import Thread
import zmq
import time
import json

########## AUX FUNCTIONS ##########



#---------------------------------------------------------------

#returns a string
def recvMessage(socket):
    socket.send_string("getMOParams")
    return socket.recv_string()

#OVGRL -> Overgrowth reinforcment learning Object
#returns a simple one level deep json like object aka dictionary
def recvOVGRLObject(socket):
    OVGRLObject = {}
    movementObjects = json.loads(recvMessage(socket))
    for entity in {'player','enemy'}:
        OVGRLObject[entity] = {}
        OVGRLObject[entity]['permHealth'] = -1
        OVGRLObject[entity]['tempHealth'] = -1
        OVGRLObject[entity]['koShield'] = -1
        OVGRLObject[entity]['isKnockedOut'] = -1

    for obj in movementObjects:
        if obj['is_player']:
            OVGRLObject['player']['permHealth'] = obj['perm_health']
            OVGRLObject['player']['tempHealth'] = obj['temp_health']
            OVGRLObject['player']['koShield'] = obj['ko_shield']
            OVGRLObject['player']['isKnockedOut'] = obj['is_knocked_out']
        else:
            # OVGRLObject['enemies'][obj['id']] = {}
            # OVGRLObject['enemies'][obj['id']]['permHealth'] = obj['perm_health']
            # OVGRLObject['enemies'][obj['id']]['tempHealth'] = obj['temp_health']
            # OVGRLObject['enemies'][obj['id']]['isKnockedOut'] = obj['is_knocked_out']
            OVGRLObject['enemies']['permHealth'] = obj['perm_health']
            OVGRLObject['enemies']['tempHealth'] = obj['temp_health']
            OVGRLObject['enemies']['koShield'] = obj['ko_shield']
            OVGRLObject['enemies']['isKnockedOut'] = obj['is_knocked_out']
    
    return OVGRLObject


def sendMessage(connection,message):
    connection.send((str(len(message)) + '@').encode())
    connection.send(message.encode())

def sendObject(connection,dataType,name,message):
    sendMessage(connection,dataType)
    sendMessage(connection,name)
    sendMessage(connection,message)

def sendDSRLObject(connection,Object):
    objectLength = len(Object)
    currentDataType = ''
    
    if objectLength == 0:
        return

    sendObject(connection,'integer','_length',str(objectLength))
    

    for key,value in Object.items():
        if type(value) == int:
            currentDataType = 'integer'
        elif type(value) == float:
            currentDataType = 'float'
        elif type(value) == str:
            currentDataType = 'string'

        sendObject(connection,currentDataType,key,str(value))


def createServer(port,callback):
    connectionThreads = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',port))
    sock.listen()
    
    while True:
        print('Waiting for connection...')
        conn, addr = sock.accept()
        print('Connected by', addr)
        currentConnectionThread = Thread(target = callback, args = [conn])
        currentConnectionThread.start()
        connectionThreads.append(currentConnectionThread)

def connectToServer(connectionString):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(connectionString)
    return socket



    
    
