# Health Calculator Microservice

Microservice Python (Flask) pour calculer le BMI et BMR, déployé sur Azure avec CI/CD.

## 📌 Fonctionnalités
- **BMI** : Calcul d'Indice de Masse Corporelle
- **BMR** : Calcul du Métabolisme de Base (Harris-Benedict)
- Déploiement automatisé via GitHub Actions

## 🔧 Prérequis
- Python 3.9+
- Docker (pour le build local)
- Compte Azure (pour le déploiement)
- GitHub Secrets configurés (`AZUREAPPSERVICE_PUBLISHPROFILE_...`)

## 🚀 Déploiement Local

### 1. Avec Docker
```bash
docker build -t health-calculator .
docker run -dp 5000:5000 --name health-app health-calculator
2. Sans Docker
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac | venv\Scripts\activate (Windows)
pip install -r requirements.txt
python app.py
🌐 Endpoints API
POST /bmi
Paramètres (JSON):

json
{
  "height": 1.75,  // en mètres
  "weight": 70     // en kg
}
Réponse:

json
{"bmi": 22.86}
POST /bmr
Paramètres (JSON):

json
{
  "height": 175,   // en cm
  "weight": 70,    // en kg
  "age": 30,       // en années
  "gender": "male" // "male" ou "female"
}
Réponse:

json
{"bmr": 1695.67}
🔄 CI/CD (GitHub Actions)
Workflow déclenché sur push vers main :

Build :

Installe Python 3.13

Crée un virtualenv

Installe les dépendances

Zip l'artefact

Deploy :

Déploie sur Azure Web App (Health-App)

Utilise le profil de publication stocké dans GitHub Secrets

yaml
name: Build and deploy Python app to Azure Web App - Health-App
on:
  push:
    branches: [main]
  workflow_dispatch:
⚙️ Configuration Azure
Service : Azure App Service (Linux)

Tier : B1 (Gratuit) ou supérieur

URL de production : https://health-app-cddfbebjheergufc.canadacentral-01.azurewebsites.net/

🛠 Structure du Projet
.
├── app.py                # Point d'entrée Flask
├── health_utils.py       # Logique de calcul
├── requirements.txt      # Dépendances
├── Dockerfile            # Configuration Docker
├── .github/workflows/    # CI/CD
│   └── ci-cd.yml        
└── tests/                # Tests unitaires
🧪 Tests
bash
python -m pytest tests/
🔒 Sécurité
HTTPS forcé via configuration Azure

Variables sensibles stockées dans GitHub Secrets