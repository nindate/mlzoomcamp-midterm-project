#Import libraries
import pandas as pd
import xgboost as xgb
import pickle
from flask import Flask, request, jsonify

#Parameters
model_file = 'xgb_model.bin'
threshold = 0.32

# Load the model
print("Loading model from file on disk")
with open(model_file,'rb') as f_in:
    poly, dv,model = pickle.load(f_in)

def predict_term_subscription(customer):
    #Create dataframe to hold the customer info received
    df_customer = pd.DataFrame()
    df_customer = df_customer.append(customer,ignore_index=True)

    cols = list(df_customer.columns.values)
    #From the input data, drop 'job' as this is not a useful feature.
    if 'jobs' in cols:
        del df_customer['job']

    #Since we might choose a random sample from entire data set or test dataset, it will also have the feature 'duration', which in real scenario will not be available.
    #Thus for the sake of this project, if 'duration' feature is available in received data, remove it
    if 'duration' in cols:
        del df_customer['duration']
        cols.remove('duration')


    #Create polynomial features for the numerical features
    num_cols = list(df_customer.columns[df_customer.dtypes != 'object'])
    X_num = poly.transform(df_customer[num_cols])
    df_X_poly = pd.DataFrame(X_num, columns=[f"poly_{i}" for i in range(X_num.shape[1])])
    poly_cols = list(df_X_poly.columns.values)

    #Replace original numerical features with the polynomial features
    df_customer.drop(num_cols,axis=1,inplace=True)
    df_customer[poly_cols] = df_X_poly[poly_cols]

    #Perform One-Hot encoding on the features
    features = list(df_customer.columns.values)
    dict_customer = df_customer[features].to_dict(orient='records')
    X_customer = dv.transform(dict_customer)


    #Prepare DMatrix of customer data to be used by the XGBoost model
    feature_names = dv.get_feature_names()
    dcustomer = xgb.DMatrix(X_customer,feature_names=feature_names)

    y_customer_pred = model.predict(dcustomer)
    subscription = (y_customer_pred > threshold)

    return y_customer_pred, subscription


app = Flask('subscription')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    y_customer_pred, subscription = predict_term_subscription(customer)

    if subscription:
        description = "Prediction: Customer will make a Term deposit"
    else:
        description = "Prediction: Customer will not make a Term deposit"

    #Need to convert numpy float and boolean to python float and bool, hence use the float() and bool() as below
    result = {
            'subscription_probability': float(y_customer_pred),
            'subscription': bool(subscription),
            'description': description
            }

    return jsonify(result)

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=9696)

