import os
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import pandas as pd
from datetime import datetime 
import numpy as np
import pickle 

from keras.models import Sequential
from keras.layers import Dense



def date_func(date):
        if type(date)==str:
            tmp= datetime.now()-datetime.strptime(date, "%Y-%m-%d")
        else:
             tmp= datetime.today()-datetime.combine(date, datetime.min.time())
        days=tmp.days
        
        return days

def minmax():
    min_max_scaler = preprocessing.MinMaxScaler()
    data=pd.read_csv('test.csv')
    X=data.drop(columns=['credit_raiting'])
    X['birth_date']=X['birth_date'].apply(lambda x:date_func(x) )
    X_scale = min_max_scaler.fit_transform(X)
    return min_max_scaler


def data_processing():
    min_max_scaler = preprocessing.MinMaxScaler()
    min_max_scaler_y = preprocessing.MinMaxScaler()
    data=pd.read_csv('test.csv')
    X=data.drop(columns=['credit_raiting'])
    Y=data[['credit_raiting']]
    X['birth_date']=X['birth_date'].apply(lambda x:date_func(x) )
    
    X_scale = min_max_scaler.fit_transform(X)
    Y_scale = min_max_scaler_y.fit_transform(Y)
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y_scale, test_size=0.3)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
    return X_train,Y_train


def model_learning(filename):
    
    X_train,Y_train = data_processing()

    classifier = Sequential()
    classifier.add(Dense(units=80, input_dim=11, kernel_initializer='uniform', activation='relu'))
    classifier.add(Dense(units=150, kernel_initializer='uniform', activation='relu'))
    classifier.add(Dense(units=150, kernel_initializer='uniform', activation='relu'))
    classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


    Model=classifier.fit(X_train,Y_train, batch_size=50 , epochs=2000, verbose=0)
    pickle.dump(Model, open(filename, 'wb'))
    return Model


def classify(data):
    min_max_scaler= minmax()
    filename = 'model.sav'
    # Defining the list of hyper parameters to try
    if os.path.isfile(filename):
        classifier=pickle.load(open(filename, 'rb'))
    else:
        classifier = model_learning(filename)

    Predictions=classifier.predict(min_max_scaler.transform(data.to_numpy()))

    return Predictions


# dta=pd.DataFrame({"birth_date":12725,
#                         "salary":77892,
#                         "active_credit_size":5606,
#                         "co_borrower_size":7314,
#                         "o_credit_peoples":7703,
#                         "poruch":True,
#                         "children_count":2,
#                         "children_aliment_count":1,
#                         "marriage":False,
#                         "amount":818121,
#                         "period":356,
#                         }, index=[0])
# print(classify(dta))