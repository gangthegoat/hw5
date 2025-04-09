def read_single_digit(d):
    if d == '0': return "영"
    if d == '1': return "일"
    if d == '2': return "이"
    if d == '3': return "삼"
    if d == '4': return "사"
    if d == '5': return "오"
    if d == '6': return "육"
    if d == '7': return "칠"
    if d == '8': return "팔"
    if d == '9': return "구"

def read_number(num):
    if len(num) == 1:
        return read_single_digit(num[0])
    elif len(num) == 2:
        return read_single_digit(num[0]) + " " + read_single_digit(num[1])
    elif len(num) == 3:
        return read_single_digit(num[0]) + " " + read_single_digit(num[1]) + " " + read_single_digit(num[2])

num = input("세 자리 정수 입력: ")

if 1 <= len(num) <= 3 and all('0' <= c <= '9' for c in num) and num <= '999':
    print(read_number(num))
else:
    print("오류")