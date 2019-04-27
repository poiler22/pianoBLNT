# Import socket module 
import socket                
import lightLED
# Create a socket object
lightLED.colorWipeClear(lightLED.strip) 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
s.connect(('192.168.43.20', port)) 
  
# receive data from the server


while True:
	isOff = False
	x = s.recv(1024)
	result = x.split("\n")
	set_X = set(result)
	list_X = list(set_X)
	for item in list_X:
		if "off" in item:
			isOff = True
	
	if isOff == True:
		a = [i for i in list_X if "off" in i]
		b = [(i.split(":"))[0] for i in a]	
		for i in b:
			lightLED.colorWipe(lightLED.strip,int(i) - 21, lightLED.Color(0,0,0))
				
	else:
		a = [i for i in list_X if "on" in i]
		b = [(i.split(":"))[0] for i in a]
		for i in b:
			lightLED.colorWipe(lightLED.strip,int(i) - 21, lightLED.Color(20,255,147))
			
		
		 					





'''
while True:
	x = s.recv(1024)
	#u = x.index(":")
	print(x)
	if "on" in x:
		for a in range(0,15):
			x = x.replace(":on", ",")
		x = x.rstrip(",")
		z = x.strip(":,on")
		z = z.split(",")
		print(z)
		for valued in set(z):
			#print(valued)
			lightLED.colorWipe(lightLED.strip,int(valued) - 21, lightLED.Color(255,0,0))
	elif "off" in x:
		for a in range(0,15):
			x = x.replace(":off", ",")
		x = x.rstrip(",")
		p = x.strip(":,off")
		p = p.split(",")
		print(p)
		for valued in set(p):
			#print(valued)
			lightLED.colorWipe(lightLED.strip,int(valued) - 21, lightLED.Color(0,0,0))
'''
		



'''

while True:
	x = s.recv(1024)
	print('data1 is ' + str((x.split(','))[0])) 
	print('data2 is ' + str((x.split(','))[1])) 
	if int((x.split(','))[1]) == 100:
		print("on")
		lightLED.colorWipe(lightLED.strip,int(((s.recv(1024)).split(','))[0]) - 21, lightLED.Color(255,0,0))
	if int((x.split(','))[1]) == 0:
		lightLED.colorWipe(lightLED.strip,int(((s.recv(1024)).split(','))[0]) - 21, lightLED.Color(0,0,0))
		print("off")


'''
# close the connection 
s.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               