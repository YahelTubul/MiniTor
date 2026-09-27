"""import modules"""
import socket

HOST = "127.0.0.1"
PORT = 8000

def main():
    """
    This function is responsible for starting the server
    :return:
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("MiniTor server listening on port 8000...")
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__":
    main()
