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

def drop_columns3(df): # Elimina las columnas de la tabla tres que no son útiles para el estudio
    df.drop("timestamp", axis = 1, inplace = True)
    df.drop("4._occupation_status", axis = 1, inplace = True)
    df.drop("5._what_type_of_organizations_are_you_affiliated_with?", axis = 1, inplace = True)
    df.drop("6._do_you_use_social_media?", axis = 1, inplace = True)
    df.drop("9._how_often_do_you_find_yourself_using_social_media_without_a_specific_purpose?", axis = 1, inplace = True)
    df.drop("10._how_often_do_you_get_distracted_by_social_media_when_you_are_busy_doing_something?", axis = 1, inplace = True)
    df.drop("11._do_you_feel_restless_if_you_haven't_used_social_media_in_a_while?", axis = 1, inplace = True)
    df.drop("12._on_a_scale_of_1_to_5,_how_easily_distracted_are_you?", axis = 1, inplace = True)
    df.drop("13._on_a_scale_of_1_to_5,_how_much_are_you_bothered_by_worries?", axis = 1, inplace = True)
    df.drop("14._do_you_find_it_difficult_to_concentrate_on_things?", axis = 1, inplace = True)
    df.drop("15._on_a_scale_of_1-5,_how_often_do_you_compare_yourself_to_other_successful_people_through_the_use_of_social_media?", axis = 1, inplace = True)
    df.drop("16._following_the_previous_question,_how_do_you_feel_about_these_comparisons,_generally_speaking?", axis = 1, inplace = True)
    df.drop("17._how_often_do_you_look_to_seek_validation_from_features_of_social_media?", axis = 1, inplace = True)
    df.drop("19._on_a_scale_of_1_to_5,_how_frequently_does_your_interest_in_daily_activities_fluctuate?", axis = 1, inplace = True)
    return df