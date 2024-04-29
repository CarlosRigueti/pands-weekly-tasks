# Display weekday and weekend 
# Author: Carlos Rigueti

week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

weekday = week[0:5]
for day in weekday:
    print(f"Yes, unfortunately {day} is a weekday.")

weekend = week[5:7]
for day in weekend:
    print(f" {day}, It is the weekend, yay!")







