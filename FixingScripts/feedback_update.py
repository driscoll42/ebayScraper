import os

import pandas as pd

directory = r'C:\Users\mdriscoll6\Dropbox\PythonProjects\eBayScraper\Spreadsheets'

fb_dict = {}

for f in os.listdir(directory):
    print(f)
    if str(f).find('~') < 0:
        df = pd.read_excel('Spreadsheets/' + f, index_col=0, engine='openpyxl')
        dup_df = df.copy(deep=True)

        for index, row in dup_df.iterrows():
            seller = row['Seller']
            sell_fb = row['Seller Feedback']

            if sell_fb == 'None':
                sell_fb = -1

            if seller in fb_dict.keys():
                fb_dict[seller] = max(sell_fb, fb_dict[seller])
            else:
                fb_dict[seller] = sell_fb

        print(len(fb_dict))
num_updates = 0

for f in os.listdir(directory):
    print(f)
    if str(f).find('~') < 0:

        create = False
        df = pd.read_excel('Spreadsheets/' + f, index_col=0, engine='openpyxl')
        dup_df = df.copy(deep=True)

        for index, row in dup_df.iterrows():
            seller = row['Seller']
            sell_fb = row['Seller Feedback']
            if sell_fb == 'None':
                sell_fb = -1

            max_fb = fb_dict[seller]

            if sell_fb < max_fb:
                create = True
                num_updates += 1
                dup_df.loc[dup_df['Seller'] == seller, 'Seller Feedback'] = max_fb

        print(num_updates)
        if create:
            dup_df.to_excel('temp/' + f, engine='openpyxl')
