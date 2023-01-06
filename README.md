# ------Churning Customers

### ------Project Description

Using the telco churn database given, there is evidence that over a quarter of customers are deciding to leave the company. There are many factors that can be causing the customers to leave and I am going to try and find out what the biggest reason is that is causing customers to churn. 

### ------Project Goal
Discover drivers of churning customers.
Use drivers to develop a machine learning model to classify customers churning or not.
This information could be used to determine whether or not the comapny should make changes to keep customers

### ------Initial Thoughts
My initial hypothesis is that customers are churning because of common reasons such as price or bad products. 

### ------The Plan
Aquire data from SQL

Prepare data

Create Engineered columns from existing data
research and familiarize myself with the data
determine columns that do not fit into my initial exploratory thoughts and get rid of them
check for null values
tidy the data (make sure it fits the 4 key components of tidy data - tabular/one value per cell/
               each observation is one and only one row/each variable is one and only one column)


##### Answer the following initial questions
- Does price affect whether or not a customer will churn?

- Does tenure affect whether or not a customer will churn?

- Does customer service/support affect whether or not a customer will churn?

- Does a bad product affect whether or not a customer will churn?

Use drivers identified in explore to build predictive models of different types
Evaluate models on train and validate data
Select the best model based on highest accuracy
Evaluate the best model on test data
Draw conclusions

### ------Data Dictionary
- Feature -               - Definition -
tenure                    - tells how long a customer has been with the company
online_security           - tells if the customer has online security
online_backup             - tells if the customer has online backup
device_protection         - tells if the customer has device protection
tech_support              - tells if the customer has tech support 
monthly_charges           - provides the monthly charges of each customer
total_charges             - provides the total charges of the customer for the length of their tenure
churn (TARGET)            - tells whether or not the customer has churned
internet_service_type     - tells what type of internet service the customer has


Steps to Reproduce
Clone this repo.
Acquire the data from Kaggle
Put the data in the file containing the cloned repo.
Run notebook.

### ------Takeaways and Conclusions


### ------Recommendations


