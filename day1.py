import math


input = "L3, R2, L5, R1, L1, L2, L2, R1, R5, R1, L1, L2, R2, R4, L4, L3, L3, R5, L1, R3, L5, L2, R4, L5, R4, R2, L2, L1, R1, L3, L3, R2, R1, L4, L1, L1, R4, R5, R1, L2, L1, R188, R4, L3, R54, L4, R4, R74, R2, L4, R185, R1, R3, R5, L2, L3, R1, L1, L3, R3, R2, L3, L4, R1, L3, L5, L2, R2, L1, R2, R1, L4, R5, R4, L5, L5, L4, R5, R4, L5, L3, R4, R1, L5, L4, L3, R5, L5, L2, L4, R4, R4, R2, L1, L3, L2, R5, R4, L5, R1, R2, R5, L2, R4, R5, L2, L3, R3, L4, R3, L2, R1, R4, L5, R1, L5, L3, R4, L2, L2, L5, L5, R5, R2, L5, R1, L3, L2, L2, R3, L3, L4, R2, R3, L1, R2, L5, L3, R4, L4, R4, R3, L3, R1, L3, R5, L5, R1, R5, R3, L1"



def first_solution():
    direction = 90#in degrees, 90 is north
    instructions = [instructionstr.strip() for instructionstr in input.split(',')]
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
    instructions = [instructionstr.strip() for instructionstr in input.split(',')]
    x, y = 0, 0
    visited_coordinates = [(x,y)]
    
    for instruction in instructions:
        if instruction[0] == 'L':
            direction = turn_left(direction)
        else:
            direction =  turn_right(direction)
        motionvector = direction_to_motionvector(direction)    
        for i in range(int(instruction[1:])):
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
    