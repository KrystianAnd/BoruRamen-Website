# 🍜 BoruRamen – Ramen Restaurant

<p align="right">
<a href="README.md">🇵🇱 Polish</a> | 🇬🇧 English
</p>

**BoruRamen** is a bilingual ramen restaurant website built with Django.  
The project is hosted on mydevil.net and publicly accessible.

## 🔗 Live demo

👉 [boruramen.pl](https://boruramen.pl)

---

## 🧠 Features

- 🌍 Language versions: Polish and English (i18n)
- 🛒 CMS – add/edit content without touching the code
- 🔍 SEO checker (based on django-check-seo)
- 📱 Responsive design (desktop and mobile)

---

## ⚙️ Technologies

- Python 3.12
- Django 5.1.5
- HTML
- CSS
- JavaScript
- SQLite (dev)
- Django CMS + Treebeard
- Hosting: mydevil.net (Linux / Python venv)

---

## 🚀 How to run locally

> ⚠️ To run the project locally, create your own `.env` file with the required variables – for example, a sample `SECRET_KEY` and the `DEBUG` value set to `True` or `False`.

```bash
git clone https://github.com/krystianand/boruramen.git
cd boruramen

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env

python manage.py migrate
python manage.py runserver
