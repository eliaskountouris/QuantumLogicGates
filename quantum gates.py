#!/usr/bin/env python
# coding: utf-8

# In[10]:


from matplotlib import pyplot as plt
import numpy as np
from qiskit import *
from qiskit.visualization import plot_bloch_vector
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")


# In[11]:


def NOT(input):

    q = QuantumRegister(1) 
    c = ClassicalRegister(1) 
    qc = QuantumCircuit(q, c) 
    
    if input=='1':
        qc.x( q[0] )
        
    qc.x( q[0] )
    
    qc.measure( q[0], c[0] )
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))

    return output


# In[12]:


def XOR(input1, input2):
    q = QuantumRegister(2)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q,c)
    
    if input1 == '1':
        qc.x(q[0])
    if input2 == '1':
        qc.x(q[1])
        
    qc.cx(q[0], q[1])
       
    qc.measure(q[1], c[0] )
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))

    return output


# In[13]:


def AND(input1, input2):
    q = QuantumRegister(3)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q,c)
    
    if input1 == '1':
        qc.x(q[0])
    if input2 == '1':
        qc.x(q[1])

    qc.ccx(q[0],q[1],q[2])
    
    qc.measure(q[2], c[0])
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))

    return output


# In[14]:


def NAND(input1, input2):
    q = QuantumRegister(3)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q,c)
    
    if input1 =='1':
        qc.x(q[0])
    if input2 =='1':
        qc.x(q[1])
        
    qc.ccx(q[0],q[1],q[2])
    qc.x(q[2])
    
    qc.measure(q[2], c[0])
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))

    return output


# In[17]:


def OR(input1, input2):
    q = QuantumRegister(3)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q,c)
    
    if input1 =='1':
        qc.x(q[0])
    if input2 =='1':
        qc.x(q[1])
        
    qc.cx(q[0],q[2])
    qc.cx(q[1],q[2])
    qc.ccx(q[0],q[1],q[2])
    
    qc.measure(q[2], c[0])
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))

    return output


# In[18]:


print('\nResults for the NOT gate')
for input in ['0','1']:
    print('    Input',input,'gives output',NOT(input))
    
print('\nResults for the XOR gate')
for input1 in ['0','1']:
    for input2 in ['0','1']:
        print('    Inputs',input1,input2,'give output',XOR(input1,input2))
        
print('\nResults for the AND gate')
for input1 in ['0','1']:
    for input2 in ['0','1']:
        print('    Inputs',input1,input2,'give output',AND(input1,input2))

print('\nResults for the NAND gate')
for input1 in ['0','1']:
    for input2 in ['0','1']:
        print('    Inputs',input1,input2,'give output',NAND(input1,input2))

print('\nResults for the OR gate')
for input1 in ['0','1']:
    for input2 in ['0','1']:
        print('    Inputs',input1,input2,'give output',OR(input1,input2))
        


# In[ ]:




