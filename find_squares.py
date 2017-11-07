from magic_squares.square import Square

def main():
    s = Square(dimension=4, power=3, max_rand_digits=5)
    s.fill()
    iteration = 1
    while not s.is_magic():
        iteration += 1
        if iteration % 1000000 == 0:
            print(f"Iteration {iteration}")
        s.empty()
        s.fill()
        if s.is_semi_magic():
            print("Semi-magic square")
            print(s)
            print(s.magic_string())
    print("Found magic square")
    print(s)
    print(s.magic_string())

if __name__ == '__main__':
    main()
