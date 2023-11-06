from create import Create
from procces import Process
from model import Model
import pandas as pd
from worker import Worker
class Task:
    def task_3(self):
        c = Create(2)
        p1 = Process(5)
        p2 = Process(1)
        p3 = Process(1)
        c.set_name("CREATOR")
        p1.set_name("PROCESSOR1")
        p2.set_name("PROCESSOR2")
        p3.set_name("PROCESSOR3")

        c.set_next_element(p1)
        p1.set_next_element(p2)
        p2.set_next_element(p3)


        p1.set_max_queue(5)
        p2.set_max_queue(5)
        p3.set_max_queue(5)

    
        elements = [c,p1,p2,p3]
        model = Model(elements)
        model.simulate(1000)

    def task_5(self):
        c = Create(2)
        p1 = Process(5)
        p2 = Process(1)
        p3 = Process(1)
        c.set_name("CREATOR")
        p1.set_name("PROCESSOR1")
        p2.set_name("PROCESSOR2")
        p3.set_name("PROCESSOR3")

        c.set_next_element(p1)
        p1.set_next_element(p2)
        p2.set_next_element(p3)


        p1.set_max_queue(5)
        p2.set_max_queue(5)
        p3.set_max_queue(5)

        w1 = Worker()
        w2 = Worker()
        w3 = Worker()
        w4 = Worker()
        w5 = Worker()

        workers = [w1, w2, w3, w4, w5]
        p1.set_workers(workers)
        p2.set_workers(workers)
        p3.set_workers(workers)
    
        elements = [c,p1,p2,p3]
        model = Model(elements)
        model.simulate(1000)

    def task_6(self):
        c = Create(2)
        p1 = Process(5)
        p2 = Process(1)
        p3 = Process(1)
        c.set_name("CREATOR")
        p1.set_name("PROCESSOR1")
        p2.set_name("PROCESSOR2")
        p3.set_name("PROCESSOR3")

        c.set_next_element(p1)
        p1.next_element = [p2, p3]

        p1.set_max_queue(5)
        p2.set_max_queue(5)
        p3.set_max_queue(5)

        w1 = Worker()
        p1.set_workers([w1])
        p2.set_workers([w1])
        p3.set_workers([w1])
    
        elements = [c,p1,p2,p3]
        model = Model(elements)
        model.simulate(1000)

    def task_4(self):
        p1_delay = [1.0, 5.0, 1.0, 1.0, 1.0, 1.0, 1.0, 5.0, 1.0,5.0]
        p2_delay = [1.0, 1.0, 5.0, 1.0, 1.0, 1.0, 1.0, 5.0, 1.0,5.0]
        p3_delay = [1.0, 1.0, 1.0, 5.0, 1.0, 1.0, 1.0, 5.0, 1.0, 5.0]
        p1_max_queue = [5, 5, 5, 5, 1, 5, 5, 5, 1,1]
        p2_max_queue = [5, 5, 5, 5, 5, 1, 5, 5, 1,1]
        p3_max_queue = [5, 5, 5, 5, 5, 5, 1, 5, 1,1]
        c_delay = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 5.0, 1.0, 1.0]
        result = pd.DataFrame()

        for i in range(10):
            c = Create(c_delay[i])
            p1 = Process(p1_delay[i])
            p2 = Process(p2_delay[i])
            p3 = Process(p3_delay[i])

            c.set_name("CREATOR")
            p1.set_name("PROCESSOR1")
            p2.set_name("PROCESSOR2")
            p3.set_name("PROCESSOR3")

            c.set_next_element(p1)
            p1.set_next_element(p2)
            p2.set_next_element(p3)


            p1.set_max_queue(p1_max_queue[1])
            p2.set_max_queue(p2_max_queue[1])
            p3.set_max_queue(p3_max_queue[1])

        
            elements = [c,p1,p2,p3]
            model = Model(elements)
            model.simulate(1000)

            data = {
                "p1_delay": [p1_delay[i]],
                "p2_delay": [p2_delay[i]],
                "p3_delay": [p3_delay[i]],
                "p1_max_queue": [p1_max_queue[i]],
                "p2_max_queue": [p2_max_queue[i]],
                "p3_max_queue": [p3_max_queue[i]],
                "c_amount": [model.elements[0].served],
                "p1_amount": [model.elements[1].served],
                "p2_amount": [model.elements[2].served],
                "p3_amount": [model.elements[3].served],
                "p1_mq": [model.elements[1].mean_queue ],
                "p2_mq": [model.elements[2].mean_queue ],
                "p3_mq": [model.elements[3].mean_queue ],
                "p1_fail": [model.elements[1].failure],
                "p2_fail": [model.elements[2].failure],
                "p3_fail": [model.elements[3].failure],
            }

            result = pd.concat([result, pd.DataFrame(data)], ignore_index=True)

        result.to_csv("result.csv")

