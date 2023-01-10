import math
a = int(input("Start time: "))
b = int(input("End time: "))

def distance_covered(a, b, delta):
  distance = 0
  t = a
  while t <= b:
    velocity_t = 2000 * math.log((140000) / (140000 - 2100 * t)) - 9.8 * t
    velocity_t_delta = 2000 * math.log((140000) / (140000 - 2100) * (t + delta)) - 9.8 * (t + delta)
    average_velocity = (velocity_t + velocity_t_delta) / 2
    distance_delta = average_velocity * delta
    distance += distance_delta
    t += delta
  return distance
delta = 0.25

distance = distance_covered(a, b, delta)
print("The distance covered between time", a, "and", b , "is", distance)

