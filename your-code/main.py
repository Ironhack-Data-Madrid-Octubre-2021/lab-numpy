#1. Import the NUMPY package under the name np.


import numpy as np

#2. Print the NUMPY version and the configuration.

print('#2. Print the NUMPY version and the configuration.')
print(np.__version__)
print(np.show_config())

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.rand(2,3,5)
a2= np.random.random_sample((2,3,5))
a3 = np.random.randint(10, size=(2,3,5)) #solo me sale de 2x3... pero en la documentación dice que le puedes meter mas dimensiones



#4. Print a.
print('#4. Print a')
print('a= ', a)
print('a2= ', a2)
print('a3= ', a3)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print('#6. Print b.')
print('b= ', b)

#7. Do a and b have the same size? How do you prove that in Python code?

print('#7. Do a and b have the same size? How do you prove that in Python code?')
print('np.size(a) == np.size --> ', np.size(a) == np.size)


#8. Are you able to add a and b? Why or why not?

print('8. Are you able to add a and b? Why or why not?')
print('No, because they are not of the same size')

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)
print(c.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

print('#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?')
d=a+c
print('d = a + c --> ', d)
print('Now it works because they have the same shape')

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.


print('#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.')
print(f'a={a} \n d = {d}')
print('The difference is 1 for each value because c is a matrix of ones and d=a+c')

#12. Multiply a and c. Assign the result to e.
print('#12. Multiply a and c. Assign the result to e.')
e=a*c
print(f'e= {e}')

#13. Does e equal to a? Why or why not?

print('#13. Does e equal to a? Why or why not?')
print('They are the same because multiplying for one gives the same value and c is a ones matrix')


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

print('14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"')
d_max,d_min,d_mean = np.max(d), np.min(d), np.mean(d)

print(f'd_max = {d_max} \n d_min = {d_min} \n d_mean = {d_mean}')

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty([2,3,5])



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

print('Populate the values in f --> 0, 25, 50, 75 or 100')
for dim1 in range(0,np.shape(d)[0]):
        for dim2 in range(0,np.shape(d)[1]):
                for dim3 in range(0,np.shape(d)[2]):
                        if d[dim1][dim2][dim3] == d_min:
                                f[dim1][dim2][dim3] = 0
                        elif d[dim1][dim2][dim3] < d_mean:
                                f[dim1][dim2][dim3] = 25
                        elif d[dim1][dim2][dim3] == d_mean:
                                f[dim1][dim2][dim3] = 50
                        elif d[dim1][dim2][dim3] < d_max:
                                f[dim1][dim2][dim3] = 75
                        else:
                                f[dim1][dim2][dim3] = 100



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
print(f'matrix d =\n {d}\n matrix f =\n{f}')

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
dt = np.dtype(object)
g = np.empty([2,3,5],dtype=dt)
g.astype('str')
for dim1 in range(0,np.shape(d)[0]):
        for dim2 in range(0,np.shape(d)[1]):
                for dim3 in range(0,np.shape(d)[2]):
                        if d[dim1][dim2][dim3] == d_min:
                                g[dim1][dim2][dim3] = str('A')
                        elif d[dim1][dim2][dim3] < d_mean:
                                g[dim1][dim2][dim3] = str('B')
                        elif d[dim1][dim2][dim3] == d_mean:
                                g[dim1][dim2][dim3] = str('C')
                        elif d[dim1][dim2][dim3] < d_max:
                                g[dim1][dim2][dim3] = str('D')
                        else:
                                g[dim1][dim2][dim3] = str('E')

print(g)