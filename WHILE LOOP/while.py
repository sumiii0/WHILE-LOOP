print("Car Suggestion System")
print("=====================")

valid_size = ['small', 'large']
valid_act = ['slow', 'fast']
valid_color = ['grey', 'black']
valid_seat = ['2 seater', '4 seater']

while True:
    size = input(
        "Enter the size of the car you want (small/large):").strip().lower()
    color = input(
        "Enter the color of the car (grey/black):").strip().lower()
    seat = input(
        "Enter the seating capacity (2 seater/4 seater):").strip().lower()
    act = input(
        "Enter the activity of the car (slow/fast):").strip().lower()

    if (
        size in valid_size and
        color in valid_color and
        seat in valid_seat and
        act in valid_act):
        if (
            size == "small" and
            act == "slow" and
            color == "grey" and
            seat == "2 seater"):
            print("A Porsche for you!")
        elif (
            size == "large" and
            act == "fast" and
            color == "black" and
            seat == "4 seater"):
            print("A BMW for you!")
        elif ( 
            size == "small" and
            act == "fast" and 
            color == "grey" and 
            seat == "4 seater"):
            print("A Rolls Royce for you!")
        elif ( 
            size == "large" and
            act == "slow" and 
            color == "black" and 
            seat == "2 seater"):
            print("A Mercedes for you!")
        elif ( 
            size == "large" and
            act == "fast" and 
            color == "grey" and 
            seat == "4 seater"):
            print("A Toyota for you!")
        elif ( 
            size == "small" and
            act == "slow" and 
            color == "grey" and 
            seat == "4 seater"):
            print("A Corolla for you!")
            
        else:
            print("Sorry, no suggestions available for this combination.")
    else:
        print("Invalid input, please try again!")

    rerun = input(
        "Are you satisfied with the suggestion? (y/n): ").strip().lower()
    if rerun == "y":
        print("Thank you!")
        break
    else:
        print("Okay, let's try again!")
        continue