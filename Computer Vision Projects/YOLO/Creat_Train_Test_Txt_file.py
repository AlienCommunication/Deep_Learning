#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os


# In[2]:


Full_Images_Path = '/home/kris/Downloads/Tensorflow_files/YOLO-3-OpenCV/Video_Frames/Labelled Frames'


# In[6]:


os.chdir(Full_Images_Path)


# In[11]:


"""

WIll make a list where I will write all found full paths to the Images

"""


p = []



for current_dir, dirs, files in os.walk('.'):
    """
    Going through all files
    """
    for f in files:
        
        """
        Checking if the file name ends with jpeg
        
        """
        if f.endswith('.jpeg'):
            """
            Preparing path to save into train.txt file
            Pay attention!
            If you're using Windows, it might need to change
            this: + '/' +
            to this: + '\' +
            or to this: + '\\' +"""
            path_to_save_into_txt_files = Full_Images_Path + '/' + f

            """
            Appending the line into the list
            We use here '\n' to move to the next line
            when writing lines into txt files
            """
            p.append(path_to_save_into_txt_files + '\n')


# In[12]:


"""

Slicing first 15% of elements from the list
to write into the test.txt file

"""

p_test = p[:int(len(p) * 0.15)]

""" 

Deleting first 15% of elements from the list

"""
p = p[int(len(p) * 0.15):]


# In[18]:


"""
Creating Train.txt and Test.txt file
Creating file train.txt and writing 85% of lines in it
"""

with open('train.txt', 'w') as train_txt:
    
    """ 
    Going through all elements of the list
    """ 
    for e in p:
        """ 
        Writing current path at the end of the file
        """
        train_txt.write(e)

""" 
Creating file test.txt and writing 15% of lines in it
"""

with open('test.txt', 'w') as test_txt:
    """ 
    Going through all elements of the list
    """ 
    for e in p_test:
        """
        Writing current path at the end of the file
        """
        test_txt.write(e)


# In[ ]:




