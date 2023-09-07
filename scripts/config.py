# Connection parameters
server = 'DESKTOP-MRHLL48\SQLEXPRESS'
database = 'insurance_practice'
username = r'harsh'
password = 'shaktimaan'

# Create a connection string for SQLAlchemy
conn_str = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

# List of text files
txt_files = [
    '../data/acme_data_enrollment.txt',
    '../data/acme_data_medical_claims.txt',
    '../data/acme_data_pharmacy_claims.txt',
    '../data/acme_data_providers.txt'
]
