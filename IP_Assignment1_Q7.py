def save_for_laptop(cost, allowance, sf, r):
  total_savings = 0
  month = 1
  while total_savings < cost:
    savings = allowance * sf
    total_savings += savings
    total_savings += total_savings * r
    month += 1
  return month, total_savings - cost

cost = int(input("Cost of Laptop: "))
allowance = 20000
sf = 0.1
r = 0.5
months, remaining_savings = save_for_laptop(cost, allowance, sf, r)
