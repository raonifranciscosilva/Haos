# def teste(x, y, z=None):
#     return x + y + z

# print(teste(1, 2))

# python function
def main(*num):
    count = 0
    # for loop
    for i in num:
        count += i
    # return value 
    return count
# calling function
print(main(10, 5))