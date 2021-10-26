#1. Import the NUMPY package under the name np.
print('1--------------------------------------------------')
import numpy as np


#2. Print the NUMPY version and the configuration.
print('2--------------------------------------------------')
print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
print('3--------------------------------------------------')
a = np.random.randint(low=0,high=10,size=(2,3,5))
#4. Print a.
print('4--------------------------------------------------')
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
print('5--------------------------------------------------')
b = np.ones((5,2,3))


#6. Print b.
print('6--------------------------------------------------')
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
print('7--------------------------------------------------')
print(a.size == b.size)



#8. Are you able to add a and b? Why or why not?

## no puedo sumarlas porque no tienen la misma forma
print('8--------------------------------------------------')
print( 'tienen la misma forma: ', (a.shape == b.shape), ' la a tiene:', a.shape, 'y b tinene:', b.shape)


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
print('9--------------------------------------------------')
c = b.transpose(1,2,0)
print(c.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = a + c
print(d)
print( '10--------------------------------------------------\nFuncionan porque tien la misma forma','\n Forma de a', a.shape, '== Forma de c', c.shape)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a, d)
print('11--------------------------------------------------\n a son int y b son floats porque al operar se han transformado')



#12. Multiply a and c. Assign the result to e.
print('12--------------------------------------------------')
print(a.shape, c.shape)
e = a * c
print( e.shape)


#13. Does e equal to a? Why or why not?
print('13-------------------------------------------------- \n e es igual a a  en forma porque se ha realizado un multiplicacion de elmento a elemento en matrices con la misma forma')



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print('14--------------------------------------------------')
d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print(d_max, d_min, d_mean)



#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
print('15--------------------------------------------------')
f = np.empty((2,3,5))
print(f)
f = f - f 

print(f)
#print( f == d)



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
print('16--------------------------------------------------')

i,v,z = -1,-1,-1
for subd, subf in zip(d,f):
    if i == 2:
        i = -1
    i += 1
    for lisd,lisf in zip(subd,subf):
        if v == 2:
            v = -1
        v += 1
        for eld,elf in zip(lisd,lisf):
            if z == 4:
                z = -1
            z += 1
            if eld > d_min and eld < d_mean:
                f[i,v,z] = 25
            elif eld > d_mean and eld < d_max:
                f[i,v,z] = 75
            elif eld == d_mean:
                f[i,v,z] = 50
            elif eld == d_min:
                f[i,v,z] = 0
            elif eld == d_max:
                f[i,v,z] = 100
print(f)


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print('17--------------------------------------------------')
print('Esta es d : ' , d)
print('esta es f : ', f)
"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
print('18--------------------------------------------------')
dtipo = np.dtype(object)
ss = np.empty([2,3,5],dtype=dtipo)

ss[f==25] = 'B'
ss[f==75] = 'D'
ss[f==50] = 'C'
ss[f==0] = 'A'
ss[f==100] = 'E'
print(ss)