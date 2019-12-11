import socket
import gc
gSocket = '' #to store the answering socket
handeler = {} #to store handelers ( key --> path requested, value --> [function to be exuted, its parameters])
resources = '' #to store the resources path


def analyze(req): #returns a tuple (the path requested,{key:value}})
    if len(req) < 5 : return (None,{})
    index = 5
    data = ""
    dataObj = {}
    key = ''
    path = ''
    #print(req)
    while True :
        if req[index] == 63 :   #?
            if len(data) == 0 :
                path = '/'
            else :
                path = data
            data = ''
            index += 1
        elif req[index] == 61 : #=
            key = data
            data = ''
            index += 1
        elif req[index] == 38 : #&
            dataObj[key] = data
            data = ""
            index += 1
        elif req[index] == 32 : #space
            #print(" space found ")
            if len(data) == 0 and len(path) == 0 :
                #print("path is / ")
                path = "/"
            elif len(key) > 0 : dataObj[key] = data
            else : path = data
            break
        else :
            data += chr(req[index])
            index += 1
    print((path,dataObj))
    return (path,dataObj)

def handel(path,parm_dict,socket): #is called to handel the path (check if it's available in handeler)
    global gSocket,resources
    gSocket = socket
    if path in handeler:
        parm = handeler[path][1]
        handeler[path][0](parm,parm_dict) #handeler is a dictionary where the key is the path and the value is a list the first item is the function and the second item is its parameters
        print("DONE")
    else :
		#print("resource file is : " + resources)
		try:
			file = open(resources+path,"r")
			#try:
			while True :
				d = file.read(1024)
				if len(d) == 0 : break
				socket.write(d)
				del d
				gc.collect()
			print("DONE")
			#except:
			#	print('error happend while writing to socket 0x2')
		except :
			gSocket.write("404 file not found")
			print("ERROR File not found")

def run_server(port) : #used to start the server
	addr = socket.getaddrinfo("0.0.0.0",port)[0][-1]
	s = socket.socket()
	s.bind(addr)
	s.listen(3)
	while True:
#		try:
		res = s.accept()
		client_s = res[0]
		client_addr = res[1]
		print("client address: ",client_addr)
		req = client_s.recv(1024)
		client_s.write("HTTP/1.0 200 OK \r\n\r\n")
		path,object = analyze(req)
		handel(path,object,client_s)
		client_s.close()
#		except:
#			print('error happend 0x01')

def serve(name,_) : #used to send files to the client (html files, imgs, js files)
	global resources
	print("openning : " + resources+name)
	f = open(resources+name,"r")
	try:
		while True :
			d = f.read(1024)
			if len(d) == 0 : break
			gSocket.write(d)
			del d
			gc.collect()
		gSocket.close()
	except:
		print('error happend while writing to socket 0x3')

def sendJson(jsonGen,_):
    gSocket.write(jsonGen())

def setHandeler(functions): #used to add handelers in handel (handel format {'key' : [function,parameters]})
    for key in functions :
        handeler[key] = functions[key]

def set_resource_folder(path): #set the folder of the website
	global resources
	resources = path+'/'
