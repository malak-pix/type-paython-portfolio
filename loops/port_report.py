#port_report.py
#Report the IANA range category for a sequence of ports
start_port = int(input("Start port:"))
end_port = int(input("End port:"))
count =0
for port in range(start_port, end_port+1):
    count+=1
    if 0<=port<=1023:
        category ="system" 
    elif 1024<=port<=49151:
        category ="user"
    else:
        category ="dynamic"
    print (f"{port}: {category}")   
print(f"Ports checked:{count}")     


