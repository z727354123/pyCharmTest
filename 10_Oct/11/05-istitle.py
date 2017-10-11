myStr = 'Afaf Aasdf 我 Sfsd'
print(myStr.istitle())          # True
myStr = 'Afaf ASDF 我 Sfsd'
print(myStr.istitle())          # False
myStr = 'Afaf Aasdf-Aasd 我 Sfsd'
print(myStr.istitle())          # True
myStr = 'Afaf Aasdf-aasd 我 Sfsd'
print(myStr.istitle())          # False
