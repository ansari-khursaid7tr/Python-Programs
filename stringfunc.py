'''my_string = "DroxElement"
print (my_string[3])            # character at position 3
print (my_string[1:5])         # from position 1 to 5
print (my_string[:5])           # from start to position 5
print (my_string[2:])           # from position 2 to the end
'''

'''print ('*' * 10)
print ('#' * 10)
print ('Hi' * 10)
print ('World' * 5)
print ('DroxElement' * 2)'''

'''title = "Drox Element, Space for Programming"
print ('Source string: ', title)
print ('Split using a space')
print (title.split(' '))
print ('Split using a comma')
print (title.split(','))'''

'''my_string = " D r o x E l e m e n t        "
print ("Total space count = ",my_string.count(' '))'''


'''my_string = "DroxElement"
print (my_string.replace("Element","Programming"))

print ('DroxElement, Space for Programming'.find('Kuhc')) '''



'''msg = 'DroxElement is number ' + str(1)
print (msg)'''


'''print ('DroxElement' == 'DroxElement')   # prints True
print ('DroxElement' == 'ElementDrox')   # prints False
print ('DroxElement' != 'ElementDrox')     # prints True
print ('droxelement' == 'DroxElement')    # prints False '''

my_string = "Drox Element"
print ('Testing a String')
print ('-' * 20)
print ('Original string : ',my_string)
print ('Does the original string starts with "D" ?', my_string.startswith('D'))
print ('Does the original string starts with "d" ?', my_string.startswith('d'))
print ('Does the original string ends with "t" ?', my_string.startswith('t'))
print ('Does the original string ends with "T" ?', my_string.startswith('T'))
print ('Does the original string has title form?', my_string.istitle())
print ('Does the original string is in upper case?', my_string.isupper())
print ('Does the original string is in lower case?', my_string.islower())

print ('String Conversions')
print ('-' * 20)
print ('Original string in upper case : ', my_string.upper())
print ('Original string in lower case : ', my_string.lower())
print ('Original string in title case : ', my_string.title())
print ('Original string in swapcase : ', my_string.swapcase())