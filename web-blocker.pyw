from datetime import *
from time import sleep
host_path = r"C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
websites = ['twitter.com','iamannitian.co.in','google.com','https://facebook.com']

# block the website between 12 am t0 132 pm
while True:
    if datetime(datetime.now().year, datetime.now().month,\
     datetime.now().day,0)< datetime.now() < \
     datetime(datetime.now().year, datetime.now().month, \
     datetime.now().day,23): 
      print("working hour")
      with open (host_path,"r+",) as file_ptr:
        content = file_ptr.read()
        for website in websites:
            if website in content:
                pass
            else:
                file_ptr.write(redirect+"   "+website+"\n")
    else:
        with open(host_path,'r+') as file:  
            content = file.readlines();  
            file.seek(0)  
            for line in content:  
                if not any(website in line for website in websites):  
                    file.write(line)  
            file.truncate() 
    sleep(5)



   