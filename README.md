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
In this task we had to implement a function called 
```python
compute_checksum(source_port: int, dest_port: int, payload: bytearray) -> int
```
this function will look at the packet headers and convert them to 2 bytes and will add the headers in binary so that we can perform a ones complement upon the total bytes array given. at the end of the function it will return an int which we will use to compare to the given checksum value received in the packet from communication. if they match the packet is not corrupted and is valid.

**You can run my udp.py script in the "Task 2" folder which contains the python file you can run to test the checksum on the packet there is also a test.py that can be run to test the checksum function, make sure the other files in this folder are present for programs to successfully work. These scripts where tested upon Python 3.8.7 upon the "csctcloud.uwe.ac.uk" server.**

## Task 3
In this task