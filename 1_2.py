from l_w_path import log_writer

f_dir = r"C:\Users\Иван\Desktop\все\Netolgy\Decorators"
f_name = "logs_new.txt"


@log_writer(f_dir, f_name)
def calculator(a, b):
	return a + b


print(calculator(a=7, b=5))
