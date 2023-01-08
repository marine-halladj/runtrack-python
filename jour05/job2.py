def draw_rectangle(width, height):
    if width < 1 or height < 1:
        return 
    
    for row in range(height):
        print('|', end='')
        for column in range(width):
            print('-', end='')

        print()

draw_rectangle(16,4)
