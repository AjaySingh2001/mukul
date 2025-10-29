# # # def repeat(times):
# # #     def decorator(func):
# # #         def wrapper(*args, **kwargs):
# # #             for i in range(times):
# # #                 func(*args, **kwargs)
# # #         return wrapper
# # #     return decorator


# # # @repeat(3)
# # # def hello():
# # #     print("Mukul!")

# # # hello()


# def decorator(fun):
#     def wrapper():
#         print("Before function")
#         fun()
#         print("After function")
#         return fun
#     return wrapper

# @decorator
# def fun():
#     print("All are good")
    
# print(fun())
# print(fun())
# # fun()


# # import sys
# # print(sys.getsizeof({1:"2", 2:"3", 3:"4", 4:"5", 6:"54", 7:"67", 8: "77"}))

