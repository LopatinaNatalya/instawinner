import os, re, argparse, dotenv
from dotenv import load_dotenv
from instabot import Bot
from pprint import pprint

def get_usernames(text):
  pattern = re.compile('(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)')
  return pattern.findall(text)


def is_user_exist(bot, username):
  return bool(bot.get_user_id_from_username(username))


def get_comments(bot, media_id):
  media_comments = bot.get_media_comments(media_id) 

  comments=[]
  for comment in media_comments:
    users={}
    users["text"]=comment["text"]
    users["user_id"]=comment["user_id"]
    users["username"]=comment["user"]["username"]
    comments.append(users)
  return comments


def exist_real_users_in_comment(bot, text):
  usernames = get_usernames(text)
  user_exist=bool()
  for username in usernames:
    user_exist += is_user_exist(bot, username)
  return  user_exist


def get_users_match_requirements(bot, comments, media_likers, followers):
  users_match_requirements = set()
  for comment in comments:
    if exist_real_users_in_comment(bot, comment["text"]):
      tuple_comment_wrote_user = comment["user_id"], comment["username"] 
      if str(comment["user_id"]) in media_likers and str(comment["user_id"]) in followers:
        users_match_requirements.add(tuple_comment_wrote_user)
  return users_match_requirements


def winners(link, login, password, username):
  bot = Bot()
  bot.login(username=login, password=password)

  media_id = bot.get_media_id_from_link(link)
  
  followers = bot.get_user_followers(username)
  media_likers = bot.get_media_likers(media_id)
  comments = get_comments(bot, media_id)

  return get_users_match_requirements(bot, comments, media_likers, followers)


def main():
  load_dotenv()

  login = os.getenv("LOGIN")
  password = os.getenv("PASSWORD")

  parser = argparse.ArgumentParser(
    description='''Поиск победителя конкурса в Инстаграм'''
  )
  parser.add_argument('username', help='Укажите имя пользователя разместившего пост')
  parser.add_argument('link', help='Укажите ссылку на пост')
  args = parser.parse_args()
  username = args.username
  link = args.link

  pprint(winners(link=link, login=login, password=password, username=username))


if __name__ == "__main__":
  main()