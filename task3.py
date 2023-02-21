# Determine the award for triathlon

time_of_swimming = int(input("Enter time in minutes for swimming:"))
time_of_cycling = int(input("Enter time in minutes of cycling:"))
time_of_run = int(input("Enter time in minutes of run:"))
total_time = time_of_swimming + time_of_cycling + time_of_run

print(f"The total time taken to complete the triathlon is:{total_time} ")

# Award based on total time, the qualifying time is 100 minutes.


if total_time >= 100:
    print("Provincial Colours")
elif total_time >= 95 and 100:
    print("Provincial Half Colours")
elif total_time >= 90 and 100:
    print("Provincial Scroll")
elif total_time < 90:
    print("No award")
