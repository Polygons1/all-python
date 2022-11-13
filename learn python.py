import time

print('loading program ...')

for wait in range(100):
	print(str(wait) + '%')
	time.sleep(1.5)

print('program started ...')
time.sleep(2)
print('-------menu-------')
time.sleep(1)
print('variables: 1')
time.sleep(1)
print('string: 2')
time.sleep(1)
print('functions: 3')

chapter = input('\nwhat do you choose? (number) ')

if chapter == '1':
	print('chapter 1: variables')
	print('to create a viriable you need to type: name = input ("string"/ number (1)) test it:')
	