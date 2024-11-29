#James Corino 5/7/21
print("Start Time")
print("----------")
start_hour = int(input("Input hour: ")) * 3600
start_minutes = int(input("Input minute: ")) * 60
start_second = int(input("Input second: "))
print("")
print("End Time")
print("----------")
end_hour = int(input("Input hours: ")) * 3600
end_minutes = int(input("Input minutes: ")) * 60
end_second = int(input("Input seconds: "))
start_elapsed = int(start_hour + start_minutes + start_second)
end_elapsed = int(end_hour + end_minutes + end_second)
elapsed = int(abs(end_elapsed - start_elapsed))
print("")
print("The total number of seconds elapsed is", elapsed, "seconds.")