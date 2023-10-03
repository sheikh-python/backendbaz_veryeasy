# def countdown(num):
#     list1=[]
#     for i in range(num+1):
#         list1.append(i)
#     list1.reverse()
#     return list1

# print(countdown(5))

def countdown(num):
    return [*range(num,-1,-1)]
