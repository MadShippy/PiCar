import sys
sys.path.append(r'/home/kaanb/RobotSystems/lib')
import time
import numpy
from picarx_improved import Picarx

class Sensor(Picarx):
    def __init__(self):
        super().__init__()
        self.C0 = ADC("A0")
        self.C1 = ADC("A1")
        self.C2 = ADC("A2")
        # ADC values for grayscale module
    def get_adc_value(self):
        adc_value_list = []
        adc_value_list.append(self.C0.read())
        adc_value_list.append(self.C1.read())
        adc_value_list.append(self.C2.read())
        return adc_value_list

def producer(sensor_bus, delay_s):
    sensor = SensorCommands()
    while(1):
        set_val = sensor.get_adc_value()
        sensor_bus.write(set_val)
        time.sleep(delay_s)
