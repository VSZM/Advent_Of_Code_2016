from day6_input import small_inputd6, inputd6
from collections import Counter





def solution(lines, fun):
    letters_at_indices = {}
    for i in range(len(lines.splitlines()[0])):
        letters_at_indices[i] = []
    
    for line in lines.splitlines():
        for i in range(len(line)):
            letters_at_indices[i].append(line[i])
    
    
    
    return ''.join([ fun(Counter(letterList)) for letterList in letters_at_indices.values()])


if __name__ == '__main__':
    print solution(inputd6, lambda counter : counter.most_common()[0][0])
    print solution(inputd6, lambda counter : counter.most_common()[-1][0])