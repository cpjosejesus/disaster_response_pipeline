# Disaster Response Pipeline Project

## Introduction
If a disaster occurs in the world, disaster response organizations receive thousands of messages. In order to be able to react very promptly to such messages, a targeted classification using machine learning algorithms is required I have developed a web application so that experts from such organizations can quickly classify and forward such reports. The application uses a classifier that was trained on the data described below.

## Data
Data includes 2 csv files:

1. `disaster_messgaes.csv`: Messages data.
2. `disaster_categories.csv`: Disaster categories of messages.

## Folder Structure
```
│   README.md
│   requirements.txt
│
├───app
│   │   run.py
│   │
│   └───templates
│           go.html
│           master.html
│
├───data
│       disaster_categories.csv
│       disaster_messgaes.csv
│       DisasterResponse.db
│       process_data.py
│
├───models
│       classifier.pkl
│       train_classifier.py


```
## Files
- `process_data.py`: Script that:

    - Loads the messages and categories datasets
    - Merges the two datasets
    - Cleans the data
    - Stores it in a SQLite database

- `train_classifier.py`: Machine Learning pipeline that:

    - Loads data from the SQLite database
    - Splits the dataset into training and test sets
    - Builds a text processing and machine learning pipeline
    - Trains and tunes a model using GridSearchCV
    - Outputs results on the test set
    - Exports the final model as a pickle file

- `run.py`: Main file to run Flask app that:

    - Classifies real time input text messages
    - Shows data visualizations

- `requirements.txt`: List of required Python libraries

## Instructions:

1. Make sure to install Python3
2. Navigate to the project's root directory in your terminal
3. Create a virtual enviroment 
```
 python -m venv env
```

Note that if you are on a Mac you should use `python3` instead

Activate your env

4. Install the project requirements:
```
pip install -r requirements
```

5. After intalling the requirements, run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
