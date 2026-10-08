#persistant data - saved data, data can be used after reload
#also - period data usable in program
#persint data can be saved any known method
with open('text.txt','w',encoding='utf-8') as file:
#создай файл тхт. но если файл есть зашифруй, затри его и запиши текст
#контекстный менеджер называется эта штука
    file.write('Hello!')

file = open('text.txt','w',encoding='utf-8')
file.write('hello stas')
file.close()
#и первая и вторая форма записи делают одно и то же
#по сути виз открывает делает и закрывает ту или иную задачу
#r -read
#w - rewrite
#a - append
#rb, wd, pd pdf screenshot

# how to guide test history file
def log_res(test_name, status):
    with open('test_1.txt','a',encoding='utf-8') as file:
        file.write(f'{test_name}:{status}\n')
#так кароче епта, если нада сохранить дату кудато пишем так
log_res('test_register','PASSED')
log_res('test_login','FAILED')
log_res('test_logout','PASSED')