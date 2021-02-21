# VAST-Challenge-MC-1-2017


WIP DataManipulator usage section, so no imports are required/tutorial for how the system works

Declare the manipulator, adding the file location to point to where your sensor data file is stored
finder = DataManipulator('C:/Users/legot/Desktop/College/DataVis/SensorData.csv') #file location
DataManipulator('file location') #Usage

Run any of the functions above, as needed
frame = finder.get_car("20154519024544-322",True)
Function returns a dataframe, which I have called frame. This xample searches the database for the car_id "20154519024544-322"
Notice the second argument of True, marking the end of the chain

Now for outputting to a csv
frame.to_csv('C:/Users/legot/Desktop/College/DataVis/foundCar.csv') #File location and name of output file
.to_csv will output the value of the dataframe to a file, which can then be used for analysis


#By adding these lines at the end of the file, no new file is needed.
finder = DataManipulator('C:/Users/legot/Desktop/College/DataVis/SensorData.csv')#Update for your own file ststem
frame = finder.get_car("20154519024544-322",True)
frame.to_csv('C:/Users/legot/Desktop/College/DataVis/foundCar.csv')#Update for your own file ststem
