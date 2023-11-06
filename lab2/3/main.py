from model import Model
from create import Create
from procces import Process
from task import Task
from worker import Worker
def main():
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
    p1.set_probality([0.3 , 0.7])


    p1.set_max_queue(5)
    p2.set_max_queue(5)
    p3.set_max_queue(5)

    ##555555

    w1 = Worker()
    w2 = Worker()
    w3 = Worker()
    w4 = Worker()
    w5 = Worker()

    workers = [w1, w2, w3, w4, w5]
    p1.set_workers([w1])
    p2.set_workers([w1])
    p3.set_workers([w1])



    print(p1.next)
    elements = [c, p1, p2, p3]

    model = Model(elements)
    model.simulate(1000)

if __name__ == "__main__":
    task = Task()
    task.task_6()
    # task_4()
    