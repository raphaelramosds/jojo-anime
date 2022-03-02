# Sistema
import time
import sys

sys.path.append("/jojo-dataset/modules")

# Módulos adicionais
from modules import handling

# Webscraping
from selenium import webdriver

# Ir até o site
browser = webdriver.Chrome()
browser.get("https://www.imdb.com/title/tt3277342/?ref_=tt_ep_pr")

# O anime JoJo Bizarre's Adventure tem 152 episodios
episodes = 151

# Prefixo de cada elemento de interesse
prefix = "#__next > main > div > section.ipc-page-background.ipc-page-background--base.MainDetailPageLayout__StyledPageBackground-sc-13rp3wh-0.hsughJ > section > div:nth-child(4) > section > section"

# Array onde ficarão os dados
data = {}

data["title"] = []
data["season"] = []
data["ep_number"] = []
data["rate"] = []
data["duration"] = []

# Percorra cada página

for j in range(3):

  print(f"[ EP ] {j}")
  # Espere ela carregar
  time.sleep(1)

  # Recupere os dados
  title = browser.find_element_by_css_selector("h1[data-testid='hero-title-block__title']")
  season = browser.find_element_by_css_selector(f"{prefix} > div.SubNav__SubNavContainer-sc-11106ua-1.hDUKxp > div > div:nth-child(1) > ul > li:nth-child(1) > span")
  ep_number = browser.find_element_by_css_selector(f"{prefix} > div.SubNav__SubNavContainer-sc-11106ua-1.hDUKxp > div > div:nth-child(1) > ul > li:nth-child(2) > span")
  rate = browser.find_element_by_css_selector(f"{prefix} > div.TitleBlock__Container-sc-1nlhx7j-0.hglRHk > div.RatingBar__RatingContainer-sc-85l9wd-0.hNqCJh.TitleBlock__HideableRatingBar-sc-1nlhx7j-4.bhTVMj > div > div:nth-child(1) > a > div > div > div.AggregateRatingButton__ContentWrap-sc-1ll29m0-0.hmJkIS > div.AggregateRatingButton__Rating-sc-1ll29m0-2.bmbYRW > span.AggregateRatingButton__RatingScore-sc-1ll29m0-1.iTLWoV")
  duration = browser.find_element_by_css_selector(f"{prefix} > div.TitleBlock__Container-sc-1nlhx7j-0.hglRHk > div.TitleBlock__TitleContainer-sc-1nlhx7j-1.jxsVNt > div.TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2.hWHMKr > ul > li:nth-child(3)")

  # Armazenar dados
  data["title"].append(title.text)
  data["season"].append(handling.extract_number(season.text, "S"))
  data["ep_number"].append(handling.extract_number(ep_number.text, "E"))
  data["rate"].append(handling.convert_to_dot(rate.text))
  data["duration"].append(handling.extract_minutes(duration.text))

  # Clique na seta da direita
  right_btn = browser.find_element_by_id("iconContext-arrow-right")
  right_btn.click()

print(data)

browser.close()
