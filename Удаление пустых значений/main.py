import re

stri = input('введите наподобии [{[], "1": {}, 34243: {}, "adfafdaf": {}, "2": [], 12323: [], "sdfDf": []}]'
             ' кавычки только двойные\n')
re_find_dict_in_key = r'(\ *)(((\d*|\"\d*\"|\"[a-zA-Z]*\")(: {})))(\,*)(\ *)'  #
re_find_list_in_key = r'(\ *)(((\d*|\"\d*\"|\"[a-zA-Z]*\")(: \[\])))(\,*)(\ *)'  #
re_find_empty_list = r'(\ *)(\[\])(\,*)(\ *)'  #
re_find_empty_dict = r'(\ *)(\{\})(\,*)(\ *)'  #
numb_dict, numb_list = 0, 0
work = [0, 0]

while True:
    a = re.search(re_find_dict_in_key, stri)
    b = re.search(re_find_list_in_key , stri)
    if a:
        start, end = a.span()
        stri = stri[:start] + stri[end:]
        numb_dict += 1
    elif b:
        start, end = b.span()
        stri = stri[:start] + stri[end:]
        numb_list += 1
    else:
        a = re.search(re_find_empty_list, stri)
        if a:
            start, end = a.span()
            stri = stri[:start] + stri[end:]
            numb_list += 1
        else:
            a = re.search(re_find_empty_dict, stri)
            if a:
                start, end = a.span()
                stri = stri[:start] + stri[end:]
                numb_dict += 1


    if work != [numb_dict, numb_list]:
        work = [numb_dict, numb_list]
        print(stri)
    else:
        print(work[0], work[1])
        break
