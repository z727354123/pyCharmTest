# myStr = ''
# # False
# print(myStr.isalpha())
# print(myStr.isdigit())
# print(myStr.isalnum())
# print(myStr.isspace())
# # True
# print(myStr.startswith(''))
# print(myStr.endswith(''))
#
# myStr = '0'
# print(myStr.isalpha())  # False
# print(myStr.isdigit())  # True
# print(myStr.isalnum())  # True  !!!
# print(myStr.isspace())  # False
# print(myStr.startswith(''))     # True
# print(myStr.endswith(''))       # True
#
# myStr = 'z'
# print(myStr.isalpha())  # True
# print(myStr.isdigit())  # False
# print(myStr.isalnum())  # True !!!
# print(myStr.isspace())  # False
# print(myStr.startswith(''))     # True
# print(myStr.endswith(''))       # True


# myStr = ' \t \n\r'
# print(myStr.isspace())  # True

myStr = '10231234'
print(myStr.startswith('1023', 0, len(myStr)))      # True
print(myStr.startswith('1023', 0, 4))               # True
print(myStr.startswith('1023', 0, 3))               # False
print(myStr.startswith('1023', 1, len(myStr)))      # False
print(myStr.startswith('1023', -len(myStr), len(myStr)))        # True
print(myStr.startswith('1023', -len(myStr) + 1, len(myStr)))    # False
