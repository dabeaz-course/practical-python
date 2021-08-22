name = input()
authorized = []
if name not in authorized:
	raise RuntimeError(f'{name} not authorized')
	try:
		authenticate(username)
	except RuntimeError as e:
		print(e)
