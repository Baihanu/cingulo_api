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
cp env-sample .env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Em ambientes Windows:
```
py -3 -m venv .venv
.venv\Scripts\activate
copy env-sample .env
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Para cadastrar os dados do usuário:
```
python manage.py shell
import request
url = "https://static.cingulo.com/bi/user_activities.json"
response_data = requests.get(url)
data_users = response_data.json()
from cinguloapi.activities.models import UserActivity
for i in range(40):
    user_activity = UserActivity()
    user_activity.user_id = data_users[i]['id']
    user_activity.activities = data_users[i]['activities']
    user_activity.save()
```
O dados referentes ao usuário será visualizado em: localhost:8000/users/