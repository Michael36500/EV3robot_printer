#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick, Motor, Port

ev3 = EV3Brick()

M_pero = Motor(Port.C)
M_pero.run_target(200, 20)

M_papir = Motor(Port.A)
M_papir.run(240)