# class Snow:
#
#     def __init__(self, num):
#         self.num = num
#
#     def makeSnow(self, snow):
#
#         for i in range(self.num // snow):
#             print('*' * snow)
#
#         print('*' * (self.num % snow))
#
#     def __add__(self, other):
#         if  not isinstance(other, (Snow, int)):
#             raise TypeError('BIM BIM BAM BAM')
#         if isinstance(other, int):
#             return Snow (self.num + other)
#         else:
#             return Snow (self.num + other.num)
#
#     def __sub__(self, other):
#         if  not isinstance(other, (Snow, int)):
#             raise TypeError('BOOM BOOM')
#         if isinstance(other, int):
#             return Snow(self.num - other)
#         else:
#             return Snow (self.num - other.num)
#
#     def __mul__(self, other):
#         if  not isinstance(other, (Snow, int)):
#             raise TypeError('HO HO HO')
#         if isinstance(other, int):
#             return Snow(self.num * other)
#         else:
#             return Snow (self.num * other.num)
#
#     def __floordiv__(self, other):
#         if  not isinstance(other, (Snow, int)):
#             raise TypeError('')
#         if isinstance(other, int):
#             return Snow(self.num // other)
#         else:
#             return Snow (self.num // other.num)
#
#
#
#
# num = Snow(52)
# num.makeSnow(5)
# print()
# num = num // 100
# num.makeSnow(20)
# print()
# pip = Snow(15)
# num = num // pip
# num.makeSnow(23)

class SnowFlake:

    def __init__(self, number):
        self.number = number

    def snow(self):
        k = 0
        st = ''
        for i in range(self.number):
            for j in range(self.number):
                if j == k:
                    st += '*'
                elif self.number - j == k + 1:
                    st += '*'
                elif j == self.number // 2:
                    st += '*'
                elif j == self.number // 2:
                    st += '*'
                else:
                    st += ' '

            print(st)
            st = ''
            k += 1


snow = SnowFlake(15)
snow.snow()
