

convert_to_int = lambda value: int(value.replace(',', ''))

print(convert_to_int('12,345'))

# sample function to test
add = lambda x,y: x+y

print(add(2,4))

dict_keys = lambda d: d.keys() if type(d) == dict else 'Invalid Input'


print(dict_keys({'a':1,'b':2}))
print(dict_keys([1,2,4,6,8]))