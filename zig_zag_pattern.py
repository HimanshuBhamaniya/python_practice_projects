import time, sys
indent = 0
indent_increasing = True

try:
    while True:  # Main program loop
        print(' ' * indent, end= '')
        print('******')
        time.sleep(0.1) # pause for 1/10th of a second.

        if indent_increasing:
            # increase the number of spaces
            indent += 1
            if indent == 20:
                indent_increasing = False
        else:
            # decreasing the number of spaces
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()

