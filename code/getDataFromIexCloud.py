import pandas as pd
import requests



def requestData(url):
    """
    :param url(string): endpoint of the api to download data
    :return: return a dataframe from the json data downloaded
    """
    data = requests.get(url).json()
    dataframe = pd.DataFrame.from_dict(data)
    return dataframe



class DataIexCloud:
    def __init__(self):
        """
        token = token api of iexCloud
        """
        self.token = ''

    def getData(self, date):
        """
        :param date(string): date of the data to download
        :return: this function return a dataframe whit the data of the date
        """
        date_chart= date.replace("-", "")
        api_url = f'https://cloud.iexapis.com/stable/stock/AAPL/chart/date/{date_chart}/?token={self.token}&chartByDay=True'
        dataframe = requestData(api_url)
        return dataframe

    def DataToPlot(self):
        """
        :return: this functions returns a dataframe whith the historical data
        """
        api_url = f'https://cloud.iexapis.com/stable/stock/AAPL/chart/?token={self.token}'
        dataframe = requestData(api_url)
        return dataframe







