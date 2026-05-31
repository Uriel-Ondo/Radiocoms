# 📡 Radiocoms - Calculatrice RF pour Liaisons Hertziennes

Une application web complète de calcul des paramètres RF (radiofréquences) pour la conception et l'optimisation de liaisons hertziennes.

## 📋 Table des matières

- [À propos](#à-propos)
- [Fonctionnalités](#fonctionnalités)
- [Paramètres Calculés](#paramètres-calculés)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Architecture](#architecture)
- [Formules Mathématiques](#formules-mathématiques)
- [Structure du projet](#structure-du-projet)
- [Licence](#licence)

## 🎯 À propos

**Radiocoms** est une calculatrice RF web dédiée aux télécommunications hertziennes. Elle permet aux ingénieurs réseau et techniciens en radiocommunications de :
- Calculer l'atténuation en espace libre (FSL - Free Space Loss)
- Déterminer la marge libre d'une liaison
- Calculer le rayon de Fresnel
- Déterminer les hauteurs optimales des pylônes
- Évaluer la qualité de la liaison radio

L'application fournit une interface simple et intuitive pour effectuer ces calculs essentiels à la mise en place de liaisons radio fiables.

## ✨ Fonctionnalités

### Calculs RF
1. **Atténuation en Espace Libre (FSL)**
   - Formule standard de Friis
   - Basée sur la fréquence et la distance
   - Résultat en décibels (dB)

2. **Marge Libre**
   - Évaluation de la performance de la liaison
   - Compte tenu de la puissance d'émission (PIRE)
   - Gain d'antenne réception et sensibilité du récepteur

3. **Rayon de Fresnel**
   - Calcul de la zone de Fresnel
   - Essentiel pour le dégagement optimal de la liaison
   - Résultat en mètres

4. **Hauteurs des Pylônes**
   - Calcul des hauteurs nécessaires pour les sites A et B
   - Dégagement du rayon de Fresnel
   - Prise en compte de l'altitude et des bâtiments

5. **Qualité de la Liaison**
   - Classification automatique en fonction de la marge libre
   - **< 15 dB** : Liaison non optimale
   - **15-30 dB** : Liaison bonne
   - **> 30 dB** : Liaison excellente

### Interface Web
- Formulaire intuitif avec 13 paramètres d'entrée
- Validation des données en temps réel
- Protection CSRF intégrée
- Affichage détaillé des résultats
- Design responsive avec CSS personnalisé

## 📊 Paramètres Calculés

### Entrées Requises

| Paramètre | Unité | Description |
|-----------|-------|-------------|
| Fréquence | MHz | Fréquence de la liaison radio |
| Distance | Km | Distance entre les deux sites |
| PIRE | dBm | Puissance Isotrope Rayonnée Équivalente |
| Rxgain | dBi | Gain de l'antenne réceptrice |
| Sensibilité | dBm | Sensibilité minimale du récepteur |
| Distance1 | m | Distance du point A à l'obstacle |
| Distance2 | m | Distance de l'obstacle au point B |
| Altitude obstacle | m | Altitude du terrain/obstacle |
| Hauteur obstacle | m | Hauteur de l'obstacle (optionnel) |
| Altitude site A | m | Altitude du bâtiment A |
| Hauteur bâtiment A | m | Hauteur de la structure A |
| Altitude site B | m | Altitude du bâtiment B |
| Hauteur bâtiment B | m | Hauteur de la structure B |

### Résultats

| Résultat | Unité | Signification |
|----------|-------|---------------|
| FSL | dB | Atténuation en espace libre |
| Marge libre | dB | Marge de sécurité de la liaison |
| Rayon de Fresnel | m | Zone de dégagement requise |
| Hauteur pylône A | m | Hauteur minimale pour le site A |
| Hauteur pylône B | m | Hauteur minimale pour le site B |
| Qualité de liaison | Texte | Évaluation qualitative |

## 📦 Prérequis

- **Python 3.8+**
- **Flask 3.0+** : Framework web
- **Flask-WTF** : Gestion des formulaires avec protection CSRF
- **WTForms** : Formulaires avec validation
- **Flask-Bootstrap** : Framework CSS
- Navigateur web moderne

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Uriel-Ondo/Radiocoms.git
cd Radiocoms
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Ou pour une installation minimale :
```bash
pip install Flask Flask-WTF WTForms Flask-Bootstrap
```

## ⚙️ Configuration

### Variables d'Environnement

Pour la production, configurez une clé secrète sécurisée :

```bash
# Créer un fichier .env
echo "SECRET_KEY=votre_clé_très_secrète_ici" > .env
```

Puis modifier `app.py` :
```python
import os
from dotenv import load_dotenv

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))
```

### Configuration Flask

Modifications optionnelles dans `app.py` :

```python
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['JSON_SORT_KEYS'] = False
```

## 🎮 Utilisation

### Lancer l'application

```bash
python app.py
```

L'application sera accessible sur `http://localhost:5000`

### Pas à pas

1. **Accédez à l'application** : Ouvrez http://localhost:5000
2. **Remplissez les paramètres** : Entrez les 13 paramètres RF nécessaires
3. **Cliquez sur "Calculer"** : Lancez les calculs
4. **Consultez les résultats** : Visualisez tous les paramètres calculés
5. **Évaluez la qualité** : Vérifiez le statut de la liaison

### Exemple de Liaison

**Scénario** : Liaison radio entre deux bâtiments à 5 km
- Fréquence : 2400 MHz (WiFi/5G)
- Distance : 5 km
- PIRE : 20 dBm
- Rxgain : 12 dBi
- Sensibilité : -100 dBm
- Distance1/Distance2 : 2500 m chacun
- Altitude obstacle : 100 m
- Altitude site A/B : 50 m
- Hauteur bâtiment : 10 m

**Résultats attendus** :
- FSL ≈ 114 dB
- Marge libre ≈ -82 dB (liaison très mauvaise - aurait besoin d'amplification)
- Rayon Fresnel ≈ 24 m

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              Interface Web (Jinja2 + Bootstrap)             │
│                  templates/index.html                      │
└────────────────────┬────────────────────────────────────────┘
                     │
         HTTP POST (données formulaire)
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Backend Flask (app.py)                         │
│        - Route POST /  - Validation formulaire             │
│        - Récupération des paramètres                       │
└────────────────────┬────────────────────────────────────────┘
                     │
         Appel des fonctions de calcul
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│          Module de Calcul (radiocoms/utils.py)            │
│    - fsl() - margelibre() - rayonfresnel() - longueurpylone()
└────────────────────┬────────────────────────────────────────┘
                     │
         Retour des résultats
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│        Rendu HTML avec résultats et qualité                 │
│              Affichage dans le navigateur                   │
└─────────────────────────────────────────────────────────────┘
```

## 📐 Formules Mathématiques

### 1. Atténuation en Espace Libre (FSL)

```
FSL = 32.44 + 20 × log₁₀(f × d)
```

Où :
- **f** = fréquence en MHz
- **d** = distance en km
- **FSL** = résultat en dB

### 2. Marge Libre

```
Marge Libre = PIRE - FSL + Rxgain - Sensibilité
```

Où :
- **PIRE** = Puissance Isotrope Rayonnée Équivalente (dBm)
- **FSL** = Atténuation en espace libre (dB)
- **Rxgain** = Gain d'antenne réception (dBi)
- **Sensibilité** = Sensibilité du récepteur (dBm)

### 3. Rayon de Fresnel

```
R = 17.31 × √((0.6 × d1 × d2) / ((d1 + d2) × f))
```

Où :
- **d1** = distance du point A à l'obstacle (m)
- **d2** = distance de l'obstacle au point B (m)
- **f** = fréquence (MHz)
- **R** = rayon en mètres

### 4. Longueur du Pylône

```
h_pylône = alt_obstacle + h_obstacle + R_Fresnel - (altitude_site + h_bâtiment)
```

## 📁 Structure du projet

```
Radiocoms/
├── app.py                       # Application Flask principale
├── forms.py                     # Définition du formulaire WTForms
├── radiocoms/
│   └── utils.py                # Fonctions de calcul RF
├── templates/
│   └── index.html              # Interface HTML
├── static/
│   └── style.css               # Feuille de style
├── requirements.txt            # Dépendances Python
├── README.md                   # Ce fichier
├── LICENSE                     # Licence MIT
└── .gitignore                  # Fichiers à ignorer
```

## 🔐 Sécurité

### Protections Intégrées
- ✅ Protection CSRF avec `Flask-WTF`
- ✅ Validation des entrées avec `WTForms`
- ✅ Gestion sécurisée de la clé secrète

### Recommandations pour la Production

⚠️ **Avant de déployer** :
- Changez la clé secrète Flask (utiliser une variable d'environnement)
- Utilisez HTTPS/SSL
- Mettez `debug=False` : `app.run(debug=False)`
- Déployez avec un serveur WSGI (Gunicorn, uWSGI)
- Validez toutes les entrées numériques
- Limitez le taux de requêtes (rate limiting)

### Configuration Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🛠️ Dépannage

### "Module 'radiocoms' not found"
```bash
# Assurez-vous que le dossier radiocoms contient __init__.py
touch radiocoms/__init__.py
```

### Les résultats ne s'affichent pas
- Vérifiez que tous les champs du formulaire sont remplis
- Consultez la console pour les erreurs de validation
- Vérifiez les logs Flask

### Erreur CSRF
- Assurez-vous que `Flask-WTF` est installé
- Vérifiez que `SECRET_KEY` est configurée

## 📊 Exemples d'Utilisation

### Liaison courte distance haute fréquence
```
Fréquence : 5800 MHz
Distance : 1 km
PIRE : 30 dBm
Rxgain : 15 dBi
Sensibilité : -95 dBm
→ Marge libre positive : Liaison possible
```

### Liaison longue distance
```
Fréquence : 800 MHz
Distance : 50 km
PIRE : 40 dBm
Rxgain : 10 dBi
Sensibilité : -105 dBm
→ Nécessite des calculs d'obstruction
```

## 📚 Ressources utiles

- [ITU-R Recommendations](https://www.itu.int/)
- [Free Space Path Loss](https://en.wikipedia.org/wiki/Free-space_path_loss)
- [Fresnel Zone](https://en.wikipedia.org/wiki/Fresnel_zone)
- [RF Calculator Tools](https://www.rfcafe.com/)
- [Radiocommunications - EC2LT](http://ec2lt.fr/)

## 📝 Licence

Ce projet est sous licence **MIT**. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Auteur** : Uriel-Ondo  
**Créé** : Février 2025  
**Dernière mise à jour** : Mars 2026  
**Langage** : Python 3.8+  
**Framework** : Flask 3.0+

### Notes

Cette application est conçue pour les calculs théoriques RF. Pour des déploiements critiques, vérifiez les résultats avec des outils de simulation profesionnels comme MATLAB ou des calculatrices RF certifiées.
