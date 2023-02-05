# CryptoPI
An ETL(Extract-Transform-Load) pipeline that utilizes the Django Restframework. The 'get' request is made to https://www.coingecko.com/. Beautifulsoup is then used to retrieve the data associated with the specified HTML tags. Once the information is retreived, the data is assigned to a dictionary and that dictionary is converted to a dataframe using the pandas library. From there the dataframe is saved to the sqlite database. Pagination and search fields have been added to the project to add extra flexibility to the project. The project utilizes the the following
libraries for the mentioned steps above:

import requests
from django.core.management.base import BaseCommand
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

The API endpoint is http://127.0.0.1:8000/api
