https://github.com/Bgolearn

https://bgolearn.netlify.app

------

# BgoFace User Manual

# 1.Introduction

The BgoFace is the user interface of the Bgolearn Platform. This user manual describes how to use BgoFace.

# 2.Upload sample file

## 2.1File format requirements

- **The training sample files and virtual sample files are Excel files with the suffix 'xls' or 'xlsx'.**
- **The last column of the training sample file is used as a single target.**

## 2.2Upload training sample and virtual sample

When in **"Input" mode**, click the **"Load Data"** button to display the file upload interface.

![image-20240731181310387](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731181310387.png)

Click the **"Browse"** button to select the training sample and virtual sample files to upload.

![image-20240731181253913](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731181253913.png)

After selecting the training sample and virtual sample, the **file path** is displayed in the Load window.

![image-20240731182453353](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731182453353.png)

Click the **"Load"** button and the files will be loaded into the main window.

![image-20240731191826547](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731191826547.png)

## 2.3Upload training sample and generate virtual sample

When in **"Manual" mode**, click the **"Load Data"** button to display the file upload interface.

![image-20240731192032524](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731192032524.png)

Similar to the above steps, upload and load the training sample file into the main window.

![image-20240731192350522](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731192350522.png)

In the Samples area, you can see that all samples are selected. **Select the samples you need to create virtual samples.**

For example, "Sn", "Bi", "In" and "Ti" to generate the virtual sample.

![image-20240731192750963](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731192750963.png)

**Select a sample and generate the corresponding virtual sample by adjusting the minimum, maximum and step size.**

![image-20240731193759116](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731193759116.png)

**Click the "OK" button to select the next sample.** **When all selected samples are processed, the virtual sample is generated and displayed in the main window.**

![image-20240731194009811](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731194009811.png)

After the virtual sample is generated, click the **"Download"** button and **select the downloaded folder to download the virtual sample.**

![image-20240731194258623](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731194258623.png)

Click the **"OK"** button to **download the virtual sample to the specified folder**.

![image-20240731194349501](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731194349501.png)

![image-20240731194323941](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731194323941.png)

# 3.Parameter setting

After obtaining the training sample and virtual sample, **set the operating parameters**. 

![image-20240731194702257](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731194702257.png)

Click **"Parameter"** in the menu bar and **set the parameters in the Parameter window**.

![image-20240731194837663](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731194837663.png)

## 3.1Regression

Choose the **"Regression"** mode, select different functions and their corresponding parameter settings. 

![image-20240731195124516](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731195124516.png)

Click the **"Reset"** button and the parameters are set to default setting.

![image-20240731195259234](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731195259234.png)

**Click the "OK" button to complete the parameter setting.**

## 3.2Classification

Choose the **"Classification"** mode, set the parameters and choose the function. 

![image-20240731195702335](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731195702335.png)

Click the **"Reset"** button and the parameters are set to default setting.

![image-20240731195501081](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731195501081.png)

**Click the "OK" button to complete the parameter setting.**

# 4.Fit

**After completing the parameter settings, click the "Fit" button to view the results in the Result window.**

![image-20240731200127255](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731200127255.png)

![image-20240731200141705](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731200141705.png)

![image-20240731200206139](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240731200206139.png)