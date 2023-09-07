import pandas as pd
import logging

def split_provider_name(df):
    if 'PROVIDER_NAME' in df.columns:
        df['PROVIDER_FIRST_NAME'] = df['PROVIDER_NAME'].apply(lambda x: x.split()[0] if x else None)
        df['PROVIDER_LAST_NAME'] = df['PROVIDER_NAME'].apply(lambda x: x.split()[-1] if x else None)
        df['PROVIDER_MIDDLE_INITIAL'] = df['PROVIDER_NAME'].apply(lambda x: x.split()[1][0] if x and len(x.split()) > 2 else None)
        df.drop(columns=['PROVIDER_NAME'], inplace=True)
    return df

def transform_data(columns, lines, file, delimiter):
    valid_data = []
    for line in lines:
        fields = line.strip().split(delimiter)
        if len(fields) == len(columns):
            valid_data.append(fields)

    df = pd.DataFrame(valid_data, columns=columns)
    
    if file.endswith("acme_data_providers.txt"):
        df = split_provider_name(df)
        logging.info(f"Transformed provider names for {file}.")

    return df
