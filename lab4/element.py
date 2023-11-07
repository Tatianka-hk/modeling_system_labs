import random
import math

class Element:
    def __init__(self, delay):
        self.delay = delay
        self.t_next = 0
        self.state = 0
        self.next = None 
        self.queue = 0
        self.failure = 0
        self.served = 0
        self.mean_queue = 0
  
    def set_workers(self, workers):
        self.workers = workers

    
    def get_delay(self):
        a = 0
        while a == 0:
            a = random.random()
        a = -self.delay * math.log(a)
        return a

    def in_act(self, t_curr):
        pass

    def out_act(self, t_curr):
        self.served += 1

    def print_info(self):
        print("Element = " + self.name + " t_next = " + str(self.t_next) + " queue: " + str(self.queue) + " state = " + str(self.state))

    def print_statistics(self, time_modeling):
        print("Element = " + self.name + " served = " + str(self.served) + " failure = " + str(self.failure))

    def print_result(self):
        print(self.name + " served = " + str(self.served))

    def do_statistics(self, delta):
        pass

    def set_next_element(self, next_element):
        self.next = next_element

    def set_name(self, name):
        self.name = name

    def set_max_queue(self, max):
        self.max_queue = max

   