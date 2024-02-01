import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_bitcoin_data():
    """
        load bitcoin transaction data and do some data cleaning
    """

    tx_df = pd.read_csv('tech-challenge-2020-obfuscation/dataset/tx_info.csv', header=0)
    time_df = pd.read_csv('tech-challenge-2020-obfuscation/dataset/time_info.csv', sep=";", header=0)
    time_df['time'] = pd.to_datetime(time_df.time, unit='s')
    # combined_df = pd.merge(tx_df, time_df, left_index=True, right_index=True)
    combined_df = pd.concat([tx_df, time_df], axis=1)
    print(combined_df[:100])
    time_ordered_df = combined_df.sort_values(by=['time'], ascending=False)
    return time_ordered_df


def is_shared_coin(row):

    """
    checks if a particular transaction is a shared coin transaction using heuristics

    shared coin heuristics:
    - typically greater than 9 inputs and > 9 outputs
    - miner fee of 0.0001 (or multiple) was always included
    - input sum and output sum will be matched

    :param row: dict()
    :return is_sharedcoin: bool
    """
    is_sharedcoin = False

    if row["fee"] % 0.0001 == 0 and row['inAds'] > 9 and row['outAds'] > 9 and row["invol"] == row["outvol"]:
        is_sharedcoin = True

    return is_sharedcoin



def get_shared_coin_transactions(df):
    """
    get all sharedcoin trnsactions from a dt of bitcoin transactions
    :param df:
    :return df with shared_coin labels:
    """
    shared_coin_list = []
    for id, row in df.iterrows():

        if is_shared_coin(row):
            shared_coin_list.append(1)
        else:
            shared_coin_list.append(0)

    df["shared_coin"] = shared_coin_list

    return df



def find_sharedCoins_and_plot():
    """
    Find shared coin transactions in bitcoin data
    :return:
    """
    print('loading date')
    df = load_bitcoin_data()
    print('getting transactions')
    shared_coin_df = get_shared_coin_transactions(df)
    print('saving to csv')

    shared_coin_df.to_csv('tech-challenge-2020-obfuscation/dataset/shared_coin_df.csv')
    print('plotting')
    shared_coin_df = shared_coin_df[shared_coin_df.shared_coin != 0]
    shared_coin_df.plot(kind = 'scatter', x='time', y='shared_coin', style='o')

    plt.show()



find_sharedCoins_and_plot()