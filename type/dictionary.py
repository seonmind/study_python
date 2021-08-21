'''
key-value로 이뤄진 사전 자료
{key:vallue, }
'''
cabinet={'a-1':"수학",'b-2':'영어'}
print(cabinet)
print(cabinet['a-1'])
print(cabinet.get(1,'빔'))
cabinet['c-1']='과학'
print(cabinet)
del cabinet['b-2']
print(cabinet)
print('a-1' in cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
