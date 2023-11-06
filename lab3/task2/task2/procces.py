from element import Element
import numpy as np

class Process(Element):
    def in_act(self, t_curr):
        if self.state == 0:
            self.state = 1
            self.t_next = t_curr + self.get_delay()
            self.print_info()
            self.total_time +=self.get_delay()
            self.processed += 1
        else:
            if self.queue < self.max_queue:
               self.queue += 1
            # else:
            #    self.failure += 1

    def out_act(self, t_curr):
        self.t_next = float('inf')
        self.state = 0
        if self.queue > 0:
            self.queue -= 1
            self.state = 1
            self.processed += 1
            self.t_next = t_curr + self.get_delay()
            self.total_time +=self.get_delay()
            self.print_info()

   

    
        



    def do_statistics(self, delta):
        self.mean_queue += self.queue * delta

    def print_result(self, t_curr):
        super().print_result()
