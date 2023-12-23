from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient("0.tcp.eu.ngrok.io", 15007)

t = threading.Thread(target=sender.start_stream)
t.start()

while input("") != "STOP":
    continue

sender.stop_stream()
