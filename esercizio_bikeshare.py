# Your team is still in the early stages of their project to develop a machine learning model to predict user churn. 
# You have received notice that your project proposal has been approved and your team has been given access to Waze’s user data. To get clear insights, the data must be inspected, organized, and prepared for analysis. 

# You discover two new emails in your inbox: one from May Santner, and one from your teammate, Chidi Ga. In the email, May asks for your help reviewing the data and completing a code notebook, and Chidi shares the details of the notebook. Review the emails, then follow the provided instructions to complete the PACE strategy document, the code notebook, and the executive summary. 

# Briefing: “Until we finish our previous project, there is no need to do a full EDA on our new user data. We’ll get to that soon. Meanwhile, do you mind reviewing the imported data for the team? It would be fantastic if you could include a summary of the data types for each variable, where missing values exist in the data, key descriptive statistics, and anything else code-related you think is worth sharing in the notebook. I haven’t had a chance to explore the data, so I really appreciate you getting an early start on this”

# Step 1) Pre processing and cleaning

# I load the dataset waze_dataset.csv into pycharm, creating a dataframe will help me to conduct data manipulation, exploratory data analysis (EDA), and statistical activities.

# input:


import pandas as pd
import numpy as np
df = pd.read_csv("waze_dataset.csv")
print(df.head(10))

# output:

