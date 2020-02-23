import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
soc.bind(('192.168.1.109',5000))
soc.listen(1)


print("waiting for clients")

while True:
	conn,addr = soc.accept()
	# conn.send("Test\r\n".encode())
	print("connected to client")
	data = conn.recv(256)
	print((data))
	if len(data) > 5:
		if data[-1] == 35:
			print("OK     :", data)
		else :
			print("ERROR  :", data)
	# print(data, "Length", len(data))
	conn.close()