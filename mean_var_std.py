import numpy as np

def calculate(list_num):
	calculations = {"mean":[], "variance":[], "standard deviation":[], "max":[], "min":[], "sum":[]}
	if len(list_num) < 9:
			raise ValueError("List must contain nine numbers.")
		
	list_num = np.array(list_num).reshape(3,3)
	for i in range(3):
		if i < 2:
			calculations["mean"].append(list(list_num.mean(axis=i)))
			calculations["variance"].append(list(list_num.var(axis=i)))
			calculations["standard deviation"].append(list(list_num.std(axis=i)))
			calculations["max"].append(list(list_num.max(axis=i)))
			calculations["min"].append(list(list_num.min(axis=i)))
			calculations["sum"].append(list(list_num.sum(axis=i)))
		else:
			calculations["mean"].append(list_num.mean())
			calculations["variance"].append(list_num.var())
			calculations["standard deviation"].append(list_num.std())
			calculations["max"].append(list_num.max())
			calculations["min"].append(list_num.min())
			calculations["sum"].append(list_num.sum())

	return calculations

