# Importing the modules
import pandas as pd
import matplotlib.pyplot as plt
# Importing the dataset
dataset = pd.read_csv('Linear regression//Data_for_LR.csv')
#get a copy of dataset exclude last column
X = dataset.iloc[:, :-1].values 
#get array of dataset in column 2st
y = dataset.iloc[:, 1].values 
# visualization part 
viz_train = plt
viz_train.scatter(X, y, color='red')
viz_train.title('Hours vs Score')
viz_train.xlabel('Hours')
viz_train.ylabel('Score')
viz_train.show()