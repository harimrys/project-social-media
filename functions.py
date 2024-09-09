import pandas as pd
def read_data(url):

    df = pd.read_csv(url)
    return df

def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_") 
    return df

def clean_table3(df):   #limpiar nombres de las columnas d la tabla 3  
    df = df.rename(columns = {"1._what_is_your_age?": "age"})
    df = df.rename(columns = {"2._gender": "gender"})
    df = df.rename(columns = {"3._relationship_status": "relationship_status"})
    df = df.rename(columns = {"7._what_social_media_platforms_do_you_commonly_use?": "platform"}) 
    return df