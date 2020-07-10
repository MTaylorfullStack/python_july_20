
# def a():
#     print(1, "Printing one, about to call function b")
#     b()
#     print(2, "Exited function b, finalizing function a")
# def b():
#     print(3, "Just called function b, within function b")
    
# print("About to call the function a")
# a()
# print("Function a has finalized")

#15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

#6
# def a(b,c):
#     print(b+c, "print statement from within the function")
#     return 15
# print("About to call the function, passing in 2 and 3")
# result_one = a(2,3)
# print(f"This is the result: {result_one}")

# print("Calling the function again, passing in 1 and 2")
# result_two = a(1,2)
# print(f"This is the result of second function call: {result_two}")

# print("Adding the results...")
# print(result_one + result_two)

# this is an abstracted version of 29 - 38
# print(a(2,3) + a(1,2))



# Write a function to print any list

def print_list(a_list):
    print(a_list)

print_list([2,4,6,8,10])