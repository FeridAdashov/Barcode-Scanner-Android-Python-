import socket
import os

try:
    os.system('netsh wlan set hostednetwork mode=allow ssid=myWifi key=12345678')
    os.system('netsh wlan start hostednetwork')

    print('Hotspot created. Connect wifi with your device\nWifi Name: myWifi\nWif Password: 12345678')    
    
    HOST = ''
    PORT = 6547

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data)

except Exception as e:
    print('Could not created HotSpot' + str(e))
