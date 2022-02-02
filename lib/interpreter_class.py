import sys
sys.path.append(r'/home/MadShippy/PiCar/lib')
import time
import numpy
from picarx_improved import Picarx


class Interpretor:
    def __init__(self, sensitivity=750, polarity=True):     
        #Initialize how we interpret greyscale sensors for line following
        self.sensitivity = sensitivity
        self.polarity = polarity

    def convert_to_discrete(self, adc_value_list):
        left_sensor = adc_value_list[0]
        centre_sensor = adc_value_list[1]
        right_sensor = adc_value_list[2]

        detect_left_edge = left_sensor - centre_sensor
        detect_right_edge = right_sensor - centre_sensor

        if abs(detect_left_edge) > self.sensitivity:
            if detect_left_edge < 0:
                discrete_left = False
            else:
                discrete_left = True
            discrete_centre = not discrete_left

            if abs(detect_right_edge) > self.sensitivity:
                discrete_right = not discrete_centre
            else:
                discrete_right = discrete_centre
        else:
            if abs(detect_right_edge) > self.sensitivity:
                if detect_right_edge < 0:
                    discrete_right = False
                else:
                    discrete_right = True
                discrete_centre = not discrete_right
                discrete_left = discrete_centre
            else:
                if left_sensor > self.sensitivity:
                    discrete_left = True
                else:
                    discrete_left = False
                discrete_right = discrete_left
                discrete_centre = discrete_left

        return [discrete_left, discrete_centre, discrete_right]

def consumer_producer(inter_bus, delay_s):
    interpret = Interpretor()
    while True:
        get_val = inter_bus.read()
        converted_val = interpret.process_adc(get_val)
        inter_bus.write(converted_val)
        time.sleep(delay_s)

