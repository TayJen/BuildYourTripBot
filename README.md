# BuildYourTripBot
Проект подготовлен в рамках хакатона ODS Pets Projects Hackaton Winter Hack 2022.

## Описание идеи
Задача команды в рамках хакатона стояла в создании чат-бота, который может распознавать достопримечательности по фото и выдавать по ним краткую сводку данных. Это поможет сделать прогулку веселее и познавательнее - больше не придется копаться в интернете в поисках информации о месте, найденном по геолокации.


## Схема работы
- После нажатия кнопки "start" пользователь сохраняется в базу данных
- Загруженная пользователем фотография обрабатывается классификационной моделью (Effiecent Net)
- Для определения фото без достопримечательностей, предусмотренных изначальным набором классов, установлен порог по уровню уверенности модели - если все коэффициенты уверенности ниже заданного числа, фотография не относится ни к одному из заданных классов - эта информация доносится до пользователя
- Если модель достаточно уверенно определила достопримечательность, выдается результат (название достопримечательности и краткая справка)
