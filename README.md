# Aktavia

Digitale Kanzleiakte – ein Dokumenten- und Aktenmanagementsystem für Anwaltskanzleien.

Eingehende Dokumente werden automatisch klassifiziert, dem passenden Mandat zugeordnet
und auf enthaltene Fristen geprüft. Diktate werden transkribiert und zu strukturierten
Vermerken zusammengefasst. Alle automatischen Vorschläge erfordern menschliche
Bestätigung (Human-in-the-loop), jeder Zugriff wird revisionssicher protokolliert.

## Stack

- **Frontend:** Angular (TypeScript)
- **Backend:** Django + Django REST Framework
- **Datenbank:** PostgreSQL
- **Async-Verarbeitung:** Celery + Redis
- **Infrastruktur:** Docker Compose

## Status

🚧 In Entwicklung.

## Entwicklung starten

```bash
docker compose up -d          # PostgreSQL + Redis
cd backend
source venv/bin/activate
python manage.py runserver    # http://localhost:8000
```