# etl-project-2
ETL PROJECT
(ETL) is the general procedure of copying data from one or more sources into a destination system, which represents the data differently from the source(s) or in a different context than the source(s).
Our Project Aim is to perform the below activities as part of ETL phase.
MOTIVATION
Airbnb dataset
Airbnb is a home-sharing platform, which provides a platform for hosts to accommodate guests with short-term lodging and tourism-related activities. Guests can search for lodging using filters such as lodging  restaurants, ratings, location, and price Guests have the ability to search before booking, users must provide personal and payment information. Some hosts also require a scan of government-issued identification before accepting a reservation.
The group picked this dataset in order to extract data about reviews made by guests regarding their stays. Another question about nearby cafes became a keen interest and we soughted out the data. This datasets were not analysed but was cleaned transformed and loaded to SQL database
EXECUTION
Data sources: Kaggle(Airbnb csv) and google maps API
Jupyter notebook running python 3.7.13 was responsible for data extraction from the downloaded CSV to dataframes. Also, google API was used to extract restauranst near the chosen airbnb locations. Please refer to the ipynb file.
PostgresSQL was responsible for storing the extracted and cleaned dataframes. The dataset was loaded from jupyter notebook.
Modules used; numpy, sqlalchemy, json and pandas
CONCLUSION
The host, with recommendations from Airbnb, determines pricing. Hosts and guests have the ability to leave reviews about the experience. The datasets stored in sql can be used for further analysis.
