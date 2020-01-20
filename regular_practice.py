import  re
'''
pattern = re.compile('^world')
value = 'world, hello'
print(re.search(pattern, value))

pattern = re.compile('^\w\w\w$')
print(re.search(pattern, 'AbF'))
print(re.search(pattern,'sfdrtgf'))

pattern=re.compile('^\d\{2,4}$')
print(re.search(pattern,'123456'))
print(re.search(pattern,'1{2,4}'))

pattern=re.compile('^[abc]+$')
print(re.search(pattern,'abcabccbacba'))
print(re.search(pattern,'abcabccbacbae'))

pattern=re.compile('^hello|world|something$')
pattern=re.compile('^hello|world|something$')'''


pattern=re.compile('^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[012])\.(\d{4})')
result=re.search(pattern,'01.12.2019')
print(re.search(pattern,'45.17.12019'))
print(result.groups())

pattern=re.compile('^\+7-?\d{3}-?\d{3}-?\d{2}-?\d{2}$')
print(re.search(pattern,'+7999-123-77-66'))
print(re.search(pattern,'+79994567898'))

pattern=re.compile('^\d{1-31}\.\d{1-12}\.\d{0-9999}$')
print(re.search(pattern,'01.12.2019'))
print(re.search(pattern,'45.17.12019'))

pattern=re.compile('^#(\d|[A-F]){6}$')
print(re.search(pattern,'#FF42A5'))
print(re.search(pattern,'#GH&*(U'))

pattern=re.compile('hello',re.IGNORECASE | re.DOTALL)
print(re.search(pattern,'helLO'))

print(re.match(pattern,'hello',))
print(re.sub('\s+', ' ','Hello      world   it\'s      me '))

pattern=re.compile('<b>(.*?)<\/b>')
value="<b>hello world</b>Werty<b>tyuhjn</b>"
print(value)
print(re.sub(pattern, '\\1*',value))