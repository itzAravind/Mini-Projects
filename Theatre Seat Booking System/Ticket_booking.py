# cinema ticket booking system

seats = []   # empty list to store the seats

# function to display the available seats
def show_seats():
    print("Available seats:")
    for row in seats:
        print(row)

# function to book a seat
def book_seat():
    row = int(input("Enter row number: "))
    seat = int(input("Enter seat number: "))
    if row < 1 or row > len(seats) or seat < 1 or seat > len(seats[0]):
        print("Invalid seat number!")
    elif seats[row-1][seat-1] == "X":
        print("This seat is already booked!")
    else:
        seats[row-1][seat-1] = "X"
        print("Seat booked successfully!")

# initialize the seats
num_rows = int(input("Enter number of rows: "))
num_seats_per_row = int(input("Enter number of seats per row: "))
for i in range(num_rows):
    row = ["O"] * num_seats_per_row
    seats.append(row)

# main loop
while True:
    print("\n1. Show available seats")
    print("2. Book a seat")
    print("3. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_seats()
    elif choice == 2:
        book_seat()
    elif choice == 3:
        break
    else:
        print("Invalid choice!")