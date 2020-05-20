!pip install facebook-scraper
import pandas as pd
from datetime import datetime,timedelta
from facebook_scraper import get_posts

groupLists=['FactlyIndia','TimesFactCheck','QuintFactCheck']
duration = datetime.today() - timedelta(days=7)
fb_data=[] 
dateTime = datetime.now()
fileName = 'data_fb_'+str(dateTime)+'.csv'
for item in groupLists:
  for post in get_posts(item, pages =20): 
    post_date = (post['time'])
    if post_date > duration: 
      temp_dict=dict(post)
      fb_data.append(temp_dict)
fb_df = pd.DataFrame(fb_data)
fb_df['scrapedDate'] = dateTime
fb_df.head()
fb_df.to_csv(fileName)
