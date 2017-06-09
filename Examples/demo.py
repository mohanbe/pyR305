from Finger import Finger
f=Finger()
while True:
    i=raw_input("1:Enroll\t2:Match\t 3:Delete\t4:Empty\t5:Exit\n")
    if(i=='1'):
        f.enroll()
    elif(i=='2'):
        f.match();
    elif(i=='3'):
        f.delete()
    elif(i=='4'):
        f.empty()
    else:
        break;

