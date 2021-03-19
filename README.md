
в main.py - тестовое на Python, в README - тестовое на SQL и ссылка на тестовое на Excel

https://docs.google.com/spreadsheets/d/1jn61ulm3pTYcUIQpLpVgDOHmDYl7zstKfGJ_it554Q4/edit?usp=sharing - Excel

SQL:

Задание 1
Выведите список уникальных id игроков, совершивших платеж на уровне 30.

SELECT user_id 
FROM DATA 
WHERE user_level=30

Задание 2
Для каждой игры найдите ее суммарный доход в разбивке на уровень игрока.
Назовите колонку с суммарным доходом “revenue”. 
Отсортируйте уровни по убыванию дохода внутри каждой игры.

ALTER TABLE DATA ADD COLUMN revenue integer
SELECT title, user level, SUM(payment_value) AS revenue
FROM DATA
GROUP BY title, user_level
ORDER BY sum41 DESC


Задание 3
Выведите список игр с суммарным доходом выше среднего (среднее считается по всем 10 играм).

SELECT title 
FROM DATA
WHERE SUM(payment_value)>
	(SELECT AVG 
		(SELECT SUM(payment_value) FROM DATA GROUP BY title) 
	FROM DATA)
GROUP BY title

Задание 4
Для каждого сегмента найдите суммарный доход от всех платежей, совершенных игроками в день установки.

SELECT USERS.segment, SUM(DATA.payment_value)  AS sum42
FROM USERS, DATA
WHERE DATA.payment_date=USERS.install_date
GROUP BY USERS.segment
