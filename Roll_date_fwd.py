import pandas as pd
import datetime

input_file = 'Super.xlsx'

#import data from xls
xls_df = pd.read_excel(input_file, sheet_name="Sheet1",index_col=0)

# function definition
def date_loop(df, date, offset, ncycles):
    #refresh index (optional)
    df.reindex
    #adding column
    df['Date'] = date
    #reformat to date
    df['Date'] = pd.to_datetime(df['Date'])
    # create temporary df to add
    df1 = df.copy()
    # cycle [ncycles] times
    for i in range(1,ncycles+1):
        #addind offset
        df1['Date'] += datetime.timedelta(days=offset)
        #append to original df
        df = pd.concat([df,df1], axis=0,ignore_index=True)
    # output final df
    return df

print(date_loop(xls_df,'01/01/2022',1,2))
