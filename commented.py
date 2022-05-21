#!/usr/bin/env pybricks-micropython
# tohole musí být 1. rádek

# importy
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

#import knvrnc
#import KCyan, KMagenta, KYellow, KBlack

# setup kostka, stopky
ev3 = EV3Brick()
stop_w = StopWatch()

# setup touch senzory
touch_sensor = TouchSensor(Port.S4)
touch_spust = TouchSensor(Port.S3)

# setup motory 
M_papir = Motor(Port.A)
M_vozik = Motor(Port.B)
M_pero = Motor(Port.C)

# setup is_up (pro řádek), cerna (isup pro sloupce)
is_up = True
cerna = False
docasna = 0

        ##########
        #odsazení#
        ##########
# setup odsazení od okraje, zespodu
set_dal = 0
dal = set_dal
paper = 0

        #######
        #scale#
        #######
# setup velikost obrázku, potřeba vyladit k sobě
zmena_p = 4
zmena_carka = 4

# setup aktuální číslo řádku, celkem (potřeba dopočítat), pro procenta
cislo_radku = 0
pocet_radku = 200

# setup toho, co chci tisknout
robot = knvrnc.Nums()

# chytrá funukce na zvednutí propisky (testuje, jestli není)
def push_up():
    global is_up
    #global M_pero
    if is_up == False:
        M_pero.run_target(200, 20)
        is_up = True

# chytrá funukce na dolů propisky (testuje, jestli není)
def push_down(): 
    global is_up
    if is_up == True:
        M_pero.run_target(200, 0)
        is_up = False

# dojede na začátek
def jdi_na():
    M_vozik.run(120)
    while True:
        if touch_sensor.pressed():
            M_vozik.brake()
            M_vozik.reset_angle(0)
            break   
# udělá nový řádek
def NRadek():
    global paper
    global dal
    global cislo_radku
    dal = set_dal
    push_up()
    #push_up()
    #M_pero.run_target(100, 0)
    cislo_radku = cislo_radku + 1
    print ((cislo_radku/pocet_radku)*100,"%", cislo_radku, ". radek", stop_w.time()/60000,)
    jdi_na()
    paper = paper + zmena_p
    M_papir.run_target(120, paper)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #push_down()

# posune vozikem o jednu jednotku
def carka(move):
    global dal
    dal = dal - (zmena_carka * move)
    # docasna = dal
    # docasna = docasna * move

    M_vozik.run_target(100, dal)

# main loop
def Print_Color(color):
    global cerna 
    for e in color:
        if e == -1:
            push_up()
            NRadek()
            cerna = False
            continue
        if cerna == True:
            push_down()
        else:
            #cerna == False:
            push_up()

        carka(e)
        cerna = not cerna
#push_up

# set up všeho
M_papir.reset_angle(0)
M_pero.run_target(200, 40)
jdi_na()

# tisk
Print_Color(robot)

# po dokončení
ev3.speaker.beep(frequency=880, duration=10000)


#push_up()
#jdi_na()
# push_down()
push_up()
