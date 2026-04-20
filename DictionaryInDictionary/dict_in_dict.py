students = {
    "Rohit": {
        "Math": 78,
        "Science": 85,
        "English": 90,
        "Hindi": 88,
        "Computer": 76
    },
    "Amit": {
        "Math": 65,
        "Science": 70,
        "English": 72,
        "Hindi": 68,
        "Computer": 74
    },
    "Priya": {
        "Math": 88,
        "Science": 92,
        "English": 95,
        "Hindi": 91,
        "Computer": 89
    },
    "Neha": {
        "Math": 75,
        "Science": 80,
        "English": 78,
        "Hindi": 82,
        "Computer": 77
    },
    "Rahul": {
        "Math": 60,
        "Science": 66,
        "English": 70,
        "Hindi": 64,
        "Computer": 68
    },
    "Sneha": {
        "Math": 90,
        "Science": 93,
        "English": 89,
        "Hindi": 94,
        "Computer": 91
    },
    "Vikas": {
        "Math": 55,
        "Science": 60,
        "English": 58,
        "Hindi": 62,
        "Computer": 59
    },
    "Anjali": {
        "Math": 82,
        "Science": 86,
        "English": 84,
        "Hindi": 88,
        "Computer": 85
    },
    "Karan": {
        "Math": 70,
        "Science": 75,
        "English": 72,
        "Hindi": 78,
        "Computer": 74
    },
    "Pooja": {
        "Math": 85,
        "Science": 88,
        "English": 90,
        "Hindi": 87,
        "Computer": 89
    }
}

# print(students["Rohit"])
for name,all_sub in students.items():
    # total = all_sub["Math"]+all_sub["Science"]+all_sub["English"]+all_sub["Hindi"]+all_sub["Computer"];
    total = 0
    for v in all_sub:
        total+=all_sub[v]
    # print(total)
    print(f"{name} -> {total}")