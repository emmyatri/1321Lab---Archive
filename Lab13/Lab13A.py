#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab13A

def main():

    x = 0
    heatwave_count = 0
    y = 0
    cold_streak = 0


    temps = input("Enter temperatures for each day separated by space: ")
    temperature = [int(x.strip()) for x in temps.split(" ")]

    for i in temperature:
        if i > 30:
            x += 1
        elif x > 2:
            heatwave_count += 1
            x = 0

        if i < 15:
            y += 1
        else:
            y = 0
        if y > cold_streak:
            cold_streak = y
    if x > 2:
        heatwave_count += 1

    print(f"Number of heat waves: {heatwave_count}")
    print(f"Longest cold streak: {cold_streak} days")
    avg = round(sum(temperature)/len(temperature), 2)
    print(f"Average temperature: {avg}°C")






if __name__ == "__main__":
    main()

