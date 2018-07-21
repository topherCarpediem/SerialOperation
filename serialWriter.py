from serial import Serial
from threading import Thread

COM_PORT = 'COM3'
BAUDRATE = 115200

serial = Serial(baudrate=BAUDRATE, port=COM_PORT, timeout=1)

class Reciever(Thread):

    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            read = serial.readline()
            if len(read) != 0:
                print("Recieved serial message", read)


def main():
    print("Waiting for serial messages")
    reciever = Reciever()
    reciever.daemon = True
    reciever.start()


if __name__ == '__main__':
    main()
    while True:
        _input = input('Send message: ')
        _input = _input + '\n'
        serial.write(_input.encode())