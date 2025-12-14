# Flask Educational Project: DateTime & Multi-Page Site
# Образовательный проект Flask: Дата/Время и Многостраничный сайт

![Flask](https://img.shields.io/badge/Flask-3.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

---

## 🇷🇺 Русский

Образовательный проект на Flask, разработанный в рамках курса "Python с AI". Демонстрирует основные концепции Flask, включая маршрутизацию, рендеринг шаблонов и работу со статическими файлами.

**Автор:** Георгий Белянин (Georgy Belyanin)

---

## 🇬🇧 English

Educational Flask project developed as part of the "Python with AI" course. Demonstrates fundamental Flask concepts including routing, template rendering, and static file handling.

**Author:** Георгий Белянин (Georgy Belyanin)

---

## 📚 Описание проекта / Project Overview

### 🇷🇺 Русский

Этот репозиторий содержит два независимых Flask-приложения:

1. **Приложение с датой и временем** (`task_1_datetime`) — простое Flask-приложение, отображающее текущие дату и время
2. **Многостраничный сайт** (`task_2_site`) — сайт на Flask с тремя страницами, навигацией Bootstrap и правильной структурой шаблонов

### 🇬🇧 English

This repository contains two independent Flask applications:

1. **DateTime Display App** (`task_1_datetime`) — Simple Flask application that shows current date and time
2. **Multi-Page Website** (`task_2_site`) — Flask-powered site with three pages, Bootstrap navigation, and proper template structure

---

## 🎯 Цели обучения / Learning Objectives

### 🇷🇺 Русский

- Понимание основ фреймворка Flask
- Работа с шаблонизатором Jinja2
- Организация структуры проекта Flask (`templates/`, `static/`)
- Реализация маршрутизации и генерация URL с помощью `url_for()`
- Интеграция Bootstrap для адаптивного дизайна
- Создание динамической навигации с подсветкой активной страницы

### 🇬🇧 English

- Understanding Flask framework basics
- Working with Jinja2 templating engine
- Organizing Flask project structure (`templates/`, `static/`)
- Implementing routing and URL generation with `url_for()`
- Integrating Bootstrap for responsive design
- Creating dynamic navigation with active page highlighting

---

## 🗂️ Структура проекта / Project Structure

```
.
├── task_1_datetime/              # Задание 1: Дата и время / Task 1: DateTime Display
│   └── app.py                    # Flask-приложение с датой/временем / Flask app showing current date/time
│
├── task_2_site/                  # Задание 2: Многостраничный сайт / Task 2: Multi-Page Site
│   ├── app.py                    # Основное Flask-приложение / Main Flask application
│   ├── templates/                # HTML-шаблоны / HTML templates
│   │   ├── index.html           # Главная страница / Home page
│   │   ├── blog.html            # Страница блога / Blog page
│   │   └── contacts.html        # Страница контактов / Contacts page
│   └── static/                   # Статические файлы / Static files
│       └── css/
│           └── style.css        # Пользовательские стили / Custom styles
│
├── requirements.txt              # Зависимости Python / Python dependencies
├── .gitignore                   # Правила игнорирования Git / Git ignore rules
└── README.md                    # Этот файл / This file
```

---

## 🚀 Быстрый старт / Quick Start

### Предварительные требования / Prerequisites

**🇷🇺 Русский:**
- Python 3.10 или выше
- pip (менеджер пакетов Python)

**🇬🇧 English:**
- Python 3.10 or higher
- pip (Python package manager)

### Установка / Installation

1. **Клонировать репозиторий / Clone the repository:**
```bash
git clone https://github.com/ergon73/Zerocoder-VD04-framework-Flask.git
cd Zerocoder-VD04-framework-Flask
```

2. **Создать виртуальное окружение (рекомендуется) / Create a virtual environment (recommended):**
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Установить зависимости / Install dependencies:**
```bash
pip install -r requirements.txt
```

### Запуск приложений / Running the Applications

#### Задание 1: Дата и время / Task 1: DateTime Display

```bash
cd task_1_datetime
python app.py
```

**🇷🇺 Русский:**  
Откройте браузер и перейдите по адресу: `http://127.0.0.1:5000/`

Страница отобразит текущие дату и время в русском формате (например, "14 декабря 2025, 10:54:41"), которые обновляются при каждом обновлении страницы.

**🇬🇧 English:**  
Open your browser and navigate to: `http://127.0.0.1:5000/`

The page will display the current date and time in Russian format (e.g., "14 декабря 2025, 10:54:41"), which updates on each refresh.

#### Задание 2: Многостраничный сайт / Task 2: Multi-Page Site

```bash
cd task_2_site
python app.py
```

**🇷🇺 Русский:**  
Доступные страницы:
- Главная: `http://127.0.0.1:5000/`
- Блог: `http://127.0.0.1:5000/blog/`
- Контакты: `http://127.0.0.1:5000/contacts/`

Перемещайтесь между страницами, используя меню навигации Bootstrap в верхней части страницы.

**🇬🇧 English:**  
Available pages:
- Home: `http://127.0.0.1:5000/`
- Blog: `http://127.0.0.1:5000/blog/`
- Contacts: `http://127.0.0.1:5000/contacts/`

Navigate between pages using the Bootstrap navigation menu at the top.

---

## 💡 Ключевые возможности / Key Features

### Задание 1: Дата и время / Task 1: DateTime Display

**🇷🇺 Русский:**
- Отображение даты и времени в реальном времени
- Интеграция модуля Python `datetime`
- Русский формат даты (например, "14 декабря 2025, 10:54:41")
- Чистый, отформатированный вывод

**🇬🇧 English:**
- Real-time date and time display
- Python `datetime` module integration
- Russian date format (e.g., "14 декабря 2025, 10:54:41")
- Clean, formatted output

### Задание 2: Многостраничный сайт / Task 2: Multi-Page Site

**🇷🇺 Русский:**
- **Три взаимосвязанные страницы** с единой навигацией
- **Интеграция Bootstrap 5** для адаптивного дизайна
- **Подсветка активной страницы** в меню навигации
- **Шаблонизация Flask** с Jinja2
- **Правильная обработка статических файлов** (CSS)
- **Генерация URL** с помощью помощника `url_for()`

**🇬🇧 English:**
- **Three interconnected pages** with consistent navigation
- **Bootstrap 5 integration** for responsive design
- **Active page highlighting** in navigation menu
- **Flask templating** with Jinja2
- **Proper static file handling** (CSS)
- **URL generation** using `url_for()` helper

---

## 🛠️ Используемые технологии / Technologies Used

**🇷🇺 Русский:**
- **Backend:** Flask 3.0.0
- **Frontend:** HTML5, CSS3
- **UI Framework:** Bootstrap 5.3.0 (CDN)
- **Шаблонизатор:** Jinja2 (входит в состав Flask)
- **Язык:** Python 3.10+

**🇬🇧 English:**
- **Backend:** Flask 3.0.0
- **Frontend:** HTML5, CSS3
- **UI Framework:** Bootstrap 5.3.0 (CDN)
- **Template Engine:** Jinja2 (included with Flask)
- **Language:** Python 3.10+

---

## 📖 Примеры кода / Code Highlights

### Маршрутизация с контекстом активной страницы / Routing with Active Page Context

```python
@app.route("/")
def index():
    return render_template("index.html", active_page="index")

@app.route("/blog/")
def blog():
    return render_template("blog.html", active_page="blog")
```

### Динамическая навигация с активным состоянием / Dynamic Navigation with Active State

```html
<ul class="nav nav-pills">
    <li class="nav-item">
        <a class="nav-link {% if active_page == 'index' %}active{% endif %}" 
           href="{{ url_for('index') }}">Главная</a>
    </li>
    <li class="nav-item">
        <a class="nav-link {% if active_page == 'blog' %}active{% endif %}" 
           href="{{ url_for('blog') }}">Блог</a>
    </li>
</ul>
```

---

## 📝 Контекст курса / Course Context

**🇷🇺 Русский:**  
Этот проект был создан в качестве домашнего задания для курса **"Python Developer from Scratch with AI"** (Модуль: Веб-разработка с Flask).

### Требования задания

**Задание 1:** Создать Flask-приложение, которое отображает текущие дату и время на главной странице.

**Задание 2:** Построить Flask-приложение с:
- Правильной структурой проекта (папки `static/` и `templates/`)
- Тремя HTML-страницами: index, blog, contacts
- Рабочим меню навигации на всех страницах
- Контентом, отображаемым с помощью `render_template()`

**🇬🇧 English:**  
This project was created as homework for the course **"Python Developer from Scratch with AI"** (Module: Web Development with Flask).

### Assignment Requirements

**Task 1:** Create a Flask application that displays current date and time on the home page.

**Task 2:** Build a Flask application with:
- Proper project structure (`static/` and `templates/` folders)
- Three HTML pages: index, blog, contacts
- Working navigation menu across all pages
- Content rendered using `render_template()`

---

## 🎓 Что я изучил / What I Learned

**🇷🇺 Русский:**
- Инициализация и настройка Flask-приложения
- Маршрутизация Flask и сопоставление URL
- Синтаксис шаблонов Jinja2 и концепции наследования
- Работа со статическими файлами в Flask
- Интеграция Bootstrap для быстрой разработки UI
- Лучшие практики организации проекта
- Рабочий процесс Git и контроль версий

**🇬🇧 English:**
- Flask application initialization and configuration
- Flask routing and URL mapping
- Jinja2 template syntax and inheritance concepts
- Working with static files in Flask
- Bootstrap integration for rapid UI development
- Project organization best practices
- Git workflow and version control

---

## 🔮 Будущие улучшения (не входят в область проекта) / Future Enhancements (Not in Scope)

**🇷🇺 Русский:**  
Хотя это образовательный проект, сфокусированный на основах Flask, потенциальные улучшения могут включать:

- Интеграцию базы данных для динамических записей блога
- Систему аутентификации пользователей
- Контактную форму с функциональностью отправки email
- Панель администратора для управления контентом
- API-эндпоинты для доступа к данным
- Развертывание на production-сервере

**Примечание:** Эти функции выходят за рамки текущих целей обучения и будут изучены в продвинутых курсах.

**🇬🇧 English:**  
While this is an educational project focused on Flask basics, potential improvements could include:

- Database integration for dynamic blog posts
- User authentication system
- Contact form with email functionality
- Admin panel for content management
- API endpoints for data access
- Deployment to production server

**Note:** These features are beyond the current learning objectives and would be explored in advanced courses.

---

## 📄 Лицензия / License

**🇷🇺 Русский:**  
Этот проект с открытым исходным кодом доступен под лицензией [MIT License](LICENSE).

**🇬🇧 English:**  
This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Благодарности / Acknowledgments

**🇷🇺 Русский:**
- Преподавателям курса за подробные уроки по Flask
- Документации Flask и сообществу
- Команде Bootstrap за отличный UI-фреймворк

**🇬🇧 English:**
- Course instructors for comprehensive Flask tutorials
- Flask documentation and community
- Bootstrap team for the excellent UI framework

---

## 👤 Автор / Author

**Георгий Белянин (Georgy Belyanin)**

R&D Engineer | DevOps | AI Integration Specialist  
R&D инженер | DevOps | Специалист по интеграции AI

---

## 📧 Контакты / Contact

**🇷🇺 Русский:**  
По вопросам или отзывам об этом образовательном проекте:

- **GitHub:** [@ergon73](https://github.com/ergon73)
- **Email:** georgy.belyanin@gmail.com
- **Telegram:** [@Ergon73](https://t.me/Ergon73)

**🇬🇧 English:**  
For questions or feedback about this educational project:

- **GitHub:** [@ergon73](https://github.com/ergon73)
- **Email:** georgy.belyanin@gmail.com
- **Telegram:** [@Ergon73](https://t.me/Ergon73)

---

**Автор / Author:** Георгий Белянин (Georgy Belyanin)  
**Email:** georgy.belyanin@gmail.com  
**Создано с ❤️ в рамках изучения Python / Built with ❤️ as part of Python learning journey**
