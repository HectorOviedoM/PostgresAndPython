from getDataFromIexCloud import requestData,DataIexCloud
from postgres_database import Database



def test_requestData():
    assert not (requestData(f'https://cloud.iexapis.com/stable/stock/AAPL/chart/date/20210315/?token=pk_3b82f0a291fa4e6daa46dabd3443f03d&chartByDay=True')).empty


def test_postgres():
    database = Database('hectoroviedo_db')
    database.queryData("select  * from muttexam.coin_data ")


def test_data_get_iexCloud():
    con = DataIexCloud()
    dataframe = con.DataToPlot()
    assert not (dataframe).empty

