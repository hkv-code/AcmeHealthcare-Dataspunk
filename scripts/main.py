import data_extraction
import data_transformation
import data_cleansing
import data_ingestion
import config
import logger_config
import logging
import os

# Configure the logger
logger_config.configure_logger()


def main():
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    for file in config.txt_files:
        file_path = os.path.join(current_directory, '..', 'data', file)


        # Extract
        columns, lines, delimiter = data_extraction.extract_data_from_file(file_path)
        if columns is None or lines is None or delimiter is None:
            continue


        # Transform
        df = data_transformation.transform_data(columns, lines, file, delimiter)
        
        # Cleanse
        df = data_cleansing.remove_duplicates(df)

        # Ingest
        data_ingestion.insert_data_into_db(df, file)

    logging.info('Bulk insert completed.')
    print("Process executed successfully!")

if __name__ == '__main__':
    main()
