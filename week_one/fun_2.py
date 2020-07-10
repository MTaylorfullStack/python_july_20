# -   Large Number - Add odd integers from 0 to 500,000, and print the final sum.

# declare a function
# create some variable to store the sum
# build our for loop, up to 500,000
    # if number is odd
        # add it into sum
# print sum

# def large_number():
#     sum = 0
#     for i in range(1,500000,2):
#         sum += i
#         print(sum, "Sum so far")
#     print(sum)

# large_number()


    
    
    
    
    
    
# -   First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

# declare a function, taking a list as a parameter
# return first value (list[0]) + length of the list (len(list))

# def first_plus_length(a_list):
#     return a_list[0] + len(a_list)

# print(first_plus_length([100,2,3,4,5]))



# -   Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

# declare a function, taking a list
# declare sum, min, max
# make our dictionary
# construct a for loop, up to arr.length
    # if value is smaller than min
        # value is min
    # if value is larger than max
        # value is max
    # accumulate sum
# avg = sum/len
# populate dictionary (remember the length)
# return dictionary

# def ultimate_analysis(analyze):
#     sum = 0
#     min = analyze[0]
#     max = analyze[0]
#     return_dict = {}
#     for i in range(len(analyze)):
#         if analyze[i] < min:
#             min = analyze[i]
#         if analyze[i] > max:
#             max = analyze[i]
#         sum += analyze[i]
#     avg = sum/len(analyze)
#     return_dict['max'] = max
#     return_dict['min'] = min
#     return_dict['avg'] = avg
#     return_dict['len'] = len(analyze)
#     return_dict['sum'] = sum
#     return return_dict

def ultimate_analysis(analyze):
    return_dict = {
        'sum': 0,
        'min': analyze[0],
        'max': analyze[0],
        'len': len(analyze)
    }
    for banana in analyze:
        if banana < return_dict['min']:
            return_dict['min'] = banana
        if banana > return_dict['max']:
            return_dict['max'] = banana
        return_dict['sum'] += banana
    return_dict['avg'] = return_dict['sum']/len(analyze)
    return return_dict


print(ultimate_analysis([2,4,6,8,10,12,14]))