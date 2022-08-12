def draw_triangle():
    m=15
    for i in range(1, m+1, 2):
        print(' ' * ((m-i)//2)+'*'*i)

# основная программа
draw_triangle()