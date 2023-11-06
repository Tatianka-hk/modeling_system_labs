from procces import Process

class Model:
    def __init__(self,elements):
        self.t_next = 0.0
        self.t_curr = self.t_next
        self.state = 0
        self.elements = elements
        self.change_queue_amount = 0

    def simulate(self, time_modeling):
        while self.t_curr < time_modeling:
            self.t_next = float('inf')


            # пошук найближчої події
            for el in self.elements:
                if el.t_next < self.t_next:
                    self.t_next = el.t_next

            # print("\nIt's time for event in " + next_e.name + ", time = " + str(self.t_next))

            for el in self.elements:
                el.do_statistics(self.t_next - self.t_curr)

            self.t_curr = self.t_next

            for el in self.elements:
                if el.t_next == self.t_curr:
                    el.out_act(self.t_curr)

            # self.print_info()

        self.print_result(time_modeling)

    def print_info(self):
        for el in self.elements:
            if el.state == 1:
                el.print_info()

    def print_result(self, time_modeling):
        print("\n-------------RESULTS-------------")
        for el in self.elements:
            el.print_result(self.t_curr)
            if isinstance(el, Process):
                mean_queue = el.mean_queue / self.t_curr
                el.mean_queue = mean_queue
                print("mean length of queue = " + str(mean_queue))
                print("avg_intervals"+ str( sum(el.intervals)/len(el.intervals)))