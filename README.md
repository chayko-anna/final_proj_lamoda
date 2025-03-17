# Проект автоматизированного тестирования сайта Lamod

---
## Цели проекта

Основная цель проекта — обеспечить автоматизированное тестирование функциональности
сайта [Lamoda](https://lamoda.ru/). 

---

## Описание

Для создания набора автоматизированных тестов были использованы фреймворки Selene, Allure и Pytest. 
В рамках автоматизированного тестирования проверяется следующая функциональность:

- **Авторизация пользователя**: Проверка процесса входа в систему для веб-версии.
- **Добавление товаров в избранное**: Проверка работы избранного, включая добавление и удаление товаров.
- **Добавление товаров в корзину**: Проверка работы корзины покупок, включая добавление и удаление товаров.

Тестирование осуществляется как для веб-версии, так и для API-тестирования.

После завершения тестирования, результаты автоматически отправляются в **Telegram** для оперативного уведомления команды
о статусе выполнения тестов и выявленных проблемах.

---

## Используемые инструменты

<p align="center">
  <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python Logo" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" alt="Chrome Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/jenkins.png" alt="Jenkins Logo" height="40" width="40" />
  <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" alt="Allure Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/telegram-app.png" alt="Telegram Logo" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" alt="Pytest Logo" height="40" width="40" />
  <img src="https://img.icons8.com/color/48/000000/pycharm.png" alt="PyCharm Logo" height="40" width="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postman/postman-plain.svg" alt="Postman Logo" height="40" width="40" />
</p>

| Инструмент         | Описание                                                                                                                   |
|--------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Selene**         | Обертка над Selenium, облегчающая написание тестов и взаимодействие с веб‑элементами.                                      |
| **Allure**         | Инструмент для создания отчетов о тестировании с поддержкой различных языков.                                              |
| **Allure TestOps** | Расширенная система управления тестированием, интегрируемая с CI/CD и Jira для мониторинга покрытия тестами и аналитики.   |                         |
| **Pytest**         | Фреймворк для написания и запуска тестов. Он предоставляет удобный синтаксис и разнообразные возможности для тестирования. |                               |
| **Postman**        | Инструмент для тестирования API, позволяющий создавать коллекции запросов и проводить автоматизацию API-тестов.            |


---

# Скриншоты

### Отчеты

#### Cтраница тестов Jenkins

![Cтраница тестов Jenkins](https://github.com/yarskii/petrovich/blob/main/resources/screenshots/jenkins_home.png)

Этот скриншот демонстрирует интерфейс Jenkins, где можно запускать тесты с различными параметрами и просматривать их
статус.

#### Общий отчёт Allure

![Общий отчёт Allure](https://github.com/yarskii/petrovich/blob/main/resources/screenshots/allure_reports.png)

Здесь представлен общий отчет Allure, который содержит сводную информацию о результатах выполнения тестов: количество
пройденных, упавших и пропущенных тестов.


### Отчет в Telegram

   <p align="center">
      <img src="https://github.com/yarskii/petrovich/blob/main/resources/screenshots/telegram_report.png" alt="Отчет в Telegram"/>
   </p>

Пример автоматического уведомления в Telegram о результате выполнения тестов.
