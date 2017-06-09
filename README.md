# pyR305
It is a Easy to use Python Library for R305 fingerprint sensor.
It is used to interface your R305 with your PC or Raspberry Pi Module.
It requires Python 2.7.
Clone the repository using "git clone https://github.com/mohanbe/pyR305.git" or download the ZIP file.
Once you clone it or extracted it from zip file you can see a folder named pyR305-master.
Go to R305 folder inside R305-master.
To use it Connect the R305 finger print module to Raspberry pi or PC using a Serial Interface,once connected notedown the Serial port.


Initial Configuration:
   ->Create a Newfile inside R305 folder.
   ->Import module:
      =>From Finger import Finger
   ->Initialize it with serial port and baud rate or by default it uses serial port as "/dev/ttyUSB0" and baudrate as 57600.
   ->create an Finger object
      =>f=Finger()
      or
      =>f=Finger(SerialPortNumber,Baudrate)

We have currently implemented 4 functions.
1:Enroll
2:Match
3:Delete
4:Empty


1:Enroll
    Usage:
        => f.enroll()
The Enroll function takes the finger two times.
When it asks for Put finger, keep your finger on the sensor and press enter a red light on the sensor blinks.
If you didnot put your finger it shows Finger Not found.
It doesnot take the same finger print again instead returns the id of the fingerprint previously saved.
If you are newly enrolling the finger it shows Finger Not Found and asks to Put Finger Again.
once you put finger again it asks for the id where to store the finger print, it takes value between 0-255.
once all are correct it prints Finger print Enrolled.


2:Match
   Usage:
     => f.match()
   
It matches for the finger from all the finger prints that are enrolled.

3:Delete
     Usage:
        => f.delete()
It delets enrolled finger prints from start id to N number or fingerprints.

4:Empty
     Usage:
        => f.empty()
It clears all the enrolled fingerprints.
