def mult(a,b):
    import numpy as np 
    k=[]
    for i in range(-1,-1*len(b)-1,-1):
        z=[]
        for j in range(-1,-1*len(a)-1,-1): 
            z.insert(0,b[i]*a[j]) #este for se encarga de la primera parte de la multiplicacion de numero grandes que es convertirlas en sumas 
        for x in range(-i,1,-1):
            z.append(0) #este ciclo se encarga de agregar los ceros al final de la suma para cumplir con el teorema de multiplicacion 
        for x in range(len(b)+i):            
            z.insert(0,0) #este ciclo se encarga de agregar ceros al pincipio de las sumas para que queden con ceros iguales 
        k.append(z)
    w=np.zeros(len(k[i]), dtype=int)
    for i in range (len(k)):
        w=w+k[i]
 
    for i in range(-1,-1*len(w),-1):
        w[i-1]=int(w[i]/10+w[i-1]) #esta parte del ciclo se encarga de sumar la parte decimal de todo el conjunto de numeros en el ciclo siguiente al actual
        w[i]=w[i]%10      #este ciclo se ecarga de suma la parte unitaria en el ciclo actual 
    if (w[0]/10)>1:
        w=np.insert(w,0,int(w[0]/10)) #si el ciclo superior queda mas grande que el ciclo actual se encarga de crear una nueva posicio para el
        w[1]=w[1]%10    
    return w
def ExpE(a,p):
    res=a
    for i in range(0,p-1):
        res=mult(res,a)#con esto se encarga de multiplicar un numero de veces 
    return res
