import requests
from django.core.management.base import BaseCommand
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3


class Command(BaseCommand):
    def handle(self, *args, **options):
        headers = {"User-Agent": generate_user_agent()}
        response = requests.get('https://www.coingecko.com/', headers=headers)
        if response.status_code == 200:
            bs_object = BeautifulSoup(response.content, 'html.parser')
            print(bs_object)
            coin_html = bs_object.find_all('span', class_='lg:tw-flex font-bold tw-items-center tw-justify-between')
            price_html = bs_object.find_all('td', class_='td-price price text-right')
            hourly_html = bs_object.find_all('td', class_='td-change1h change1h stat-percent text-right col-market')
            daily_html = bs_object.find_all('td', class_='td-change24h change24h stat-percent text-right col-market')

            coin_name = [coin.text.strip() for coin in coin_html]
            price = [float(cost.text.strip().replace('$', '').replace(',', '')) for cost in price_html]
            hourly_change = [hourly.text.strip() for hourly in hourly_html]
            daily_change = [daily.text.strip() for daily in daily_html]

            pre = {
                'coin_name': coin_name,
                'price': price,
                'hourly_change': hourly_change,
                'daily_change': daily_change
            }
            print(pre)

            pre_df = pd.DataFrame(pre)
            print(pre_df)
            connection = sqlite3.connect("db.sqlite3")
            pre_df.to_sql(name='api_crypto', con=connection, if_exists='append', index=False)

        else:
            print('unsuccessful')
            print(response.status_code)
