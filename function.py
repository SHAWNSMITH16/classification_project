from env import get_connection
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import scipy.stats as stats
from scipy import stats
# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")


seed = 42

def telco_churn(df):
    '''This function takes in the telco df specifically and drops the 
    listed columns, creates dummy variables for the selected columns, and renames
    the dummy variable columns to make them easier to read'''
    
    drop_cols = ['Unnamed: 0', 'payment_type_id', 'contract_type_id', 'gender', 
                   'senior_citizen', 'partner', 'dependents', 'phone_service', 'multiple_lines',
                   'streaming_tv', 'streaming_movies', 'contract_type', 'payment_type', 'internet_service_type_id']
    
    df.drop(columns = drop_cols, inplace = True)
    
    dummies = pd.get_dummies(df[['online_security','online_backup', 'device_protection', 
                        'tech_support', 'paperless_billing', 'churn', 'internet_service_type']], drop_first = True)

    df = pd.concat([df, dummies], axis = 1)
    
    df.drop(columns = ['online_security','online_backup', 'device_protection', 
                        'tech_support', 'paperless_billing', 'churn', 'internet_service_type'], inplace = True)
    
    df.rename(columns = {'online_security_No internet service': 'online_security_NA', 
                         'online_backup_No internet service': 'online_backup_NA',
                         'device_protection_No internet service': 'device_prot_NA',
                         'tech_support_No internet service': 'tech_support_NA', 
                         'internet_service_type_Fiber optic': 'has_fiber',
                         'internet_service_type_None': 'internet_service_type_NA'}, inplace = True)
    
    return df



def cleanup(df):
    '''The purpose of this function is to cleanup the total_charges column by first removing
    any whitespace using the strip function, then identifying any non-values (not nulls),
    then changing the datatype from an object to a float to make it readable for the model, 
    and finally making all of the columns lower case for uniformity'''
    df.total_charges = df.total_charges.str.strip()
    
    df = df[df.total_charges != ""]
    
    df.total_charges = df.total_charges.astype(float)
    
    df.columns = df.columns.str.lower()
    
    return df




def model_report():
    data = {'Model': ['Decision Tree', 'Random Forest', 'Logistic Regression'],
            'Train Accuracy': [79.11, 78.91, 79.92],
            'Validate Accuracy': [79.06, 78.67, 79.46],
            'Precision': [81, 80, 84]}
    return pd.DataFrame(data)



def get_tree(X_train, X_validate, y_train, y_validate):
    '''get decision tree accuracy on train and validate data'''

    # create classifier object
    clf = DecisionTreeClassifier(max_depth=3, random_state=123)

    #fit model on training data
    clf = clf.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Decision Tree on train data is {clf.score(X_train, y_train)}")
    print(f"Accuracy of Decision Tree on validate data is {clf.score(X_validate, y_validate)}")



def get_forest(X_train_rf, X_validate_rf, y_train_rf, y_validate_rf):
    '''get random forest accuracy on train and validate data'''

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=3, random_state=123)
    rf.fit(X_train_rf,y_train_rf)

    # print result
    print(f"Accuracy of Random Forest on train is {rf.score(X_train_rf, y_train_rf)}")
    print(f"Accuracy of Random Forest on validate is {rf.score(X_validate_rf, y_validate_rf)}")



def get_log_reg(X_train_lr, X_validate_lr, y_train_lr, y_validate_lr):
    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    logit = LogisticRegression(solver='liblinear')
    logit.fit(X_train_lr, y_train_lr)

    # print result
    print(f"Accuracy of Logistic Regression on train is {logit.score(X_train_lr, y_train_lr)}")
    print(f"Accuracy of Logistic Regression on validate is {logit.score(X_validate_lr, y_validate_lr)}")