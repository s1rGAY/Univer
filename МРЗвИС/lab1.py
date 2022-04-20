import numpy as np

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
'''
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
'''

def get_start_values():
    return np.zeros((4,8)), 0, 1, [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]

def multipicity_for_4_bits(first_numb, sec_numb, third_numb, fouth_numb):
    first_numb, sec_numb, third_numb, fouth_numb = formater(first_numb), formater(sec_numb), formater(third_numb), formater(fouth_numb)
    multip, row, extra_bit, real_answ1, real_answ2 = get_start_values()
    for i in range(len(sec_numb)+1):
        print('такт : '+str(i))
        if i!= (len(sec_numb)):
            multip[row] = np.concatenate((np.concatenate((np.zeros((1,extra_bit)), primitive_multiplicator(first_numb, sec_numb[i])), axis=None),np.zeros(4-extra_bit)), axis=None)
            real_answ1 = sum(real_answ1,multip[row].tolist())
        if row >= 1:
            multip[row-1] = np.concatenate((np.concatenate((np.zeros((1,(extra_bit-1))), primitive_multiplicator(third_numb, fouth_numb[i-1])), axis=None),np.zeros(5-extra_bit)), axis=None)
            real_answ2 = sum(real_answ2,multip[row-1].tolist())
        row = row + 1
        extra_bit = extra_bit + 1
        print('Матрица : ')
        print(multip)
    return real_answ1, real_answ2

print(multipicity_for_4_bits(11,12,14,15))