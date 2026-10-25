# Program: Port Classifier
# Description: Classifies a port number by range and identifies
# the service for ports 22, 80, and 443.
port = int(input("Port?:"))
if port < 0 or port > 65535:
    print("Invalid port,Use number between 0 and 65535")
elif port <= 1023:
    print("Range:System")
elif port <= 49151:
    print("Range:User")
else:
    print("Range:dynamic or private")        
if 0<=port<=65535:
    if port == 22:
        print("Service:ssh")
    elif port == 80:  
        print("Service:http")  
    elif port == 443:
        print("Service:https")

    
