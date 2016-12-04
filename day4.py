from collections import Counter
from day4_input import inputd4
import string


abc = list(string.ascii_lowercase)
roomToFind = 'northpole object storage'

def comparator(a, b):
    if a[1] == b[1]:
        return ord(a[0]) - ord(b[0])
    else:
        return b[1] - a[1]

def is_real_room(line):
    checksum = line[-7:][1:][:-1]
    letters = filter(lambda char: char != '-', line[:-11])
    occurences = Counter(letters)
    valid_checksum = map(lambda item: item[0] , sorted(occurences.items(), cmp=comparator))
    return checksum == "".join(valid_checksum[:5])

def get_room_id(line):
    return int(line[-10:][:3])


def first_solution(lines):
    rooms = filter(is_real_room, lines.splitlines())
    return sum(map(get_room_id, rooms))


def shift(word, roomid):
    return ''.join([chr((ord(letter) + roomid - ord('a')) % len(abc) + ord('a')) for letter in word])
        


def get_name(line):
    encrypted = line[:-11]
    roomid = get_room_id(line)
    encrypted_words = encrypted.split('-')
    return ' '.join(map(lambda word: shift(word, roomid), encrypted_words))

def second_solution(lines):
    rooms = filter(is_real_room, lines.splitlines())
    return get_room_id(filter(lambda room: get_name(room) == roomToFind, rooms)[0])

if __name__ == '__main__':
    print first_solution(inputd4)
    print second_solution(inputd4)
