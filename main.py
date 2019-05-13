import os, re, argparse
from dotenv import load_dotenv
from instabot import Bot
from pprint import pprint

def get_usernames(text):
  # Code: Regex for Instagram Username and Hashtags
  # https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/

  pattern = re.compile('(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)')
  return pattern.findall(text)


def is_user_exist(bot, username):
  return bool(bot.get_user_id_from_username(username))


def exist_real_users_in_comment(bot, text):
  return bool([username for username in get_usernames(text) if is_user_exist(bot, username)])

def get_users_match_requirements(bot, comments, media_likers, followers):
  users_match_requirements = set()
  for comment in comments:
    if exist_real_users_in_comment(bot, comment["text"]):
      tuple_comment_wrote_user = comment["user_id"], comment["user"]["username"]
      if str(comment["user_id"]) in media_likers and str(comment["user_id"]) in followers:
        users_match_requirements.add(tuple_comment_wrote_user)
  return users_match_requirements


def get_action_participants(link, login, password, username):
  bot = Bot()
  bot.login(username=login, password=password)

  media_id = bot.get_media_id_from_link(link)
  
  followers = bot.get_user_followers(username)
  media_likers = bot.get_media_likers(media_id)
  comments = bot.get_media_comments(media_id)
  winners = get_users_match_requirements(bot, comments, media_likers, followers)
  bot.logout()
  return winners


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

  pprint(get_action_participants(link=link, login=login, password=password, username=username))


if __name__ == "__main__":
  main()