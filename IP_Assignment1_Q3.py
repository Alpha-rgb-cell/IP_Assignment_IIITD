def main():
    x, y = 5.0, 5.0
    total_distance = 0.0
    
    distance = float(input("Enter the distance to travel (0 or less to stop): "))
    
    while distance > 0:
        if distance <= 25:
            y += distance
        elif distance <= 50:
            y -= distance
        elif distance <= 75:
            x += distance
        else:
            x -= distance
        
        total_distance += distance
        
        distance = float(input("Enter the distance to travel (0 or less to stop): "))
    
    straight_line_distance = ((x - 5.0)**2 + (y - 5.0)**2)**(1/2)
    
    print("Final coordinates:", (x, y))
    print("Total distance traveled:", total_distance)
    print("Straight line distance:", straight_line_distance)

if __name__ == "__main__":
    main()