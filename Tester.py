from DataManipulator import DataManipulator


data = DataManipulator('Lekagul Sensor Data.csv')
data.average_car_type_by_weekday()
print(data.output)
data.average_gate_usage_by_weekday()
print(data.output)