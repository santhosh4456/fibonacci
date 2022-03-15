#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers = int(input("How many numbers? :"))
a, b =  0, 1
count = 0
if numbers<=0:
    print("Please enter a positive integer")
else:
    for i in range(0, numbers):
        print(count, end= " ")
        a = b
        b = count
        count = a + b


# In[ ]:




