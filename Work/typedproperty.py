String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)

def typedproperty(name, expected_type):
	private_name = '_' + name
	@property
	def prop(self):
		return getattr(self, private_name)

	@prop.setter
	def prop(self, value):
		if not isinstance(value, expected_type):
			raise TypeError(f'Expected {expected_type}')
		setattr(self, private_name, value)
	return prop
