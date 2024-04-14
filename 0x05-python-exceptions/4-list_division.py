#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_value = []
    for idx in range(list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
            final_value.append(result)
        except TypeError:
            print("wrong type")
            final_value.append(0)
        except ZeroDivisionError:
            print("division by 0")
            final_value.append(0)
        except IndexError:
            print("out of range")
            final_value.append(0)
    return final_value
