import numpy as np 

def TfmNmo (n):
    
    n=str(n)
    n_T=[]
    for x in n:
        n_T.append(x)
    return n_T

def VerTipo (a):
    if type(a)==type(""):
        return TfmNmo(a)
    else:
        return a
def RestaE (a,b):
    #alguien me ayuda a crear un programa que verifique si es 
    a=VerTipo(a)
    b=VerTipo(b)
    if len(a)>len(b):
        menor=len(b)
        mayor=len(a)
            
        Sum=np.zeros(mayor)
        for i in range(-1,-1*menor-1,-1):
            Sum[i]=int(a[i])-int(b[i])+Sum[i]
            if Sum[i]<0:
                Sum[i]=Sum[i]+10
                Sum[i-1]=Sum[i-1]-1
        for i in range(0,mayor-menor,1):
            if len(a)>len(b):
                Sum[i]=Sum[i]+int(a[i]) 
    elif len(a)<len(b):
        x=a
        a=b
        b=x
        menor=len(b)
        mayor=len(a)
        Sum=np.zeros(mayor)
        
        for i in range(-1,-1*menor-1,-1):
            Sum[i]=int(a[i])-int(b[i])+Sum[i]
            if Sum[i]<0:
                Sum[i]=Sum[i]+10
                Sum[i-1]=Sum[i-1]-1
        for i in range(0,mayor-menor,1):
            if len(a)>len(b):
                Sum[i]=Sum[i]+int(a[i])
        Sum[0]=Sum[0]*-1
    else:
            Sum=np.zeros(len(a)+1)
            for i in range(-1*len(a),0,1): 
                Sum[i]=int(a[i])-int(b[i])-Sum[i]
                if Sum[i]<0:
                    Sum[i+1]=Sum[i+1]-1
                    Sum[i]=Sum[i]+ 1                    
            return Sum
           
        
    return Sum   
