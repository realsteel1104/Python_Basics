def calculate_total(list1,list2) :

    for i in range(len(list1)):
        list3[i] = list1[i] + list2[i]
    return list3

list12= [1,2,4]
list23= [5,6,7]
list4 = []

list3 = [0] * len(list12)
calculate_total(list12, list23)
print(list3)

def print_length(length_one):
    print(length_one)