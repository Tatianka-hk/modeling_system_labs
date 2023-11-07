from model import Model
from create import Create
from procces import Process
import pandas as pd
def checking(n, elements):
     for i in range(n):
        print (elements[i].name +" - "+ elements[i].next.name)

def analizing():
    n_array=[3, 5, 7, 3, 5, 7, 3, 5, 7]
    time_array =[1000, 1000, 1000, 5000, 5000, 5000, 7000, 7000, 7000]
    result = pd.DataFrame() 
    for i in range(9):
        model = creator_model_1(n_array[i], time_array[i])
        data = {
                "n": [n_array[i]],
                "time": [time_array[i]],
                "c_amount": [model.elements[0].served],
            }
        for j in range(n_array[i]):
            data[f"p{j+1}_amount"] = [model.elements[j+1].served]
        for i in range(n_array[i]):
            data[f"p{j+1}_mean_queue"] = [model.elements[j+1].mean_queue]
        for i in range(n_array[i]):
            data[f"p{j+1}_failure"] = [model.elements[j+1].failure]
        result = pd.concat([result, pd.DataFrame(data)], ignore_index=True)
    result.to_csv("result.csv")


    


def creator_model_1(n , time):
    c = Create(2)
    c.set_name("Creator")
    elements = []
    elements.append(c)
    procces_names=["FIRTS", "SECOND", "THIRD", "FOURTH", "FIFTH", "SEXTH" , "SEVENTH"]
    for i in range(n):
        curr_name= procces_names[i]+"PROCESS"
        curr_process= Process(5)
        curr_process.set_max_queue(5)
        curr_process.set_name(curr_name)
        elements[i].set_next_element(curr_process) 
        elements.append(curr_process)

    model = Model(elements)
    model.simulate(time)
    return model


if __name__ == "__main__":
    creator_model_1(5, 1000)
    analizing()
    