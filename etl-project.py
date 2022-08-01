
# import dependencies
import pandas as pd
import gmaps
from sqlalchemy import create_engine
from config import api_key
from urllib import response
import requests
import json
import numpy as np



listing_df=pd.read_csv('resources/listings.csv')
listing_df.head()
len(listing_df)



new_df=listing_df[['id', 'host_id', 'name', 'host_location', 'review_scores_location', \
        'latitude', 'longitude', 'price']]
new_df.rename(columns={'name':'airbnb_name'}, inplace=True)
new_df.sort_values(by=['review_scores_location'], ascending=False)



reviews_df=pd.read_csv('resources/reviews.csv', encoding='utf-8')



new_df3=reviews_df[['listing_id', 'id', 'comments']]




cafe_df=new_df[['id','airbnb_name','latitude','longitude']]
cafe_df['cafe_name']=''
cafe_df['cafe_rating']=''



params={
    'radius':20,
    'types':'restaurant',
    'keyword':'restaurant',
    'key':api_key
}


for index, row in cafe_df.iterrows():
    lat=row['latitude']
    lng=row['longitude']

    params['location']=f'{lat},{lng}'

    url='https://maps.googleapis.com/maps/api/place/nearbysearch/json'

    response=requests.get(url, params=params).json()


    try:
        cafe_df.loc[index,'cafe_name']=response['results'][0]['name']
        cafe_df.loc[index, 'cafe_rating']=response['results'][0]['rating']

    except(KeyError, IndexError):



cafe_df['cafe_name'].replace('', np.nan, inplace=True)
cafe_df.dropna(subset=['cafe_name'], inplace=True)




connection_string='postgres:Harvey90@localhost:5432/etl_project'
engine=create_engine(f'postgresql://{connection_string}')


engine.table_names()


new_df.to_sql(name='listing', con=engine, if_exists='append', index=False)


cafe_df.to_sql(name='cafes', con=engine, if_exists='append', index=False)


new_df3.to_sql(name='reviews', con=engine, if_exists='append', index=False)


pd.read_sql_query('select * from listing', con=engine).head()


pd.read_sql_query('select * from reviews', con=engine).head()


pd.read_sql_query('select * from cafes', con=engine).head()


