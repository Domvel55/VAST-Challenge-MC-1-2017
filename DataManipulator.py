import pandas as pd
import typing
import re



class DataManipulator():

    '''

    my idea here is to create a general class that specilizes in querring the CSV
    for all our data Needs.

    using pandas the CSV can be queried much like a SQL table,thus circumventing the need to use SQLite.
    https://towardsdatascience.com/how-to-rewrite-your-sql-queries-in-python-with-pandas-8d5b01ab8e31

    don't be to intimated my the number of classes most of them are linerss, I'm just trying to cover all the bases.

    in order to do function chaining properly you need to put a true as the last argument in your last function in the chain.''

    also to make this work properly be sure to open a text editor and,
    change any dashes to underscores in the column headers in order for the code to work properly.

    -Nico
    '''

    main_dataframe = None
    output = None

    def __init__(self, csv_path : str):

        self.main_dataframe = pd.read_csv(csv_path)
        self.output = None
    def get_day(self, day : str, give_back=False) -> pd.DataFrame:

        day = pd.Timestamp(day)

        if(self.output is None):
            self.output = self.main_dataframe[self.main_dataframe["Timestamp"].apply(lambda row : True if( pd.Timestamp(row).day == output.day ) else False)]

        else:
            self.output = self.output[self.output["Timestamp"].apply(lambda row : True if( pd.Timestamp(row).day == output.day ) else False)]

        if(give_back):
            return self.output

        else:
            return self

    def get_timeframe(self, time1 : str, time2 : str, give_back=False ) -> pd.DataFrame:

        time1 = pd.Timestamp(time1)
        time2 = pd.Timestamp(time2)

        if(self.output is None):
            output_indexes = self.main_dataframe["Timestamp"].apply(lambda row : True if( time1 <= pd.Timestamp(row) <= time2 ) else False)
            self.output = self.main_dataframe[output_indexes]

        else:
            output_indexes = self.output["Timestamp"].apply(lambda row : True if( time1 <= pd.Timestamp(row) <= time2 ) else False)
            self.output = self.output[output_indexes]

        if(give_back):
            return self.output

        else:
            return self

    def get_car(self, car_id : str, give_back=False) -> pd.DataFrame:

        if(self.output is None):
            self.output = self.main_dataframe[self.main_dataframe.car_id == car_id]

        else:
            self.output = self.output[self.output.car_id == car_id]

        if(give_back):
            return self.output

        else:
            return self

    def get_cartype(self, car_type : str, give_back=False) -> pd.DataFrame:

        if(self.output is None):
            self.output = self.main_dataframe[self.main_dataframe.car_type == str(car_type)]

        else:
            self.output = self.output[self.output.car_type == str(car_type)]

        if(give_back):
            return self.output

        else:
            return self

    def get_specific_gate(self, gate_name : str, give_back=False) -> pd.DataFrame:

        if(self.output is None):
            self.output =  self.main_dataframe[self.main_dataframe.gate_name == gate_name]

        else:
            self.output = self.main_dataframe[self.main_dataframe.gate_name == gate_name]

        if(give_back):
            return self.output

        else:
            return self

    def get_gatetype(self, gate_type : str, give_back=False) -> pd.DataFrame:

        if(self.output is None):
            output_indexes = self.main_dataframe["gate_name"].apply(lambda row : True if( re.search( gate_type, row) ) else False)
            self.output =  self.main_dataframe[output_indexes]

        else:
            output_indexes = self.output["gate_name"].apply(lambda row : True if( re.search( gate_type, row) ) else False)
            self.output =  self.output[output_indexes]

        if(give_back):
            return self.output

        else:
            return self
