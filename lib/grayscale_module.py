from adc import ADC

class Grayscale_Module(object):
    def __init__(self,ref = 1000):
        self.C0 = ADC("A0")
        self.C1 = ADC("A1")
        self.C2 = ADC("A2")
        self.ref = ref
        self.old_data = self.get_grayscale_data()


    def get_line_status(self,fl_list):

        if fl_list[0] > self.ref and fl_list[1] > self.ref and fl_list[2] > self.ref:
            return 'stop'
            
        elif fl_list[1] <= self.ref:
            return 'forward'
        
        elif fl_list[0] <= self.ref:
            return 'right'

        elif fl_list[2] <= self.ref:
            return 'left' 
 
#Function to steer based on light/dark data
    def get_line_pos(self, target = "dark", sensitivity = 1.5):
        current = self.get_grayscale_data()
        if target == "dark":
            idx = current_data.index(math.min(current_data))
        else:
            idx = current_data.index(math.max(current_data))
            
        if idk == 0:
            return -1
        elif idk == 1:
            return 0
        elif idx == 2:
            return 1
        
        self.old_data = current data        
  

    def get_grayscale_data(self):
        adc_value_list = []
        adc_value_list.append(self.C0.read())
        adc_value_list.append(self.C1.read())
        adc_value_list.append(self.C2.read())
        return adc_value_list

if __name__ == "__main__":
    import time
    GM = Grayscale_Module(950)
    while True:
        print(GM.get_grayscale_data())
        time.sleep(1)
