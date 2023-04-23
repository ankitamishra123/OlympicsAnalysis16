import pandas as pd

def preprocess():
    # read CSV files
    try:
        df = pd.read_csv('athlete_events.csv', on_bad_lines='skip')
    except KeyError:
        print("Error: 'Season' column is missing in the CSV file.")
        return None

    region_df = pd.read_csv('noc_regions.csv', delimiter=',')

    # filtering for summer olympics
    if 'Season' in df.columns:
        df = df[df['Season'] == 'Summer']
    else:
        print("Warning: 'Season' column is not found in the CSV file.")

    # merge with region_df
    #df = df.merge(region_df, on='NOC', how='left')

    # dropping duplicates
    df.drop_duplicates(inplace=True)

    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df






