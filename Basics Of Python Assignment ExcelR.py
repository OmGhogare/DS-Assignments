#!/usr/bin/env python
# coding: utf-8

# In[6]:


#  Python Programming Assignment  #


# In[7]:


#Coding Exercises


# In[8]:


# Exercise 1: Prime Numbers


# In[5]:


def is_prime(number):
    if number<=1:
        return False
    
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
    


num=int(input("Enter a number to check if it is prime : "))
if is_prime(num):
    print(f"{num} is a prime number ")
else:
    print(f"{num} is a not prime number ")
    


# In[9]:


# Exercise 2: Product of Random Numbers


# In[14]:


import random

def multiplication():
    number1=random.randint(1,10)  # Generate two random numbers between 1 and 10
    number2=random.randint(1,10)
    
    answer=number1*number2           # Calculate the correct product
    
    print(f"What is the product of {number1} and {number2}?")  # Ask the user for their answer
    user_value=int(input("enter your answer: "))
    
    if user_value==answer:  # Check if the user's answer is correct
        print("correct answer !")
    else:
        print("Sorry Incorrect ! The correct answer is : ", answer)
        
    
multiplication()


# In[ ]:


# Exercise 3: Squares of Even/Odd Numbers


# In[3]:


def odd_even_square():
    print("Squares of even number: ")
    for number in range (100,201):
        #if number%2==0:
            print(f"The square of {number} is {number**2}")
      
'''  
    print("Squares of odd number: ")
    for number in range (100,201):
        if number%2!=0:
            print(f"The square of {number} is {number**2}")    
# number=int(input("Enter a number : "))
'''
odd_even_square()


# In[ ]:


#Exercise 4: Word counter
'''write a program to count the number of words in a given text.
example:
input_text = "This is a sample text. This text will be used to demonstrate the word counter."
Expected output:
'This': 2 
'is': 1
'a': 1
'sample': 1
'text.': 1
'''


# In[22]:


from collections import Counter

def word_counter(input_text):
    
    words = input_text.split()    # Split the text into words
 
    word_counts = Counter(words)  # Count the occurrences of each word
    
    # Print the results
    for word, count in word_counts.items():
        print(f"'{word}': {count}")


input_text = "This is a sample text. This text will be used to demonstrate the word counter."
word_counter(input_text)


# In[ ]:


# Exercise 5: Check for Palindrome


# In[29]:


def is_palindrome(string):
    return string == string[::-1]  # logic for palindrome   string [::-1] reverses the string string.

   
    
input_string=input("Enter a string to check for palindrome: ")
   
    
if is_palindrome(input_string):
    print(f"{input_string} is palindrome ")
else:
    print(f"{input_string} is not a palindrome ")
        


# In[ ]:




