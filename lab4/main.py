from model import Model
from create import Create
from procces import Process
import pandas as pd
def checking(n, elements):
     for element in elements:
        for j in range (len(element.next)):
             print (element.name +" - "+ element.next[j].name)
       

def analizing(model_type):
    n_array=[3, 5, 7, 3, 5, 7, 3, 5, 7]
    time_array =[1000, 1000, 1000, 5000, 5000, 5000, 7000, 7000, 7000]
    result = pd.DataFrame() 
    for i in range(9):
        if model_type == 1:
            model = creator_model_1(n_array[i])
        else:
            model = creator_model_2(n_array[i])
        model.simulate(time_array[i])
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

def teor_analizing(model_type):
    res = []
    for j in range(5):
        time_array =[1000,  2500,5000, 7000, 10000]
        if model_type == 1:
            model = creator_model_1(7)
        else:
            model = creator_model_2(7)
        max_amount = 0
        for i in range(5):
            amount_t = model.simulate(time_array[j])
        if max_amount< amount_t:
            max_amount = amount_t
        res.append(time_array[i] * max_amount)
    for i in range(5):
        print ("for time = "+ str(time_array[i])+ " difficulty = "+str(res[i])+"n")

        
    
    
    

    


def creator_model_1(n ):
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
        elements[i].next.append(curr_process) 
        elements.append(curr_process)

    model = Model(elements)
    return model

def creator_model_2(n):
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
        if i == 0 or i == 1 or i == 4:
            elements[i].next.append(curr_process)  
        elif i == 2 or i == 5:
            elements[i-1].next.append(curr_process) 
        else:
            elements[i].next.append(curr_process) 
            elements[i-1].next.append(curr_process) 
        elements.append(curr_process)

    checking(7, elements)

    model = Model(elements)
    return model


if __name__ == "__main__":
    model = creator_model_1(7)
    analizing(1)
    teor_analizing(1)
    analizing(2)
    teor_analizing(2)
    
    