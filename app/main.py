from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from faker import Faker  # Import Faker library for generating fake data
import random

app = FastAPI()

# Define database connection URL
DATABASE_URL = "postgresql://postgres:password@postgres-db:5432/aventus"

# Create SQLAlchemy engine and metadata
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define users table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
)

# Create the table in the database
metadata.create_all(engine)

# Initialize Faker instance
fake = Faker()

@app.get("/populate")
def populate_database():
    """
    Populate the database with random data.
    """
    try:
        with engine.connect() as connection:
            for _ in range(10):
                # Generate random name using Faker
                name = fake.name()
                # Generate random age
                age = random.randint(18, 60)
                # Execute SQL insert statement
                connection.execute(users.insert().values(name=name, age=age))
                # Log inserted user
                print(f"Inserted user: {name}, {age}")
            # Commit the transaction
            connection.commit()
        return {"message": "Database populated with random data"}
    except Exception as e:
        print(f"Error while populating database: {e}")
        return {"error": "Failed to populate database"}

@app.get("/delete")
def delete_data():
    """
    Delete all data from the users table.
    """
    with engine.connect() as connection:
        # Execute SQL delete statement
        connection.execute(users.delete())
    return {"message": "All data deleted from the database"}

