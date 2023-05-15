# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как запустить

Для запуска сайта вам понадобится [Python третьей версии](https://www.python.org/downloads/)

* Скачайте код с [GitHub](https://github.com/Almaznur1/WMaster)
* Установите зависимости:

```sh
pip install -r requirements.txt
```

* Запустите сайт командой:

```sh
python3 main.py
```

* Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Изменение входных данных

По умолчанию сайт берет данные из файла `wine3.xlsx`, который находится в родительской папке. При необходимости вы можете:

* Изменить файл `wine3.xlsx` и внести в него свои данные

* Указать программе на свой файл, запустив её со следующим аргументом:

```python main.py --drinks_catalog <путь до вашего файла относительно родительской папки>```

Если вы добавили новые напитки, то вам необходимо добавить файл с картинкой напитка в папку `images`


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
