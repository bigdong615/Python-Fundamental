def binary_Search(search_list: list, search_num: int):
    min_index = 0
    max_index = len(search_list) - 1
    now_index = 0


    while True:
        mid_index = (min_index + max_index) // 2

        if search_num > search_list[mid_index]:
            min_index = mid_index + 1
        elif search_num == search_list[mid_index]:
            print("找到数据", "索引是{}".format(mid_index))
            print("一共查找{}次".format(now_index))
            break
        else:
            max_index = mid_index - 1

        now_index += 1

if __name__ == '__main__':
    list1= [i for i in range(1000)]
    num=5
    binary_Search(list1,num)
