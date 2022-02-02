from sensor_class import Sensor
from interpreter_class import Interpreter
from controller_class import Controller

from sensor_class import producer as sensor_function
from interpretor_class import consumer_producer as interpreter_function
from controller_class import consumer_producer as controller_function
from bus import Bus. 
from picarx_improved import PiCar
import concurrent.futures

if __name__ == '__main__':
  sensor = Sensor()
  interpreter = Interpreter(sensitivity = 2, polarity = 1)
  controller =  Controller(scalingFactor = 10)
  
  sens_bus = Bus()
  inter_bus = Bus()
  cont_bus = Bus()
  
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
   eSensor = executor.submit(sensor.producer, sens_bus, 0.01)
   eInterpreter = executor.submit(interpreter.consumer_producer, sens_bus, inter_bus, 0.01)
   eController = executor.submit(controller.consumer, inter_bus, 0.01)

   eSensor.result()
   eInterpreter.result()
   eController.result()
