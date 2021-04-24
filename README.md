# iot-worksheet3

This gitlab contains the work for worksheet 3 for internet of things module at UWE.

## Contents
1. [Task 1](#Task-1)
2. [Task 2](#Task-2)
3. [Task 3](#Task-3)

## Task 1
In this task we had to program a simple client receiver that will take the welcome message from the UDP server that we connected to using websockets, using the given URI:
```python
uri = "ws://localhost:5612"
```
This simple program will not do any sort of error checking just simply displaying the contents of the packet if available. Which can be seen here below:
```python
Base64: b'CgAqACEAyztXZWxjb21lIHRvIElvVCBVRFAgU2VydmVy'
UDP: b'\n\x00*\x00!\x00\xcb;Welcome to IoT UDP Server'
source-port: 10
dest-port: 42
data-len: 33
checksum: 15307
payload: 'Welcome to IoT UDP Server'
```

**You can run my udp.py script in the "Task 1" folder which contains the python file you can run, make sure the other files in this folder are present for programs to successfully work. These scripts where tested upon Python 3.8.7 upon the "csctcloud.uwe.ac.uk" server.**


## Task 2
In this task

## Task 3
In this task