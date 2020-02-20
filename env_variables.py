from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv('PASSWORD')
print(password)
