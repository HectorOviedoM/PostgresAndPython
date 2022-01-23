from getDataFromIexCloud import DataIexCloud
from postgres_database import Database
import sys

#to run a command line python app we have to specify a date in ISO8601 format, for example : 2021-03-15 , and "yes" if we want to save the df in a postgres table
#command line example : python dataFromDate.py 2021-03-24 YES

#get the DataIexCloud object to connect
con = DataIexCloud()

#get the command-line argument
date_sys = str(sys.argv[1])

#use the connection and get data from the {date_sys} date
dataframe = con.getData(date_sys)
dataframe.to_csv(f"save_results/files/aapl_chart_{date_sys}.csv")

#save the dataframe in a postgres table if the second command-line argument if "yes
if (str(sys.argv[2])).lower() == 'yes':
    database_postgres = Database('hectoroviedo_db')
    database_postgres.createTable(dataframe,'aapl_chart')

#check :
#from postgres_database import Database
#database = Database('hectoroviedo_db')
#database.queryData("select *  from public.aapl_chart")


