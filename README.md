# Flask Educational Project: DateTime & Multi-Page Site

![Flask](https://img.shields.io/badge/Flask-3.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

Educational Flask project developed as part of the "Python with AI" course. Demonstrates fundamental Flask concepts including routing, template rendering, and static file handling.

**Author:** Георгий Белянин (Georgy Belyanin)

## 📚 Project Overview

This repository contains two independent Flask applications:

1. **DateTime Display App** (`task_1_datetime`) — Simple Flask application that shows current date and time
2. **Multi-Page Website** (`task_2_site`) — Flask-powered site with three pages, Bootstrap navigation, and proper template structure

## 🎯 Learning Objectives

- Understanding Flask framework basics
- Working with Jinja2 templating engine
- Organizing Flask project structure (`templates/`, `static/`)
- Implementing routing and URL generation with `url_for()`
- Integrating Bootstrap for responsive design
- Creating dynamic navigation with active page highlighting

## 🗂️ Project Structure

```
.
├── task_1_datetime/              # Task 1: DateTime Display
│   └── app.py                    # Flask app showing current date/time
│
├── task_2_site/                  # Task 2: Multi-Page Site
│   ├── app.py                    # Main Flask application
│   ├── templates/                # HTML templates
│   │   ├── index.html           # Home page
│   │   ├── blog.html            # Blog page
│   │   └── contacts.html        # Contacts page
│   └── static/                   # Static files
│       └── css/
│           └── style.css        # Custom styles
│
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ergon73/Zerocoder-VD04-framework-Flask.git
cd Zerocoder-VD04-framework-Flask
```

2. Create a virtual environment (recommended):
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Applications

#### Task 1: DateTime Display

```bash
cd task_1_datetime
python app.py
```

Open your browser and navigate to: `http://127.0.0.1:5000/`

The page will display the current date and time in Russian format (e.g., "14 декабря 2025, 10:54:41"), which updates on each refresh.

#### Task 2: Multi-Page Site

```bash
cd task_2_site
python app.py
```

Available pages:
- Home: `http://127.0.0.1:5000/`
- Blog: `http://127.0.0.1:5000/blog/`
- Contacts: `http://127.0.0.1:5000/contacts/`

Navigate between pages using the Bootstrap navigation menu at the top.

## 💡 Key Features

### Task 1: DateTime Display
- Real-time date and time display
- Python `datetime` module integration
- Russian date format (e.g., "14 декабря 2025, 10:54:41")
- Clean, formatted output

### Task 2: Multi-Page Site
- **Three interconnected pages** with consistent navigation
- **Bootstrap 5 integration** for responsive design
- **Active page highlighting** in navigation menu
- **Flask templating** with Jinja2
- **Proper static file handling** (CSS)
- **URL generation** using `url_for()` helper

## 🛠️ Technologies Used

- **Backend:** Flask 3.0.0
- **Frontend:** HTML5, CSS3
- **UI Framework:** Bootstrap 5.3.0 (CDN)
- **Template Engine:** Jinja2 (included with Flask)
- **Language:** Python 3.10+

## 📖 Code Highlights

### Routing with Active Page Context

```python
@app.route("/")
def index():
    return render_template("index.html", active_page="index")

@app.route("/blog/")
def blog():
    return render_template("blog.html", active_page="blog")
```

### Dynamic Navigation with Active State

```html
<ul class="nav nav-pills">
    <li class="nav-item">
        <a class="nav-link {% if active_page == 'index' %}active{% endif %}" 
           href="{{ url_for('index') }}">Home</a>
    </li>
    <li class="nav-item">
        <a class="nav-link {% if active_page == 'blog' %}active{% endif %}" 
           href="{{ url_for('blog') }}">Blog</a>
    </li>
</ul>
```

## 📝 Course Context

This project was created as homework for the course **"Python Developer from Scratch with AI"** (Module: Web Development with Flask). 

### Assignment Requirements

**Task 1:** Create a Flask application that displays current date and time on the home page.

**Task 2:** Build a Flask application with:
- Proper project structure (`static/` and `templates/` folders)
- Three HTML pages: index, blog, contacts
- Working navigation menu across all pages
- Content rendered using `render_template()`

## 🎓 What I Learned

- Flask application initialization and configuration
- Flask routing and URL mapping
- Jinja2 template syntax and inheritance concepts
- Working with static files in Flask
- Bootstrap integration for rapid UI development
- Project organization best practices
- Git workflow and version control

## 🔮 Future Enhancements (Not in Scope)

While this is an educational project focused on Flask basics, potential improvements could include:

- Database integration for dynamic blog posts
- User authentication system
- Contact form with email functionality
- Admin panel for content management
- API endpoints for data access
- Deployment to production server

**Note:** These features are beyond the current learning objectives and would be explored in advanced courses.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Course instructors for comprehensive Flask tutorials
- Flask documentation and community
- Bootstrap team for the excellent UI framework

## 👤 Author

**Георгий Белянин (Georgy Belyanin)**

R&D Engineer | DevOps | AI Integration Specialist

## 📧 Contact

For questions or feedback about this educational project:

- **GitHub:** [@ergon73](https://github.com/ergon73)
- **Email:** georgy.belyanin@gmail.com
- **Telegram:** [@Ergon73](https://t.me/Ergon73)

---

**Author:** Георгий Белянин (Georgy Belyanin)  
**Email:** georgy.belyanin@gmail.com  
**Built with ❤️ as part of Python learning journey**
