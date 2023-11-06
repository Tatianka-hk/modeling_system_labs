from model import Model
from create import Create
from procces import Process
from worker import Worker



if __name__ == "__main__":
    c = Create(15)
    c.set_name("Creator")    
  
    atdoctor = Process(15)
    atdoctor.set_name("ATDOCTOR")
    doctor1 = Worker("Doctor1")
    doctor2 = Worker("Doctor2")
    atdoctor.set_workers([doctor1, doctor2])

    registration=Process(4.5)
    registration.set_name("ATREGISTRATION")
    registrator1 = Worker("REGISTRATOR1")
    registrator2 = Worker("REGISTRATOR2")
    registration.set_workers([registrator1, registrator2])
    registration.set_distribution("erlang")
    registration.n = 3
    

    

    atlabaratory = Process(4)
    atlabaratory.set_name("ATLABARATORY")
    laborant1 = Worker("LABORANT1")
    laborant2 = Worker("LABORANT2")
    atlabaratory.set_workers([laborant1, laborant2])
    atlabaratory.set_distribution("erlang")
    atlabaratory.n = 2

    accompaning = Process(3)
    accompaning.set_name("ACCOMPANING")
    accompaning1 = Worker("ACCOMPANING1")
    accompaning2 = Worker("ACCOMPANING2")
    accompaning3 = Worker("ACCOMPANING3")
    accompaning.set_workers([accompaning1, accompaning2, accompaning3])
    accompaning.set_distribution("erlang")
    accompaning.n = 8


    c.next =[atdoctor, registration]   
    registration.next = [atlabaratory]
    atlabaratory.next= [atdoctor]
    atdoctor.next =[accompaning,registration ]

    elements = [c, atdoctor, registration, atlabaratory,accompaning ]

    model = Model(elements)
    model.simulate(1000)
