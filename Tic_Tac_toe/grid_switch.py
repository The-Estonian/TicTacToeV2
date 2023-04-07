a = "┌──────────┬──────────┬──────────┐"
b = "│          │          │          │"
c = "│          │          │          │"
d = "│          │          │          │"
e = "│          │          │          │"
f = "├──────────┼──────────┼──────────┤"
g = "│          │          │          │"
h = "│          │          │          │"
j = "│          │          │          │"
k = "│          │          │          │"
m = "├──────────┼──────────┼──────────┤"
n = "│          │          │          │"
p = "│          │          │          │"
q = "│          │          │          │"
r = "│          │          │          │"
s = "└──────────┴──────────┴──────────┘"

b1 = "  ╲  ╱  "
b2 = "   ╲╱   "
b3 = "   ╱╲   "
b4 = "  ╱  ╲  "

a1 = "╭──────╮"
a2 = "│      │"
a3 = "│      │"
a4 = "╰──────╯"

grid_list = [a, b, c, d, e, f, g, h, j, k, m, n, p, q, r, s]
x_pic = [b1, b2, b3, b4]
o_pic = [a1, a2, a3, a4]


def grid():
    print(f"{grid_list[0]}\n{grid_list[1]}\n{grid_list[2]}\n{grid_list[3]}\n{grid_list[4]}\n{grid_list[5]}\n{grid_list[6]}\n{grid_list[7]}\n{grid_list[8]}\n{grid_list[9]}\n{grid_list[10]}\n{grid_list[11]}\n{grid_list[12]}\n{grid_list[13]}\n{grid_list[14]}\n{grid_list[15]}\n")


first_box_coord = [0, 2, 10, 50]
second_box_coord = [0, 13, 21, 50]
third_box_coord = [0, 24, 32, 50]


def box(picture, grid, coord):
    grid[1] = grid[1][coord[0]:coord[1]]+picture[0]+grid[1][coord[2]:coord[3]]
    grid[2] = grid[2][coord[0]:coord[1]]+picture[1]+grid[2][coord[2]:coord[3]]
    grid[3] = grid[3][coord[0]:coord[1]]+picture[2]+grid[3][coord[2]:coord[3]]
    grid[4] = grid[4][coord[0]:coord[1]]+picture[3]+grid[4][coord[2]:coord[3]]
    return grid


if __name__ == "__main__":
    box(x_pic, grid_list, first_box_coord)
    box(x_pic, grid_list, second_box_coord)
    box(x_pic, grid_list, third_box_coord)
    grid()
