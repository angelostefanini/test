{
  "project": {
    "name": "Machine Learning Model for User Churn Prediction",
    "status": "Early Stages",
    "description": "Developing a machine learning model to predict user churn.",
    "approvalStatus": "Approved",
    "accessToData": "Granted",
    "dataProcessingInstructions": [
      "Inspect, organize, and prepare Waze's user data for analysis."
    ],
    "teamEmails": [
      {
        "sender": "May Santner",
        "request": "Help reviewing the data and completing a code notebook."
      },
      {
        "sender": "Chidi Ga",
        "details": "Shared the details of the notebook."
      }
    ],
    "briefing": {
      "message": "Until we finish our previous project, there is no need to do a full EDA on our new user data. We’ll get to that soon. Meanwhile, review the imported data for the team. Include a summary of the data types for each variable, where missing values exist, key descriptive statistics, and any other code-related information worth sharing in the notebook.",
      "appreciation": "I haven’t had a chance to explore the data, so I really appreciate you getting an early start on this."
    },
    "tasks": [
      {
        "step": "Step 1",
        "description": "Pre-processing and cleaning",
        "action": "Load the dataset waze_dataset.csv into PyCharm, creating a dataframe to conduct data manipulation, exploratory data analysis (EDA), and statistical activities."
      }
    ]
  }
}

# input:


import pandas as pd
import numpy as np
df = pd.read_csv("waze_dataset.csv")
print(df.head(10))

# output:

