from typing import Counter
size=16

def convert(n, p=2, q=10):
    D = '0123456789'
    if isinstance(n, str):
        n = float(n, q)
    if n >= p:
        return convert(n // p, p) + D[n % p]
    else:
        return D[n]
#Done
def input_data(first,second):
    global first_num,second_num
    first_num = first
    second_num = second
    try:
        float(first_num) or int(first_num) and float(second_num) or int(second_num)
    except Exception:
        pass
#Done
def sum_of_positive(first_num, sec_num):
    answer = ["0" for str_code in range(size)]
    overload = 0;
    first_num,sec_num=to_straight_code(first_num),to_straight_code(sec_num)
    for a in range(14):
            a=15-a
            temp_f,temp_s=int(first_num[a]),int(sec_num[a])

            if temp_f+temp_s+overload<2:
                answer[a]=str(temp_f+temp_s+overload)
                overload=0
            elif temp_f+temp_s+overload==2:
                answer[a]='0'
                overload=1
            else:
                answer[a]='1'
                overload=1
    return answer
#Done
def addition(first, second):
    result = ["0" for str_code in range(size)]
    plus_one = False

    for i in range(len(result) - 1,-1,-1):

        temp1,temp2,temp3=True,True,True
        if first[i]!='1':
            temp1=False
        if second[i]!='1':
            temp2=False
        if result[i]!='1':
            temp3=False

        if (temp1 & temp2 & temp3):
            result[i] = '1'
            if (i != 0):
                result[i - 1] = '1'
                
        elif (temp1 ^ temp2 ^ temp3):
            result[i] = '1'
        elif ((temp1 & (temp2 | temp3)) or ((temp1 | temp2) & temp3)):
            result[i] = '0'
            if (i != 0):
                result[i - 1] = '1'
    return result;
#Done
def find_fractional_fl(frac_part):
    frac_part_list = ['0' for i in range(size)]
    frac_part = float('0.' + frac_part)
    frac_part *= 2
    for i in range(size):
        if frac_part > 1:
            frac_part_list[i] = '1'
            frac_part -= 1

        frac_part *= 2

    return frac_part_list    
#Done
def from_list_str_to_str(list):
    s = ''
    for i in range(len(list)):
        s += list[i]
    return s
#Done
def from_str_to_list_str(s):
    l = []
    for i in range(len(s)):
        l.append(s[i])
    return l
#Done
def divide_into_two_parts(fl_num):
    fl_num = str(fl_num)
    
    index = ''
    for i in range(len(fl_num)):
        if fl_num[i] == '.':
            index = i
    
    whole_part = ''
    for i in range(index):
        whole_part += str(fl_num[i])

    frac_part = ''
    for i in range(index + 1, len(fl_num)):
        frac_part += str(fl_num[i])
    

    return whole_part, frac_part
#Done
def bin_sum(num1, num2, loc_size):
    res = ['' for i in range(loc_size)]
    
    overload = 0

    for i in range(loc_size - 1, 0, -1):
        if num1[i] == '1' and num2[i] == '1' and overload > 0:
            res[i] = '1'
        elif num1[i] == '1' and num2[i] == '1' and overload == 0:
            res[i] = '0'
            overload += 1
        elif (num1[i] == '1' or num2[i] == '1') and overload > 0:
            res[i] = '0'
            overload -= 1 
        elif (num1[i] == '1' or num2[i] == '1') and overload == 0:
            res[i] = '1'
        elif (num1[i] == '0' and num2[i] == '0') and overload > 0:
            res[i] = '1'
            overload -= 1
        elif (num1[i] == '0' and num2[i] == '0') and overload == 0:
            res[i] = '0'
    
    res[0] = '0'

    return res



def to_straight_code(number):
    str_code = ["0" for str_code in range(size)] #заполнение 0 при помощи генератора списков

    if number<0:
        number=abs(number)
        str_code[0]="1"

    number=list(str(convert(number))) #перевод в двоичную систему

    for a in range(len(number)):
        str_code[len(str_code)-(a+1)]=number[len(number)-(a+1)]
    return str_code
#Done
def to_reverse_code(number):
    str_code=to_straight_code(number)
    if str_code[0]=="0":
        return str_code
    else:
        for a in range(len(str_code)-1):
            if str_code[a+1]=='0':
                str_code[a+1]='1'
            else:
                str_code[a+1]='0'
        return str_code
#Done
def to_additional_code(number):
    str_code=to_straight_code(number)
    if str_code[0]=="0":
        return str_code
    else:      
        #rev_temp = reverse_code(str_code)
        rev_temp = to_reverse_code(number)
        overload = 1
        a=len(rev_temp)-1
        while overload!=0:
            #вариант с использованием значения перегрузки разряда
            '''
            if a==1 and rev_temp[a]=='1':
                rev_temp[a]='0'
                rev_temp[len(rev_temp)-1]='1'
                overload=0     
            elif rev_temp[a]=='0':
                rev_temp[a]='1'
                overload=0
            elif rev_temp[a]!='0':
                rev_temp[a]='0'  
            a=a-1
            '''

            #вариант через break
            if a==1 and rev_temp[a]=='1':
                rev_temp[a]='0'
                rev_temp[len(rev_temp)-1]='1'
                break
            if rev_temp[a]!='1':
                rev_temp[a]='1'
                break
            if rev_temp[a]=='1':
                rev_temp[a]='0'
                a=a-1
            
        #главной проблемой является переполнение в разрядах
    return rev_temp
#Done
def to_float(num):
    whole_part, frac_part = divide_into_two_parts(num)
    frac_part_list = find_fractional_fl(frac_part)
    frac_part_str = from_list_str_to_str(frac_part_list)
    return  from_list_str_to_str(to_straight_code(int(whole_part))) + '.' + frac_part_str
#Done



def straight_code_operation(first_num, sec_num):
    if int(first_num)>=0 and int(sec_num)>=0:
        return sum_of_positive(first_num,sec_num)
    #Done

    elif int(first_num)<=0 and int(sec_num)>=0 or int(first_num)>=0 and int(sec_num)<=0:
        answer = ["0" for str_code in range(size)]

        if abs(int(first_num))==abs(int(sec_num)):
            answer[0]='0'
        elif abs(int(first_num))>abs(int(sec_num)):
            answer[0]=to_straight_code(first_num)[0]
        else:
            answer[0]=to_straight_code(sec_num)[0]

        if abs(int(first_num))<abs(int(sec_num)): 
            first_num,sec_num=to_straight_code(sec_num),to_straight_code(first_num)
        else:
            first_num,sec_num=to_straight_code(first_num),to_straight_code(sec_num)

        

        for a in range(14):
            a=15-a

            if (int(first_num[a])-int(sec_num[a]))==0:
                answer[a]='0'

            elif int(first_num[a])-int(sec_num[a])==1:
                answer[a]='1'

            elif int(first_num[a])-int(sec_num[a])==-1:
                count=0
                while True:
                    if(int(first_num[a-count])==0):
                        count=count+1
                    else:
                        first_num[a-count]='0'
                        answer[a]='1'
                        for i in range(1,count-1):
                            first_num[a-i]='1'
                        break
        else:
            return answer
    #Done

    else:
        answer=sum_of_positive(abs(first_num),abs(sec_num))
        answer[0]="1"
        return answer
    #Done
#Done
def reverse_code_operation(first_num,sec_num):

    if int(first_num)>=0 and int(sec_num)>=0:
        return sum_of_positive(first_num,sec_num)
    #Done

    elif int(first_num)>0 and int(sec_num)<0 or int(first_num)<0 and int(sec_num)>0:

        temp_first_num,temp_sec_num=to_reverse_code(first_num),to_reverse_code(sec_num)
        answer = ["0" for str_code in range(size)]

        overload=0;
        for a in range(len(answer)):
            a=15-a
            temp_f,temp_s=int(temp_first_num[a]),int(temp_sec_num[a])

            if temp_f+temp_s+overload<2:
                answer[a]=str(temp_f+temp_s+overload)
                overload=0
            elif temp_f+temp_s+overload==2:
                answer[a]='0'
                overload=1
            else:
                answer[a]='1'
                overload=1
        if overload!=0:
            for a in range(len(answer)):
                a=15-a
                temp_f,temp_s=int(temp_first_num[a]),int(temp_sec_num[a])

                if temp_f+temp_s+overload<2:
                    answer[a]=str(temp_f+temp_s+overload)
                    overload=0
                elif temp_f+temp_s+overload==2:
                    answer[a]='0'
                    overload=1
                else:
                    answer[a]='1'
                    overload=1
        return answer
    #Done

    elif int(first_num)<0 and int(sec_num)<0:
        temp_first_num,temp_sec_num=to_reverse_code(first_num),to_reverse_code(sec_num)
        answer = ["0" for str_code in range(size)]
        overload=0;
        for a in range(len(answer)):
            a=15-a
            temp_f,temp_s=int(temp_first_num[a]),int(temp_sec_num[a])

            if temp_f+temp_s+overload<2:
                answer[a]=str(temp_f+temp_s+overload)
                overload=0
            elif temp_f+temp_s+overload==2:
                answer[a]='0'
                overload=1
            else:
                answer[a]='1'
                overload=1
        if overload!=0:
            for a in range(len(answer)):
                a=15-a
                temp_f,temp_s=int(temp_first_num[a]),int(temp_sec_num[a])

                if temp_f+temp_s+overload<2:
                    answer[a]=str(temp_f+temp_s+overload)
                    overload=0
                elif temp_f+temp_s+overload==2:
                    answer[a]='0'
                    overload=1
                else:
                    answer[a]='1'
                    overload=1
        return answer
    #Done
#Done
def additional_code_operation(first_num, sec_num):
    c=False
    if first_num<0 and sec_num<0:
        c=True
    answer = ["0" for str_code in range(size)]

    if abs(int(first_num))==abs(int(sec_num)):
        answer[0]='0'
    elif abs(int(first_num))>abs(int(sec_num)):
        answer[0]=to_straight_code(first_num)[0]
    else:
        answer[0]=to_straight_code(sec_num)[0]

    overload = 0;
    first_num,sec_num=to_additional_code(int(first_num)),to_additional_code(int(sec_num))
    for a in range(15):
            a=15-a
            temp_f,temp_s=int(first_num[a]),int(sec_num[a])
            if temp_f+temp_s+overload<2:
                answer[a]=str(temp_f+temp_s+overload)
                overload=0
            elif temp_f+temp_s+overload==2:
                answer[a]='0'
                overload=1
            else:
                answer[a]='1'
                overload=1
    if c==True:
        answer[0]='1'
    return answer

    '''
    if int(first_num)>=0 and int(second_num)>=0:
        return sum_of_positive(first_num,second_num)

    elif int(first_num)<0 and int(sec_num)>0:
        #просто сложение
        return

    elif int(first_num)>0 and int(sec_num)<0:
        #просто сложение
        return

    elif int(first_num)<0 and int(sec_num)<0:
        #просто сложение
        return
    '''
#Done



#Here you can use DISPATCH 
def multiplication(first_num,sec_num):
    answer = ["0" for str_code in range(size)]
    if first_num<0 or sec_num<0:
        answer[0]='1'
    if first_num<0 and sec_num<0:
        answer[0]='0'
    first_num,sec_num=abs(int(first_num)),abs(int(sec_num))
    if abs(first_num*sec_num)>32767:
        return "You are out of range"
    else:

        temp_len_for_massive = len(convert(sec_num))
        first_num,sec_num=to_straight_code(first_num),to_straight_code(sec_num)

        #двумерный массив заполнен
        for i in range(temp_len_for_massive):

            temp_mas=['0' for str_code in range(size)]
            overload = 0; 

            for a in range(15):
                a=15-a
                temp_mas[a]=int(sec_num[15-i])*int(first_num[a])


                temp_f,temp_s=int(answer[a-i]),int(temp_mas[a])

                if temp_f+temp_s+overload<2:
                    answer[a-i]=str(temp_f+temp_s+overload)
                    overload=0
                elif temp_f+temp_s+overload==2:
                    answer[a-i]='0'
                    overload=1
                else:
                    answer[a-i]='1'
                    overload=1    
        return answer
#Done
def division(first_num, sec_num):

    dividend,divider=to_straight_code(first_num),to_straight_code(sec_num)

    result =[]
    remainder=[]

    first_one_position1, first_one_position2,difference = 0,0,0
    answer = ''

    sign = False
    number = '1'
    sign = int(dividend[0]) ^ int(divider[0])

    if dividend[0]=='1':
	    dividend[0] = '0'

    if divider[0]=='1':
	    divider[0] = '0'

    while True:
	    first_one_position1+=1
	    if dividend[first_one_position1]=='1': break

    while True:
	    first_one_position2+=1
	    if divider[first_one_position2]=='1': break



    difference = first_one_position2 - first_one_position1

    for i in range(difference):
	    divider.append('0')
	    divider.remove(divider[0])

    temp_str=''
    for i in divider:
        temp_str+=i

    divider_additional = to_additional_code(int(temp_str,2)*(-1))
    remainder = addition(dividend, divider_additional)


    if(remainder[0]=='1'):
        number='0'
    else:
        number='1'

    result.insert(0,number)
    null_check=False
    
    next_index = len(remainder) - difference
    if next_index!=0:

        if number=='0':
            remainder = addition(remainder, divider)

        for i in range(difference):
            divider.pop()
            divider.insert(0, '0')
            divider_additional = divider

            temp_str2=''
            for i in divider_additional:
                temp_str2+=i

            divider_additional = to_additional_code(int(temp_str2,2)*(-1))
            number = '1'


            for j in range(len(remainder)):
                if (remainder[j] != remainder[0]):
                    null_check = False
                    break
                null_check = True
			
            #null_check && next_index == remainder.size()-1
            if null_check==True and next_index == (len(remainder)-1):
                number = '0'
                result.append(number)
                break

			
            remainder = addition(remainder, divider_additional)

            if remainder[0]=='1':
                number = '0'
                remainder = addition(remainder, divider)	
            result.append(number)
            next_index+=1
    #ТУТ ВСЁ ВЕРНО
    for i in range(5):
        number = '1'
        null_check = False
        remainder.append('0')
        remainder.remove(remainder[0])

        for i in range(len(remainder)):
            if remainder[i] != remainder[0]:
                null_check=False
                break
            null_check = True

        if null_check==True:
            number = '0'

        remainder = addition(remainder, divider_additional)

        if remainder[0]=='1':
            number = '0'
            remainder = addition(remainder, divider)
           
        result.append(number)

    for i in range(size-len(result)):
        result.insert(0, '0')

    if sign==True:
        answer += "-"

    for i in range(len(result)-5):
        if result[i]=='1':
            answer += '1'
        else:
            answer += '0'

    answer +=','

    for i in range(11,len(remainder)):
        if result[i]=='1':
            answer += '1'
        else:
            answer += '0'
    return answer
#Done
def float_sum(num1, num2):
    num1, num2 = to_float(num1), to_float(num2)
    wh_part_1, fr_part_1 = divide_into_two_parts(num1)

    wh_part_2, fr_part_2 = divide_into_two_parts(num2)
    
    res_wh = bin_sum(from_str_to_list_str(wh_part_1), from_str_to_list_str(wh_part_2), size)#
    res_fr = bin_sum(from_str_to_list_str(fr_part_1), from_str_to_list_str(fr_part_2), size)#
    res = bin_sum(from_str_to_list_str(num1), from_list_str_to_str(num2), size * 2 + 1)#

    for i in range(len(res)):
        if res[i] == '':
            res[i] = '.'

    res1 = from_list_str_to_str(res_wh) + '.' + from_list_str_to_str(res_fr)
    return res1
#Done



print(division(4,5),)
