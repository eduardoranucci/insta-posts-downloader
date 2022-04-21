from instaloader import Instaloader
import instaloader

user = input('Insira seu usuário: ').strip()
password = input('Insira sua senha: ').strip()
target_user = input('Insira o nome do usuário-alvo: ').strip()

insta = Instaloader()
insta.login(user, password)

profile = instaloader.Profile.from_username(insta.context, target_user)

for highlight in insta.get_highlights(profile):

    for item in highlight.get_items():
        insta.download_storyitem(item, target=profile.username)
