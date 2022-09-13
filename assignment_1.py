# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aWqhkVA1HUMnJ87bpk2QQB97yvcdjNul

## 1. Split this string

# Basic Python
"""

s = "Hi there Sam!"

x=s.split()
print(x)

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

planet = "Earth"
diameter = 12742
print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a=lst[3][1][2];
print(a)

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)

array=np.ones(10)*5
print("An array of 10 fives:")
print(array)

"""## 5. Create an array of all the even integers from 20 to 35"""

lst = list(range(20,35))
print(lst)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

import numpy as np
x =  np.arange(0, 9).reshape(3,3)
print(x)

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

import numpy as np
a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])
np.concatenate((a, b), axis=None)
([1, 2, 3, 4, 5, 6])

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

data = [['tomy', 72], ['nike', 73], ['riya', 74]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

import pandas as pd 
per1 = pd.date_range(start ='01-01-2023', end ='02-10-2023')
for val in per1:
    print(val)

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

import pandas as pd  
lst = [[ 'aaa', 22], ['bbb', 25], 
       ['ccc', 24]]  
df = pd.DataFrame(lst, ) 
print(df )