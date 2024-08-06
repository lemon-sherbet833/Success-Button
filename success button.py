import tkinter
from playsound import playsound
import threading
import pygame

maxChannels = 3
targetChannel = 0

pygame.mixer.init()
pygame.mixer.set_num_channels(maxChannels)
success_sound = pygame.mixer.Sound("success sound.mp3")

def playSuccess(channelNum):
    pygame.mixer.Channel(channelNum).play(success_sound)
    while pygame.mixer.Channel(channelNum).get_busy():
        continue

def startPSThread():
    global targetChannel
    PSThread = threading.Thread(target=playSuccess, args=(targetChannel, ))
    PSThread.start()
    targetChannel += 1
    if (targetChannel >= maxChannels):
        targetChannel = 0

rootWindow = tkinter.Tk()
rootWindow.title("Dopamine")
rootWindow.iconphoto(True, tkinter.PhotoImage(file="window icon.png"))
rootWindow.geometry("250x50")

button = tkinter.Button(rootWindow, text="Success!", command=startPSThread, height=2, width=15)
button.pack(pady=10)

rootWindow.mainloop()
