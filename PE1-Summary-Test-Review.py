#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Variables and outputs
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print (x, y, z)


# In[ ]:


#Nested function: you deleting from index position, which matches [2]= 4=16
my_list = [x * x for x in range (5)]
def fun (lst):
    del lst [lst [2]]
    return lst

print (fun(my_list))


# In[ ]:


x = int(input())
y = int (input())
x = x % y
x = x % y
y = y % x
print (y)


# In[ ]:


y = input ()
x = input ()
print (x + y)


# 

# In[1]:


#TypeError: 'tuple' object does not support item assignment
my_tuple = (1, 2, 3, 4)
my_tuple[1] = my_tuple[1] + my_tuple[0]


# In[2]:


#Indexing tuples
tup = ( 1, 2, 4, 8)
tup = tup [-2:-1]
tup = tup [-1]
print (tup)


# In[ ]:


#The list is empty. It has a range_iterator instance. But it is empty.
lst = [ i for i in range (-1, -2)]
print (len(lst))


# In[ ]:


#The value of else is returned till y = x, then the if clause is executed. 
def fun (x, y):
    if x ==y:
        return x
    else:
        return fun(x, y-1)
print (fun (0, 3))


# In[3]:


#The else clause executes until x = y and then the if clause is executed.
def fun (x, y):
    if x ==y:
        return x
    else:
        return fun(x, y-1)
#print (fun (0, 3))
print (fun (8, 9))


# In[4]:


#The variable asked about is v and not k, so the loop doesnt affect v.
dct = {'one':'two', 'three':'one', 'two':'three'}
v = dct ['three']
    
for k in range (len(dct)):
    v = dct [v]
print (v)


# In[ ]:


#SyntaxError: positional argument follows keyword argument
def func (a, b):
    return b**a
print (func(b=2,2))


# In[ ]:


#Binary operation
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print (a, b)


# In[ ]:


##x is the key to the dictionary, so we use it to call objects by its index.
dct = {}
dct ['1'] = (1, 2)
dct ['2'] = (2, 1)
print (dct)

for x in dct.keys ():
    print (dct [x][1], end='')



# In[ ]:


#x is the key to the dictionary, so we use it to call objects by its index. 
dct = {}
dct ['yes'] = (4, 5)
dct ['no'] = (6, 7)
print (dct)

for x in dct.keys ():
    print (dct [x][1], end='')
    
    


# In[ ]:


A little intro to dictionary

d={'a':'apple','b':'ball'}
d.keys()  # displays all keys in list
['a','b']
d.values() # displays your values in list
['apple','ball']
d.items() # displays your pair tuple of key and value
[('a','apple'),('b','ball')
Print keys,values method one

for x in d.keys():
    print(x +" => " + d[x])
Another method

for key,value in d.items():
    print(key + " => " + value)
You can get keys using iter

>>> list(iter(d))
['a', 'b']
You can get value of key of dictionary using get(key, [value]):

d.get('a')
'apple'
If key is not present in dictionary,when default value given, will return value.

d.get('c', 'Cat')
'Cat'


# In[ ]:


nums = [1, 2, 3]
vals = nums

del vals [:]

print (nums)
print (vals)


# In[ ]:


#tuple.index: lloks for s specified item and returns the position where it was found.
foo = (1, 2, 3)


# In[ ]:


#Nested function: The function is called starting with the inner most one.
def fun (x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print (fun (fun(2))) 


# In[ ]:


#Handling multiple errors: capital letters at the beginning, comma separated, in parentheses, with colon at the end.
try:
    name ='Bob'
    name += 5
except (NameError, TypeError)as error:
    print (error)


# In[ ]:


#Break not in a loop. Default exception not last.
try: 
    print(5/0)
    break
except:
    print ('Sorry, something went wrong...')
except (ValueError, ZeroDivisionError):
    print('Too bad...')


# In[ ]:


try: 
    print(5/0)

except (ValueError, ZeroDivisionError):
    print('Too bad...')
    
except:
    print ('Sorry, something went wrong...')


# In[ ]:


#The result is 0.0. The input is an int divided by the len(int)=1, if 2 digits divided by 2 and so on. 
try:
    value = input("Enter a value: ")
    print (int(value)/len(value))
    
except ValueError:
    print ('Bad input...')
    
    


# In[ ]:




