#This script sends request to web service which accepts customer info and returns the prediction whether customer will subscribe for Term Deposit with the Bank

#Before running this script, ensure you have run the following command from command line on the linux server that hosts the code to start the web service OR you have created Docker container that runs this script
#python predict.py

#Import libraries
import pandas as pd
import numpy as np
import requests

#Change the URL if the prediction service is running from Cloud
url = 'http://localhost:9696/predict'

customer1 = {'age': 39, 'job': 'blue-collar', 'marital': 'married', 'education': 'high.school', 'default': 'no', 'housing': 'yes', 'loan': 'no', 'contact': 'telephone', 'month': 'may', 'day_of_week': 'fri', 'duration': 480, 'campaign': 2, 'pdays': 999, 'previous': 0, 'poutcome': 'nonexistent', 'emp.var.rate': 1.1, 'cons.price.idx': 93.994, 'cons.conf.idx': -36.4, 'euribor3m': 4.855, 'nr.employed': 5191.0}
customer2 = {'age': 53, 'job': 'services', 'marital': 'married', 'education': 'basic.9y', 'default': 'no', 'housing': 'yes', 'loan': 'no', 'contact': 'cellular', 'month': 'aug', 'day_of_week': 'mon', 'duration': 196, 'campaign': 2, 'pdays': 999, 'previous': 0, 'poutcome': 'nonexistent', 'emp.var.rate': -1.7, 'cons.price.idx': 94.027, 'cons.conf.idx': -38.3, 'euribor3m': 0.898, 'nr.employed': 4991.6}
customer3 = {'age': 38, 'job': 'blue-collar', 'marital': 'single', 'education': 'basic.4y', 'default': 'no', 'housing': 'no', 'loan': 'no', 'contact': 'cellular', 'month': 'may', 'day_of_week': 'wed', 'duration': 207, 'campaign': 1, 'pdays': 999, 'previous': 1, 'poutcome': 'failure', 'emp.var.rate': -1.8, 'cons.price.idx': 92.893, 'cons.conf.idx': -46.2, 'euribor3m': 1.334, 'nr.employed': 5099.1}
customer4 = {'age': 36, 'job': 'admin.', 'marital': 'single', 'education': 'basic.6y', 'default': 'no', 'housing': 'yes', 'loan': 'no', 'contact': 'telephone', 'month': 'may', 'day_of_week': 'wed', 'duration': 125, 'campaign': 2, 'pdays': 999, 'previous': 1, 'poutcome': 'failure', 'emp.var.rate': -1.8, 'cons.price.idx': 92.893, 'cons.conf.idx': -46.2, 'euribor3m': 1.334, 'nr.employed': 5099.1}
customer = customer4

response = requests.post(url,json=customer).json()
subs_prob = response['subscription_probability']
subs = response['subscription']

if subs:
    print(f"Customer is likely to subscribe to Term Deposit with Bank with a probability of {subs_prob}. Make a call to the customer to secure Term Deposit")
else:
    print(f"Customer may not subscribe to Term Deposit. The probability of this is {subs_prob}. Not required to call the customer")
