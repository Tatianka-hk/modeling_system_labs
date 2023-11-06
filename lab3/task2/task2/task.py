from create import Create
from procces import Process
from model import Model


class Task:
    def condition_1(self):
        c = Create(0.5)
        p1 = Process(1)
        p2 = Process(1)

        p1.set_delay_dev(0.3)
        p2.set_delay_dev(0.3)
        
        p1.set_distribution("norm")
        p2.set_distribution("norm")

        p1.state = 1
        p2.state = 1
        c.set_name("Creator")
        p1.set_name("Process1")
        p2.set_name("Process2")


        c.next= [p1, p2]


        p1.set_max_queue(3)
        p2.set_max_queue(3)

        p1.set_priority(2)
        p2.set_priority(1)

        print(p1.next)
        elements = [c, p1, p2]

        model = Model(elements)
        model.simulate(60)

    def condition_2(self):
        c = Create(0.5)
        p1 = Process(0.3)
        p2 = Process(0.3)
        c.t_next = 0.1


        c.set_name("Creator")
        p1.set_name("Process1")
        p2.set_name("Process2")


        c.next= [p1, p2]


        p1.set_max_queue(3)
        p2.set_max_queue(3)

        p1.set_priority(2)
        p2.set_priority(1)

        print(p1.next)
        elements = [c, p1, p2]

        model = Model(elements)
        model.simulate(60)

    def condition_3(self):
        c = Create(0.5)
        p1 = Process(0.3)
        p2 = Process(0.3)


        c.set_name("Creator")
        p1.set_name("Process1")
        p2.set_name("Process2")

        p1.queue=2
        p2.queue=2


        c.next= [p1, p2]


        p1.set_max_queue(3)
        p2.set_max_queue(3)

        p1.set_priority(2)
        p2.set_priority(1)

        print(p1.next)
        elements = [c, p1, p2]

        model = Model(elements)
        model.simulate(60)

    def all(self):
        c = Create(0.5)
        p1 = Process(1)
        p2 = Process(1)

        p1.set_delay_dev(0.3)
        p2.set_delay_dev(0.3)
        
        p1.set_distribution("norm")
        p2.set_distribution("norm")

        c.set_name("Creator")
        p1.set_name("Process1")
        p2.set_name("Process2")
        c.t_next = 0.1 #2

        p1.queue=2
        p2.queue=2


        c.next= [p1, p2]


        p1.set_max_queue(3)
        p2.set_max_queue(3)

        p1.set_priority(2)
        p2.set_priority(1)

        print(p1.next)
        elements = [c, p1, p2]

        model = Model(elements)
        model.simulate(60)