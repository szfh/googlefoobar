def solution(cake):
    for n in range(len(cake)):
        slice = cake[:n+1]
        slice_length = len(slice)

        for index, letter in enumerate(slice):
            if (len(cake) == (n + index + 1)):
                return(1)
            elif (letter != cake[n + index + 1]):
                break
            elif (index == slice_length-1) & (slice * (len(cake) // slice_length) == cake):
                return(len(cake) // slice_length)

if __name__ == '__main__':
    s1 = 'abc'*4
    print(solution(s1))
    s2 = 'abccba'*5
    print(solution(s2))
    s3 = 'abccba'*2 + 'abcdeffedcba' *2 + 'abccba' *2
    print(solution(s3))
    s4 = ('abc'*5 + 'cba'*5)*2
    print(solution(s4))
    s5 = 'abc'*4 + 'abcdeffedcba' * 2 + 'abccba' * 2
    print(solution(s5))
    s6 = 'aaaaaa'
    print(solution(s6))
    s7 = 'abcd'
    print(solution(s7))