import random
import math

class Element:
    def __init__(self, delay):
        self.delay = delay
        self.delay_dev = 0
        self.t_next = 0
        self.state = 0
        self.next = [] 
        self.queue = 0
        self.failure = 0
        self.mean_queue = 0
        self.distribution = "exp"
        self.processed =0
        self.total_time =0;
        self.intervals =[]
        self.t_last=0;
  
    
    def set_priority(self ,priority ):
        self.priority =priority

    def set_delay_dev(self, delay_dev):
        self.delay_dev = delay_dev

    def set_distribution(self,distribution ):
        self.set_distribution = distribution
    

    def get_from_priority(self):
        max = -1
        max_index = 0
        i = 0
        for el in self.next:
            if el.priority > max:
                max = el.priority
                max_index =i
            i+=1
        return max_index
        

    
    def get_delay(self):
        if self.distribution == "exp":
            a = 0
            while a == 0:
                a = random.random()
            a = -self.delay * math.log(a)
            return a
        elif self.distribution == "norm":
            return self.delay + self.delay_dev * random.gauss(0.0, 1.0)

        

    def in_act(self, t_curr):
        pass

    def out_act(self, t_curr):
        self.processed += 1

    def print_info(self):
        print("Element = " + self.name + " t_next = " + str(self.t_next) + " queue: " + str(self.queue) + " state = " + str(self.state))
        print()

    def print_statistics(self, time_modeling):
        print("Element = " + self.name + " processed = " + str(self.processed) + " failure = " + str(self.failure))

    def print_result(self):
        print(self.name + " processed = " + str(self.processed))

    def do_statistics(self, delta):
        pass

    def set_next_element(self, next_element):
        self.next = next_element

    def set_name(self, name):
        self.name = name

    def set_max_queue(self, max):
        self.max_queue = max

   