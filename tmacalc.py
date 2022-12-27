from cs50 import get_float
import math

##Create range calculator using BR and relative speed across LOS
def bearing_rate():
    b1 = get_float("What is B1? ")
    b2 = get_float("What is B2? ")
    mark = get_float("Leg length? ")
    br = (b1 - b2) / mark
    print(br)

def tma_calc():
##Get input
    dmho = int(input("What is O/S speed? "))
    co = int(input("What is O/S course? "))
    los = int(input("What is Target bearing? "))
    fr = float(input("What is recieved frequency? "))
    fo = float(input("What is base frequency? "))
    dmht = int(input("What is assumed target speed? "))
##Do math for LLA
    cqos = co - los
##Convert input to radians
    x = math.radians(cqos)
##Do math with radians for O/S speed in and across LOS
    xdmho = round(dmho * math.sin(x), 1)
    ydmho = round(dmho * math.cos(x), 1)
    print(f"xDmho is: {xdmho}")
    print(f"yDmho is: {ydmho}")
##Do hz/knot ratio
    hk = fo / 3000
    print(f"Freq/Knot is: {hk}")
##Deterime O/S impact Fr and print corrected frequency
    y = round(hk * ydmho, 2)
    print(f"O/S impact on Fr is: {y}")
    fc = abs(y - fr)
    print(f"Corrected frequency is: {fc}")
##Determine the impact of target speed on base frequency and target speed into los
    z = (fc - fo)
    ydmht = round(z / hk, 2)
    print(f"Target speed in/out the LOS is: {ydmht}")
## Do math for aob
    ydmhtr = math.radians(ydmht)
    dmhtr = math.radians(dmht)
    a = math.acos(ydmhtr / dmhtr)
    aob = round(math.degrees(a))
    print(f"AOB: {aob}")
##Do math for target speed across the los
    aobr = math.radians(aob)
    xdmht = round(dmht * math.sin(aobr), 1)
    print(f"Target speed across LOS is: {xdmht}")
#Determine inverse of target bearing
    if los > 180:
        ilos = los - 180
    else:
        ilos = los + 180
    print(f"Inverse of LOS is: {ilos}")
##Deterime Target course
    ct = ilos + aob
    ct2 = ilos - aob
    if ct > 360:
        ctx = ct - 360
    else:
        ctx = ct
    if ct2 > 360:
        ctx2 = ct2 - 360
    else:
        ctx2 = ct2
    print(f"Target course is: {ctx} or {ctx2}")
##Determine SALOS
    if ctx and dmho > 180:
        salos = xdmht - xdmho
    elif ctx and dmho < 180:
        salos = xdmht - xdmho
    else:
        salos2 = xdmht + xdmho
    if ctx2 and dmho > 180:
        salos2 = xdmht - xdmho
    elif ctx2 and dmho < 180:
        salos2 = xdmht - xdmho
    else:
        salos = xdmht + xdmho
    print(f"SALOS is: {salos} or {salos2}")

##Deterime which function the user wants
greeting = input("Do you want B/R Calc or TMA Calc? ")
if greeting == 'B/R Calc':
    bearing_rate()
else:
    tma_calc()
