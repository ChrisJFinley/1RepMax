# 1RepMax
def get_max():
    while True:
        max_input = input("Enter your 1RM: ")
        if max_input.isdigit():
            max_weight = int(max_input)
            if max_weight > 0:
                return max_weight  # Return the max weight once it's valid
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

def get_working_sets():
    while True:
        sets_input = input("How many sets? ")
        if sets_input.isdigit():
            sets = int(sets_input)
            if 2 < sets < 8:  # Make sure the number of sets is between 2 and 10
                return sets  # Return the number of sets once it's valid
            else:
                print("Number of sets must be between 2 and 8.")
        else:
            print("Please enter a number.")

def get_reps():
    while True:
        reps_input = input("How many reps? ")
        if reps_input.isdigit():
            reps = int(reps_input)
            if 2 < reps < 8:  # Make sure the number of reps is between 2 and 8
                return reps  # Return the number of sets once it's valid
            else:
                print("Number of reps must be between 2 and 8.")
        else:
            print("Please enter a number.")


def get_percentage(max_weight, num_sets):
    if num_sets == 3: 
      return max_weight * .95 
    if num_sets == 4: 
      return max_weight * .85 
    elif num_sets == 5:
      return max_weight * .75 
    else: 
      return max_weight * .65 

def get_volume(max_weight, num_sets, num_reps):
    working_weight = get_percentage(max_weight, num_sets)
    return working_weight * num_reps * num_sets


max_weight = get_max()
num_sets = get_working_sets()
num_reps = get_reps()
percentage = get_percentage(max_weight, num_sets)
volume = get_volume(percentage, num_sets, num_reps)
print(f"Your working weight will be {percentage} pounds")
print(f"Your total volume will be {volume} pounds")

def get_run_time():
  while True:
      run_input = input("Enter your 1-mile run time (in minutes): ")
      try:
          run_time = float(run_input)
          if run_time > 0:
              return run_time  # Return the run time once it's valid
          else:
              print("Run time must be greater than 0.")
      except ValueError:
          print("Please enter a valid number.")

def get_adjusted_run_time(run_time):
  # Assuming a linear adjustment for a 2-mile run based on the 1-mile run time
  adjusted_run_time = run_time * 2
  return adjusted_run_time

def get_total_distance(run_time):
  return run_time * 2  # Assuming an average speed of 2 miles per minute for the adjusted run time

run_time = get_run_time()
adjusted_run_time = get_adjusted_run_time(run_time)
total_distance = get_total_distance(adjusted_run_time)

print(f"Your adjusted run time for a 2-mile run will be approximately {adjusted_run_time:.2f} minutes")
print(f"You are expected to cover a total distance of approximately {total_distance:.2f} miles")
