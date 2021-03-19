from DataManipulator import DataManipulator
import pandas as pd


data = DataManipulator('Lekagul Sensor Data.csv')

print(data.cars_that_stayed())