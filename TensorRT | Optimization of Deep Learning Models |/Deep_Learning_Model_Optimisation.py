#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""

Optimising the frozen model to TensorRT Graph

"""

trt_graph = trt.create_inference_graph(
    input_graph_def=frozen_graph,
    outputs=your_outputs,
    max_batch_size=2,
    max_workspace_size_bytes=2*(10**9),
    precision_mode="FP32")

"""
Let's write the TensorRT Model to be used later for inference

"""

with gfile.FastGFile("./model/TensorRT_model.pb", 'wb') as f:
    f.write(trt_graph.SerializeToString())
print("TensorRT model is successfully stored!")


# In[ ]:


"""

In case you would like to know number of nodes or operation before or after optimisation

"""

"""

Checking Frozen model's operations

"""
all_nodes = len([1 for n in frozen_graph.node])
print("numb. of all_nodes in frozen graph:", all_nodes)

"""
Checking TensorRT model's operation

"""
trt_engine_nodes = len([1 for n in trt_graph.node if str(n.op) == 'TRTEngineOp'])
print("numb. of trt_engine_nodes in TensorRT graph:", trt_engine_nodes)
all_nodes = len([1 for n in trt_graph.node])
print("numb. of all_nodes in TensorRT graph:", all_nodes)


# In[ ]:




