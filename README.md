# test_quiz

Веб сервис на FastAPI выполняющий следующие функции:
Реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}

После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.
Далее, полученные ответы сохраняются в БД, если в БД имеется такой же вопрос, к публичному API с викторинами выполняются дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
Ответом на запрос будет предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

## Пример запроса:

http://127.0.0.1:8000/?questions_number=3

payload = {
    "questions_num": 1
}

Ответ:

{
  "id": 0,
  "question_text": "string",
  "answer_text": "string",
  "create_date": "2023-10-22T07:01:16.916Z"
}

## Инструкция по запуску

