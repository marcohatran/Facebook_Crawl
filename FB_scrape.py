!pip install facebook-scraper
import pandas as pd
from datetime import datetime

groupLists=['FactlyIndia','TimesFactCheck','QuintFactCheck']
fb_data=[] 
dateTime = datetime.now()
fileName = 'data_fb_'+str(dateTime)+'.csv'
print(fileName)
for item in groupLists:
  for post in get_posts(item, pages =20):     
    temp_dict=dict(post)
    fb_data.append(temp_dict)
    # fb_data.append(item)
  # print(tweet)
fb_df = pd.DataFrame(fb_data)
fb_df['scrapedDate'] = dateTime
fb_df.head()
fb_df.to_csv(fileName)
