#!/usr/bin/env python
#By M24-Py
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
##
import googletrans,os,sys,time
from googletrans import Translator
from time import sleep 
#
banner = """
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{}
____       _____                    _       _
|  _ \ _   |_   _| __ __ _ _ __  ___| | __ _| |_ ___  _ __
| |_) | | | || || '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
|  __/| |_| || || | | (_| | | | \__ \ | (_| | || (_) | |
|_|    \__, ||_||_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|
       |___/
{}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{}
"""
banmer = """

1 > TᖇᗩᑎSᒪᗩTE   69 > Exit

2 > ᗩᗷOᑌT

"""
def about():
  os.system("clear")
  sleep(1.5)
  print(69 * '-' + Y)
  sleep(0.1)
  print(G + "Py-Translate By Cheems-M24")
  sleep(0.1)
  print(B + "Coded with ACode Software On Android Q")
  sleep(0.1)
  print(69 * '-' + Y)
  sleep(2.5)
   
#
def cheems():
  os.system("clear")
  sleep(1.4)
  print(50 * '-' + W)
  sleep(0.1)
  print(B + "Cheems ")
  sleep(0.1)
  print(50 * '-' + W) 
  sleep(1.9)
  os.system("clear")
#
def trlt():
   try:
     trs = Translator()
     os.system("clear")
     sleep(1)
     print(Y + banner)
     sleep(0.1)
     print(G + banmer)
     print("")
     sleep(0.1)
     txt = str(input(G + "Text To Translate > "))
     sleep(0.1)
     bhs = str(input(W + "To Language (id,ja,ko,ru) > "))
     hasl = trs.translate(txt, dest = bhs)
     sleep(1.5)
     print(W + "From Lang : " ,txt.src, "To",hsl.dest )
     print(G + "Result : ", txt, G + ">",hsl.text)
     sleep(0.1)
     print("")
    
       
def menu():
   os.system("clear")
   sleep(1)
   print(Y + banner)
   sleep(0.1)
   print(G + banmer)
   try:
     ch = str(input( G + "> "))
     if ch==1:
       trlt()
     elif ch==2:
       about()
     elif ch==3:
       cheems()
     else:
       print(R + "Invalid Option")
       sleep(1.5)
      
   except KeyboardInterrupt:
     cheems() 
#Coded By Cheems-M24 / M24-py or M24-sh
#12:23PM (UTC +7 ) West Indonesian Time ,Sun 27 Dec 2K20 
#V1.01