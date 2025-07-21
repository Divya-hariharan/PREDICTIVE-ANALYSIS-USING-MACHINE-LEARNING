# PREDICTIVE-ANALYSIS-USING-MACHINE-LEARNING
*COMPANY NAME*-- CODTECH IT SOLUTIONS PVT.LTD

*NAME*: DIVYA H

*INTERN ID*: CT04DG233

*DOMAIN*:  DATA ANALYTICS

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH KUMAR 

# DESCRIPTION FOR TASK 2:

Task Overview: Preparing Raw Data for Analysis through Data Wrangling
In this task, the focus is on preprocessing raw data to make it suitable for meaningful analysis and predictive modeling. Raw data, especially in real-world scenarios, often contains various inconsistencies such as missing values, irregular formats, outliers, and unstructured text. These inconsistencies can significantly skew the results of any statistical or machine learning analysis if left unaddressed.

To resolve this, the task involves comprehensive data wrangling using Pandas, one of the most powerful and widely-used Python libraries for data manipulation. The goal is to clean, structure, and transform the raw data into a consistent and analyzable format. The cleaned dataset will then be ready for use in exploratory data analysis (EDA), feature engineering, and machine learning model training.

# Objective of the Task
The primary objective is to transform messy, unstructured, or inconsistent data into a high-quality dataset that adheres to the expected schema, format, and type requirements for further data analysis and machine learning. This process includes:

Treating null or missing values.

Standardizing both categorical and numerical variables.

Detecting and removing outliers.

Encoding categorical variables for model input.

Normalizing or scaling numerical values.

Converting unstructured textual data into structured formats.

Through this task, you gain practical experience in data preparation, a critical step that can make or break the performance of analytics workflows and predictive models.

# Key Skills Practiced
1. Data Wrangling Using Pandas
Pandas offers a versatile set of tools for data cleaning and manipulation. This includes:

Importing data from various formats (CSV, Excel, JSON, etc.).

Inspecting and understanding data using .head(), .info(), and .describe().

Modifying and transforming columns and rows to create a clean dataset structure.

2. Null Value Treatment
Handling missing values is crucial, as they can distort averages, correlations, and training data distributions. Strategies for null value treatment include:

Removal: Dropping rows or columns with too many missing values using .dropna().

Imputation: Filling missing values using statistical methods:

Mean, median, or mode imputation for numerical columns.

Constant or most frequent value for categorical features using .fillna().

Choosing the appropriate method depends on the nature of the feature and its importance to the analysis.

3. Label Encoding and Normalization
Most machine learning algorithms require numerical input, so categorical variables must be encoded:

Label Encoding: Converts categories into integers (e.g., Male → 0, Female → 1).

One-Hot Encoding: Creates binary columns for each category, useful when no ordinal relationship exists between values.

Pandas’ .get_dummies() and Scikit-learn’s LabelEncoder are commonly used here.

Normalization ensures that features are on a similar scale, which is especially important for algorithms like KNN, SVM, or neural networks. Techniques include:

Min-Max Scaling: Transforms features to a 0–1 range.

Z-score Standardization: Rescales values based on mean and standard deviation.

4. Outlier Detection and Treatment
Outliers can drastically affect the performance of machine learning models and statistical summaries. Detecting and removing them improves model robustness. Methods include:

Boxplot and IQR Method: Identifies values outside 1.5 times the interquartile range.

Z-score Method: Flags data points whose standard score is above a threshold (commonly >3 or <-3).

Domain Knowledge: In healthcare or finance data, some thresholds are predefined by domain expertise.

Once detected, outliers can be removed or treated (e.g., capped or transformed).

# Use Case Example

Imagine a dataset containing healthcare information with fields like Age, Gender, BloodPressure, Cholesterol, Diabetic, and Outcome. Here’s what a typical workflow would look like:

-Load the data using Pandas and inspect its structure.

-Identify and treat missing values in Cholesterol or BloodPressure using median imputation.

-Convert categorical columns like Gender and Diabetic into numeric form using label encoding.

-Normalize continuous variables like Age and BloodPressure for consistent scale.

-Detect outliers in Cholesterol using IQR and remove or cap extreme values.

Prepare the final cleaned DataFrame for machine learning algorithms or visualization.

# output
<img width="964" height="383" alt="Image" src="https://github.com/user-attachments/assets/fa0addaa-1296-4eea-8b40-751a8f6bbfcc" />

<img width="903" height="723" alt="Image" src="https://github.com/user-attachments/assets/9717fb6f-5196-4055-9c36-8ce26f0b83f4" />

<img width="710" height="435" alt="Image" src="https://github.com/user-attachments/assets/35762d2f-c75c-46d0-aa47-d3a2974ab13b" />

<img width="845" height="730" alt="Image" src="https://github.com/user-attachments/assets/ff7e92ee-65d6-46a6-9f07-7e8bc8b78211" />

<img width="1080" height="750" alt="Image" src="https://github.com/user-attachments/assets/f46d325f-4fda-4dce-862d-f913da6b0480" />
