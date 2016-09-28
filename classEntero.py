# -*- coding: utf-8 -*-
"""
Created on %(28/sept/2016)s

@author: %(danielbetancur)s
"""
class Entero:
    def __init__(self,E):
        ent=[]
        for i in E:
            ent.append(int(i))
        self.entero=ent
        self.isDecimal=True
        self.isFraccionario=True
        
    def __str__(self):
        return str(self.entero)
    def toDecimal(self):
        string=""
        for i in self.entero:
            string+=str(i)
        return Decimal(string)
    def toFraccionario(self):
        string=""
        for i in self.entero:
            string+=str(i)
        string+=".0"
        return Fraccionario(string)
    def toString(self):
        string=""
        for i in self.entero:
            string+=str(i)
        return string 
    def SumaE (self, other):
        import numpy as np 

    #alguien me ayuda a crear un programa que verifique si es 
        a=self.entero
        b=other.entero
        if len(a)>len(b):
            menor=len(b)
            mayor=len(a)
        elif len(a)<len(b):
            menor=len(a)
            mayor=len(b)
        else:
                Sum=np.zeros(len(a)+1, dtype=int)
                for i in range(-1*len(a),0,1): 
                    Sum[i]=int(a[i])+int(b[i])+Sum[i]
                    if Sum[i]>9:
                        Sum[i-1]=Sum[i-1]+1
                        Sum[i]=Sum[i]-10
                        string=""
                        for i in Sum:
                            string+=str(i)
                        return string 
    
        Sum=np.zeros(mayor, dtype=int)
        for i in range(-1*menor,0,1): 
            Sum[i]=int(a[i])+int(b[i])+Sum[i]
            if Sum[i]>9:
                Sum[i-1]=Sum[i-1]+1
                Sum[i]=Sum[i]-10     
        i=0    
        if len(a)>len(b):
            while Sum[i]==0:
                Sum[i]=a[i]
                i+=1
        else:
            while Sum[i]==0:
                Sum[i]=b[i]
                i+=1

            string=""
            for i in Sum:
                string+=str(i)
            return string 
a=Entero("2343225")
b=Entero("12123898")
print a.SumaE(b)