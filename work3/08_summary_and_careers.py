bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
num_people = int(input("Enter number of people: "))
total_with_tip = bill + (bill * tip_percent / 100)
each_person_pays = total_with_tip / num_people
each_person_pays = round(each_person_pays, 2)
print(f"Each person pays: {each_person_pays}")
