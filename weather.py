import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C" #constant, degree symbols etc


def format_temperature(temp): 
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string): #PASSED
    """Converts and ISO formatted date into a human readable format.

    date = "2021-07-05T07:00:00+08:00"
    expected_result = "Monday 05 July 2021"

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    convert_iso = datetime.fromisoformat (iso_string) #convert this string "2021-07-05T07:00:00+08:00" into iso date format
    convert_iso_date = convert_iso.strftime ("%A %d %B %Y") #convert isoformat from above into another string format same as expected result Monday 05 July 2021

    return convert_iso_date
    pass


def convert_f_to_c(temp_in_farenheit): #PASSED
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_f = float(temp_in_farenheit)
    convert_f_to_c = float((temp_in_f - 32) * 5/9)
    convert_f_to_c = format(convert_f_to_c, '.1f')
   
    return float(convert_f_to_c)
    pass


def calculate_mean(weather_data): #PASSED
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    weather_data = list(map(float, weather_data)) #convert elements in weather data to list and array of float type
    avg = sum(weather_data) / len(weather_data)
    return float(avg)
    pass


def load_data_from_csv(csv_file): #PASSED
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather = [] #creating empty list

    with open (csv_file) as csv_file: #opening csv file
        reader = csv.reader(csv_file) #reading
        next (reader) #skipping header
        for line in reader: #for each row in csv
            if len(line) > 0:  #if the row not empty, then run the following
                weather.append([line[0], int(line[1]), int(line[2])]) #add row to empty list, list within list and return right type e.g. str to int
  
    return weather #return the list    
    pass

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data) == 0: 
        return ()

    min_index = 0
    minimum = float(weather_data[0]) 

    for data in enumerate(weather_data):
        index, temp = data
        temp = float(temp)

        if temp <= minimum:
            minimum = temp
            min_index = index
    
    return (minimum, min_index)
    pass

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """

    if len(weather_data) == 0: 
        return ()

    max_index = 0
    maximum = float(weather_data[0]) 
    
    for data in enumerate(weather_data):
        index, temp = data
        temp = float(temp)

        if temp >= maximum:
            maximum = temp
            max_index = index
    
    return (maximum, max_index)
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.

    #5 Day Overview
        The lowest temperature will be #9.4°C, and will occur on #Friday 02 July 2021.
        The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
        The average low this week is 12.2°C.
         The average high this week is 17.8°C.
    """
    min_temps = []
    max_temps = []
    count_day = len(weather_data)
 
    for item in weather_data:
        min_temps.append(convert_f_to_c(item[1])) 
        max_temps.append(convert_f_to_c(item[2]))
        
    min_temp = find_min(min_temps)
    max_temp = find_max(max_temps)

    formatted_min_temp = format_temperature(min_temp[0])
    formatted_min_date = convert_date(weather_data[min_temp[1]][0])

    formatted_max_temp = format_temperature(max_temp[0])  
    formatted_max_date = convert_date(weather_data[max_temp[1]][0])

    avg_low = calculate_mean(min_temps)
    formatted_avg_low = format_temperature(round(avg_low,1))

    avg_high = calculate_mean(max_temps)
    formatted_avg_high = format_temperature(round(avg_high,1))   
       
    summary = f"{count_day} Day Overview\n  The lowest temperature will be {formatted_min_temp}, and will occur on {formatted_min_date}.\n  The highest temperature will be {formatted_max_temp}, and will occur on {formatted_max_date}.\n  The average low this week is {formatted_avg_low}.\n  The average high this week is {formatted_avg_high}.\n"

    # print (summary)
    return (summary)
    pass

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    ---- Friday 02 July 2021 ----
    Minimum Temperature: 9.4°C
    Maximum Temperature: 19.4°C
    """

    daily_summary = "" 

    for daily_weather_list in weather_data:
        date_string = daily_weather_list[0]
        formatted_date_string = convert_date(date_string)
        min_temp_f = daily_weather_list[1]
        min_temp_c = convert_f_to_c(min_temp_f) 
        min_temp_c_formatted = format_temperature(min_temp_c)
        max_temp_f = daily_weather_list[2]
        max_temp_c = convert_f_to_c(max_temp_f)
        max_temp_c_formatted = format_temperature(max_temp_c) 
        day_summary = f"---- {formatted_date_string} ----\n  Minimum Temperature: {min_temp_c_formatted}\n  Maximum Temperature: {max_temp_c_formatted}\n\n"
        daily_summary = daily_summary + day_summary 
    
    # print(date_summary)
    return daily_summary
    pass