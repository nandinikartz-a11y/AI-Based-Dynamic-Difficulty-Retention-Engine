# AI-Based-Dynamic-Difficulty-Retention-Engine
A machine learning-based gaming project that analyzes player data, predicts player behaviour and churn risk, and provides actionable recommendations for better player retention.

## 📌 Project Overview

This project is an AI-based gaming analytics and player retention system that uses **machine learning and rule-based logic** to transform player data into understandable predictions and actionable recommendations.

The system analyzes player characteristics and gameplay-related data to categorize players, identify potential churn risk, and provide suitable recommended actions. It is designed to support gaming teams in making more informed, data-driven decisions related to player engagement and retention.

## 🎯 Objectives

The main objectives of this project are:

- To analyze player data and gameplay behavior.
- To categorize players based on their activity.
- To identify players who may be at risk of churn.
- To generate appropriate recommended actions.
- To support personalized player engagement.
- To automate basic player segmentation and intervention selection.
- To support data-driven player retention strategies.


## 🤖 Machine Learning Outputs

The project focuses on three main outputs:

### 1. Player Category

Players are categorized based on their gameplay activity into different groups such as:

- Casual
- Moderate
- Expert

This helps gaming teams understand different types of players and provide appropriate engagement strategies.

### 2. Churn Risk

The system predicts whether a player has:

- Low Risk
- High Risk

This helps identify players who may require early retention support.

### 3. Recommended Action

The system generates an appropriate action based on player characteristics, risk factors, and prediction results.

The recommended action is designed to help gaming teams decide what type of intervention may be appropriate for a particular player.

---

## 🔄 Project Workflow

The overall workflow of the project is:

Player Data  
↓  
Data Preprocessing  
↓  
Exploratory Data Analysis  
↓  
Feature Engineering  
↓  
Machine Learning Models  
↓  
Prediction  
↓  
Rule-Based Recommendation  
↓  
Streamlit Web Application

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Data Processing
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- XGBoost

### Data Visualization
- Matplotlib
- Seaborn
- Plotly

### Backend
- FastAPI

### Frontend / Web Application
- Streamlit

### Database
- Supabase

### Model Deployment / Storage
- Joblib
- Pickle

---

## 📊 Dataset

The project uses player-level gaming data containing information related to player demographics, gameplay behavior, engagement, and progression.

Example features include:

- Age
- Gender
- Location
- Game Genre
- In-Game Purchases
- Game Difficulty
- Sessions Per Week
- Average Session Duration
- Player Level
- Achievements Unlocked
- Engagement Level
- Progression Speed
- Reports Received
- Match Abandonment
- Ads Viewed Per Session

The dataset is processed and transformed before being provided to the machine learning models.

---

## 🧹 Data Preprocessing

The following preprocessing and feature engineering steps are performed:

- Handling missing values where required.
- Cleaning inconsistent data.
- Encoding categorical variables.
- Preparing numerical features.
- Creating derived gameplay features.
- Removing unnecessary or redundant features.
- Preparing the data for machine learning models.

Categorical variables are handled using techniques such as **One-Hot Encoding**.

---

## 🧠 Machine Learning Approach

Different machine learning algorithms can be evaluated during model development, including:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- XGBoost

The selected models are trained using processed player data and evaluated using appropriate performance metrics.

---

## ⚙️ Rule-Based Recommendation System

In addition to machine learning, the project uses **rule-based logic** to generate recommended actions.

The recommendation system uses prediction results and player-related conditions to determine an appropriate intervention.

This combination of:

**Machine Learning + Rule-Based Logic**

allows the system to convert predictive outputs into practical actions.

---

## 🌐 Application Architecture

The project uses a simple frontend-backend architecture.

### Streamlit

Streamlit provides the interactive user interface where users can enter player information and view predictions.

### FastAPI

FastAPI provides the backend API responsible for receiving player information and returning prediction results.

### Machine Learning Models

The trained models process the input data and generate predictions.

### Supabase

Supabase can be used for storing and managing project data.

---

## 📁 Project Structure

```text
AI-Gaming-Player-Retention/
│
├── app.py
├── main.py
├── config.py
├── schemas.py
├── database.py
│
├── models/
│   ├── difficulty_score_xgb_model.pkl
│   ├── difficulty_logistic_regression.pkl
│   ├── RetentionRisk_KNN_model.pkl
│   └── RecommendedAction_XGB_model.pkl
│
├── data/
│   └── player_data.csv
│
├── notebooks/
│   └── project_analysis.ipynb
│
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
