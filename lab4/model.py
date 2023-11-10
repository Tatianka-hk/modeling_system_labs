from procces import Process

class Model:
    def __init__(self,elements):
        self.t_next = 0.0
        self.t_curr = self.t_next
        self.state = 0
        self.elements = elements

    def simulate(self, time_modeling):
        while self.t_curr < time_modeling:
            self.t_next = float('inf')
            next_e = None
            # пошук найближчої події
            for el in self.elements:
                if el.t_next < self.t_next:
                    self.t_next = el.t_next
                    next_e = el

            print("\nIt's time for event in " + next_e.name + ", time = " + str(self.t_next))

            for el in self.elements:
                el.do_statistics(self.t_next - self.t_curr)

            self.t_curr = self.t_next

            for el in self.elements:
                if el.t_next == self.t_curr:
                    el.out_act(self.t_curr)

            self.print_info()

        max_amount=self.print_result()
        print(max_amount)
        return max_amount

    def print_info(self):
        for el in self.elements:
            if el.state == 1:
                el.print_info()

    def print_result(self):
        print("\n-------------RESULTS-------------")
        max_amount = 0
        for el in self.elements:
            el.print_result()
            if isinstance(el, Process):

                mean_queue = el.mean_queue / self.t_curr
                #4 ts
                el.mean_queue = mean_queue
                failure_prob = el.failure / (el.served + el.failure)
                print("mean length of queue = " + str(mean_queue))
                print("failure probability = " + str(failure_prob))
                if max_amount < el.served:
                    max_amount = el.served
        return max_amount