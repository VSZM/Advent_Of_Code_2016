from day2_input import inputd2



numberPad1 = {
    (1, 1) : '1', 
    (1, 2) : '2', 
    (1, 3) : '3', 
    (2, 1) : '4', 
    (2, 2) : '5', 
    (2, 3) : '6', 
    (3, 1) : '7', 
    (3, 2) : '8', 
    (3, 3) : '9'
    }

numberPad2 = {
    (1, 3) : '1', 
    (2, 2) : '2', 
    (2, 3) : '3', 
    (2, 4): '4', 
    (3, 1) : '5', 
    (3, 2) : '6', 
    (3, 3) : '7', 
    (3, 4) : '8', 
    (3, 5) : '9', 
    (4, 2) : 'A', 
    (4, 3) : 'B', 
    (4, 4) : 'C', 
    (5, 3) : 'D', 
    }

stepToMovement = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}

def solution(numberPad):
    position = (2, 2)
    code = []
    for line in inputd2.split('\n'):
        for step in line:
            movement = stepToMovement[step]
            would_be_position = position[0] + movement[0], position[1] + movement[1]
            if would_be_position in numberPad.keys():
                position = would_be_position
        code.append(numberPad[position])    
    return "".join(code)


if __name__ == '__main__':
    print solution(numberPad1)
    print solution(numberPad2)
