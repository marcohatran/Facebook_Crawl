!pip install facebook-scraper
import pandas as pd
fb_data=[]
from facebook_scraper import get_posts
for post in get_posts('FactlyIndia'):     
  temp_dict=dict(post)
  fb_data.append(temp_dict)
  # print(tweet)
fb_df = pd.DataFrame(fb_data)
fb_df.head()
fb_df.to_csv('FactlyIndia_fb.csv')
