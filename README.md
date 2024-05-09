# **Machine Learning-Based Prediction of Cardiovascular Disease Risk Using Lifestyle Factors**

## Overview
In recent times, healthcare has become one of the most significant global concerns, especially following the COVID-19 pandemic. Chronic diseases, such as cardiovascular diseases (CVDs), remain a leading cause of mortality worldwide, particularly in the United States. CVDs are usually appropriately recognized based on indicators measured in the hospital, but due to people's busy schedules, many are unwilling to spend time and effort for check-ups in the hospital. Lifestyle habits are assumed to play a role in the development of CVDs, making it crucial to modify these behaviors to predict and prevent these diseases.
     
Previous studies have used machine learning to predict disease risk based on various factors. However, these studies may not fully capture the dynamic relationship between lifestyle data and the presence of cardiovascular diseases. To address this, this thesis aims to build on previous findings and improve the accuracy of predicting CVDs by analyzing data from the NHANES dataset, which combines information on lifestyle habits and health indicators, using machine learning techniques such as CatBoost, Gradient Boosting, XGBoost, Linear Regression, and Support Vector Machines. The ultimate objective is to identify the relationship between lifestyle habits and CVDs, and thus reduce the number of potential patients.

## Table of Contents
- [Author Information](#author-information)
- [Installation](#installation)
- [Usage](#usage)

## Author Information
- Author: Le Ngoc Uyen Phuong
- Advisor: Assoc. Prof. Nguyen Thi Thuy Loan
- University: Ho Chi Minh City Vietnam National University – INTERNATIONAL UNIVERSITY
- Department: School of Computer Science and Engineering
- Graduation Year: 2024

## Installation
Instructions on how to install and set up the project.

1. The required libraries to be installed with latest version numbers are listed in the `requirements.txt` file. There are some code lines in the `main.py` file to run this file for installation.
2. Open `main.py`.
3. Open a New Terminal.
4. Run `streamlit run main.py` to run the prediction web-app using Catboost model and the data gathered from the questions.

## Usage
1. The website aims to **predict the possibility that a people can have cardiovascular diseases in the future** based on the answers they give for the questions of key features in the list at the top.
2. The key features list at the beginning of the web consists of various data types, including binary, integer, and float values. 
3. The next part of the web app allows people to answer some questions about their information and health status data by **choosing from select boxes and filling in numerical values** (Hit Enter to save each input answer).
4. The data inputted by the user is recorded to a dataframe (at the bottom), then the data is applied to the **Catboost model** for prediction. This web app use CatBoost model as it has the best performance with the highest accuracy for the data, and it can reduce errors by its boosting algorithm. 
5. For the questions that the user does not answer, the **mean value** of that feature will be filled in as default for avoiding missing values. 
6. Press the **“Predict” button** at the end of the web application to show the prediction results from the obtained data above. The result can be high or low possibility of having cardiovascular diseases based on the user’s data, along with a short suggestion for the user to have a check-up in the hospitals to keep track of their health better. (The result for the default input is high possibility).
> [!TIP]
> To show the other prediction result (low possibility), change these features as below:
> - DMDEDUC2: 5
> - RIDAGEYR: 22
> - BMXWT: 53
> - BMXBMI: 19.9