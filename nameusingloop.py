
def name_formation(rows):
    '''It will print name "VAIBHAV"'''
    # Outer loop will print number of rows
    for i in range(1, rows + 1):
        # Inner loop will print number of Astrisk

        # For letter "V"
        for j in range(i):
            print("*", end='')
        print(" " * ((rows - i) * 2), end="")
        for j in range(i):
            print("*", end='')

        print(" " * 2, end="")

        # For letter "A"
        for j in range(rows + 1 - i):
            print("*", end="")
        if i == rows // 2 + 1:
            print("*" * ((i - 1) * 2), end="")
        else:
            print(" " * ((i - 1) * 2), end="")
        for j in range(rows + 1 - i):
            print("*", end="")

        print(" " * 2, end="")

        # For letter "I"
        if i == 2 or i == rows - 1:
            print("*" + " " * (rows - 1), end="")
        elif i > 2 and i < rows - 1:
            if rows % 2 == 0:
                print("*" * (rows // 2) + " " * (rows // 2), end="")
            else:
                print("*" * (rows // 2 + 1) + " " * (rows // 2), end="")
        for j in range(rows):
            if i >= 2 and i <= rows - 1:
                continue
            else:
                print("*", end="")
        if i == 2 or i == rows - 1:
            print(" " * (rows - 1) + "*", end="")
        elif i > 2 and i < rows - 1:
            if rows % 2 == 0:
                print(" " * (rows // 2) + "*" * (rows // 2), end="")
            else:
                print(" " * (rows // 2) + "*" * (rows // 2 + 1), end="")
        for j in range(rows):
            if i >= 2 and i <= rows - 1:
                continue
            else:
                print("*", end="")

        print(" " * 2, end="")

        # For letter "B"
        mid = rows // 2
        if i == 2 or i == rows-1 or i == mid+1:
            print("*", end="")
        for j in range(rows):
            if i == 2 or i == rows-1 or i == mid+1:
                if j < rows - 1:
                    print(" ", end="")
            else:
                if j == 1:
                    if i == 1 or i == rows:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print("*", end="")
        for j in range(rows):
            if i == 2 or i == rows-1 or i == mid+1:
                if j>=rows-2:
                    print("*",end="")
                else:
                    print(" ", end="")
            elif i <mid or i <rows -1 :
                if j==rows-2:
                    if i==1 or i==rows:
                        print("*", end="")
                    else:
                        print(" ",end="")
                else:
                    print("*", end="")
            else:
                print("*", end="")

        print()

if __name__ == '__main__':
    rows_number = int(input("Enter the rows:"))
    name_formation(rows_number)