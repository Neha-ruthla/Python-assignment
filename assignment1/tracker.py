# tracker.py
# Daily Calorie Tracker
# made by (Neha)
# Roll no = 2501730310
#course= btech.cse (AI $ ML)


import datetime

meals = []
calories = []

num = int(input("How many meals did you eat today? "))
for i in range(num):
    name = input(f"Enter meal name {i+1}: ")
    cal = float(input(f"Enter calories for {name}: "))
    meals.append(name)
    calories.append(cal)

print("Data saved successfully!")

total_cal = sum(calories)
avg_cal = total_cal / num
limit = float(input("Enter your daily calorie limit: "))

if total_cal > limit:
    print("⚠️ You have exceeded your daily calorie limit!")
else:
    print("✅ You are within your calorie limit.")

print("Meal Name\tCalories")
for i in range(num):
    print(f"{meals[i]:<15}\t{calories[i]:>6.2f}")

print(f"Total:\t{total_cal:.2f}")
print(f"Average:\t{avg_cal:.2f}")

save = input("Do you want to save this record? (yes/no): ")

if save.lower() == "yes":
    f = open("calorie_log.txt", "w")
    f.write("Calorie Tracker Report\n")
    f.write("Date: " + str(datetime.datetime.now()) + "\n")
    f.write("Meal Name\tCalories\n")
    for i in range(num):
        f.write(f"{meals[i]:<15}\t{calories[i]:>6.2f}\n")
    f.write(f"Total:\t{total_cal:.2f}\n")
    f.write(f"Average:\t{avg_cal:.2f}\n")
    f.write(f"Limit:\t{limit}\n")
    if total_cal > limit:
        f.write("Status: Exceeded Limit\n")
    else:
        f.write("Status: Within Limit\n")
    f.close()
    print("File saved successfully (calorie_log.txt)")

print("Thank you for using the program ")

