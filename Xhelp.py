report=[]
issue_type=input("What Is The Issue?: ")
location =input("Where is the damage? ")
severity=input("How bad is it ? (High/Medium/Low): ")
report.append(issue_type)
report.append(location)
report.append(severity)
print("REPORT SAVED: There Is",issue_type,"Issue With",severity,"level In",location)
print("FULL LIST: ",report)