import numpy as np

#распараллелить умножение x4
#распараллелить сложение ч2


def convert(n, p=2, q=10):
    D = '0123456789'
    if isinstance(n, str):
        n = float(n, q)
    if n >= p:
        return convert(n // p, p) + D[n % p]
    else:
        return D[n]

def formater(number):
    n = list(convert(number))
    #через lambda переделать
    for i in range(len(n)):
        n[i] = int(n[i])
    return np.array(n)

def primitive_multiplicator(first, sec):
    if sec == 1:
        return first
    else:
        first[first >= 0] = 0
        return first

def sum(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]

    # дополнить числа нулями
    size = max(len(num1), len(num2))

    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))

    # сложить 2 числа
    overflow = 0
    res = []
    for obj in zip(num1, num2):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        res.append(value % 2)

    # если флаг переполнения установлен - добавить бит в начало нового числа
    if overflow == 1:
        res.append(1)

    # перевернуть число назад
    res = res[::-1]

    return(res)

#ебать тут говнокод
#да и похую на этот мп3
def ne_konv(first_numb, sec_numb):
    first_numb, sec_numb = formater(first_numb), formater(sec_numb)
    answ = np.zeros((4,8))
    real_answ = [0, 0, 0, 0, 0, 0, 0, 0]
    a = 0
    otstup = 1
    for i in sec_numb:
        answ[a] = np.concatenate((np.concatenate((np.zeros((1,otstup)), primitive_multiplicator(first_numb, i)), axis=None),np.zeros(4-otstup)), axis=None)  
        a = a + 1
        otstup = otstup + 1
    
    for i in range(answ.shape[0]):
        real_answ = sum(real_answ,answ[i].tolist())
    print(real_answ)

def multipicity_for_4_bits(first_numb, sec_numb):
    first_numb, sec_numb = formater(first_numb), formater(sec_numb)
    answ, a, extra_bit = np.zeros((4,8)), 0, 1
    real_answ = [0, 0, 0, 0, 0, 0, 0, 0]
    #конвейер
    for i in sec_numb:
        #произведение
        answ[a] = np.concatenate((np.concatenate((np.zeros((1,extra_bit)), primitive_multiplicator(first_numb, i)), axis=None),np.zeros(4-extra_bit)), axis=None)
        #сумма
        real_answ = sum(real_answ,answ[a].tolist())  
        a = a + 1
        extra_bit = extra_bit + 1
    return real_answ

print(multipicity_for_4_bits(15,15))