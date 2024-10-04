import sys

ARGS = sys.argv

def run():
    min = 0
    max = 0

    # Default mode
    if len(ARGS) == 1:
        min = 0
        max = 99

    elif len(ARGS) == 2:

        # Help mode
        if ARGS[1] == 'help':
            print('0 arguments: Displays the first 100 characters.')
            print('1 argument: Displays characters from 0 up to the given number.')
            print('2 arguments: Displays characters from the first number up to the second number.')
            return

        # 0 ~ MAX mode
        if not ARGS[1].isdigit():
            print('Argument must be an integer.')
            return
        min = 0
        max = ARGS[1]

    # MIN to MAX mode
    elif len(ARGS) == 3:
        if not (ARGS[1].isdigit and ARGS[2].isdigit()):
            print('Arguments must be integers.')
            return
        if not int(ARGS[1]) < int(ARGS[2]):
            print('First argument must be less than the second argument.')
            return
        min = ARGS[1]
        max = ARGS[2]

    elif len(ARGS) > 3:
        print('Too many arguments.')
        return

    min = int(min)
    max = int(max)
    characters = []
    for i in range(min, max + 1):
        characters.append((i, chr(i)))

    # format the width of the column based on the max number of digits
    width = len(str(max))

    # print one column for less than 30 characters
    if len(characters) < 30:
        for i in range(min, max + 1):
            print(f"    {i}:".rjust(width + 1), f"{chr(i)}")
    else:
        for i in range(min, max + 1):
            if i % 2 == 0:
                print(f"    {i}:".rjust(width + 1), chr(i), end='')
            else:
                print(f"    {i}:".rjust(width + 1), chr(i), end='\n')
    print('')
    
run()
