# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lowers yor cost, you should consider quitting smoking")
  else:
    print("Smoking is not an issue for you.")

def analyze_age(current_age):
  if current_age <= 20:
    print("You have the cheapest insurance.")
  elif current_age >= 20 and current_age < 55:
    print("Your insurance will increase as you get older.")
  else:
    print("Your insurance will not increase.")
 
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_age(age)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

andrea_insurance_cost = estimate_insurance_cost(name = 'Andrea', age = 19, sex = 0, num_of_children = 1, smoker = 0)

john_insurance_cost = estimate_insurance_cost(name = 'John', age = 64, sex = 1, num_of_children = 5, smoker = 0)
