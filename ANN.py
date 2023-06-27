import numpy as np
import matplotlib.pyplot as plt
from challenge1 import neurona, MSE

def neural_network(x,w_input,w_hidden,w_out,capa_entrada,capa_oculta):
    if len(w_input)!=capa_entrada or len(w_hidden)!=capa_oculta:
        return "error, las dimensiones de la capas no coinciden con los pesos"
    input_layer_output=[]
    for neurons in range(capa_entrada):
        neuron=neurona(x,w_input[neurons])
        input_layer_output.append(neuron)
    hidden_layer=[]
    for hidden_neurons in range(capa_oculta):
        hidden_neuron=neurona(input_layer,w_hidden[hidden_neurons])
        hidden_layer.append(hidden_neuron)
    return neurona(hidden_layer,w_out)


def inicializacion(x,capa_entrada,capa_oculta):
    w_entrada=[]
    for i in range(capa_entrada):
        w=[]
        for value in range(len(x)+1):
            w.append(np.random.randint(0,100)/100)
        w_entrada.append(w)
    w_capa_oculta=[]
    for i in range(capa_oculta):
        w=[]
        for value in range(capa_entrada+1):
            w.append(np.random.randint(0,100)/100)
        w_capa_oculta.append(w)
    w_out=[]
    for i in range(capa_oculta+1):
        w_out.append(np.random.randint(0,100)/100)
    w_final=[w_entrada,w_capa_oculta,w_out]
    return w_final

def artificial_ann(x,w,capa_entrada,capa_oculta):
    x1=[]
    r=[]
    w_input=w[0]
    w_middle=w[1]
    w_out=w[2]
    for second_index in range(len(x[0])):
        for first_index in range(len(x)):
            x1.append(x[first_index][second_index])
        r1=neural_network(x1,w_input,w_middle,w_out,capa_entrada,capa_oculta)
        x1=[]
        r.append(r1)
    return r

def algoritmo_optimizacion(w,x,y,error,capa_entrada,capa_oculta):
    population=[]
    
    for especimen in range(population_size):
        espec=inicializacion(x,capa_entrada,capa_oculta)
        population.append(espec)
        
        
        
    
    

def ANN_training(x,y,capa_entrada,capa-oculta):
    w=inicializacion(x,capa_entrada,capa_oculta)
    out1=artifial_ann(x,w,capa_entrada,capa_oculta)
    error1=MSE(out1,y)
    it=0
    while error1>0.0001 and it<5000:
        w=algoritmo_optimizacion(w,x,y,error1,capa_entrada,capa_oculta)
        out1=artificial_ann
        error1=MSE(out1,y)
    return w
    
    
