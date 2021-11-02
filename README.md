# ML Zoomcamp Midterm Project

This repo contains the work carried out as part of the Mid Term project for the course ML Zoomcamp. This course is conducted by Alexey Grigorev. You can take the course at any time and it is free. Links to course mentioned below:

* https://datatalks.club/courses/2021-winter-ml-zoomcamp.html
* https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp

## Table of Contents
* [1. About the Project](#about-project)
* [2. Key files and folders explained](#key-files)
* [3. Work explained](#work-explained)
* [4. Virtual environment and package dependencies](#venv)
* [5. Train the model](#train-model)
* [6. Model deployment as a web service](#deploy-model)
* [7. Deploy model as a web service to Docker container](#deploy-model-docker)
* [8. Deploy model as a web service to Heroku Cloud](#deploy-model-cloud)

<a id='about-project'></a>
## 1. About the Project

Banks are important institutions that provide funds, in terms of loans, to businesses and individuals to function and prosper. However banks need money to provide as loan and to also make their own investments (e.g. in stocks). One such good source that banks have is in the from of Term Deposits that bank's customers make.

Banks regularly make calls to their customers to secure such Term deposits. However, from a big list of all its customers, it would be wise to make calls to the customers who are more likely to invest. This way, banks can reduce the cost of acquisition of Term deposit (in the form of payment to staff making call, call charges and so on.).

This project aims at building a machine learning model that can be trained from previous marketing campaigns and data collected, to predict customers that potentialy will subscribe to Term deposit with the bank. Further, the prediction model will be hosted as a web service, which can accept customer data (in JSON format) and return the prediction (whether customer is likely to subscribe to Term deposit).

<a id='key-files'></a>
## 2. Key files and folders explained


<a id='work-explained'></a>
## 3. Work explained

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

<a id='venv'></a>
## 4. Virtual environment and package dependencies
To ensure all scripts work fine and libraries used during development are the ones which you use during your deployment/testing, Python venv has been used to manage virtual environment and package dependencies. Follow the below steps to setup this up in your environment.

The steps to install Python venv will depend on the Operating system you have. Below steps have been provided in reference to installation on Ubuntu, however you can refer to Official documentation at https://docs.python.org/3/tutorial/venv.html to know appropriate steps for your OS.

1. Install pip3 and venv if not installed (below sample commands to be used on Ubuntu hav been provided

```
sudo apt install -y python3-pip python3-venv
```

2. Create a virtual environment. Below command creates a virtual environment named mlzoomcamp

```
python3 -m venv mlzoomcamp
```

3. Activate the virtual environment.

```. ./mlzoomcamp/bin/activate```

4. Clone this repo

```git clone https://github.com/nindate/mlzoomcamp-midterm-project.git```

5. Change to the directory that has the required files

```cd mlzoomcamp-midterm-project/```

4. Install packages required for this project

```pip install -r requirements.txt```


<a id='train-model'></a>
## 5. Train the model
You can train the model using below steps.

You can skip steps 1, 2 and 3 if your followed instructions in 4. Virtual environment and package dependencies above and are now performing these steps.

1. Activate the virtual environment if not done already. Follow the steps in [4. Virtual environment and package dependencies](#venv)

2. Clone this repo (if you have not done already)

```git clone https://github.com/nindate/mlzoomcamp-midterm-project.git```

3. Check whether you are already in the project directory which you cloned from git. If not change to that directory.

```pwd```

If output of above commands does not show mlzoomcamp-midterm-project at the end, it means you are not in the project directory you cloned. In that case change to the project directory (Below command assumes you are in the directory from where you ran the git clone command above)

```cd mlzoomcamp-midterm-project/```

4. Run the training script

```python train.py```

<a id='deploy-model'></a>
## 6. Model deployment as a web service
For actual use of a model in real world, it needs to be deployed as a service (application) so that users (e.g. in this case Bank's staff who are supposed to call customer for Term Deposit subscription, can use this service. They can now send customer data to the service and get a prediction whether the customer is likely to make a Term deposit or not and hence whether it would be benificial to make the call to customer). 

To test the model deployment as a web service - open 2 separate terminal sessions into your machine (where all this code resides) and activate the virtual environment as explained in [4. Virtual environment and package dependencies](#venv)

From one terminal session run the following command to host the prediction model as a web service.

```gunicorn --bind 0.0.0.0:9696 predict.py```

From other terminal session from the cloned project directory, execute the following command to make a request to this web service

```python request.py```

<a id='deploy-model-docker'></a>
## 7. Deploy model as a web service to Docker container
You can deploy the trained model as a web service running inside a docker container on your local machine.

*Pre-requisites: You should have Docker installed and running on the machine where you want to perform model deployment to docker.*
Run the below commands to check whether docker service is running and then to see if any docker containers are running.

```
systemctl status docker
docker ps -a
```


Following are the steps to do this:
1. Clone this repo (if you have not done already)

```git clone https://github.com/nindate/mlzoomcamp-midterm-project.git```

2. Change to the directory that has the model file, python script (predict.py) for the web service and other required files

```cd mlzoomcamp-midterm-project/app-deploy```

3. Build docker image named bank-td-prediction

```docker build -t "bank-td-prediction" .```

4. Check docker image available. Output of below command should show the image with name bank-td-prediction

```docker images```

5. Create a docker container from the image. The model prediction script as a web service will then be running inside this container. Below command will create and run a docker container named bank-td-cont (**--name bank-td-cont**) running as a daemon i.e. non-interactive mode (**-d**), mapping the port 9696 on host to port 9696 on container (**-p 9696:9696** first port is host port, second is container port. If you want to map different port on host just change the first number), from image **bank-td-prediction**. The container will be deleted if stopped or when you shutdown your machine (**--rm**).

```docker run --rm --name bank-td-cont -d -p 9696:9696 bank-td-prediction```

6. Check whether docker container running. Below command should show the container in Running state and not Exited.

```docker ps -a```

7. Test sending some sample customer data to the web service and see the results. For this you can use the request.py script provided as part of this repo, which has some sample customer entries and can make a request to the Web app service.

```python request.py```


<a id='deploy-model-cloud'></a>
## 8. Deploy model as a web service to Heroku Cloud
