def move_disk(disk, from_peg, to_peg):
    print(f"Move disk {disk} from peg {from_peg} to peg {to_peg}")


def hanoi(n, start, end):
    if n == 1:
        move_disk(1, start, end)
    else:
        spare = 6 - start - end
        hanoi(n - 1, start, spare)
        move_disk(n, start, end)
        hanoi(n - 1, spare, end)


hanoi(3, 1, 2)
# Move disk 1 from peg 1 to peg 2
# Move disk 2 from peg 1 to peg 3
# Move disk 1 from peg 2 to peg 3
# Move disk 3 from peg 1 to peg 2
# Move disk 1 from peg 3 to peg 1
# Move disk 2 from peg 3 to peg 2
# Move disk 1 from peg 1 to peg 2

hanoi(4, 1, 2)
# Move disk 1 from peg 1 to peg 3
# Move disk 2 from peg 1 to peg 2
# Move disk 1 from peg 3 to peg 2
# Move disk 3 from peg 1 to peg 3
# Move disk 1 from peg 2 to peg 1
# Move disk 2 from peg 2 to peg 3
# Move disk 1 from peg 1 to peg 3
# Move disk 4 from peg 1 to peg 2
# Move disk 1 from peg 3 to peg 2
# Move disk 2 from peg 3 to peg 1
# Move disk 1 from peg 2 to peg 1
# Move disk 3 from peg 3 to peg 2
# Move disk 1 from peg 1 to peg 3
# Move disk 2 from peg 1 to peg 2
# Move disk 1 from peg 3 to peg 2
