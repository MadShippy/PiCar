import sys
sys.path.append(r'/home/kaanb/RobotSystems/lib')
import time
import numpy
from picarx_improved import Picarx


class Interpreter(Sensor):
    def __init__(self, sensitivity = 2, polarity= 1):
        super().__init__()
        self.sensitivity = sensitivity
        self.polarity = polarity
        # Sensitivity: Ratio of light to dark readings of sensor (Dark surface: lower readings, Light surface: higher readings)
        # Polarity: -1 for light line, 1 for dark line
        
     def val_buffer(self):
        adc_readings = []
        norm_adc_readings = []
        for i in range(10):
          adc_readings.append(self.get_adc_value())
          average_readings = numpy.mean(adc_readings, axis=0)
          sum_readings = numpy.sum(average_readings)
        for i in range(3):
          norm_adc_readings.append(average_readings[i] / sum_readings)
        return norm_adc_readings
      
      ###IMPLEMENT EDGE DETECTION

