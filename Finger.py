import struct as st
import serial as ser
import time,sys
from PIL import Image
head=[0xef01,0x00000000,0x01]
print(type(head[2]))
s=ser.Serial("/dev/ttyUSB1",57600);
class FingerPrint():
    def pack(self,data):
       a=sum(head[-1:]+data)
       pack_str='!HIB'+'B'*len(data)+'H'
       l=head+data+[a]
       d=st.pack(pack_str,*l)
       return d
    def unpack(self,data):
       ret=[]
       print(data)
       ret.extend(st.pack('!H',data[4]))
       return ret[1]
    def readpac(self,):
        time.sleep(1)
        w=s.inWaiting()
        ret=[]
        if(w>=9):
           sd=s.read(9)
           ret.extend(st.unpack('!HIBH',sd))
           ln=ret[-1]
           time.sleep(1)
           w=s.inWaiting()
           if w>=ln:
              sd=s.read(ln)
              form='!'+'B'*(ln-2)+'H'
              ret.extend(st.unpack(form,sd))
           return ret
    def writepac(self,data):
       d=self.pack(data)
       #print(repr(d))
       s.write(d)
    def getimg(self):
       data=[0x00,0x03,0x01]
       self.writepac(data)
       d=self.readpac()
       x=list(d)[4]
       if(x==0):
          print("Fingerprint Taken")
       elif(x==2):
          print("No Finger Found")
    def genchar(self,v):
        if v==1:
            data=[0x00,0x04,0x02,0x01]
        else:
            data=[0x00,0x04,0x02,0x02]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Converted to Charfile")
        elif(x==6):
          print("Fingerprint Corrupt")
        else:
            print(x)
    def regmodel(self):
        data=[0x00,0x03,0x05]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Model Registered")
          return 1
        elif x==10:
          print("No File in Charbuffer")
          return 0
        else:
            print(x)
            return 0
    def store(self,fid):
        data=[0x00,0x06,0x06,0x01,0x00,int(fid)]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Fingerprint Stored at:-"+fid)
        else:
            print(x)
    def search(self):
        data=[0x00,0x08,0x04,0x01,0x00,0x00,0x00,0x10]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Fingerprint Found:-")
          print("ID:")
          print(list(d)[6])
          return list(d)[6]
        elif x==9:
            print("No Match Found")
            print(d)
            return -1
        else:
            print(x)
            print(d)
            return -1
    def delete(self,fid,n):
        data=[0x00,0x07,0x0c,0x00,int(fid),0x00,int(n)]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print(str(n)+" Fingerprint Successfully Deleted from:"+str(fid))
        else:
            print(x)
    def empty(self):
        data=[0x00,0x03,0x0d]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("All Fingerprint Deleted")
        else:
            print(x)
    def upimg(self):
        data=[0x00,0x03,0x0a]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Ready to transfer")
          d=self.readpac()
          print(list(d)[10:])
          return str(d)
        else:
            print("Failed")
            print(x)
    def tz(self):
        data=[0x00,0x04,0x02,0x01]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Charfile Created")
        elif x==21:
            print("Failed")
        else:
            print(x)
    def upchar(self):
        data=[0x00,0x04,0x08,0x01]
        self.writepac(data)
        d=self.readpac()
        x=list(d)[4]
        if(x==0):
          print("Charfile Ready")
          d=self.readpac()
          print(list(d[5:]))
          print(len(list(d[5:])))
          im=Image.frombytes('L',(16,16),str(d[5:]))
          im.show()
        elif x==21:
            print("Failed")
        else:
            print(x)
f=FingerPrint()
f.getimg()
f.tz()
f.upchar()
def enroll():
  raw_input("Put Finger:")
  f.getimg()
  f.genchar(1)
  r=f.search()
  if(r!=-1):
      print("Finger Already Taken at:"+str(r))
      sys.exit()
  raw_input("Put Finger Again:")
  f.getimg()
  f.genchar(2)
  y=f.regmodel()
  if y:
   fid=raw_input("Enter ID (0-254):")
   f.store(fid)
  else:
   print("Error")
def match():
     raw_input("Want T0 search")
     f.getimg()
     f.genchar(1)
     r=f.search()
     if(r!=-1):
       print("Finger Found at:"+str(r))
while True:
    i=raw_input("1:Enroll\t2:Match\t 3:Delete\t4:Empty\t5:Exit\n")
    if(i=='1'):
        enroll()
    elif(i=='2'):
        match();
    elif(i=='3'):
        fid=raw_input("Enter Start Address")
        n=raw_input("Enter No of Fingerprints")
        f.delete(fid,n)
    elif(i=='4'):
        f.empty()
    else:
        break;
