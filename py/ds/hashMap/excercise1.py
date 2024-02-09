"""
nyc_weather.csv contains new york city weather for first few days in the month of January.
Write a program that can answer following,
    What was the average temperature in first week of Jan
    What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem
"""

from icecream import ic

arr = []

with open(file="nyc_weather.csv", mode="r") as f:
    for line in f:
        tokens = line.split(",")
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except Exception as e:
            ic("Ignored exception")
    f.close()
# 1 What was the average temperature in first week of Jan
ic(sum(arr[:7]) / len(arr[:7]))
# 2 What was the maximum temperature in first 10 days of Jan
ic(max(arr[:10]))
