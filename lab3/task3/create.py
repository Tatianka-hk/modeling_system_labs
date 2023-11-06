from element import Element
from patient import Patient
import numpy as np
class Create(Element):
    def out_act(self, t_curr):
        super().out_act(t_curr)
        self.intervals.append(t_curr -self.t_last )
        self.t_last = t_curr     
        num = [1,2,3]
        probability = [0.5, 0.1, 0.4]
        i = np.random.choice(a=num, p=probability)
        patient = Patient(i)
        patient.init()
        self.i+=1
        self.print_info(patient)
        self.t_next = t_curr + self.get_delay()
        if patient.type == 1 or patient.type ==2:
            self.next[0].in_act(t_curr, patient)
        else:
            self.next[1].in_act(t_curr, patient)

      
    def print_info(self, patient):
        print("created patient.type - ", patient.type, "time - ", self.t_next )

    def print_result(self, t_curr):
        print(self.name + " served = " + str(self.processed))
        print("avg_intervals"+ str( sum(self.intervals)/len(self.intervals)))
