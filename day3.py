from day3_input import inputd3

def is_triangle(a, b, c):
    return a + b > c and a < b + c and a + c > b

def first_solution(line_numbers):
    triangle_count = 0
    
    for numbers in line_numbers:
        if is_triangle(numbers[0], numbers[1], numbers[2]):
            triangle_count += 1
            
    return triangle_count

def second_solution(line_numbers):
    triangle_count = 0
    
    for i in range(len(line_numbers)-2)[::3]:
        if (is_triangle(line_numbers[i + 0][0], line_numbers[i + 1][0], line_numbers[i + 2][0])):
            triangle_count += 1
        if (is_triangle(line_numbers[i + 0][1], line_numbers[i + 1][1], line_numbers[i + 2][1])):
            triangle_count += 1
        if (is_triangle(line_numbers[i + 0][2], line_numbers[i + 1][2], line_numbers[i + 2][2])):
            triangle_count += 1
    
    return triangle_count

if __name__ == '__main__':
    line_numbers = [ [ int(item) for item in line.split()]  for line in inputd3.splitlines()]
    
    print first_solution(line_numbers)
    print second_solution(line_numbers)
    
    
    
    
