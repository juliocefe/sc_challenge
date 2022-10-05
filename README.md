# SC_Challenge


## Installation

Start the project

```bash
docker compose -f local.yml up -d
```

## Usage

We need to create a superuser in django, so we can try the example
```bash
docker compose run --rm django python manage.py createsuperuser
```

Answer the prompts with:

```bash
Username (leave blank to use 'root'): stori
Email address: 
Password: Stori12345
Password (again): Stori12345
```

In your browser got to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

In username type: stori

In password type: Stori12345



    
