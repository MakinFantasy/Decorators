from datetime import datetime


def log_writer(some_func):
	def new_func(*args, **kwargs):
		time = datetime.now()
		now = time.strftime("%d/%m/%Y %H:%M:%S")
		name = some_func.__name__
		result = some_func(*args, **kwargs)
		res = f"Date and time: {now}, name: {name}, args: {args}, kwargs: {kwargs}, result: {result}"
		with open("logs.txt", 'w', encoding = 'utf-8') as f:
			f.write(res)
			f.close()
		return "Логи успешно обновлены"
	return new_func
