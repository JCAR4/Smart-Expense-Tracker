import pandas as pd

data = {
    "Description": [
        "Pizza Hut Dinner", "Uber Ride", "Electricity Bill",
        "Bus Ticket", "Dominos Lunch", "Water Bill",
        "Flight Ticket", "Cafe Coffee", "Gas Bill"
    ],
    "Amount": [500, 300, 1500, 50, 400, 600, 5000, 250, 1200],
    "Category": [
        "Food", "Travel", "Utilities",
        "Travel", "Food", "Utilities",
        "Travel", "Food", "Utilities"
    ]
}

df = pd.DataFrame(data)
print(df)
