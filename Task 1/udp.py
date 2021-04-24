"""
    This is a script for Internet Of Things Worksheet 3 Task 1
"""
"""
    import python modules
"""
import asyncio
import websockets
import json
import time
import base64

from struct import *
from aioconsole import ainput, aprint

async def recv_packet(websocket):
    """recv_packet(websocket) -> b64decoded_packet"""

    # wait for packet to be received
    packet = await websocket.recv()

    # print the base64 packet to meet task 1 requirements
    print(f"Base64: {packet}")

    # return decoded message
    return base64.b64decode(packet)

async def recv_and_decode_packet(websocket):
    """ recv_and_decode_packet(websocket) -> None, awaits for receive of packet from websocket and outputs its contents"""

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
    payload = packet[8:(length+8)].decode("utf-8")

    print(f"UDP: {packet}\nsource-port: {source_port}\ndest-port: {dest_port}\ndata-len: {length}\nchecksum: {checksum}\npayload: '{payload}'")


async def main():
    """main() -> None, establishes connection with uri using a web socket and awaits for recv_and_decode_packet(websocket)"""

    # uri to connect to the server
    uri = "ws://localhost:5612"

    # an asynchronous web socket
    async with websockets.connect(uri) as websocket:
        # await for recv and decode function to execute
        await recv_and_decode_packet(websocket)

# begin running async code
asyncio.get_event_loop().run_until_complete(main())