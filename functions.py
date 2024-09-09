import pandas as pd
def read_data(url):

    df = pd.read_csv(url)
    return df

