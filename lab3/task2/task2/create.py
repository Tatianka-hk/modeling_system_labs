from element import Element

class Create(Element):
    def out_act(self, t_curr):
        super().out_act(t_curr)
        self.intervals.append(t_curr -self.t_last )
        self.t_last = t_curr
        self.print_info()
        self.t_next = t_curr + self.get_delay()
        if self.next[0].queue >= 3 and self.next[1].queue  >= 3: 
            self.failure += 1
        elif (self.next[0].queue ==0 and self.next[1].queue == 0 )or (self.next[0].queue == self.next[1].queue): 
            index = self.get_from_priority()
            self.next[index].in_act(t_curr)    
        else:
            if self.next[0].queue > self.next[1].queue:
                self.next[1].in_act(t_curr)
            else:
                self.next[0].in_act(t_curr)
    def print_info(self):
        print("queue 1 - ",self.next[0].queue, " queue2 - ", self.next[1].queue, "time - ", self.t_next )

    def print_result(self, t_curr):
        print(self.name + " served = " + str(self.processed))
        print("av_client =" + str(self.processed/t_curr))
        print("av_client_time =" + str(t_curr/self.processed))

        print("avg_intervals =" +str(sum(self.intervals) /len(self.intervals)))
        print("failure - ", self.failure)
        failure_prob = self.failure / (self.processed + self.failure)
        print("failure probability = " + str(failure_prob))