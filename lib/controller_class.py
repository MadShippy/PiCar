import sys
sys.path.append(r'/home/kaanb/RobotSystems/lib')
import time
import numpy
from picarx_improved import Picarx

class Controller(Interpreter):
    def __init__(self, scalingFactor=20):
        super().__init__()
        self.scalingFactor = scalingFactor

    def steering(self):
        direction, degree = self.edge_detection()
        steer = int(self.scalingFactor * degree)
