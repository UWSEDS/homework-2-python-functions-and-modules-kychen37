import requests
import pandas as pd
import io

def read_link(some_link):
    urlData = requests.get(some_link).content
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    return df

def test_create_dataframe(dataframe, col_list):
    count = 0
    if set(dataframe.columns) == set(col_list):
        count +=1
    if all(isinstance(x,(object)) for x in dataframe.columns):
        count +=1
    if len(dataframe) >= 10:
        count +=1
 
    if count == 3: print('True')
    else: print('False')
