from element import Element
import random

class Process(Element):
    def in_act(self, t_curr):
        # if self.state == 0:
        #     self.state = 1
        #     self.t_next = t_curr + self.get_delay()
        # else:
        #     if self.queue < self.max_queue:
        #        self.queue += 1
        #     else:
        #        self.failure += 1
        st =0
        for worker in self.workers:
            if worker.state == 0:
                worker.state = 1
                self.t_next = t_curr + self.get_delay()
                st = 1 
                break
        if st == 0:
            if self.queue < self.max_queue:
                self.queue += 1
            else:
                self.failure += 1 
         
        
            

    def out_act(self, t_curr):
        # super().out_act(t_curr)
        # self.t_next = float('inf')
        # self.state = 0
        # if self.queue > 0:
        #     self.queue -= 1
        #     self.state = 1
        #     self.t_next = t_curr + self.get_delay()
        # if self.next is not None:
        #     self.next.in_act(t_curr)
        super().out_act(t_curr)
        self.t_next = float('inf')
        for worker in self.workers:
            if worker.state == 1:
                worker.state = 0
                if self.queue > 0:
                    self.queue -= 1
                    worker.state = 1
                    self.t_next = t_curr + self.get_delay()
                    break
                # if self.next is not None
        if len(self.next) >0:
            print(self.next)
            next = random.choice(self.next) #6task
            next.in_act(t_curr)  #elimina primer parte de frase



    def do_statistics(self, delta):
        self.mean_queue += self.queue * delta

    def print_result(self):
        super().print_result()
        print("failure = " + str(self.failure))