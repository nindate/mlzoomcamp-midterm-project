# ML Zoomcamp Midterm Project

This repo contains the work carried out as part of the Mid Term project for the course ML Zoomcamp. This course is conducted by Alexey Grigorev. You can take the course at any time and it is free. Links to course mentioned below:

* https://datatalks.club/courses/2021-winter-ml-zoomcamp.html
* https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp

## Table of Contents
* [1. About the Project](#about-project)
* [2. Key files and folders explained](#key-files)
* [3. Work explained](#work-explained)
* [4. Train the model](#train-model)
* [5. Deploy model as a web service to Docker container](#deploy-model-docker)
* [6. Deploy model as a web service to Heroku Cloud](#deploy-model-cloud)

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

<a id='train-model'></a>
## 4. Train the model

<a id='deploy-model-docker'></a>
## 5. Deploy model as a web service to Docker container
You can deploy the trained model as a web service running inside a docker container on your local machine.

*Pre-requisites: You should have Docker installed and running on the machine where you want to perform model deployment to docker.*
Run the below commands to check whether docker service is running and then to see if any docker containers are running.

```
$ systemctl status docker
$ docker ps -a
```


Following are the steps to do this:
1. Clone this repo (if you have not done already)

```$ git clone https://github.com/nindate/mlzoomcamp-midterm-project.git```

2. Change to the directory that has the model file, python script (predict.py) for the web service and other required files

```$ cd mlzoomcamp-midterm-project/app-deploy```

3. Build docker image named bank-td-prediction

```$ docker build -t "bank-td-prediction" .```

4. Check docker image available. Output of below command should show the image with name bank-td-prediction

```docker images```

5. Create a docker container from the image. The model prediction script as a web service will then be running inside this container. Below command will create and run a docker container named bank-td-cont (**--name bank-td-cont**) running as a daemon i.e. non-interactive mode (**-d**), mapping the port 9696 on host to port 9696 on container (**-p 9696:9696** first port is host port, second is container port. If you want to map different port on host just change the first number), from image **bank-td-prediction**. The container will be deleted if stopped or when you shutdown your machine (**--rm**).

```docker run --rm --name bank-td-cont -d -p 9696:9696 bank-td-prediction```

6. Check whether docker container running. Below command should show the container in Running state and not Exited.

```docker ps -a```

7. Test sending some sample customer data to the web service and see the results. For this you can use the request.py script provided as part of this repo.

```python request.py```


<a id='deploy-model-cloud'></a>
## 6. Deploy model as a web service to Heroku Cloud
