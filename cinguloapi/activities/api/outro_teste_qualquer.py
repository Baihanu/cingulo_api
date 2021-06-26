import requests
from cinguloapi.activities.models import UserActivity


url = "https://static.cingulo.com/bi/user_activities.json"
response_data = requests.get(url)
data_users = response_data.json()

user_activity = UserActivity()


for i in range(40):
    user_activity.user_id = data_users[i]['id']
    user_activity.activities = data_users[i]['activities']
    user_activity.save()
    user_activity = UserActivity()
