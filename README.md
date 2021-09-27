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
 
 ## Data Dictionary 
 
Below is a data dictionary of the features that we will use in this project. 
 
|    | Feature                      | Datatype   |
|---:|:-----------------------------|:-----------|
|  1 | typeconstructiontypeid       | float64    |
|  2 | storytypeid                  | float64    |
|  3 | propertylandusetypeid        | float64    |
|  4 | id                           | int64      |
|  5 | heatingorsystemtypeid        | float64    |
|  6 | architecturalstyletypeid     | float64    |
|  7 | airconditioningtypeid        | float64    |
|  8 | parcelid                     | int64      |
|  9 | basementsqft                 | float64    |
| 10 | bathroomcnt                  | float64    |
| 11 | bedroomcnt                   | float64    |
| 12 | buildingqualitytypeid        | float64    |
| 13 | calculatedbathnbr            | float64    |
| 14 | decktypeid                   | float64    |
| 15 | finishedfloor1squarefeet     | float64    |
| 16 | calculatedfinishedsquarefeet | float64    |
| 17 | finishedsquarefeet12         | float64    |
| 18 | finishedsquarefeet13         | float64    |
| 19 | finishedsquarefeet15         | float64    |
| 20 | finishedsquarefeet50         | float64    |
| 21 | finishedsquarefeet6          | float64    |
| 22 | fips                         | float64    |
| 23 | fireplacecnt                 | float64    |
| 24 | fullbathcnt                  | float64    |
| 25 | garagecarcnt                 | float64    |
| 26 | garagetotalsqft              | float64    |
| 27 | hashottuborspa               | float64    |
| 28 | latitude                     | float64    |
| 29 | longitude                    | float64    |
| 30 | lotsizesquarefeet            | float64    |
| 31 | poolcnt                      | float64    |
| 32 | poolsizesum                  | float64    |
| 33 | pooltypeid10                 | float64    |
| 34 | pooltypeid2                  | float64    |
| 35 | pooltypeid7                  | float64    |
| 36 | propertycountylandusecode    | object     |
| 37 | propertyzoningdesc           | object     |
| 38 | rawcensustractandblock       | float64    |
| 39 | regionidcity                 | float64    |
| 40 | regionidcounty               | float64    |
| 41 | regionidneighborhood         | float64    |
| 42 | regionidzip                  | float64    |
| 43 | roomcnt                      | float64    |
| 44 | threequarterbathnbr          | float64    |
| 45 | unitcnt                      | float64    |
| 46 | yardbuildingsqft17           | float64    |
| 47 | yardbuildingsqft26           | float64    |
| 48 | yearbuilt                    | float64    |
| 49 | numberofstories              | float64    |
| 50 | fireplaceflag                | float64    |
| 51 | structuretaxvaluedollarcnt   | float64    |
| 52 | taxvaluedollarcnt            | float64    |
| 53 | assessmentyear               | float64    |
| 54 | landtaxvaluedollarcnt        | float64    |
| 55 | taxamount                    | float64    |
| 56 | taxdelinquencyflag           | object     |
| 57 | taxdelinquencyyear           | float64    |
| 58 | censustractandblock          | float64    |
| 59 | airconditioningdesc          | object     |
| 60 | architecturalstyledesc       | object     |
| 61 | heatingorsystemdesc          | object     |
| 62 | logerror                     | float64    |
| 63 | transactiondate              | object     |
| 64 | last_trans_date              | object     |
| 65 | propertylandusedesc          | object     |
| 66 | storydesc                    | object     |
| 67 | typeconstructiondesc         | object     |
| 68 | bathroomcnt_scaled           | float64    |
| 69 | bedroomcnt_scaled            | float64    |