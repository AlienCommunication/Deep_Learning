#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""

Let's put the full path of the folder having labelled frames from the video

"""

Full_Images_Path = '/home/kris/Downloads/Tensorflow_files/YOLO-3-OpenCV/Video_Frames/Labelled Frames'

"""


Now Let's create the classes.names file

=================================================


Defining the counter for the classes

"""
c = 0

""" 
Let's use the exisiting file classes.txt which is in the labelled image folder and create this classes.names file

"""

with open(Full_Images_Path + '/' + 'classes.names', 'w') as names,      open(Full_Images_Path + '/' + 'classes.txt', 'r') as txt:

    """
    Will go through all the lines in txt file and write them into .names file
    
    """
    
    for line in txt:
        names.write(line)  
        

        """
        
        Increasing the counts
        
        """
        c += 1


# In[4]:


"""


Creating the .data file

"""

with open(Full_Images_Path + '/' + 'labelled_data.data', 'w') as data:
    
    
    data.write('classes = ' + str(c) + '\n')

    """ 
    Location of the train.txt file
    
    """
    data.write('train = ' + Full_Images_Path + '/' + 'train.txt' + '\n')

    """
    
    Location of the test.txt file
    
    """
    data.write('valid = ' + Full_Images_Path + '/' + 'test.txt' + '\n')

    """
    Location of the .names file
    
    """
    data.write('names = ' + Full_Images_Path + '/' + 'classes.names' + '\n')

    """
    
    Backup or save the weights for later use
    
    """
    data.write('backup = backup')


# In[ ]:





# In[ ]:




