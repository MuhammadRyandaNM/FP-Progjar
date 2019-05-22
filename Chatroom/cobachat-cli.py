import socket
import os
import json
import datetime

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889

class ChatClient:
	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = (TARGET_IP,TARGET_PORT)
		self.sock.connect(self.server_address)
		self.tokenid=""

	def proses(self,cmdline):
		j=cmdline.strip().split(" ")

		try:
			command=j[0]
			if (command=='auth'):
				username=j[1]
				password=j[2]
				return self.login(username,password)

			elif (command=='send'):
				usernameto = j[1]
				message=""
				for w in j[2:]:
					message="{} {}" . format(message,w)
				return self.sendmessage(usernameto,message)

			elif (command=='inbox'):
				return self.inbox()

			elif (command == 'logout'):
				return self.logout()

			elif (command == 'join_group'):
				group_token = j[1]
				return self.join_group(group_token)

			elif (command == 'leave_group'):
				group_token = j[1]
				return self.leave_group(group_token)

			elif (command == 'create_group'):
				group_name = j[1]
				return self.create_group(group_name)

			elif (command == 'inbox_group'):
				group_name = j[1]
				return self.inbox_group(group_name)

			elif (command == 'list_group'):
				group_name = j[1]
				return self.list_group(group_name)

			elif (command == 'send_group'):
				group_token = j[1]
				message=""
				for w in j[2:]:
					message="{} {}" . format(message, w)
				return self.send_group(group_token, message)

			elif (command == 'send_file'):
				usernameto = j[1]
				filename = j[2]
				return self.send_file(usernameto, filename)

			elif (command == 'download_file'):
				filename = j[1]
				return self.download_file(filename)

			elif (command == 'ls'):
				return self.ls()

			else:
				return "*Maaf, command tidak benar"

		except IndexError:
			return "-Maaf, command tidak benar"


	# NOT FULLY INMPLEMENTED
	def send_file(self,source,destination, filename):
		if not os.path.exists(destination):
			os.mkdir(destination)

		completeName = os.path.join(destination, imgname)
		# print completeName
		fp = open(completeName, "rb")
		pckg = fp.read()
		sizeSent = 0
		fp.close()
		sock.sendto(("START " + imgname).ljust(1024))
		iterate=(len(pckg)/BUFSIZE)
		for i in range(iterate + 1):
			data = []
			if (i+1)*BUFSIZE > len(pckg):
				data = pckg[i*BUFSIZE:len(pckg)]
				sizeSent += len(data)
				data.ljust(1024)
			else:
				data = pckg[i*BUFSIZE:(i+1)*BUFSIZE]
				sizeSent += len(data)
			sock.sendto(data, addr)
			print "Sending "+str(sizeSent) + "/" + str(len(pckg)) + " bytes To " + str(addr[0]) + ":" + str(addr[1])
		sock.sendto(("END " + imgname).ljust(1024), addr)

	def rcvFiles(self,destination,filename):
		fp = None
		fileName = None
		received = 0

		sock.sendto("REQ", (SERVER_IP, SERVER_PORT))
		print "Request Sent"
		while True:
		    data, addr = sock.recvfrom(BUFSIZE)
		    if data[:5] == "START":
		        fileName = data[6:].replace(" ", "")
		        received = 0
		        completeName = os.path.join(mypath, fileName)
		        fp = open(completeName, "wb+")
		        print "Receiving " + fileName
		    elif data[:3] == "END":
		        print fileName + " Received"
		        fp.close()
		    elif data[:5] == "CLOSE":
		        print "Terminating Connection"
		        break
		    else:
		        
		        fp.write(data)
		        received += len(data)
		        print "Receiving "+ str(received) +" bytes of data"
		print "Request Finished"
	def sendstring(self,string):
		try:
			self.sock.sendall(string)
			receivemsg = ""
			while True:
				data = self.sock.recv(10)
				if (data):
					receivemsg = "{}{}" . format(receivemsg,data)
					if receivemsg[-4:]=="\r\n\r\n":
						return json.loads(receivemsg)
		except:
			self.sock.close()

	def login(self,username,password):
		if(self.tokenid!=""):
			return "Error, authorized already"
		string="auth {} {} \r\n" . format(username,password)
		result = self.sendstring(string)

		if result['status']=='OK':
			self.tokenid=result['tokenid']
			return "username {} logged in, token {} " .format(username,self.tokenid)
		else:
			return "Error, {}" . format(result['message'])

	def sendmessage(self,usernameto="xxx",message="xxx"):
		if (self.tokenid==""):
			return "Error, not authorized"
		string="send {} {} {} \r\n" . format(self.tokenid,usernameto,message)
		result = self.sendstring(string)

		if result['status']=='OK':
			return "message sent to {}" . format(usernameto)
		else:
			return "Error, {}" . format(result['message'])

	def inbox(self):
		if (self.tokenid==""):
			return "Error, not authorized"
		string="inbox {} \r\n" . format(self.tokenid)
		result = self.sendstring(string)

		if result['status']=='OK':
			return "{}" . format(json.dumps(result['messages']))
		else:
			return "Error, {}" . format(result['message'])

	def logout(self):
		if (self.tokenid==""):
			return "Error, not authorized"
		string = "logout {} \r\n" . format(self.tokenid)
		result = self.sendstring(string)

		if result['status']=='OK':
			self.tokenid = ""
			return "{}" . format(result['message'])
		else:
			return "Error, {}" . format(result['message'])

	def create_group(self, group_name):
		if (self.tokenid==""):
			return "Error, not authorized"
		string = "create_group {} {} \r\n" . format(self.tokenid, group_name)
		result = self.sendstring(string)

		if result['status']=='OK':
			return "{}" . format(result['messages'])
		else:
			return "Error, {}" . format(json.dumps(result['messages']))

	def join_group(self, group_token):
		if (self.tokenid==""):
			return "Error, not authorized"
		string = "join_group {} {} \r\n" . format(self.tokenid, group_token)
		result = self.sendstring(string)

		if result['status']=='OK':
			return "{}" . format(result['message'])
		else:
			return "Error, {}" . format(result['message'])

	def leave_group(self, group_token):
		if (self.tokenid==""):
			return "Error, not authorized"
		string = "leave_group {} {} \r\n" . format(self.tokenid, group_token)
		result = self.sendstring(string)

		if result['status']=='OK':
			return "{}" . format(result['message'])
		else:
			return "Error, {}" . format(result['message'])

	def inbox_group(self, group_token):
		if (self.tokenid==""):
			return "Error, not authorized"
		string = "inbox_group {} {} \r\n" . format(self.tokenid, group_token)
		result = self.sendstring(string)

		if result['status']=='OK':
			return "{}" . format(json.dumps(result['messages']))
		else:
			return "Error, {}" . format(result['message'])

	def send_group(self, group_token, message):
		if (self.tokenid==""):
			return "Error, not authorized"
		string = "send_group {} {} {} \r\n" . format(self.tokenid, group_token, message)
		result = self.sendstring(string)

		if result['status']=='OK':
			return "{}" . format(result['message'])
		else:
			return "Error, {}" . format(result['message'])

if __name__=="__main__":
	cc = ChatClient()
	while True:
		cmdline = raw_input("Command: ")
		print cc.proses(cmdline)
