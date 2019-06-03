from django.shortcuts import render
from pastebins.models import pastebins
import pandas as pd
import os.path



def pd_stats(file_name, username, custom_share, content, created, private_bool, public_bool):

    cols = {'Username':username, 
        "Share_with":custom_share, 
        "Content":content,
        "Created":created,
        "Private":private_bool,
        "Public":public_bool,
        }
    df = pd.DataFrame(
        cols, columns=['Username', 'Share_with', 'Content', "Created", "Private", "Public"]
        ) # to set columns in your order: https://stackoverflow.com/questions/51878601/pandas-dataframe-to-csv-how-to-set-column-names
    if os.path.exists(file_name):
        fileContent = pd.read_csv(file_name, names=['Username', 'Share_with', 'Content', "Created", "Private", "Public"])
        if  df["Content"][0] in fileContent["Conent"].tolist():
            pass
        else:
            with open(file_name, 'a', encoding="utf-8") as f:
                df.to_csv(f, header=None, index=False)
    else:
        with open(file_name, 'a', encoding="utf-8") as f:
            df.to_csv(f, header=None, index=False)



