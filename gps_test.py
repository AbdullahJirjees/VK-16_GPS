import serial
import pynmea2

def read_gps_data(serial_port='COM3', baudrate=9600):
    ser = serial.Serial(serial_port, baudrate=baudrate, timeout=1)
    while True:
        data = ser.readline()
        if data.startswith(b'$GPGGA'):
            msg = pynmea2.parse(data.decode('utf-8'))
            print(f"Latitude: {msg.latitude}, Longitude: {msg.longitude}")

if __name__ == "__main__":
    read_gps_data()
