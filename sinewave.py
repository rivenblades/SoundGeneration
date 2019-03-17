#Sample rate(samples per second)
sr = 8000
#Frequency(Hertz)
h = 261.625565
#ByteBeat
b = sr/256#8bit sound
#Volume
v=127

import math as m
t = 0#time
while 1:
    print(int((m.sin(t*2*3.14/(sr*h))+1)*v).to_bytes(2, byteorder="big"))
    #print(int(((t<<1)^((t<<1)+(t>>7)&t>>12))|t>>(4-(1^7&(t>>19)))|t>>7).to_bytes(8,byteorder="big"))
    t+=1
