#!/usr/bin/env python
# coding: utf-8

#Import libraries

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
import pickle


#Read data
datafile = 'bank-additional-full.csv'
df = pd.read_csv(datafile,delimiter=';')


#Convert y value from 'yes', 'no' to 1 and 0
df['y'] = (df['y'] == 'yes').astype(int)
df['y'].value_counts(normalize=True)


#Splitting data as Full Train (90%), Test (10%) - we will use only the full train data in this script for training.
df_full_train, df_test = train_test_split(df,test_size=0.1,shuffle=True,random_state=1)
df_full_train = df_full_train.reset_index(drop=True)


#Define y_full_train and delete it from dataframe to avoid accidental use
y_full_train = df_full_train['y'].values
del df_full_train['y']

#Delete feature 'duration'. According to the info provided in dataset, this relates to call made to a customer and if call is made anyway the outcome is known. Thus practical perspective 'duration' shoult not be used to build a practical model 
del df_full_train['duration']

#Delete feature 'job' since based on experiments performed we found that removing this feature increases the score of model
del df_full_train['job']

#Hyper-parameters that let to best score for the best model XGBoost
xgb_params = {
    'seed': 42, 
    'eval_metric': 'auc', 
    'n_jobs': -1,
    'booster': 'gbtree', 
    'colsample_bytree': 0.4,
    'learning_rate': 0.01, 
    'max_depth': 3, 
    'min_child_weight': 5,  
    'objective': 'binary:logistic', 
    'random_state': 42,
}

#Initialize DictVectorizer
dv = DictVectorizer(sparse=False)

#As per experiments we found that using polynomial features from the numerical features gave better score
poly = preprocessing.PolynomialFeatures(degree=3, interaction_only=True, include_bias=False)

#Determine the numerical features and for these find the polynomial features
num_cols = list(df_full_train.columns[df_full_train.dtypes != 'object'])
X_full_train_num = poly.fit_transform(df_full_train[num_cols])
df_full_train_poly = pd.DataFrame(X_full_train_num, columns=[f"poly_{i}" for i in range(X_full_train_num.shape[1])])

#Replace the original numerical features with these polynomial features
df_full_train.drop(num_cols,axis=1,inplace=True)
poly_cols = list(df_full_train_poly.columns.values)
df_full_train[poly_cols] = df_full_train_poly[poly_cols]


#Perform One-hot encoding using DictVectorizer
new_features = list(df_full_train.columns.values)
dict_full_train_new = df_full_train[new_features].to_dict(orient='records')
X_full_train_new = dv.fit_transform(dict_full_train_new)

#Create the DMatrix for training using XGBoost
feature_names = dv.get_feature_names()
dfulltrain = xgb.DMatrix(X_full_train_new,label=y_full_train,feature_names=feature_names)

#Train the model
model = xgb.train(xgb_params,dfulltrain,num_boost_round=335)

# Save model to disk
model_output_file = f'xgb_model.bin'

with open(model_output_file,'wb') as f_out:
    pickle.dump((poly,dv,model),f_out)

