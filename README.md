# Pyhaproxy
* Для начала нужно установить виртуальное окружение [тут](https://virtualenv.readthedocs.org/en/latest/installation.html) 
* Создать виртуальное окружение и активировать его:
```bash
$ virtualenv pyhaproxy
$ source pyhaproxy/bin/activate
```
* Выполнить команду для установки пакета "pyhaproxy"
```bash
(pyhaproxy)$ pip install pyhaproxy
```
* config_path - переменная, в которой нужно указать путь к файлу конфигурации HAproxy;
* table_name - переменная, в которой нужно указать имя таблицы.

Запустить скрипт командой:
```bash
(pyhaproxy)$ python3 HAproxyConfigParser.py
```
