# 🏍️ BLR Riders – Intelligent Rider Companion App

BLR Riders is a cross-platform application designed for motorcycle riders, focused on **group ride coordination, safety, learning, and community building**.  
It brings together **ride planning, real-time GPS tracking, AI-based assistance, rider education, and community features** into a single unified platform.

---

## 🚀 Key Features

- 🗺️ **Ride Hosting & Discovery**  
  Create, host, and discover rides based on distance, destination, bike type, and difficulty.

- 📍 **Real-Time GPS Group Tracking**  
  Track all riders in a group ride on a live map to improve coordination and safety.

- 🤖 **AI Chatbot Assistant**  
  Chatbot support for ride planning, safety FAQs, basic troubleshooting, and app guidance.

- 🦺 **Rider Safety & Learning Module**  
  Structured modules on road safety, group riding etiquette, and basic bike maintenance.

- 👥 **Community & Social Layer**  
  Join groups, participate in events, and interact with other riders.

- 📊 **Behavior-Based Insights (Planned)**  
  Use ride data and patterns to offer personalized recommendations and safety insights.

---

## 🧱 Tech Stack

### Frontend (Web App)
- Streamlit (Python) - For rapid UI development
- Leaflet.js - For interactive maps (free and open-source)
- WebSockets - For real-time updates

### Backend
- FastAPI - Modern, fast web framework for APIs
- PostgreSQL - Relational database
- SQLAlchemy - ORM for database operations
- WebSockets - For real-time communication
- JWT - For authentication

### AI & Services
- Rule-based chatbot with OpenAI API (free tier)
- Mapbox GL JS - For turn-by-turn navigation (free tier available)

### Infrastructure
- Supabase - For database hosting and authentication
- GitHub Actions - For CI/CD pipelines
- Docker - For containerization

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL
- Node.js (for some frontend dependencies)
- Docker (optional)

### Local Development Setup
1. Clone the repository
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables (create a `.env` file):
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/blr_riders
   SECRET_KEY=your-secret-key
   MAPBOX_ACCESS_TOKEN=your-mapbox-token
   ```
5. Run database migrations:
   ```bash
   alembic upgrade head
   ```
6. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
7. Start the Streamlit frontend:
   ```bash
   streamlit run frontend/app.py
   ```

---

## 📂 Project Structure

```
blr-riders/
├── backend/               # FastAPI backend
│   ├── app/               
│   │   ├── api/          # API routes
│   │   ├── core/         # Core configurations
│   │   ├── db/           # Database models and migrations
│   │   ├── schemas/      # Pydantic models
│   │   └── services/     # Business logic
│   ├── tests/            # Backend tests
│   └── requirements.txt  # Python dependencies
│
├── frontend/             # Streamlit frontend
│   ├── app.py           # Main Streamlit app
│   ├── components/      # Reusable UI components
│   └── assets/          # Static files
│
├── .github/              # GitHub Actions workflows
├── docker/               # Docker configurations
├── .env.example         # Example environment variables
└── README.md            # This file
```

---

## 🛠️ Development Workflow

1. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them
3. Push to the branch and create a pull request
4. After code review, merge to `main`

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
- Firebase Auth, Firestore, Cloud Storage, (optional: Realtime Database)

**Backend (API Layer)**  
- FastAPI (Python)  
- RESTful APIs for rides, users, tracking, learning, and chatbot integration  
- Firebase Admin SDK (for auth & data)  
- WebSockets / Firebase Realtime DB for live tracking

**AI & Integrations**  
- Dialogflow / OpenAI API for chatbot  
- Analytics (Firebase Analytics / custom)

---

## 🏗️ High-Level Architecture

- **Flutter App** handles UI, navigation, maps, and user interactions.  
- **FastAPI Backend** exposes REST APIs for:
  - User & ride management  
  - Learning modules  
  - Chatbot proxy  
- **Firebase** manages:
  - Authentication & user identities  
  - Persistent data (users, rides, modules, chats)  
  - Cloud Storage for media  
- **Real-Time Tracking** through:
  - WebSockets (FastAPI) or  
  - Firebase Realtime Database channels for each active ride.

---

## 📂 Project Structure (Suggested)

```bash
BLR-Riders/
├── mobile_app/           # Flutter project
│   ├── lib/
│   └── android/ios/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   └── requirements.txt
└── docs/                 # Diagrams, reports, documentation

BLR-Riders/
│
├── .github/                  # GitHub specific files
│   └── workflows/           # GitHub Actions workflows
│
├── blr_riders/              # Main package
│   ├── __init__.py
│   ├── config/              # Configuration files
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── app/                 # Main application code
│   │   ├── __init__.py
│   │   ├── models/         # Database models
│   │   ├── routes/         # API/View routes
│   │   ├── services/       # Business logic
│   │   └── utils/          # Helper functions
│   │
│   └── tests/              # Test files
│       ├── __init__.py
│       ├── unit/
│       └── integration/
│
├── docs/                    # Documentation
│   ├── api.md
│   └── setup.md
│
├── scripts/                # Utility scripts
│   ├── setup.sh
│   └── deploy.sh
│
├── .env.example           # Example environment variables
├── .gitignore            # Already created
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── setup.py             # Package setup file