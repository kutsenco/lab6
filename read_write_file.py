"""
In this file i have implemented read file
"""

from typing import List
import urllib.request

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    We are given a link to a file containing students. It is necessary
    to correctly sort this file. The number of students is 77.
    Therefore, the variable num will take the value -int and in
    the range from 0 to 77
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt', 1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt', 2)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt', 0)
    []
    """
    result = []
    with urllib.request.urlopen(url) as file_1 :
        open('total.csv', 'w').close()
        with open('total.csv', 'a', encoding="utf8") as file_2 :
            file_2.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
        file_1.readline()
        file_1.readline()
        while number > 0 :
            number -= 1
            line_result_1 = file_1.readline().decode("utf8").replace('\r\n', '').strip() \
                .replace('До наказу', '+').replace('Рекомендовано (контракт)', '+')
            if line_result_1 == '' :
                break
            line_result_2 = line_result_1.split('\t')[:4]
            while True :
                try :
                    if line_result_2[2] == '+' :
                        break
                except IndexError :
                    line_result_1 = file_1.readline().decode("utf8").replace('\r\n', '').strip() \
                        .replace('До наказу', '+')
                    if line_result_1 == '' :
                        break
                    line_result_2 = line_result_1.split('\t')[:4]
            file_1.readline()
            file_1.readline()
            line_result_1 = file_1.readline().decode("utf8").replace('\r\n', '')
            line_result_1 = line_result_1.split(" ")
            line_result_2 += [line_result_1[6]]
            result.append(line_result_2)
            file_1.readline()
            file_1.readline()
            file_1.readline()
    return result
print(read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt', 5))

def write_csv_file(url: str):
    """
    The results of the first function in a csv file
    """
    csv_result = read_input_file(url, 77)
    with open('total.csv', 'a', encoding="utf8") as file_2 :
        for j in range(len(csv_result)) :
            res = ','.join(csv_result[j]) + '\n'
            file_2.write(res)
print(write_csv_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt'))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
