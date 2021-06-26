# Desafio Cingulo API

Repositório para submissão do desafio para Cingulo. 

Você pode conhecer a empresa clicando [aqui](https://www.cingulo.com/).

O teste consiste na implementação de uma api que leia e salve os dados de acesso de usuários.
Você pode acessar os dados utilizados clicando [aqui](https://static.cingulo.com/bi/user_activities.json).

## Para desenvolver:
### Em ambientes linux:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Em ambientes Windows:
```
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Para conferir se o código segue a PEP8:
```
flake8
```