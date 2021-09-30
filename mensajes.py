import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def mensajes_por_mes_por_persona(df):
    # df = df.resample('M',level=1).msg.count()

    agg = df.groupby(by='sender').resample('3M').msg.count().reset_index()
    print(agg)
    # return agg
    sns.barplot(data=agg, x='date',y='msg')
    # plt.plot()
    # print(agg)

def kde_totmsj(df):
    # df = df.resample('M',level=1).msg.count()

    agg = df.resample('D').msg.count().reset_index()
    print(agg)
    # return agg
    sns.kdeplot(data=agg,x='date', weights='msg')
    # plt.plot()
    # print(agg)

def count_msg_per_person(df):
    def count_char(x):
        if x == '<Media omitted>':
            return 0
        else:
            return len(str(x))
    df['msg'] = df.msg.apply(lambda x: count_char(x))

    agg = df.groupby(by='sender').msg.sum().reset_index()
    print(agg)
    sns.barplot(data=agg, x='sender',y='msg')
