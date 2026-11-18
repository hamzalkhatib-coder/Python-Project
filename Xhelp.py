import json

report=[]
try:
  with open("report.json") as maryam:
    report=json.load(maryam)
except FileNotFoundError:
 pass

count_2=0
count_1=0
count_3=0
count_4=0
def show_issue():
  print("Issue Received:",issue_type)
def welcome_1():
  print("WELCOME TO XHELP")
  print("Report Problems In Your Neighborhood: ")


for f in report:
 if f["severity"]=="high":
  count_2+=1
def report_5():
  print("Previously Saved Reports:")

  for c in report:
   
    print("Issue:",c["issue"])
    
    print("Location:",c["location"])
  
    print("Severity:",c["severity"])
    print("")
   

welcome_1()
report_5()
print("Previously Saved Reports: ",len(report))
print("High Severity Reports:",count_2)
print("URGENT PROBLEMS:")
for a in report:
  if a["severity"] =="high":
    print(a)
urgent_1=input("Search Urgent Problems In Which Location?:").strip().lower()
for q in report:
 if q["location"].lower()==urgent_1 and q["severity"].lower() =="high":
  count_3+=1
  print(q)
print("Total Urgent Problem Here:",count_3)

  
while True:
    issue_type = input("What Is Issue?: ").strip().lower()
    while issue_type == "":
        issue_type = input("What Is Issue?: ").strip().lower()

    show_issue()

    location_1 = input("Where is the damage? ").strip()
    while location_1 == "":
        location_1 = input("Where is the damage? ").strip()

    severity_1 = input("How bad is it? (high/medium/low): ").strip().lower()
    while severity_1 not in ["high", "medium", "low"]:
        severity_1 = input("How bad is it? (high/medium/low): ").strip().lower()
    
    # Check existing reports for duplicates
    count_4 = 0

    for t in report:
        if t["issue"].lower().strip() == issue_type and t["location"].strip().lower() == location_1.lower():
            count_4 += 1

    if count_4 > 0:
        print("Possible Duplicate!")
        print("Similar Reports Already Exist:", count_4)

    # Create and save the new report
    report_new = {
        "issue": issue_type,
        "location": location_1,
        "severity": severity_1,
        "id":len(report)

    }
    report.append(report_new)

    with open("report.json", "w") as file:
        json.dump(report, file)

    print("REPORT SAVED!")

    another_one = input("Do You Want To Add Another Report?: ").strip().lower()

    while another_one not in ["yes", "no"]:
        another_one = input("Do You Want To Add Another Report?: ").strip().lower()

    if another_one == "no":
        wanted = input("What do you want to search?: ").strip().lower()

        matches = 0

        for b in report:
            if b["issue"].lower() == wanted:
                matches += 1
                print(b)

        print("Total Matching Issues:", matches)

        if matches == 0:
            print("No Report Was Found.")

        break