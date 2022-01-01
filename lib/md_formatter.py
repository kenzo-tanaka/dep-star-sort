import configparser
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

class MdFormatter:
  def __init__(self, array) -> None:
      self.array = array

  def display(self):
    result = ''
    for repo in self.array: result += self.__list_row(repo)
    return(result)

  def __list_row(self, repo):
    return(f"- [{self.__repo_name(repo)}・star {self.__star_count(repo)}]({self.__repo_url(repo)})\n")

  def __repo_name(self, repo):
    return(repo[config_ini['DEFAULT']['Repository']].replace('https://github.com/',''))

  def __star_count(self, repo):
    return(repo[config_ini['DEFAULT']['Star']])

  def __repo_url(self, repo):
    return(repo[config_ini['DEFAULT']['Repository']])
