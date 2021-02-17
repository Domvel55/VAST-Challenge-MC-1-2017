import pandas as pd
import typing
import re



class DataManipulator():

    '''

    my idea here is to create a general class that specilizes in querring the CSV
    for all our data Needs.

    using pandas the CSV can be queried much like a SQL table,thus circumventing the need to use SQLite.

    IMPORTANT!: in order to get anything out of a function chain
                you need to pass true as the last argument, in the last function
                of your chain, or else you will just get the DataManipulator passed back to you.
                this also applies for single function calls

    -Nico
    '''

    main_dataframe = None
    output = None

    def __init__(self, csv_path : str):

        self.main_dataframe = pd.read_csv(csv_path)
        self.output = None

    def get_day(self, day : str, give_back=False) -> pd.DataFrame:

        '''
            takes in a string of fromat year-month-day,
            and turns data from that day

        '''

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

        '''
            to get any timeframe, between time1, and time2
            where they are 2 strings in the format of year-month-day hour:minute:second

        '''

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

        '''

        unlike get_gatetype you can use this to get a specific gate like camping0

        '''

        if(self.output is None):
            self.output =  self.main_dataframe[self.main_dataframe.gate_name == gate_name]

        else:
            self.output = self.main_dataframe[self.main_dataframe.gate_name == gate_name]

        if(give_back):
            return self.output

        else:
            return self

    def get_gatetype(self, gate_type : str, give_back=False) -> pd.DataFrame:

        '''
        unlike get_specific_gate you can use this to get data for a set of gates, like all ranger stops.
        '''

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
