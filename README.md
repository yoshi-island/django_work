# Preperation
Create mysite/mysite/.env
```
SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''
SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''
SOCIAL_AUTH_FACEBOOK_KEY = ''  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = ''  # App Secret
```
DB migration
```
% docker exec -it mysite_web_1 bash
# ./manage.py migrate
```

# Execution
```
% cd mysite/
% docker-compose build
% docker-compose up
```
