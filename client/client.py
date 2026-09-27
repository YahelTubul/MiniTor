"""import modules"""
import socket

def main():
    """
    This function is the client for the server I built before,send test message.
    :return:
    """
    msg : str = "test"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('localhost', 8000))
        client.sendall(msg.encode())
        data = client.recv(1024)
        if not data:
            return
    print(data.decode())

if __name__ == "__main__":
    main()
