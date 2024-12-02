### Project Structure

```
fantasy_sports_league/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── league.py
│   │   ├── team.py
│   │   ├── player.py
│   │   ├── match.py
│   │   ├── draft.py
│   │   ├── trade.py
│   │   ├── event.py
│   │   ├── waiver.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── league.py
│   │   ├── team.py
│   │   ├── player.py
│   │   ├── match.py
│   │   ├── draft.py
│   │   ├── trade.py
│   │   ├── event.py
│   │   ├── waiver.py
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── league.py
│   │   ├── team.py
│   │   ├── player.py
│   │   ├── match.py
│   │   ├── draft.py
│   │   ├── trade.py
│   │   ├── event.py
│   │   ├── waiver.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── league.py
│   │   ├── team.py
│   │   ├── player.py
│   │   ├── match.py
│   │   ├── draft.py
│   │   ├── trade.py
│   │   ├── event.py
│   │   ├── waiver.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   ├── config.py
├── requirements.txt
├── structure DDL.sql
└── endpoints.md
```

### Description of the Structure

- **app/main.py**: The entry point of the application where the FastAPI app is created and routes are included.
- **app/database.py**: Contains the database connection setup.
- **app/models/**: Contains SQLAlchemy models for each table in the database.
- **app/schemas/**: Contains Pydantic models (schemas) for request and response validation.
- **app/crud/**: Contains CRUD operations for each model.
- **app/routes/**: Contains route definitions for each module (user, league, team, etc.).
- **app/utils/**: Contains utility functions and dependencies (e.g., security, authentication).
- **app/config.py**: Contains configuration settings for the application.
- **requirements.txt**: Lists the dependencies required for the project.
- **structure DDL.sql**: Contains the SQL DDL statements for creating the database tables.
- **endpoints.md**: Contains the API endpoint documentation.
