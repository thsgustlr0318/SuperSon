import socket
import os
import time
from threading import Thread
import pyaudio
import wave
import sys
import pyttsx3

CHUCK = 1024

def play_wav(wav_filename):
    wf = wave.open(wav_filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)
    data = wf.readframes(1024)

    while len(data)>0:
        stream.write(data)
        data=wf.readframes(1024)

    stream.stop_stream()
    stream.close()

    p.terminate()

def tts(id):

    while True :
        HOST = 'xx.xx.xx.xx' # 서버 ip입력
        PORT = 9999

        engine = pyttsx3.init()
        print("start")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print("connect")
    
        while True:
            data = client_socket.recv(1024)
            print(data.decode())
        
            if not data:
                break
            if data.decode() == "hurryup":
                play_wav("voice/hurryup.wav")
            elif data.decode() == "hurrydown":
                play_wav("voice/hurydown.wav")
            elif data.decode() == "paldown":
                play_wav("voice/paldown.wav")
            elif data.decode() == "palup":
                play_wav("voice/palup.wav")
            elif data.decode() == "upup":
                play_wav("voice/up.wav")
            else :
                engine.say(data.decode())
                engine.runAndWait()
        client_socket.close()
    return


def time(id):
    os.system('sh mjpg.sh')

    return


if __name__ == "__main__":
    th1 = Thread(target=tts, args=(1,))
    th2 = Thread(target=time, args=(2,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()

