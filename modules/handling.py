# 7,4 should be 7.4
def convert_to_dot(decimal):
  decimal = float(decimal.replace(",", "."))
  return decimal

# 25 min should be 25
def extract_minutes(duration):
  time, time_unit = duration.split(" ")
  return convert_to_dot(time)

# S1 and E2 should be 1 and 2
def extract_number(string,flag):
  none, number = string.split(flag)
  return number
