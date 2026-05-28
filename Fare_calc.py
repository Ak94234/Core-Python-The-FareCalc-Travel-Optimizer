rates={
    'ECONOMY':10,
    'PREMIUM':18,
    'SUV':25
}

def calculate_fare(km,vehicle_type,hour):
    if vehicle_type not in rates:
        return "Service Not Available"
    base_rate=rates[vehicle_type]
    fare=base_rate*km
    surge=0
    if hour>=17 and hour<=20:
        fare=fare*1.5
    return fare

try:
    km=float(input("Enter distance in km:"))
    vehicle_type=input("Enter vehicle type (Economy,Premium,SUV):")
    vehicle_type = vehicle_type.upper()
    hour=int(input("Enter hour of day(0-23):"))

    if hour<0 or hour>23:
        print("Invalid Hour. Hour must be between 0 and 23")

    result=calculate_fare(km,vehicle_type,hour)

    print("\n ---- Ride Bill ----")
    print(f"Distance: {km} km")
    print(f"Vehicle Type: {vehicle_type}")
    print(f"Hour: {hour} 00 hrs")

    if result == "Service Not Available":
        print(result)
    else:
        print(f"Ride Estimation: {result}")

except ValueError:
    print("Invalid Input Please Try Again")




