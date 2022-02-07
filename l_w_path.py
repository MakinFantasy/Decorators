from datetime import datetime
import os

def log_writer(directory, file_name):
	file = os.path.join(directory, file_name)
	def wrap(some_func):
		def new_func(*args, **kwargs):
			time = datetime.now()
			now = time.strftime("%d/%m/%Y %H:%M:%S")
			name = some_func.__name__
			result = some_func(*args, **kwargs)
			res = f"Date and time: {now}, name: {name}, args: {args}, kwargs: {kwargs}, result: {result}"
			with open(file, 'w', encoding = 'utf-8') as f:
				f.write(res)
				f.close()
			return result
		return new_func
	return wrap