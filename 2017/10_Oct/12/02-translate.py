myStr = 'im string from import component justify content vultr aaa x0zzzZ'
print(str.maketrans('m', 'x'))
print(str.maketrans({97: 117}))
print(myStr.translate(str.maketrans('a', 'x', 'o')))
print(myStr.translate(str.maketrans({97: 117, 109: 117})))
