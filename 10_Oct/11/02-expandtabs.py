myStr = '1\t12\t123\t1234\t12345\t123456\t'
print(myStr.expandtabs())   # 1       12      123     1234    12345   123456
print(myStr.expandtabs(7))  # 1      12     123    1234   12345  123456
print(myStr.expandtabs(6))  # 1     12    123   1234  12345 123456
print(myStr.expandtabs(5))  # 1    12   123  1234 12345     123456
print(myStr.expandtabs(4))  # 1   12  123 1234    12345   123456
print(myStr.expandtabs(3))  # 1  12 123   1234  12345 123456
print(myStr.expandtabs(2))  # 1 12  123 1234  12345 123456
print(myStr.expandtabs(1))  # 1 12 123 1234 12345 123456
print(myStr.expandtabs(0))  # 112123123412345123456
myStr = '1\t12\t\n123456789\t123456\t'
print(myStr.expandtabs())
# 1       12
# 123456789       123456
print(myStr.expandtabs(10))
# 1         12
# 123456789 123456

