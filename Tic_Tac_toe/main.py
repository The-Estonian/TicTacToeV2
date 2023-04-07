from grid_switch import grid, box1

def game():
    grid()

def logic():
    game = True
    while game:
        player = input("Box number: ")
        if player == "1":
            box("x")
            grid()
        else:
            box1("o")
            grid()


if __name__ == "__main__":
    logic()

