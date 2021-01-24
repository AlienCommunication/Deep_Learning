Note : Please make sure Python3 is already installed on your Machine

Setting up the Enviroment 


**Create Virtual Environment within the project folder**

1. cd ImageProcessingChallenge
3. sudo apt install python3-venv
4. python3 -m venv CVEngineer_project_env
5. source CVEngineer_project_env/bin/activate

***Once you have activated the virtual environment you will find this environment name ahead your command all***

**Let's install the requirred dependencies :**

6. pip install opencv-python

**Let's run the project :**

7. python3 src.py

To display the resule

7. open writeup.html

**Following Techniques have been demonstrated in this project**

1. Brighten the Image
2. Change the contrast of the image
3. Sharpen the image
4. Blur the image
5. Change the saturation of the image
6. Detect the edges in the image
7. Composite operation: I have used alpha channel on the top of masked image

Result

==================================

![alt text](https://github.com/aish0606/ImageProcessing/blob/main/ImageProcessingChallenge/result.PNG)


References:

1. https://www.cs.princeton.edu/courses/archive/spring14/cos426/assignment1/examples.html
2. https://learnopencv.com/alpha-blending-using-opencv-cpp-python/
