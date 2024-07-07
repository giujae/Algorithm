N = int(input())

def move(num, x, y):

    if(N <= 20):
        if num == 1:
            print(x, y)
            return
        
        move(num-1, x, 6-x-y)
            
        print(x, y)

        move(num-1, 6-x-y, y)

print(2**N -1)
move(N, 1, 3)