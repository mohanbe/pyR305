import struct as st
import serial as ser
import time,sys
head=[0xef01,0x00000000,0x01]
from Finger import FingerPrint
class Finger:
    def __init__(self):
        self.f=FingerPrint()
    def enroll(self):
        raw_input("Put Finger:")
        self.f.getimg()
        self.f.genchar(1)
        r=self.f.search()
        if(r!=-1):
           print("Finger Already Taken at:"+str(r))
           sys.exit()
        raw_input("Put Finger Again:")
        self.f.getimg()
        self.f.genchar(2)
        y=self.f.regmodel()
        if y:
          fid=raw_input("Enter ID (0-254):")
          self.f.store(fid)
        else:
           print("Error")
    def match(self):
        raw_input("Want to search:")
        self.f.getimg()
        self.f.genchar(1)
        r=self.f.search()
        if(r!=-1):
           print("Finger Found at:"+str(r))
    def delete(self):
        fid=raw_input("Enter Start Address")
        n=raw_input("Enter No of Fingerprints")
        self.f.delete(fid,n)
    def empty(self):
        self.f.empty()
g=Finger()
while True:
    i=raw_input("1:Enroll\t2:Match\t 3:Delete\t4:Empty\t5:Exit\n")
    if(i=='1'):
        g.enroll()
    elif(i=='2'):
        g.match();
    elif(i=='3'):
        g.delete()
    elif(i=='4'):
        g.empty()
    else:
        break;

        

