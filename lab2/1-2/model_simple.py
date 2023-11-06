import random, math
class Model:

    def __init__(self, delayCr, delayPr, maxQ):
        self.delayCreate = delayCr
        self.delayProcess = delayPr
        self.tnext = 0.0
        self.tcurr = self.tnext
        self.t0 = self.tcurr # коли створено 
        self.t1 = float('inf') # коли оброблено 
        self.maxqueue =maxQ
        self.numCreate = 0
        self.numProcess = 0
        self.failure = 0
        self.state = 0
        self.queue = 0
        self.nextEvent = 0
        self.totalTime = 0

    def simulate(self, timeModeling):
        while self.tcurr < timeModeling:
            self.tnext = self.t0
            self.nextEvent = 0
            #знаходимо найближчу подію
            if self.t1 <= self.tnext:
                self.tnext = self.t1
                self.nextEvent = 1

            self.tcurr = self.tnext

            if self.nextEvent == 0:
                self.event0()
            elif self.nextEvent == 1:
                self.event1()

            self.print_info()

        self.print_statistic(timeModeling)

    def event0(self):
        self.t0 = self.tcurr + self.getDelayCreate()
        self.numCreate += 1

        if self.state == 0:
            self.state = 1
            self.t1 = self.tcurr + self.getDelayProcess()
            self.totalTime += self.getDelayProcess()
        else:
            if self.queue < self.maxqueue:
                self.queue += 1
            else:
                self.failure += 1

    def event1(self):
        self.t1 = float('inf')
        self.state = 0

        if self.queue > 0:
            self.queue -= 1
            self.state = 1
            self.t1 = self.tcurr + self.getDelayProcess()
            self.totalTime += self.getDelayProcess() # 2 task
        
        self.numProcess += 1

    def print_statistic(self, time_modeling):
        avgLoad = self.totalTime / time_modeling
        print("numCreate = " + str(self.numCreate) +
              " numProcess = " + str(self.numProcess) +
              " failure = " + str(self.failure) +
              " avgLoad = " + str(avgLoad))

    def print_info(self):
        print("t = " + str(self.tcurr) +
              " state = " + str(self.state) +
              " queue = " + str(self.queue))

    def getDelayCreate(self):
        return self.funRandExp(self.delayCreate)

    def getDelayProcess(self):
        return self.funRandExp(self.delayProcess)

    #  с экспоненциальным распределением (Exp)
    def funRandExp(self, rate):
        return -1.0 * math.log(1.0 - random.random()) / rate
