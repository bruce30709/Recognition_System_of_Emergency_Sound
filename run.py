from bluetooth import *
import os
server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ]
                    )

print("Waiting for connection on RFCOMM channel %d" % port)
try:
    while True:

        client_sock, client_info = server_sock.accept()

        print("Accepted connection from ", client_info)
		
        data = client_sock.recv(1024)
        print(data)
        if data == bytes([0x01]): 
            f2 = open('C:/Users/user/Desktop/detect/exit.txt', 'w')
            f2.close()
        if len(data) == 0: break
        f = open('C:/Users/user/Desktop/detect/flag.txt', 'r')
        
        if int(f.read()) >= 70:
            client_sock.send("3")
        os.remove('C:/Users/user/Desktop/detect/exit.txt')
        
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")