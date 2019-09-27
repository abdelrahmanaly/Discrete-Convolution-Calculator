import numpy as np
import matplotlib.pyplot as plot

def gentriangle(x):
    array=[0]*(x)
    
    for i in range(0,int(x/2)+1):
        array[i]=i
        if i==0:
            continue
        else:
            array[len(array)-i-1]=array[i]
    array[len(array)-1]=0
    return array
def gensquare(a,x):
    array=[a]*x
    array[0]=0
    array[len(array)-1]=0
    return array

def discrete_convolution(a,b):
    array=np.convolve(a,b)
    return array

choice=int(input("which graphs would you you like to see convoloted, Square * triangle(1),Triangle *Triangle(2),Square * Square(3)"))
graph_length=int(input("how long is your graph moving for ? "))

if choice==1: 
    a=int(input("please insert amplitude of sqaure?"))
    plot.subplot(333)
    plot.title("Square Function")
    square_wave_array=gensquare(a,graph_length)
    square_wave=plot.stem(square_wave_array)
    plot.setp(square_wave)
    plot.subplot(331)
    plot.title("Triangular Function")
    triangle_wave=plot.stem(gentriangle(graph_length+1))  
    plot.setp(triangle_wave) 
    plot.subplot(313)
    plot.title("Resulting convolution of both functions")
    convolution1=plot.stem(discrete_convolution(gensquare(a,graph_length),gentriangle(graph_length))) #issues in this line
    plot.setp(convolution1)
    plot.show()
elif choice==2: 
    plot.subplot(333)
    plot.title("First trianguler function")
    triangle_wave=plot.stem(gentriangle(graph_length+1))
    plot.setp(triangle_wave)
    plot.subplot(331)
    plot.title("Second trianguler function")
    triangle_wave=plot.stem(gentriangle(graph_length+1))
    plot.setp(triangle_wave)
    plot.subplot(313)
    plot.title("Resulting convolution for both functions")
    convolution1=plot.stem(discrete_convolution(gentriangle(graph_length),gentriangle(graph_length)))
    plot.setp(convolution1)
    plot.show()
else:
    a=int(input("please insert amplitude of sqaure?"))
    plot.subplot(333)
    plot.title("First Square function")
    square_wave=plot.stem(gensquare(a,graph_length))
    plot.setp(square_wave)
    plot.subplot(331)
    plot.title("Second Square function")
    square_wave=plot.stem(gensquare(a,graph_length))
    plot.setp(square_wave)
    plot.subplot(313)
    plot.title("Resulting convolution for both functions")
    square=gensquare(a,graph_length)
    convolution1=plot.stem(discrete_convolution(square,square))
    plot.setp(convolution1)
    plot.show()



