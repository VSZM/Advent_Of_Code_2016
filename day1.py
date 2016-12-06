import math
from day1_input import inputd1





def first_solution():
    direction = 90#in degrees, 90 is north
    instructions = [instructionstr.strip() for instructionstr in inputd1.split(',')]
    x, y = 0, 0
    
    for instruction in instructions:
        if instruction[0] == 'L':
            direction = turn_left(direction)
        else:
            direction =  turn_right(direction)
        motionvector = direction_to_motionvector(direction)    
        xyDelta = motionvector[0] * int(instruction[1:]), motionvector[1] * int(instruction[1:])    
        x += xyDelta[0]
        y += xyDelta[1]
        
    print '{0}, {1}'.format(x, y)
    return abs(x) + abs(y)



def second_solution():
    direction = 90#in degrees, 90 is north
    instructions = [instructionstr.strip() for instructionstr in inputd1.split(',')]
    x, y = 0, 0
    visited_coordinates = [(x,y)]
    
    for instruction in instructions:
        if instruction[0] == 'L':
            direction = turn_left(direction)
        else:
            direction =  turn_right(direction)
        motionvector = direction_to_motionvector(direction)    
        for _ in range(int(instruction[1:])):
            x += motionvector[0]
            y += motionvector[1]
            
            if visited_coordinates.count((x, y)) > 0:
                print '{0}, {1}'.format(x, y)
                return abs(x) + abs(y)
            else:
                visited_coordinates.append((x, y))

def turn_right(direction):
    return direction - 90

def turn_left(direction):
    return direction + 90

def direction_to_motionvector(direction):
    return int(math.cos(math.radians(direction))), int(math.sin(math.radians(direction)))




if __name__ == '__main__':
    print first_solution()
    print second_solution()
    