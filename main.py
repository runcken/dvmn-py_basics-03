import smtplib
from dotenv import load_dotenv
import os
import base64


load_dotenv()

email_text = """Привет, %friend_name%! %my_name% приглашает тебя на \
сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно \
столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём \
GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о \
релизе сразу на имейл."""

email_text = email_text.replace('%website%', '{website}')
email_text = email_text.replace('%friend_name%', '{friend_name}')
email_text = email_text.replace('%my_name%', '{my_name}')

website = 'https://dvmn.org/profession-ref-program/runcken/O6OOp/'
friend_name = 'Максим'
my_name = 'Runcken'

email_text = email_text.format(website=website, friend_name=friend_name, \
	my_name=my_name)

email_from = os.getenv('SENDER')
email_to = os.getenv('DESTINATION')
subject = "Приглашение!"
encoded_subject = f"=?utf-8?B?{base64.b64encode(subject.encode\
	('utf-8')).decode('utf-8')}?="

letter = """\
From: {sender}
To: {destination}
subject: {encoded_subject}

{email_text}""".format(email_text=email_text, sender=email_from, \
	destination=email_to, encoded_subject=encoded_subject)

letter = letter.encode("UTF-8")

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()