# Diabetes Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-prediction-fj59zbnzs6s3qjqm8ixafv.streamlit.app/)

This project is an end-to-end machine learning application that predicts the likelihood of a person having diabetes based on several medical diagnostic measurements. The model is deployed as an interactive web application using Streamlit.

## App Demo

![App Screenshot](https://github.com/nidhi-ai01/Diabetes-Prediction/blob/main/thumbnail.png) 


## Features

-   **Real-Time Prediction:** Get instant predictions by entering patient data.
-   **Data Preprocessing:** Implements a data cleaning pipeline to handle missing values before training.
-   **User-Friendly Interface:** A simple and intuitive UI built with Streamlit.
-   **Deployed Model:** The `RandomForestClassifier` model is trained and saved for production use.

## Tech Stack

-   **Language:** Python
-   **Libraries:** Scikit-learn, Pandas, Joblib
-   **Frontend:** Streamlit
-   **Deployment:** Streamlit Community Cloud

## Local Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/nidhi-ai01/Diabetes-Prediction.git](https://github.com/nidhi-ai01/Diabetes-Prediction.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Diabetes-Prediction
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Project Structure

```
├── app.py                  # Streamlit web application script
├── diabetes_model.joblib   # Saved, pre-trained machine learning model
├── requirements.txt        # List of Python dependencies
├── diabetes.csv            # The dataset used for training
└── README.md               # Project documentation
```

## Dataset

This project uses the **PIMA Indians Diabetes Database** sourced from Kaggle.
