# ML Zoomcamp Midterm Project

This repo contains the work carried out as part of the Mid Term project for the course ML Zoomcamp. This course is conducted by Alexey Grigorev. You can take the course at any time and it is free. Links to course mentioned below:

* https://datatalks.club/courses/2021-winter-ml-zoomcamp.html
* https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp

## About the Project

Banks are important institutions that provide funds, in terms of loans, to businesses and individuals to function and prosper. However banks need money to provide as loan and to also make their own investments (e.g. in stocks). One such good source that banks have is in the from of Term Deposits that bank's customers make.

Banks regularly make calls to their customers to secure such Term deposits. However, from a big list of all its customers, it would be wise to make calls to the customers who are more likely to invest. This way, banks can reduce the cost of acquisition of Term deposit (in the form of payment to staff making call, call charges and so on.).

This project aims at building a machine learning model that can be trained from previous marketing campaigns and data collected, to predict customers that potentialy will subscribe to Term deposit with the bank. Further, the prediction model will be hosted as a web service, which can accept customer data (in JSON format) and return the prediction (whether customer is likely to subscribe to Term deposit).


## Key files and folders explained



## Work explained

Jupyter notebook [notebook.ipynb](./notebook.ipynb) contains all the code for coming up with the ML model for this project. This notebook contains the following:
```
1. About the project
2. Import libraries and load data
3. Exploratory data analysis (EDA)
  3.1 EDA - basic
  3.2 EDA - additional
4. Baseline model
5. Improvement over baseline model
  5.1 Logistic Regression
  5.2 Decision Tree
  5.3 Random Forest
  5.4 XGBoost
6. Final model
  6.1 Compare results from hyper-parameter tuning for the different models and choose final model
  6.2 Train final model
```


## Train the model


## Deployment of model as a web service, running as a Docker container


## Deployment of model as a web service, running on Cloud
