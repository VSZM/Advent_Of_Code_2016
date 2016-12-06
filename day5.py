import hashlib




def first_solution(inputstr):
    index = 0
    password = ''
    while len(password) < 8:
        hashed = hashlib.md5(inputstr + str(index)).hexdigest()
        if hashed[:5] == '00000':
            password = password + hashed[5]
            print index, password
        index += 1
            
    return password

def second_solution(inputstr):
    index = 0
    password = [ '_' for _ in range(8)]
    valid_indices = [ str(i) for i in range(8)]
    
    while password.count('_') > 0:
        hashed = hashlib.md5(inputstr + str(index)).hexdigest()
        if hashed[:5] == '00000' and valid_indices.count(hashed[5]) > 0 and password[int(hashed[5])] == '_':
            password[int(hashed[5])] = hashed[6]
            print index, password
        index += 1
            
    return ''.join(password)


if __name__ == '__main__':
    print first_solution('ffykfhsq')
    print second_solution('ffykfhsq')
    