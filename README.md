# FareCalc CityCab Travel Optimizer

FareCalc CityCab Travel Optimizer is a simple Python console based fare calculator developed for the fictional ride sharing startup CityCab.

The application calculates ride fares based on:

Distance traveled

Vehicle type

Peak hour surge pricing

This project demonstrates the use of dictionaries, functions, conditional statements, error handling, user input processing, and formatted console output.

## Problem Statement

CityCab needs a backend fare calculation system where ride prices vary depending on:

Vehicle category

Distance traveled

Peak hour surge pricing

The system should generate a formatted ride estimate receipt for customers.

## Features

Dictionary based fare rate management

Dynamic fare calculation

Peak hour surge pricing support

Function based modular code

Input validation and error handling

Formatted ride receipt generation

## Technologies Used

Python

Dictionaries

Functions

Exception Handling

Conditional Logic

## Project Structure

FareCalc

farecalc.py

README.md

## Vehicle Fare Rates

Economy  Rate per KM is 10 Rupees

Premium  Rate per KM is 18 Rupees

SUV  Rate per KM is 25 Rupees

## Surge Pricing Logic

If the ride is booked during Peak Hours from 5 PM to 8 PM:

17:00 hrs to 20:00 hrs

A 1.5x surge multiplier is applied to the total fare.

## Function Used

```python id="e8nq7x"
def calculate_fare(km, vehicle_type, hour):
```

This function:

Calculates the base fare

Applies surge pricing if applicable

Returns the final ride estimate

## Error Handling

The program handles the following cases:

Invalid vehicle types

Invalid numeric input

Invalid hour values

Example:

Service Not Available

## Sample Output

```text id="u4jq9m"
Enter distance in km: 12

Enter vehicle type (Economy, Premium, SUV): Premium

Enter hour of day (0-23): 18

---- Ride Bill ----

Distance: 12.0 km

Vehicle Type: PREMIUM

Hour: 18:00 hrs

Ride Estimation: 324.0 Rupees
```

## How To Run

Step 1 Run the Python Script

```bash id="x1kq7c"
python farecalc.py
```

OR

```bash id="m5p2zr"
python3 farecalc.py
```

## Concepts Covered

Python Dictionaries

Functions

Conditional Statements

Exception Handling

User Input Validation

String Formatting

## Future Improvements

GUI version using Tkinter

Database integration

Live GPS fare estimation

Coupon and discount system

Online payment support

## Author

Ayush Kumar
