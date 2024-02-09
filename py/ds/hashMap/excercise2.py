"""
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    What was the temperature on Jan 9?
    What was the temperature on Jan 4?
Figure out data structure that is best for this problem
"""

from icecream import ic

weather_dict = {}

with open(file="nyc_weather.csv", mode="r") as f:
    for line in f:
        tokens = line.split(",")
        try:
            weather_dict[tokens[0]] = int(tokens[1])
        except Exception as e:
            ic("Ignored exception")

    f.close()
ic("What was the temperature on Jan 9?\n", weather_dict.get("Jan 9"))
# 4 What was the temperature on Jan 4?
ic("What was the temperature on Jan 4?\n", weather_dict.get("Jan 4"))
