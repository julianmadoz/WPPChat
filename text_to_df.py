import pandas as pd
from datetime import datetime


def txt_to_df(file='file:///home/julianmadoz/Downloads/WhatsApp Chat with 🫑🪅🧑‍🎤FCDJ🧑‍🎤🪅🫑.txt'):
    fileloaded = pd.read_csv(file, delimiter='\t', header=None)
    df = fileloaded[0].str.extract(r'(\S*, \S*) - (.*?): (.*)')
    df.columns = ['date', 'sender', 'msg']
    df.index = pd.to_datetime(df.date)
    df.drop(columns='date', inplace=True)
    print(df.sender.unique())
    return df
