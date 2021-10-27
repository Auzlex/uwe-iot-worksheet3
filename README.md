# UWE Assignment Year 2 | Internet Of Things | Worksheet 3

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

Here is my compute checksum function:
```python
def compute_checksum( source_port:int, dest_port:int, payload:bytearray ):
    """calculates the checksum value to validate a packet"""

    checksum = 0                # checksum value
    length = 8 + len(payload)   # header plus payload length

    source_port_bytes = source_port.to_bytes(2, byteorder='little')     # convert the source port to 2 bytes
    dest_port_bytes = dest_port.to_bytes(2, byteorder='little')         # convert the destination port to 2 bytes
    size_bytes = length.to_bytes(2, byteorder='little')                 # convert the length of the packet to 2 bytes
    checksum_bytes = checksum.to_bytes(2, byteorder='little')           # convert checksum to 2 bytes

    # sum of the packet in bytes
    total_binary_of_packet = source_port_bytes + dest_port_bytes + size_bytes + checksum_bytes + payload

    # check if the sum of the bytes is a multiple of 2,
    if len(total_binary_of_packet) % 2 != 0:
        total_binary_of_packet += struct.pack("!B",0) # append zero byte

    # iterate over the byte array at 2 bytes at a time
    for i in range( 0, length, 2 ):
        # append the value to the checksum variable
        checksum += (total_binary_of_packet[i] << 8) + (total_binary_of_packet[i + 1])

    # perform ones complement
    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum = ~checksum & 0xFFFF

    # return checksum value
    return checksum
```
here is my test output results for task 2:
```python
testing checksums



testing packet checksum
Base64: b'CgAqACEAyztXZWxjb21lIHRvIElvVCBVRFAgU2VydmVy'
UDP: b'\n\x00*\x00!\x00\xcb;Welcome to IoT UDP Server'
source-port: 10
dest-port: 42
data-len: 33
checksum: 15307
checksum_computed: 15307
payload: 'Welcome to IoT UDP Server'
packet is VALID and not corrupted

finished testing checksums ALL passed!
```

**You can run my udp.py script in the "Task 2" folder which contains the python file you can run to test the checksum on the packet there is also a test.py that can be run to test the checksum function, make sure the other files in this folder are present for programs to successfully work. These scripts where tested upon Python 3.8.7 upon the "csctcloud.uwe.ac.uk" server.**

## Task 3
In this task we had to implement and add a new function called
```python
await send_packet(websocket, 0, 542, b'1111')
```
This function will use the already connected websocket to send a packet that will be constructed using "little endian" and encoded in base64 before being sent to the server. In this example we are going to pass in a source port, destination port and our payload of "1111" which will instruct the server to return the current time in 24hour format.

Here is my send packet function
```python
async def send_packet(websocket, source_port:int, dest_port:int, payload:bytearray):

    # construct a packet
    # convert the given source and destination ports into bytes
    source_port_bytes = source_port.to_bytes(2,byteorder='little')
    dest_port_bytes = dest_port.to_bytes(2,byteorder='little')
    checksum_bytes = compute_checksum(source_port, dest_port, payload).to_bytes(2,byteorder='little')

    # size of the packet to bytes
    size = (8 + len(payload)).to_bytes(2,byteorder='little')
    
    # construct packet in bytes/binary :: packet as follows source,dest,size,checksum,payload
    constructed_packet = source_port_bytes + dest_port_bytes + size + checksum_bytes + payload

    # encode packet base 64
    encoded_packet = base64.b64encode(constructed_packet)

    # send the encoded packet to the server
    await websocket.send(encoded_packet)
```
Note: The test file for send packet will compare the received time to the os time, so if time zones are not correct with the server testing may fail. 

Here are my test results for task 3
```python
testing checksums



testing packet time validation
Base64: b'CgAqACEAyztXZWxjb21lIHRvIElvVCBVRFAgU2VydmVy'
UDP: b'\n\x00*\x00!\x00\xcb;Welcome to IoT UDP Server'
source-port: 10
dest-port: 42
data-len: 33
checksum: 15307
checksum_computed: 15307
payload: 'Welcome to IoT UDP Server'
packet is VALID


sending constructed packet
sent packet
Base64: b'HgIAABAAIf8xNjoyNToyOQ=='
UDP: b'\x1e\x02\x00\x00\x10\x00!\xff16:25:29'
source-port: 542
dest-port: 0
data-len: 16
checksum: 65313
checksum_computed: 65313
payload: '16:25:29'
packet is VALID


os: 16:25:29 server: 16:25:29
passed

finished testing checksums ALL passed!
```

**You can run my udp.py && test.py script in the "Task 3" folder which contains the python files, make sure the other files in this folder are present for programs to successfully work. These scripts where tested upon Python 3.8.7 upon the "csctcloud.uwe.ac.uk" server.**
