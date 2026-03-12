# Import
from sqlalchemy import create_engine, text

# Define engine
user = "postgres"
pwd = "Abb98bertobis1!"
host = "localhost"
port = "5432"
database = "mobility_network"
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{database}')

# Test connection
try:
    with engine.connect() as connection:
        # Execute a simple test query (standard SQL)
        result = connection.execute(text("SELECT version();"))
        
        # Get result
        version = result.fetchone()
        
        print("Connection established.")

except Exception as e:
    print("Connection failed.")
    print(f"Error: {e}")