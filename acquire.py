#Disable warnings
import warnings
warnings.filterwarnings("ignore")

#Libraries for processing data
import pandas as pd

#Libraries for obtaining data from SQL databse
import env
import os

#First we establish a connection to the SQL server
def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
     We establish a connection to the SQL database, using my information stored in the env file.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#Now we will make our DataFrame with the relevant Zillow data
def get_zillow_data():
    '''
    We will run a SQL query that uses joins to obtain all information for properties with a 
    transaction date in 2017 in Los Angles, Orange, and Ventura County. 
    '''
    filename = "zillow.csv"
  
    sql = ''' 
    SELECT *
    FROM properties_2017
    LEFT OUTER JOIN airconditioningtype 
    USING(airconditioningtypeid)
    LEFT OUTER JOIN architecturalstyletype
    USING(architecturalstyletypeid)
    LEFT OUTER JOIN buildingclasstype 
    USING(buildingclasstypeid)
    LEFT OUTER JOIN heatingorsystemtype
    USING(heatingorsystemtypeid)
    LEFT OUTER JOIN predictions_2017
    USING(id)
    INNER JOIN (
	SELECT id, MAX(transactiondate) as last_trans_date 
	FROM predictions_2017
	GROUP BY id
    ) predictions ON predictions.id = properties_2017.id AND predictions_2017.transactiondate = predictions.last_trans_date
    LEFT OUTER JOIN propertylandusetype
    USING(propertylandusetypeid)
    LEFT OUTER JOIN storytype
    USING(storytypeid)
    LEFT OUTER JOIN typeconstructiontype
    USING(typeconstructiontypeid)
    JOIN unique_properties
    ON unique_properties.parcelid = properties_2017.parcelid
    WHERE latitude IS NOT NULL and longitude IS NOT NULL;
    '''
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(sql, get_connection('zillow'))
        #eliminate duplicate columns
        df = df.loc[:,~df.columns.duplicated()]
        return df
    df = pd.read_sql(sql, get_connection('zillow'))
    return df

def only_single_unit(df):
    '''
    This function retunrs only the properties in the Zillow Dataset which are single-unit 
    or single-family homes.
    '''
    df = df[df.propertylandusetypeid.isin([261.0, 266.0, 263.0, 269.0, 275.0, 264.0])]
    
    ## We will reset the index, since we have just elimated some rows. 
    df = df.reset_index()
    
    ## Drop any columns which were left completely null as a result 
    df.dropna(how='all', axis=1, inplace=True)

    return df


def zillow_data():
    df = get_zillow_data()

    df = only_single_unit(df)

    return df