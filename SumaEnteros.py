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
def SumaE (a,b):
    #alguien me ayuda a crear un programa que verifique si es 
    a=VerTipo(a)
    b=VerTipo(b)
    if len(a)>len(b):
        menor=len(b)
        mayor=len(a)
    elif len(a)<len(b):
        menor=len(a)
        mayor=len(b)
    else:
            Sum=np.zeros(len(a)+1)
            for i in range(-1*len(a),0,1): 
                Sum[i]=int(a[i])+int(b[i])+Sum[i]
                if Sum[i]>9:
                    Sum[i-1]=Sum[i-1]+1
                    Sum[i]=Sum[i]-10
                    
            return Sum

    Sum=np.zeros(mayor)
    for i in range(-1*menor,0,1): 
        Sum[i]=int(a[i])+int(b[i])+Sum[i]
        if Sum[i]<9:
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
    return Sum
	
