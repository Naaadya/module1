password = input('password:')
while len(password)<8 or password.islower() or password.isupper():
	password = input('incorect password, input new password:')
print('SUCCESS!!!')
