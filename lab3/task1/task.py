from create import Create
from procces import Process
from model import Model


class Task:
    def with_probability(self):
        c = Create(2)
        p1 = Process(5)
        p2 = Process(1)
        p3 = Process(1)

        c.set_name("Creator")
        p1.set_name("Process1")
        p2.set_name("Process2")
        p3.set_name("Process3")

        c.set_next_element(p1)
        p1.next = [p2,p3]
        p1.set_probability([0.3 , 0.7])


        p1.set_max_queue(5)
        p2.set_max_queue(5)
        p3.set_max_queue(5)


        print(p1.next)
        elements = [c, p1, p2, p3]

        model = Model(elements)
        model.simulate(1000)

    def with_priority(self):
        c = Create(2)
        p1 = Process(5)
        p2 = Process(1)
        p3 = Process(1)
        p4 = Process(1)

        c.set_name("Creator")
        p1.set_name("Process1")
        p2.set_name("Process2")
        p3.set_name("Process3")
        p4.set_name("Process4")

        c.set_next_element(p1)
        p1.next = [p2,p3, p4]
        p1.set_priority(1)
        p2.set_priority(1)
        p3.set_priority(4)
        p4.set_priority(2)



        p1.set_max_queue(5)
        p2.set_max_queue(5)
        p3.set_max_queue(5)
        p4.set_max_queue(5)

  


        print(p1.next)
        elements = [c, p1, p2, p3, p4]

        model = Model(elements)
        model.simulate(1000)