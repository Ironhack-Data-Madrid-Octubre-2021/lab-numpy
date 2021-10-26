#1. Import the NUMPY package under the name np.
import numpy as np
from numpy.lib.histograms import _histogram_dispatcher


#2. Print the NUMPY version and the configuration.
print(np.__version__)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2, 3, 5))
np.shape(a)

a_1 = np.random.randint(10, size =(3, 5))
np.shape(a_1)

a_2 = np.random.randint(low=3, high=5, size=(2, 3, 5))
np.shape(a_2)

#4. Print a.
print(a)
print(a_1)
print(a_2)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.random.randint(low=1, high=2, size=(5, 2, 3))

#6. Print b.

print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print(np.size(a) == np.size(b))
print(np.size(a))
print(np.size(b))

#8. Are you able to add a and b? Why or why not?

        #No because they have different shapes. E.g.: 
#a + b error

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1, 2, 0)

print(a.shape)
print(b.shape)
print(c.shape)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c

print(d)


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)

#'d' is the sum of each of the items that share the same position in 'a' and 'b'.


#12. Multiply a and c. Assign the result to e.

e = a * c
print(e)

#13. Does e equal to a? Why or why not?

print(e == a)
#True, 'e' is equal to ('a' * 'b') and 'b' is a table of 1's



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
print(d)

d_max, d_min, d_mean = d.max(), d.min(), d.mean()

print(f'd max value is {d_max}')
print(f'd min value is {d_min}')
print(f'd mean is {d_mean}')


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2, 3, 5))

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

#if value == 'd_min': f = 0
#if value > 'd_min' and value < 'd_mean': f = 25
#if value == 'd_mean': f = 50
#if value > 'd_mean' and value < 'd_max': f = 75
#if value == 'd_max': f = 100
print("____________________________________________________________________")
print (f)
print("____________________________________________________________________")

np.shape(f)
x = np.shape(f)[0]
y = np.shape(f)[1]
z = np.shape(f)[2]

for i in range(x):
        for w in range(y):
                for q in range(z):
                        if d[i,w,q] == d_min:
                                f[i,w,q] = 0
                        elif d[i,w,q] > d_min and d[i,w,q] < d_mean:
                                f[i,w,q] = 25
                        elif d[i,w,q] == d_mean:
                                f[i,w,q] = 50
                        elif d[i,w,q] > d_mean and d[i,w,q] < d_max:
                                f[i,w,q] = 75
                        else:
                                f[i,w,q] = 100


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

print(d)
print(f)

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


f = np.ndarray.astype(f, dtype=str)
for i in range(x):
        for w in range(y):
                for q in range(z):
                        if d[i,w,q] == d_min:
                                f[i,w,q] = 'E'
                        elif d[i,w,q] > d_min and d[i,w,q] < d_mean:
                                f[i,w,q] = 'D'
                        elif d[i,w,q] == d_mean:
                                f[i,w,q] = 'C'
                        elif d[i,w,q] > d_mean and d[i,w,q] < d_max:
                                f[i,w,q] = 'B'
                        else:
                                f[i,w,q] = 'A'

print(f)