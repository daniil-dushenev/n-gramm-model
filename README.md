# N-граммная языковая модель 
Этот проект выполнен для вступительного экзамена на курсы ML/DL Тинькофф Обучение.
Перед использованием нужно обучить модель, так как GitHub не дал загрузить большой файл модели. Да и впринципе, не сильно то и нужно.

Файл train.py имеет параметры:
  - --input_dir - путь до папки с текстовыми файлами для обучения, по умолчанию папка "texts"
  - --model - путь до модели, по умолчанию model/model.pickle, если модели не существует, он ее создает.

Файл generate.py имеет параметры:
  - --model - путь до модели, по умолчанию model/model.pickle
  - --prefix - начальное слово для генерации, если не указано, выбирается случайное слово из модели
  - --length - длина генерируемого текста, если не указано - случайное число от 20 до 50
  - --off_sigmoid - если значение 1, отключает применение функции активации сигмоида
  
После обучения модели текстами из папки texts, модель будет разговаривать словами из произведений Пушкина, Толстого, Гоголя, Достоевского и Стивена Кинга(!). Последний автор добавляет интереса к генерируемым фразам. Ниже приведу примеры интересных фраз, которые выдал бот:
   - наполеон все более напоминал ему огромный электронный дом с привидениями где цифровые призраки и перепуганные люди в постоянном напряжении соседствовали друг с другом
   
   ![Аннотация 2022-09-04 180806](https://user-images.githubusercontent.com/44606552/188836983-37bd2071-5a60-42cd-93f8-8b1d93eb5adb.jpg)
   
   ![Аннотация 2022-09-04 181127](https://user-images.githubusercontent.com/44606552/188837083-8e3511a5-1e45-431a-9796-91e29e28ae01.jpg)
   
Тексты я скачивал бесплатно, поэтому проскакивает и такое)

Также замечу, что я добавил параметр отключения функции активации. Без нее текст становится более связаным, но часто модель дает предпочтение вырезкам из текста, то есть проскакивают прямые цитаты из книг. Так не интересно, но иногда получается забавно, когда смешиваются два текста (как на примере с наполеоном). Поэтому решил добавить этот параметр

Если добавить текстов побольше и разнообразнее, модель будет разговаривать получше. Но думаю, сейчас и так вышло неплохо)
