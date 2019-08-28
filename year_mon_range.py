#coding:gbk
year_mon_list = []

def year_mon_range(start_year_mon, end_year_mon):
    """
    该函数获取年月
    """
    start_year_str = start_year_mon[0:4]
    start_mon_str = start_year_mon[4:7]

    end_year_str = end_year_mon[0:4]
    end_mon_str = end_year_mon[4:7]

    if int(start_year_mon) > (end_year_mon):
        print 'start_year_mon more than end_year_mon, end!'

    if  start_year_str == end_year_str:
        for item in range(int(start_year_mon), int(end_year_mon) + 1):
            #print(item)
            year_mon_list.append(item)
    else:
        interval_year = int(end_year_str) - int(start_year_str)
        for i in range(0, interval_year + 1):
            if i == 0:
                for j in range(int(start_mon_str), 13):
                    if len(str(j)) == 1:
                        #print(start_year_str + '0' + str(j))
                        year_mon_list.append(int(start_year_str + '0' + str(j)))
                    else:
                       #print(start_year_str + str(j))
                       year_mon_list.append(int(start_year_str + str(j)))
            elif int(start_year_str) + i == int(end_year_str):
                for j in range(1, int(end_mon_str) + 1):
                    if len(str(j)) == 1:
                        #print(end_year_str + '0' + str(j))
                        year_mon_list.append(int(end_year_str + '0' + str(j)))
                    else:
                        #print(end_year_str + str(j))
                        year_mon_list.append(int(end_year_str + str(j)))
            else:
                for j in range(1, 13):
                    if len(str(j)) == 1:
                        #print(str(int(start_year_str) + i) + '0' + str(j))
                        year_mon_list.append(int(str(int(start_year_str) + i) + '0' + str(j)))
                    else:
                        #print(str(int(start_year_str) + i) + str(j))
                        year_mon_list.append(int(str(int(start_year_str) + i) + str(j)))

year_mon_range('201801', '201908')

for i in range(len(year_mon_list)):
    print(year_mon_list[i])


# for i in year_mon_list：
#     print(i)