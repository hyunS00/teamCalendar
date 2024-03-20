from dotenv import load_dotenv
import os

load_dotenv()

def get_value(key):
    os.chdir('../')
    return os.environ.get(key)