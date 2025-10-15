# KanMind Backend

## Projekt- & App-Struktur

Das Projekt wurde entsprechend den Anforderungen umstrukturiert:

### Hauptprojekt
- **core** - Das Hauptprojekt
  - `settings.py` - Django-Einstellungen
  - `urls.py` - Haupt-URL-Konfiguration
  - `wsgi.py` - WSGI-Anwendung
  - `asgi.py` - ASGI-Anwendung

### App-Struktur
Alle Apps erhalten sprechende Namen mit Präfix/Suffix und eine standardisierte `api/`-Struktur:

#### auth_app
```
auth_app/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── migrations/
└── api/
    ├── __init__.py
    ├── serializers.py    # DRF Serializers
    ├── views.py         # API Views
    ├── urls.py          # API URL-Konfiguration
    └── permissions.py   # Custom Permissions
```

#### tasks_app
```
tasks_app/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── migrations/
└── api/
    ├── __init__.py
    ├── serializers.py    # DRF Serializers
    ├── views.py         # API Views (ViewSets)
    ├── urls.py          # API URL-Konfiguration
    └── permissions.py   # Custom Permissions
```

### API-Endpunkte

#### Authentifizierung (auth_app)
- `POST /api/auth/register/` - Benutzerregistrierung
- `POST /api/auth/login/` - Benutzeranmeldung
- `POST /api/auth/logout/` - Benutzerabmeldung
- `GET /api/auth/profile/` - Benutzerprofil

#### Tasks (tasks_app)
- `GET /api/tasks/tasks/` - Alle Tasks des Benutzers
- `POST /api/tasks/tasks/` - Neue Task erstellen
- `GET /api/tasks/tasks/{id}/` - Einzelne Task abrufen
- `PUT /api/tasks/tasks/{id}/` - Task aktualisieren
- `DELETE /api/tasks/tasks/{id}/` - Task löschen
- `POST /api/tasks/tasks/{id}/toggle_completed/` - Task-Status umschalten

### Vorteile der neuen Struktur

1. **Klare Trennung**: Der `core`-Ordner ist eindeutig vom Rest der Apps unterscheidbar
2. **Konsistente Benennung**: Alle Apps haben sprechende Namen mit eindeutigen Präfixen/Suffixen
3. **API-Organisation**: Jede App hat einen eigenen `api/`-Ordner mit allen API-bezogenen Dateien
4. **Skalierbarkeit**: Neue Apps können einfach nach dem gleichen Schema hinzugefügt werden
5. **Wartbarkeit**: Klare Struktur erleichtert das Auffinden und Warten von Code

## Installation

```bash
# Virtual Environment aktivieren
source env/bin/activate

# Dependencies installieren
pip install -r requirements.txt

# Migrationen ausführen
python manage.py makemigrations
python manage.py migrate

# Entwicklungsserver starten
python manage.py runserver
```
