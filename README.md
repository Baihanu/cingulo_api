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

#### Para cadastrar os dados do usuário: Copie e cole
##### Os dados referentes aos usuário serão visualizados em: localhost:8000/users/
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

#### Para cadastrar os dados referentes aos acessos mensais:
##### Os dados referentes aos usuário serão visualizados em: localhost:8000/month/
```
from cinguloapi.activities.models import MonthActivity
from cinguloapi.activities.api.monthdailyactivities import jan_data, fev_data, mar_data

month_activity = MonthActivity()
month_activity.name = 'janeiro'
month_activity.activities = jan_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'fevereiro'
month_activity.activities = fev_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'março'
month_activity.activities = mar_data
month_activity.save()

from cinguloapi.activities.api.monthdailyactivities import apr_data, may_data, jun_data

month_activity = MonthActivity()
month_activity.name = 'abril'
month_activity.activities = apr_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'maio'
month_activity.activities = may_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'junho'
month_activity.activities = jun_data
month_activity.save()

from cinguloapi.activities.api.monthdailyactivities import jul_data, aug_data, sep_data

month_activity = MonthActivity()
month_activity.name = 'julho'
month_activity.activities = jul_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'agosto'
month_activity.activities = aug_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'setembro'
month_activity.activities = sep_data
month_activity.save()

from cinguloapi.activities.api.monthdailyactivities import oct_data, nov_data, dec_data

month_activity = MonthActivity()
month_activity.name = 'outubro'
month_activity.activities = oct_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'novembro'
month_activity.activities = nov_data
month_activity.save()

month_activity = MonthActivity()
month_activity.name = 'dezembro'
month_activity.activities = dec_data
month_activity.save()
```

#### Para cadastrar as atividades diárias
##### Os dados referentes as atividades dos usuários serão visualizados em: localhost:8000/daily/
```
from cinguloapi.activities.api.monthdailyactivities import year_data
from cinguloapi.activities.models import DailyActivity
daily_activity = DailyActivity()
daily_activity.name = 'atividades diarias'
daily_activity.activities = year_data
daily_activity.save()
```

### Não está conseguindo visilizar os dados não é mesmo?
#### Você precisa registrar um usuário
##### É só você digitar exatamente o que está abaixo.
```
python manage.py createsuperuser
admin
admin@admin.com
admin
admin
y
```