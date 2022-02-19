# reverse string
def solution(x):
    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])


# print(solution(-12345))
# print(solution(23456))


# average word length
def solution(sentence):
    for p in ",.';?!":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    s = words.index('is')
    return s
    # return round(sum(len(word) for word in words)/len(words),1)


sentence1 = 'Programming is fun'


# print(solution(sentence1))

# add strings
def solution(num1, num2):
    # eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))


num1 = '364'
num2 = '1836'


# print(solution(num1, num2))

def solution(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)

    for i in num1:
        n1 += (ord(i) - ord('0')) * m1
        m1 = m1 // 10

    for i in num2:
        n2 += (ord(i) - ord('0')) * m2
        m2 = m2 // 10

    return str(n1 + n2)


# print(solution(num1, num2))


def sentence(x):
    x = x.split(' ')
    s = x[0][0]
    t = x[1][0]
    r = s + t
    return r


# print(sentence('oyedele yusuff'))

def non_repeating_letter(x):
    x = str(x)
    for i in x:
        if x.count(i) == 1:
            return x.index(i)


# print(non_repeating_letter('barbados'))

def palindrome():
    s = 'radkar'
    i = list(s)
    i.remove('k')
    return i


# print(palindrome())

def solution(sentence):
    (i for i in ',.-@#$')
    # for  in sentence:
    #     t = p.index(p)
    # return t


# print(solution('a,b$c'))


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(str(i)+' fizz buzz')
#     elif i % 5 == 0:
#         print(str(i)+' buzz')
#     elif i % 3 == 0:
#         print(str(i)+' fizz')
#     else:
#         print(i)

def solution():
     p = '@#$&'
     for i in p:
         print(i)
print(solution())


