import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
from datetime import datetime 
import numpy as np
import pickle 

from keras.models import Sequential
from keras.layers import Dense

data=pd.read_csv('test.csv')

def date_func(date):
    tmp= datetime.now()-datetime.strptime(date, "%Y-%m-%d")
    days=tmp.days
    return days

X=data.drop(columns=['credit_raiting'])

Y=data[['credit_raiting']]
X['birth_date']=X['birth_date'].apply(lambda x:date_func(x) )
min_max_scaler = preprocessing.MinMaxScaler()
min_max_scaler1 = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)
Y_scale = min_max_scaler1.fit_transform(Y)
X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y_scale, test_size=0.3)
X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)






# Defining a function for finding best hyperparameters
def FunctionFindBestParams(X_train, y_train):  
    filename = 'model.sav'
    # Defining the list of hyper parameters to try
    if os.path.isfile(filename):
        classifier=pickle.load(open(filename, 'rb'))
    else:
    # Creating the classifier ANN model
        classifier = Sequential()
        classifier.add(Dense(units=80, input_dim=11, kernel_initializer='uniform', activation='relu'))
        classifier.add(Dense(units=150, kernel_initializer='uniform', activation='relu'))
        classifier.add(Dense(units=150, kernel_initializer='uniform', activation='relu'))
        classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
        classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


        survivalANN_Model=classifier.fit(X_train,y_train, batch_size=50 , epochs=2000, verbose=0)
    # Fetching the accuracy of the training
    
    
    # printing the results of the current iteration
   
    dta=pd.DataFrame({"birth_date":12725,
                        "salary":77892,
                        "active_credit_size":5606,
                        "co_borrower_size":7314,
                        "o_credit_peoples":7703,
                        "poruch":True,
                        "children_count":2,
                        "children_aliment_count":1,
                        "marriage":False,
                        "amount":818121,
                        "period":356,
                        }, index=[0])
    
    Predictions=classifier.predict(min_max_scaler.transform(dta.to_numpy()))
    # Scaling the test data back to original scale
    if ~os.path.isfile('model.keras'):
        pickle.dump(classifier, open(filename, 'wb'))
        
    
    return Predictions
 
###############################################
 
# Calling the function
# ResultsData=FunctionFindBestParams(X_train, Y_train)
# print(ResultsData)