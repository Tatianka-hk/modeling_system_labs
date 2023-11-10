from element import Element

class Create(Element):
    def out_act(self, t_curr):
        super().out_act(t_curr)
        self.t_next = t_curr + self.get_delay()
        self.next[0].in_act(t_curr)