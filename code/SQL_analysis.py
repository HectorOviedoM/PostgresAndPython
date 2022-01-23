from postgres_database import Database
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)

#create the object
database = Database('hectoroviedo_db')



#the average price for each coin by month
#database.queryData("select coin,date_part('year',date) as year , date_part('month',date) as month , avg(price) as avg_price  from muttexam.coin_data group by year,month, coin order by coin, month,year")

# how much each coin has changed each day
#database.queryData("select coin, date , price as actual_price , (price - (lag(price) over (partition by coin order by coin, date))  )  as price_diff from muttexam.coin_data" )


#the lowest and the greatest price for each day
#database.queryData("select  distinct on (date) date , (last_value(coin) over (partition by date order by price desc)) as min_coin , (last_value(price) over (partition by date order by price desc)) as min_price , (first_value(coin) over (partition by date order by price desc)) as max_coin , (first_value(price) over (partition by date order by price desc)) as max_coin_price from muttexam.coin_data group by date, coin order by date,price asc")


