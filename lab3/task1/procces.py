from element import Element
import numpy as np

class Process(Element):
    def in_act(self, t_curr):
        if self.state == 0:
            self.state = 1
            self.t_next = t_curr + self.get_delay()
            if self.status == 2:
                if len(self.next) >0:
                    print(self.next)
                    next = np.random.choice(a=self.next, p=self.probability)
                    next.in_act(t_curr)  
            elif self.status == 1:
                if len(self.next) >0:

                    index = self.get_from_priority()

                    self.next[index].in_act(t_curr)

        else:
            if self.queue < self.max_queue:
               self.queue += 1
            else:
               self.failure += 1

    def out_act(self, t_curr):
        super().out_act(t_curr)
        self.t_next = float('inf')
        self.state = 0
        if self.queue > 0:
            self.queue -= 1
            self.state = 1
            self.t_next = t_curr + self.get_delay()
        if self.status == 2:
            if len(self.next) >0:
                print(self.next)
                next = np.random.choice(a=self.next, p=self.probability)
                next.in_act(t_curr)  
        elif self.status == 1:
            if len(self.next) >0:

                index = self.get_from_priority()

                self.next[index].in_act(t_curr)

    
        



    def do_statistics(self, delta):
        self.mean_queue += self.queue * delta

    def print_result(self):
        super().print_result()
        print("failure = " + str(self.failure))