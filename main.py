#!/usr/bin/env pybricks-micropython
# tohole musí být 1. rádek

# importy
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
import DIRTYimg2num as imgnm

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

# setup is_up (pro řádek), cerna (is_up pro sloupce)
is_up = True
cerna = False
docasna = 0

# setup odsazení od okraje, zespodu
set_dal = 0
dal = set_dal
paper = 0

# setup velikost obrázku, potřeba vyladit k sobě
zmena_p = 4
zmena_carka = 4

# setup aktuální číslo řádku, celkem (potřeba dopočítat), pro procenta
cislo_radku = 0
pocet_radku = 200

# setup toho, co chci tisknout
robot = imgnm.Nums()