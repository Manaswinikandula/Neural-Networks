#!/usr/bin/env python
# coding: utf-8

# In[1]:


#QUESTION 1
#input the string,delete atleast 2 characters,reverse the resultant string and print it
str=input("Enter a string")
length=len(str)
delete=str[:length-2]
strRev = delete[::-1]
print ("final output is:", strRev)


# In[3]:


#QUESTION 2

#accept a sentence and replace each occurance of 'python' with 'pythons'

str="I'm ready to learn python"
modified_str=str.replace('python','pythons')
print("Modified string:")
print(modified_str)


# In[4]:


#QUESTION 3

#print the letter grade based on input class score

score=int(input("Enter your score:"))
print("Your score is",score)
if score >= 90 and score <= 100:
    print("Your Grade is A")
elif score >= 80 and score <= 89:
    print("Your Grade is B")
elif score >= 70 and score <= 79:
    print("Your Grade is C")
elif score >= 60 and score <= 69:
    print("Your Grade is D")
else:
    print("Your Grade is F")


# In[ ]:




