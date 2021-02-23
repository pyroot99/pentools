## PenTools
This repo consists of scripts that i build while learning to make tools in python3**

### 1. iprecon.py
+ This [script](./iprecon.py) takes the url as input and returns ip address and location information of the host.
![iprecon example](./img/iprecon.png)  

### 2. client.py
+ This [script](./server/client.py) takes the port number as input and connects to that port on localhost

### 3. server.py
+ This [script](./server/server.py) takes the port number as input and listens for connection on that port on localhost
+ The Server also acknowledges the data that receives.
![client/server](./img/client_server.gif)

### 4. subfuzz.py
+ This [script](./subfuzz/subfuzz.py) is a simple subdomain bruteforcer takes url and a file containing subdomains in each line.
![subfuzz.py](./img/subfuzz.gif)

### 5. md5crack.py
+ [md5crack.py](./md5crack/md5crack.py) is a simple md5hash cracker written in python3 it takes two arguments hash and wordlist and returns the word from the hash if cracked.
![md5crack.py](./img/md5crack.png)

### 6. chmac.py
+ [chmac.py](./chmac.py) is a simple mac changer works with linux os.
+ It is written in python, It takes interface and macaddress as arguments and changes the macaddress to the given macaddress.
+ This script can calculate its own random macaddress if macaddress is not given.
