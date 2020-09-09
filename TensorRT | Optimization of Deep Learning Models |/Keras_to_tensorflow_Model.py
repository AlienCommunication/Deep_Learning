#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[8]:


"""
Note : I already have the .h5 file saved in my directory.

Import the Libraries

"""

import tensorflow as tf

"""
Use this line of code only if you have batch normalisation in your keras model architecture. Now Why am I using it so

I do not want to put the penalty on gradients again

"""
tf.keras.backend.set_learning_phase(0) 
from tensorflow.keras.models import load_model
"""
This is the Path I want to save my converted Tensorflow Model
"""

Tensorflow_Model_Path = "./Models"

"""
Loading the keras model (.h5 file)

""" 
Keras_Model = load_model("./Models/modelLeNet5.h5")


"""
Saver is same for Keras and Tensorflow hence using it for conversion
"""
saver = tf.train.Saver()
sess = tf.keras.backend.get_session()
save_path = saver.save(sess, Tensorflow_Model_Path)

print("Your new tensorflow model has been saved in the directory "+ Tensorflow_Model_Path)


# In[ ]:




