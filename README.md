# What are the Drivers of the Error in the Zestimate?

## Objectives 
### Project Goals 
 - To document **code**, **processs**, **findings**, and **key takeaways** in a Jupyter Notebook. 
 
 - To create modules `acquire.py` and `prepare.py` which contain functions that make our proces repeatable. 
 
 - To construct a model that determines the biggest driver errors in the Zestimate using clustering and regression modeling. 
 
 - To deliver a five-minute presentation that is a high-level walkthrough of the findings. 
 
### Business Goals
 - To determine which feature in the Zillow Data is the biggest predictor of error in Zestimate for single unit properies with a transaction date in 2017 in Los Angeles, Orange, and Ventura County. 

### Audience 
 - The Zillow data science team. 

## Pipeline States Breakdown

### Project Planning 
 - Create a `READ.md` file with an outline of a plan for the project. 

### Data Acquisition 
#### In the `acquire.py` file 
 - Create an `acquire.py` file in the same repository. 
 - Create a function SQL query which obtains data for all single unit/single families homes with a transaction date in 2017.
#### In the Notebook
 - Call the function from `acquire.py` to obtain a pandas DataFrame with data for single unit/single family homes with a transaction date in 2017.
 - Get basic information about the DataFrame by running `.head()`, `.info()`, and `describe()`.
 - Graph distributions of features. 
 
### Data Preparation 
#### In the `prepare.py` file
 - Create a function which eliminates columns and rows that fail to meet a threshold of non-null values. 
 - Create a function which imputes the remaining null values. 
#### In the Notebook 
 - Call the function from `prepare.py` to clean our pandas DataFrame. 
 - Get basic information about the cleaned DataFrame by running `.head()`, `.info()`, and `describe()`.
 
### Data Exploration 
#### In the Notebook 
 - Use statisical methods to test hypotheses regarding the relationship between independent variables and the target variable `logerror`. 
 - Use visualizations to explore the relationship between independent variables and the target variables `logerror`. 
 - Use clustering to explore the data. Utilize at least three different combinations of features for clustering. 
     - Visualize at the results of clustering. 
     - Run statistical testing to confirm that clustering is useful. 
     
### Modeling 
#### In the Notebook 
 - Create at four different models on the clusters. 
     - Compare the models' performance. Compare Validate and Train RMSE. 
 - Select the best performing model and run that model on the test dataset. 
     - Evaluate results of the model on the test DataSet. 
     
## Reproduce my project
To reproduce my project, you will need to obtain your own `env.py` file with database credentials, in addition to the actions listed below:
 - Read this `READ.md` file. 
 - Download the `acquire.py`, `prepare.py`, and `Final_Project.ipynb` files. 
 - Add your own `env.py` file to your directory. You will need to access the SQL database to obtain the Zillow data. 
 - Run the `Final_Project.ipynb` notebook. 