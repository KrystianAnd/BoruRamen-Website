# 🍜 BoruRamen – Restauracja z ramenem


<p align="right">
🇵🇱 Polski | <a href="README.en.md">🇬🇧 English</a>
</p>

**BoruRamen** to dwujęzyczna strona restauracji z ramenem, zbudowana w Django.  
Projekt postawiony na hostingu mydevil.net i dostępny publicznie.


## 🔗 Demo online

👉 [boruramen.pl](https://boruramen.pl)

---

## 🧠 Funkcje

- 🌍 Wersje językowe: polska i angielska (i18n)
- 🛒 CMS – możliwość dodawania treści bez edycji kodu
- 🔍 SEO checker (oparty na django-check-seo)
- 📱 Responsywny design (desktop i mobile)

---

## ⚙️ Technologie

- Python 3.12
- Django 5.1.5
- HTML
- CSS
- JavaScript
- SQLite (dev) 
- CMS Django + Treebeard
- Hosting: mydevil.net (Linux / Python venv)

---

## 🚀 Jak uruchomić lokalnie

> ⚠️ Aby uruchomić projekt lokalnie, utwórz własny plik `.env` z odpowiednimi danymi – np. przykładowym `SECRET_KEY` oraz wartością `DEBUG` ustawioną na `True` lub `False`.

```bash
git clone https://github.com/krystianand/boruramen.git
cd boruramen

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env

python manage.py migrate
python manage.py runserver
