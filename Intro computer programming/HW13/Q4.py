def tower_of_hanoi(n, start, end, aux):
    if n == 1:
        print(f"Move disk 1 from tower {start} to tower {end}")
    else:
        tower_of_hanoi(n-1, start, aux, end)
        print(f"Move disk {n} from tower {start} to tower {end}")
        tower_of_hanoi(n-1, aux, end, start)

tower_of_hanoi(3, 'A', 'C', 'B')