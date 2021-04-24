"""
    This is a script for Internet Of Things Worksheet 3 Task 3
"""
"""
    import python modules
"""
import asyncio
import struct
import websockets
import json
import time
import base64

#from struct import *
from aioconsole import ainput, aprint

def compute_checksum( source_port:int, dest_port:int, payload:bytearray ):
    """calculates the checksum value to validate a packet"""

    checksum = 0                # checksum value
    length = 8 + len(payload)   # header plus payload length

    #print("source_port","{:08b}".format(int(source_port_bytes.hex(),16)))

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

async def recv_packet(websocket):
    """awaits for packet from websocket recv() and returns a base64 decoded packet"""

    # wait for packet to be received
    packet = await websocket.recv()

    # print the base64 packet to meet task 1 requirements
    print(f"Base64: {packet}")

    # return decoded message
    return base64.b64decode(packet)

async def recv_and_decode_packet(websocket):
    """awaits for receive of packet from websocket and outputs its contents"""

    # await for packet receive and decode
    packet = await recv_packet(websocket)

    # get the length of the packet
    length = int.from_bytes(packet[4:6],'little')

    # get the source port
    source_port = int.from_bytes(packet[0:2],'little')

    # get the dest port
    dest_port = int.from_bytes(packet[2:4],'little')

    # the packet checksum
    checksum = int.from_bytes(packet[6:8],'little')

    # content of the packet
    payload = packet[8:(length+8)]
    payload_decoded = payload.decode("utf-8")

    # invoke the compute checksum
    checksum_computed = compute_checksum( source_port, dest_port, payload )

    print(f"UDP: {packet}\nsource-port: {source_port}\ndest-port: {dest_port}\ndata-len: {length}\nchecksum: {checksum}\nchecksum_computed: {checksum_computed}\npayload: '{payload_decoded}'")

    # validate checksum
    if checksum == checksum_computed:
        print("packet is VALID")
    else:
        print("[WARNING] packet is NOT valid its corrupted")

    print("\n")

    return payload_decoded # return payload decoded

async def send_packet(websocket, source_port:int, dest_port:int, payload:bytearray):

    # construct a packet

    # convert the given source and destination ports into bytes
    source_port_bytes = source_port.to_bytes(2,byteorder='little')
    dest_port_bytes = dest_port.to_bytes(2,byteorder='little')
    checksum_bytes = compute_checksum(source_port, dest_port, payload).to_bytes(2,byteorder='little')

    # size of the packet
    size = (8 + len(payload)).to_bytes(2,byteorder='little')
    
    # construct packet in bytes/binary
    constructed_packet = source_port_bytes + dest_port_bytes + size + checksum_bytes + payload

    # encode packet base 64
    encoded_packet = base64.b64encode(constructed_packet)

    # send the encoded packet to the server
    print("sending constructed packet")
    await websocket.send(encoded_packet)
    print("sent packet")

async def main():
    """establishes connection with uri using a web socket and awaits for recv_and_decode_packet(websocket)"""

    # uri to connect to the server
    uri = "ws://localhost:5612"

    # an asynchronous web socket
    async with websockets.connect(uri) as websocket:

        # await for recv and decode function to execute
        await recv_and_decode_packet(websocket)

        # for ever
        while True:
            
            # send packet to the server
            await send_packet(websocket, 0, 542, b'1111')

            # await for receiver
            await recv_and_decode_packet(websocket)

            # wait a second
            time.sleep(1)


async def main_test():
    """establishes connection with uri using a web socket and awaits for send_packet() and recv_and_decode_packet()"""

    # uri to connect to the server
    uri = "ws://localhost:5612"

    # an asynchronous web socket
    async with websockets.connect(uri) as websocket:

        # await for recv and decode function to execute
        await recv_and_decode_packet(websocket)

        # send packet to the server
        await send_packet(websocket, 0, 542, b'1111')

        # await for receiver
        payload_decoded = await recv_and_decode_packet(websocket)

        return payload_decoded

def run():

    # begin running async code
    asyncio.get_event_loop().run_until_complete(main())

def run_test():
    # begin running async code
    return asyncio.get_event_loop().run_until_complete(main_test())

# if this the entry point of the script
if __name__ == "__main__":

    # begin running async code
    run()