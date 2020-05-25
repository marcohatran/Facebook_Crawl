!pip install facebook-scraper

import pandas as pd
from facebook_scraper import get_posts, _extract_time, _get_group_posts,_extract_post
from datetime import datetime, timedelta

pageLists=['FactlyIndia','TimesFactCheck','QuintFactCheck']
keyword_pageList = ['COVID','government']
groupLists=['/groups/FaceTAV/']
keyword_groupList = ['session','break']
duration_days = 7
groupfb_data=[] 
searched_groupdata = []

page_df = pd.DataFrame()
duration = datetime.today() - timedelta(days=duration_days)
searched_pagedata = pd.DataFrame()
fb_pagedf = pd.DataFrame()
dateTime = datetime.now()
page_fileName = 'pageList_fb_'+str(dateTime)+'.csv'
group_fileName = 'groupList_fb_'+str(dateTime)+'.csv'

for item in pageLists:
  for post in get_posts(item, pages =20,extra_info=True): 
    post_date = (post['time'])
    if post_date > duration:
      if('reactions' in post.keys()):
        fb_pagedf = pd.DataFrame(post['reactions'], index=[0])
      fb_pagedf['text'] = post['text']
      fb_pagedf['PostDate'] = post['time']
      fb_pagedf['PostID'] = post['post_id']
      fb_pagedf['ImageURL'] = post['image']
      fb_pagedf['Likes'] = post['likes']
      fb_pagedf['Shares'] = post['shares']
      fb_pagedf['Comments'] = post['comments']
      fb_pagedf['PostURL'] = post['post_url']
      fb_pagedf['scrapedDate'] = dateTime
      page_df = page_df.append(fb_pagedf)
      for keyword_page in keyword_pageList:
        text = post['text']
        if(keyword_page in text): 
          searched_pagedata = searched_pagedata.append(fb_pagedf)

if pageLists:
  page_df.to_csv(page_fileName)
  searched_pagedata.to_csv("fbPage_searchedcontent.csv")

for element in groupLists:
  for post in _get_group_posts(element): 
    post_date = (post['time'])
    # if post_date > duration:
    temp_dict=dict(post)
    groupfb_data.append(temp_dict)
    for keyword_group in keyword_groupList:
      group_text = post['text']
      if(keyword_group in group_text): 
        searched_groupdata.append(temp_dict)
group_df = pd.DataFrame(groupfb_data)
searchedgroup_df = pd.DataFrame(searched_groupdata)
group_df['scrapedDate'] = dateTime
searchedgroup_df['scrapedDate'] = dateTime
del group_df['post_text']
del group_df['shared_text']
del group_df['link']
del searchedgroup_df['post_text']
del searchedgroup_df['shared_text']
del searchedgroup_df['link']
if groupLists:
  group_df.to_csv(group_fileName)
  searchedgroup_df.to_csv('fbGroup_searchedcontent.csv')
