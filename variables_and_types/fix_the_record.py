# fix_the_record.py
# This program prints a short record about a network device.
device_name = "edge-router"
#The var start with num 
#2nd_ip = "192.0.2.1"   
sec_ip="192.0.2.1"
#class is keyword
#class = "router"
device_class = "router"
#int() change only string number like "22"
#port = int("twenty-two")
port=int("22")
#in print statment device_name is uncorrect so it's undefined
#print("Device:", device_nam)
print("Device:",device_name)
#we use 2nd_ip
#print("Backup IP:", 2nd_ip)
print("Backup IP:",sec_ip)
#like we say class is keyword
#print("Type:", class)
print("Type:",device_class)
print("Port:", port)
