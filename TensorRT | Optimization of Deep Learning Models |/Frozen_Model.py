#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import tensorflow.contrib.tensorrt as trt
from tensorflow.python.platform import gfile


# In[21]:


print(tf.__version__)


# In[8]:


"""
Creating session for TensorRT Optimisation
"""
with tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(per_process_gpu_memory_fraction=0.50))) as sess:
    """
    importing the .meta file from tensorflow Model
    
    """
    saver = tf.train.import_meta_graph("Models.meta")
    """
    Restore the weights to meta graph
    """
    saver.restore(sess, "./Models")
    
    """
    
    Here You need to specify the tensor you want as output, To find this. You can look at the model's graph
    You can tensorboard to find the graph of your model or a web application which is already on internet
    
    """
    your_outputs = ["output_tensor/Softmax"]
    


# In[25]:


"""
Convert to Frozen Model

"""

frozen_graph = tf.compat.v1.graph_util.convert_variables_to_constants(
        sess, tf.compat.v1.get_default_graph().as_graph_def(),
        output_node_names=your_outputs)


# In[ ]:




