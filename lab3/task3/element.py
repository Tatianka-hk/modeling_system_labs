import random
import math
import numpy as np
class Element:
    def __init__(self, delay):
        self.delay = delay
        self.delay_dev = 0
        self.t_next = 0
        self.state = 0
        self.next = [] 
        self.mean_queue = 0
        self.distribution = "exp"
        self.processed =0
        self.total_time =0;
        self.intervals =[]
        self.t_last=0;
        self.workers = []
        self.patients = []
        self.n = 0
        self.queue = 0
        self.i =0 

    def set_workers(self, workers):
        self.workers  = workers
    
    def set_delay_dev(self, delay_dev):
        self.delay_dev = delay_dev

    def set_distribution(self,distribution ):
        self.set_distribution = distribution
    

        

    
    def get_delay(self):
        if self.distribution == "exp":
            a = 0
            while a == 0:
                a = random.random()
            a = -self.delay * math.log(a)
            return a
        elif self.distribution == "norm":
            return self.delay + self.delay_dev * random.gauss(0.0, 1.0)
        elif self.distribution == "erlang":
            res = 1
            for i in range(self.n):
                res *= random.random()
            return - np.log(res) / (self.n * self.delay)
        elif self.distribution == "unif":
            res = 0.0
            while res == 0:
                res = random.random()
            return self.delay + res * (self.n - self.delay)

        

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

   