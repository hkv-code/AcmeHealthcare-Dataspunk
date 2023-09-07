import logging

def extract_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file_handle:
        lines = file_handle.readlines()

        # Detect delimiter
        if ',' in lines[0]:
            delimiter = ','
        elif '|' in lines[0]:
            delimiter = '|'
        else:
            logging.error(f"Delimiter not detected for {file}. Skipping...")
            return None, None, None

        columns = lines[0].strip().split(delimiter)
        logging.info(f"Data extracted from {file_path}.")
        return columns, lines[1:], delimiter
