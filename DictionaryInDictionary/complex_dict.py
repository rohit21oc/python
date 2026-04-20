students = {
    "Rohit": {
        "roll_no": 101,
        "age": 22,
        "gender": "Male",
        "city": "Delhi",
        "mobile": "9876543210",
        "marks": {
            "Math": 78,
            "Science": 85,
            "English": 90,
            "Hindi": 88,
            "Computer": 76
        }
    },
    "Amit": {
        "roll_no": 102,
        "age": 21,
        "gender": "Male",
        "city": "Mumbai",
        "mobile": "9123456780",
        "marks": {
            "Math": 65,
            "Science": 70,
            "English": 72,
            "Hindi": 68,
            "Computer": 74
        }
    },
    "Priya": {
        "roll_no": 103,
        "age": 20,
        "gender": "Female",
        "city": "Patna",
        "mobile": "9988776655",
        "marks": {
            "Math": 88,
            "Science": 92,
            "English": 95,
            "Hindi": 91,
            "Computer": 89
        }
    },
    "Neha": {
        "roll_no": 104,
        "age": 22,
        "gender": "Female",
        "city": "Kolkata",
        "mobile": "9871234560",
        "marks": {
            "Math": 75,
            "Science": 80,
            "English": 78,
            "Hindi": 82,
            "Computer": 77
        }
    },
    "Rahul": {
        "roll_no": 105,
        "age": 23,
        "gender": "Male",
        "city": "Chennai",
        "mobile": "9012345678",
        "marks": {
            "Math": 60,
            "Science": 66,
            "English": 70,
            "Hindi": 64,
            "Computer": 68
        }
    },
    "Sneha": {
        "roll_no": 106,
        "age": 21,
        "gender": "Female",
        "city": "Bangalore",
        "mobile": "9090909090",
        "marks": {
            "Math": 90,
            "Science": 93,
            "English": 89,
            "Hindi": 94,
            "Computer": 91
        }
    },
    "Vikas": {
        "roll_no": 107,
        "age": 22,
        "gender": "Male",
        "city": "Lucknow",
        "mobile": "9870001111",
        "marks": {
            "Math": 55,
            "Science": 60,
            "English": 58,
            "Hindi": 62,
            "Computer": 59
        }
    },
    "Anjali": {
        "roll_no": 108,
        "age": 20,
        "gender": "Female",
        "city": "Jaipur",
        "mobile": "9998887776",
        "marks": {
            "Math": 82,
            "Science": 86,
            "English": 84,
            "Hindi": 88,
            "Computer": 85
        }
    },
    "Karan": {
        "roll_no": 109,
        "age": 23,
        "gender": "Male",
        "city": "Pune",
        "mobile": "9812345678",
        "marks": {
            "Math": 70,
            "Science": 75,
            "English": 72,
            "Hindi": 78,
            "Computer": 74
        }
    },
    "Pooja": {
        "roll_no": 110,
        "age": 21,
        "gender": "Female",
        "city": "Hyderabad",
        "mobile": "9700002222",
        "marks": {
            "Math": 85,
            "Science": 88,
            "English": 90,
            "Hindi": 87,
            "Computer": 89
        }
    }
}

for name,details in students.items():
    total_marks = sum(details["marks"].values())
    percentage = total_marks/500*100
    result = ""
    if percentage>30:
        result ="Pass"
    else:
        result = "Fail"
    print("Name: ",name ,"\nRoll no: " ,details["roll_no"],"\nTotal Marks: ", total_marks, "\nPercentage: ",percentage,"Result: ",result)
