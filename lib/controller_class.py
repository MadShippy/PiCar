import sys
sys.path.append(r'/home/kaanb/RobotSystems/lib')
import time
import numpy
from picarx_improved import Picarx

class Controller(Interpreter):
    def __init__(self, scalingFactor=20):
        self.scalingFactor = scalingFactor

    def steering(self, motor):
        direction, degree = self.edge_detection()
        steer = int(self.scalingFactor * degree)
        motor.set_dir_servo_angle(angle)
        motor.forward(10)


def consumer_producer(control_bus, delay_s):
    control = Controller()
    motor = motor_commands.MotorCommands()
    while True:
        get_val = control_bus.read()
        angle = control.main_control(get_val, motor)
        control_bus.write(angle)
        time.sleep(delay_s)
