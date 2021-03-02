import re
from datetime import datetime

import pandas as pd


class DataManipulator():

    '''

    my idea here is to create a general class that specilizes in querring the CSV
    for all our data Needs.

    using pandas the CSV can be queried much like a SQL table,thus circumventing the need to use SQLite.

    IMPORTANT!: in order to get anything out of a function chain
                you need to pass true as the last argument, in the last function
                of your chain, or else you will just get the DataManipulator passed back to you.
                this also applies for single function calls

    ALSO :
        make sure in the CSV to change any dashes in the column headers, to underscores

    -Nico

    I made the average gate usage per day function and to be honest idk if its as efficient as possible
    If you see anything that could be change be my guest and change it

    -Dom
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
            self.output = self.main_dataframe[self.main_dataframe["Timestamp"].apply(lambda row : True if( pd.Timestamp(row).day == self.output.day ) else False)]

        else:
            self.output = self.output[self.output["Timestamp"].apply(lambda row : True if( pd.Timestamp(row).day == self.output.day ) else False)]

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

    # Return total amount of days in the dataframe
    def get_days(self) -> pd.DataFrame:

        days = 1

        # Needed this as a temp value for prev_day when counting days
        # Create a datetime object of the previous day
        prev_day = pd.Timestamp(self.main_dataframe['Timestamp'][1])

        # Iterates through entire dataframe and gathers each day
        for i in self.main_dataframe.index:
            # Creates a datetime object of the current day
            current_day = pd.Timestamp(self.main_dataframe['Timestamp'][i])
            # If datatime.day() is not equal add one to the current day
            if not prev_day.date() == current_day.date():
                days += 1
            # Sets prev_day to current_day to iterate along the list
            prev_day = current_day

        return days

    def daily_average_gate_usage(self) -> pd.DataFrame:

        # Use this as my general use dictionary to at first store total gate usage, then daily gate average
        counts = {}
        days = self.get_days()

        # This loop gathers the total usage for each gate from the entire dataset and total days
        for i in self.main_dataframe.index:
            # (String) current gate name
            current_gate = self.main_dataframe['gate_name'][i]
            if self.main_dataframe['gate_name'][i] in counts:
                counts[current_gate] = counts.get(current_gate)+1
            else:
                counts[current_gate] = 1

        # Take the average of each gate
        for gate in counts:
            # Rounding down for simplicity
            counts[gate] = int(counts.get(gate)/days)

        # Returns a dictionary of each gate and its average usage per day
        self.output = counts

        return self

    def average_by_weekday_helper(self, type : str) -> pd.DataFrame:

        counts = {}
        days = self.get_days()

        # Iterate through the entire dataframe for gate_name and timestamp
        for i in self.main_dataframe.index:
            # Creates the current gate and current day
            current_type = self.main_dataframe[type][i]
            current_day = pd.Timestamp(self.main_dataframe['Timestamp'][i]).weekday()
            # Combines the two for easier readability for dictionary purposes
            curr_tag = current_type + ' ' + str(current_day)
            if curr_tag in counts:
                counts[curr_tag] = counts.get(curr_tag) + 1
            else:
                counts[curr_tag] = 1

        # Figures the average for each gate usage in each day of the week
        for entry in counts:
            counts[entry] = int(counts.get(entry) / (days / 7))

        return counts

    def average_gate_usage_by_weekday(self) -> pd.DataFrame:

        counts = self.average_by_weekday_helper('gate_name')

        # Returns a dictionary of each gate and its average usage per day

        self.output = counts

        return self

    def average_car_type_by_weekday(self) -> pd.DataFrame:

        counts = self.average_by_weekday_helper('car_type')

        # Returns a dictionary of each gate and its average usage per day
        self.output = counts

        return self
