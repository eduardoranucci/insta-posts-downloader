from datetime import datetime
import instaloader
import pytz

utc = pytz.UTC

user = input('Insira seu usuário: ').strip()
password = input('Insira sua senha: ').strip()
target_user = input('Insira o nome do usuário-alvo: ').strip()

insta = instaloader.Instaloader()
insta.login(user, password)

posts = instaloader.Profile.from_username(insta.context, target_user).get_posts()

#SINCE = datetime(2021, 9, 1).replace(tzinfo=utc)
#UNTIL = datetime(2021, 9, 30).replace(tzinfo=utc)

#for post in posts:
#    if (post.date >= SINCE) and (post.date <= UNTIL):
#        insta.download_post(post, f'{target_user}')

for post in posts:
    insta.download_post(post, target_user)
