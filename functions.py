import pandas as pd
def read_data(url):

    df = pd.read_csv(url)
    return df

def clean_data(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_") 
    return df

def clean_table3(df):   #limpiar nombres de las columnas de la tabla 3  
    df = df.rename(columns = {"1._what_is_your_age?": "age"})
    df = df.rename(columns = {"2._gender": "gender"})
    df = df.rename(columns = {"3._relationship_status": "relationship_status"})
    df = df.rename(columns = {"7._what_social_media_platforms_do_you_commonly_use?": "platform"}) 
    df = df.rename(columns = {"8._what_is_the_average_time_you_spend_on_social_media_every_day?": "social_media_usage_hours"})
    df = df.rename(columns = {"18._how_often_do_you_feel_depressed_or_down?": "depressed_feelings(1-5)"})
    df = df.rename(columns = {"18._how_often_do_you_feel_depressed_or_down?": "depressed_feelings(1-5)"})
    df = df.rename(columns = {"20._on_a_scale_of_1_to_5,_how_often_do_you_face_issues_regarding_sleep?": "sleep_problems(1-5)"})
    return df

def drop_columns1(df):  #Elimina las columnas de la tabla una que no son útiles para el estudio
    df.drop("technology_usage_hours", axis = 1, inplace = True)
    df.drop("gaming_hours", axis = 1, inplace = True)
    df.drop("screen_time_hours", axis = 1, inplace = True)
    df.drop("support_systems_access", axis = 1, inplace = True)
    df.drop("work_environment_impact", axis = 1, inplace = True)
    df.drop("online_support_usage", axis = 1, inplace = True)

    return df

def drop_columns2(df): # Elimina las columnas de la tabla dos que no son útiles para el estudio
    df.drop("interests", axis = 1, inplace = True)
    df.drop("profession", axis = 1, inplace = True)
    df.drop("income", axis = 1, inplace = True)
    df.drop("indebt", axis = 1, inplace = True)
    df.drop("ishomeowner", axis = 1, inplace = True)
    df.drop("owns_car", axis = 1, inplace = True)
    return df