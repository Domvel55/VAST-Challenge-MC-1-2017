import pandas as pd
import typing

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

    def __init__(self, csv_path : str):

        main_dataframe = pd.read_csv(csv_path)

    def get_timeframe(self, day : str) -> pd.DataFrame

        return "filler"

    def get_timeframe(self, to : str, from : str ) -> pd.DataFrame

        return "filler"

    def get_timeframe(self, history : pd.DataFrame, day : str) -> pd.DataFrame

        return "filler"

    def get_timeframe(self, history : pd.DataFrame, to : str, from : str ) -> pd.DataFrame

        return "filler"

    def get_car_history(self, car_id : str) -> pd.DataFrame:

        return "filler"

    def get_car_history(self, history : pd.DataFrame, car_id : str, day: Timestamp) -> pd.DataFrame:

        return "filler"

    def get_cartype_history(self, car_type : str) -> pd.DataFrame:

        return "filler"

    def get_cartype_history(self, history : pd.DataFrame, car_type : str, day: Timestamp) -> pd.DataFrame:

        return "filler"

    def get_specific_gate_history(self, gate_name : str) -> pd.DataFrame:

        return "filler"

    def get_specific_gate_history(self, history : pd.DataFrame, gate_name : str) -> pd.DataFrame:

        return "filler"

    #probably going to need regexs to work properly
    #
    def get_gatetype_history(self, history : pd.DataFrame, gate_type : str) -> pd.DataFrame:

        return "filler"

    def get_gatetype_history(self, history : pd.DataFrame, gate_type : str, day: Timestamp) -> pd.DataFrame:

        return "filler"
