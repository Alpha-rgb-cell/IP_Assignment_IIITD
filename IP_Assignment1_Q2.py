def profit(x1, x2, M):
    
  table_profit = 90 if x1 <= M else 100
  chair_profit = 25 if x2 <= M else 30

  return x1 * table_profit + x2 * chair_profit

def assembly_constraint(x1, x2):
  table_labor = 8
  chair_labor = 2
  return x1 * table_labor + x2 * chair_labor

def finishing_constraint(x1, x2):
  table_labor = 2
  chair_labor = 1
  return x1 * table_labor + x2 * chair_labor

max_assembly = 400
max_finishing = 120

max_profit = 0
optimal_tables = 0
optimal_chairs = 0

M = 10

for x1 in range(0, max_assembly//8 + 1):
  for x2 in range(0, max_finishing//2 + 1):
    if assembly_constraint(x1, x2) > max_assembly or finishing_constraint(x1, x2) > max_finishing:
      continue

    curr_profit = profit(x1, x2, M)
    if curr_profit > max_profit:
      max_profit = curr_profit
      optimal_tables = x1
      optimal_chairs = x2

print("Optimal number of tables", optimal_tables)
print("Optimal number of chairs", optimal_chairs)
print("Maximum profit","$",max_profit)