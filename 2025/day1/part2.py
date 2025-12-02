def solve():
    with open('input.txt', 'r') as file:
        content = file.read()
        steps = content.split()
        
        current_position = 50
        zero_click = 0
        
        for step in steps:
            direction = step[0]
            distance = int(step[1:])
            
            # naive approach.. why not?
            while distance > 0:
                if direction == 'L':
                    current_position -= 1
                else:
                    current_position += 1
                if(current_position % 100 == 0):
                    zero_click += 1
                distance -= 1
        
        print(zero_click)
            
    
if __name__ == '__main__':
    solve()    