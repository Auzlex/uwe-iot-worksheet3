"""
    This is a test script for Internet Of Things Worksheet 3 Task 2
"""
"""
    import modules
"""
import udp

def test_checksum():

    #perform 5 checksum tests
    assert udp.compute_checksum( 10,42,'Welcome to IoT UDP Server'.encode() ) == 15307, "Should be 15307"
    assert udp.compute_checksum( 5656,9090,'message test'.encode()) == 49803, "Should be 49803"
    assert udp.compute_checksum( 23232,23233,'qwertyuiopasdfghjklzxcvbnm'.encode()) == 51889, "Should be 51889"
    assert udp.compute_checksum( 420,69,'stonks on the dogecoin'.encode()) == 43484, "Should be 43484"
    assert udp.compute_checksum( 25565,443,'connecting to minecraft server'.encode()) == 14301, "Should be 14301"

    # perform packet validation
    print("\n\n")
    print("testing packet checksum")
    udp.run()

# if this the entry point of the script
if __name__ == "__main__":

    print("testing checksums")
    test_checksum()
    print("\nfinished testing checksums ALL passed!")
