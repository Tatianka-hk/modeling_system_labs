from element import Element
import numpy as np

class Process(Element):
    def in_act(self, t_curr, patient):
        flag = 0
        self.intervals.append(t_curr -self.t_last )
        self.t_last = t_curr        
        for worker in self.workers :
            if worker.state == 0:
                worker.state = 1
                self.t_next = t_curr + self.get_delay()
                self.total_time +=self.get_delay()
                self.processed += 1
                if self.name == "ATDOCTOR":
                    if patient.type == 1:
                        self.next[0].in_act(self.t_next, patient)
                        #палата 
                    else:
                        self.next[1].in_act(self.t_next, patient)
                        #реєстрація 
                elif self.name == "ATREGISTRATION":
                    self.next[0].in_act(self.t_next, patient)
                elif self.name == "ATLABARATORY":
                    if patient.type == 2:
                        self.next[0].in_act(self.t_next, patient)
                        #доктор 
                flag =1
                self.print_info(patient, self.name, self.get_delay())
                break
        if flag == 0:
            self.queue += 1
            self.patients.append(patient)


    def out_act(self, t_curr):
        self.t_next = float('inf')
        for worker in self.workers :
               if worker.state == 1:
                    worker.state = 0
                    if self.queue > 0:
                        flag =0
                        patient = None
                        for p in self.patients:
                            if p.priority == 1:
                                patient =p
                                flag =1
                                break
                        if flag ==0:
                            patient = self.patients[0]
                        self.queue -= 1
                        self.state = 1
                        self.processed += 1
                        self.t_next = t_curr + self.get_delay()
                        self.total_time +=self.get_delay()
                        if self.name == "ATDOCTOR":
                            if patient.type == 1:
                                self.next[0].in_act(self.t_next, patient)
                                #палата 
                            else:
                                self.next[1].in_act(self.t_next, patient)
                                #реєстрація 
                        elif self.name == "ATREGISTRATION":
                            self.next[0].in_act(self.t_next, patient)
                        elif self.name == "ATLABARATORY":
                            if patient.type == 2:
                                patient.type ==1
                                patient.priority =1
                                self.next[0].in_act(self.t_next, patient)
                                #доктор 
                        self.print_info(patient, self.name, self.get_delay())

    def set_type(self, type):
        self.type = type
        
    def print_info(self, patient, name , delay):
        print("patient.type - ", patient.type, " in ",name ,  " time - ", self.t_next , " delay - ", delay, )



    def do_statistics(self, delta):
        self.mean_queue += self.queue * delta

    def print_result(self, t_curr):
        super().print_result()
