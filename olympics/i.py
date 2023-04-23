import pandas as pd

# set the chunk size to read the CSV file in chunks
chunk_size = 100000

# initialize an empty DataFrame to store the combined chunks
df = pd.DataFrame()

# iterate over each chunk in the CSV file
for chunk in pd.read_csv('athlete_events.csv', chunksize=chunk_size):
    # do your data processing here
    # for example:
    chunk['NOC'] = chunk['NOC'].apply(lambda x: x * 2)
    
    # append the processed chunk to the final DataFrame
    df = pd.concat([df, chunk], ignore_index=True)

# save the final DataFrame to a CSV file
df.to_csv('processed_file.csv', index=False)

