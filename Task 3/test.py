"""
    This is a script for Internet Of Things Worksheet 3 Task 3
"""
"""
    import python modules
"""
import udp
from datetime import datetime

def test_checksum():

    #perform 5 checksum tests
    assert udp.compute_checksum( 10,42,'Welcome to IoT UDP Server'.encode() ) == 15307, "Should be 15307"
    assert udp.compute_checksum( 5656,9090,'message test'.encode()) == 49803, "Should be 49803"
    assert udp.compute_checksum( 23232,23233,'qwertyuiopasdfghjklzxcvbnm'.encode()) == 51889, "Should be 51889"
    assert udp.compute_checksum( 420,69,'stonks on the dogecoin'.encode()) == 43484, "Should be 43484"
    assert udp.compute_checksum( 25565,443,'connecting to minecraft server'.encode()) == 14301, "Should be 14301"

    # perform packet validation
    print("\n\n")
    print("testing packet time validation")

    # get last time response
    time = str(udp.run_test())

    # get the time
    now = datetime.now()

    # format time to str to match the response
    current_time = str(now.strftime("%H:%M:%S"))

    # output them both
    print("os:", current_time, "server:", time)

    # assert
    assert current_time == time, "Time did not match should be the same"
    print("passed")


# if this the entry point of the script
if __name__ == "__main__":

    print("testing checksums")
    test_checksum()
    print("\nfinished testing checksums ALL passed!")