Wine Quality Predictor Server
---<!-- omit in toc -->

Backend server for the [Wine Quality Predictor](https://github.com/andaviaco/wine-quality-prediction).


**Table of contents**
- [About the project](#about-the-project)
  - [Dataset](#dataset)
  - [Prediction Model](#prediction-model)
  - [Tools](#tools)
- [Requirements](#requirements)
- [Install dependencies](#install-dependencies)
- [Run dev server](#run-dev-server)
- [API](#api)
  - [Get a prediction](#get-a-prediction)

## About the project
**Note**:
Be aware was one-weekend project I built back in 2018.

The goal is to predict the sensorial quality of a wine base on its physicochemical qualities

### Dataset
The dataset was downloaded from [Kaggle's Red Wine Quality dataset](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009).

The dataset contains the following data for each row.
##
|Feature|Description
|-|-|-|
|Fixed acidity|Most acids involved with wine or fixed or nonvolatile (do not evaporate readily).
|Volatile acidity|The amount of acetic acid in wine, which at too high of levels can lead to an unpleasant, vinegar taste.
|Citric acid|Found in small quantities, citric acid can add 'freshness' and flavor to wines.
|Residual sugar|The amount of sugar remaining after fermentation stops
|Chlorides|The amount of salt in the wine.
|Free sulfur dioxide|The free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents.
|Total sulfur dioxide|Amount of free and bound forms of S02; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2.
|Density|The density of water is close to that of water depending on the percent alcohol and sugar content.
|PH|Describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic).
|Sulphates|A wine additive which can contribute to sulfur dioxide gas (S02) levels.
|Alcohol|Percentage of alcohol in the wine.


### Prediction Model
WIP

Classification Algorithm: [Support Vector Clustering (SVC)](http://www.scholarpedia.org/article/Support_vector_clustering)

Other algorithms considered:
- [Random Forest](https://www.section.io/engineering-education/introduction-to-random-forest-in-machine-learning)

### Tools
Model
- Scikit-learn
- Pandas
- Numpy

Server
- Flask

## Requirements
- Python 3.x


## Install dependencies
Create virtual environment.
```sh
python3 -m venv env
```

Activate virtual environment.
```sh
source env/bin/activate
```

Install dependencies.
```sh
python3 -m pip install -r requirements.txt
```

## Run dev server
Export app name.
```
export FLASK_APP=server
```

Start server at default port.
```
flask run
```

## API
### Get a prediction
POST `/predict`

|Field|Type|Description
|-|-|-|
|`values`|Array\<Number>|Model input/Descriptor. This is an array of 11 number.

Example JSON Body
```json
{
  "values": [8, 0.5, 0.2, 2.5, 0.08, 15, 46.5, 0.999, 3.3, 0.65, 10]
}
```

Example response
```json
{
  "predicted": 6
}
```
