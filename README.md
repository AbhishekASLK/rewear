# 👕 ReWear – Community Clothing Exchange

ReWear is a web-based platform that empowers individuals to exchange unused clothing through direct swaps or a point-based redemption system. The mission: reduce textile waste and promote sustainable fashion by giving garments a second life instead of tossing them aside.

## 🚀 Features

- User authentication and dashboard
- Clothing item management and inventory
- Admin panel for moderation
- Point system to encourage fair exchanges
- TailwindCSS-powered UI for a clean and responsive experience

## 🛠️ Getting Started

Follow these instructions to get ReWear up and running locally.

### 📥 Clone the Repository

```bash
git clone https://github.com/your-username/rewear.git
cd rewear
```

## 🧪 Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

## 🏃 Run the Server

uvicorn app.main:app --reload


## 📂 Project Structure

```bash

app/
├── core/
│   ├── config/              # App-wide settings and configs
│   ├── templating/          # Jinja2 templating helpers
│   └── ui/
│       ├── templates/       # HTML templates
│       └── components/      # Reusable UI elements
│
├── modules/
│   ├── admin/               # Admin functionality
│   ├── auth/                # User authentication
│   ├── dashboard/           # User dashboard and metrics
│   └── items_manager/       # Clothing item upload, update, and search
│
└── main.py                  # FastAPI entry point
```

## 🌍 Contribution

Want to help ReWear grow? Contributions are welcome! Whether it’s feature suggestions, UI improvements, or bug fixes — feel free to open an issue or pull request.

## Contributers:

- Abhishek Bhosale
- Chinmay Gokhale
- Swaroop Naik