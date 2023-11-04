#!/usr/bin/env python
# coding: utf-8

# In[2]:



def read_txt(file_name):
    ##Data_description = np.loadtxt("dataset_description.txt", dtype=int)
    #get file object
    f = open(file_name , "r")

    while(True):
        #read next line
        line = f.readline()
        #if line is empty, you are done with all lines in the file
        if not line:
            break
        #you can access the line
        print(line.strip())

    #close file
    f.close


def plot_missing_values(x_val , y_val):
    plt.figure(figsize=(18 , 8))
    plt.xlabel("Number of missing values")
    plt.ylabel("Columns")
    plt.title("Missing values count in Dataset")
    plt.barh(x,sorted(y))
    plt.show()


# In[ ]:




