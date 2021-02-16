import pandas as pd
import typing

def get_timeframe( history : pd.DataFrame, time1 : str, time2 : str ) -> pd.DataFrame:

    time1 = pd.Timestamp(time1)
    time2 = pd.Timestamp(time2)

    return history[history["Timestamp"].apply(lambda row : True if( time1 <= pd.Timestamp(row) <= time2 ) else False)]

def get_day( history : pd.DataFrame, day : str) -> pd.DataFrame:

    day = pd.Timestamp(day)

    return history[history["Timestamp"].apply(lambda row : True if( pd.Timestamp(row).day == output.day ) else False)]

def get_car( history : pd.DataFrame, car_id : str) -> pd.DataFrame:

    return history[history.car_id == car_id]

def get_cartype( history : pd.DataFrame, car_type : str) -> pd.DataFrame:

    return history[history.car_type == car_type]

def get_gatetype( history : pd.DataFrame, gate_type : str) -> pd.DataFrame:

    output_indexes = history["gate_name"].apply(lambda row : True if( re.search( gate_type, row) ) else False)

    return history[output_indexes]

def get_specific_gate( history : pd.DataFrame, gate_name : str) -> pd.DataFrame:

    return history[history.gate_name == gate_name]

class DataManipulator():

    '''

    my idea here is to create a general class that specilizes in querring the CSV
    for all our data Needs.

    using pandas the CSV can be queried much like a SQL table,thus circumventing the need to use SQLite.
    https://towardsdatascience.com/how-to-rewrite-your-sql-queries-in-python-with-pandas-8d5b01ab8e31

    don't be to intimated my the number of classes most of them are linerss, I'm just trying to cover all the bases.

    more functions can be added to this class depending on the groups data needs

    also to make this work properly be sure to open a text editor and,
    change any dashes to underscores in the column headers in order for the code to work properly.

    -Nico
    '''

    main_dataframe = None
    output = None

    def __init__(self, csv_path : str):

        self.main_dataframe = pd.read_csv(csv_path)

    def get_day(self, day : str, give_back=False) -> pd.DataFrame:

        day = pd.Timestamp(day)

        self.output = self.main_dataframe[self.main_dataframe["Timestamp"].apply(lambda row : True if( pd.Timestamp(row).day == output.day ) else False)]

        if(give_back):
            return self.output


    def get_timeframe(self, time1 : str, time2 : str, give_back=False ) -> pd.DataFrame:

        time1 = pd.Timestamp(time1)
        time2 = pd.Timestamp(time2)

        self.output =  self.main_dataframe[self.main_dataframe["Timestamp"].apply(lambda row : True if( time1 <= pd.Timestamp(row) <= time2 ) else False)]

        if(give_back):
            return self.output

    def get_car(self, car_id : str, give_back=False) -> pd.DataFrame:

        self.output =  self.main_dataframe[self.main_dataframe.car_id == car_id]

        if(give_back):
            return self.output

        else:
            return self

    def get_cartype(self, car_type : str, give_back=False) -> pd.DataFrame:

        self.output =  self.main_dataframe[self.main_dataframe.car_type == car_type]

        if(give_back):
            return self.output

        else:
            return self

    def get_specific_gate(self, gate_name : str, give_back=False) -> pd.DataFrame:

        self.output =  self.main_dataframe[self.main_dataframe.gate_name == gate_name]

        if(give_back):
            return self.output

        else:
            return self

    def get_gatetype(self, gate_type : str, give_back=False) -> pd.DataFrame:

        output_indexes = self.main_dataframe["gate_name"].apply(lambda row : True if( re.search( gate_type, row) ) else False)

        self.output = main_dataframe[output_indexes]

        if(give_back):
            return self.output
        else:
            return self
