import logging

def remove_duplicates(df):
    initial_length = len(df)
    df.drop_duplicates(inplace=True)
    final_length = len(df)

    num_dropped = initial_length - final_length
    if num_dropped > 0:
        logging.info(f"{num_dropped} duplicate rows removed.")

    return df
