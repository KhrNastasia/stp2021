import sys
_file_object = None

#перенаправление стандартного вывода в заданный файл
def capture_otput(file="myfile.txt"):
    _file_object = open(file,'w')
    sys.stdout = _file_object

#восстановление стандартного вывода
def restore_output():
    global _file_object
    sys.stdout = sys.__stdout__
    _file_object.close()

#вывод на экран
def print_file(file="myfile.txt"):
    f = open(file, 'r')
    print(f.read())
    f.close()