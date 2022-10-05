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

In your browser got to [django admin](http://127.0.0.1:8000/admin)

In username type: stori

In password type: Stori12345

Register an account name and upload file transactions.csv in the accounts formulary

![alt text](https://github.com/juliocefe/sc_challenge/blob/main/accounts.png?raw=true)

After submit the formulary, got to check if transactions were created.

![alt text](https://github.com/juliocefe/sc_challenge/blob/main/transactions.png?raw=true)


To conclude go to [mailhog](http://127.0.0.1:8025), and we are going to see our email there.

Thanks for follow the steps, sorry for the ugly images edition :s


    
