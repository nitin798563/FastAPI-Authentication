# FastAPI-Authentication
OAuth2 with Password (and hashing), Bearer with JWT tokens

Required Packages:
 fastapi uvicorn passlib[bcrypt] python-jose[cryptography] python-dotenv sqlalchemy python-jwt mysql-connector-python

DATABASE_URL = mysql+mysqlconnector://<username>:<password>@localhost:3306/<database_name>
SECRET_KEY = your_secret_key
