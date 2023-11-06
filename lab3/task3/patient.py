class Patient:
    def __init__(self, type):
          self.type =type
          self.priority = 0
          self.singing_time =15
          self.id=0
        

    def set_priority(self, priority):
         self.priority = priority

    def init(self):
         if self.type == 1:
              self.priority = 1
         elif self.type == 2 :
              self.singing_time = 40
         elif self.type == 3 :
              self.singing_time = 30
        