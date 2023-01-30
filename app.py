#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st


import requests


import html5lib


from datetime import date
from datetime import datetime


# In[2]:



##Updating Page Logo and Tab Title
st.set_page_config(page_title='yes.chef',
                   page_icon='https://w7.pngwing.com/pngs/184/60/png-transparent-chef-s-uniform-hat-toque-hat.png',
                   layout="wide")



##Creating Text format options with base and team colors
def highlight(text):
     st.markdown(f'<p style="text-align: center;color:#013369;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
def color(text):
     st.markdown(f'<p style="color:#013369;font-size:20px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)
def accuracy(text):
     st.markdown(f'<p style="color:#013369;font-size:15px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)
def disclaimer(text):
     st.markdown(f'<p style="color:red;font-size:15px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)


# In[4]:




##--------------------------------------------------------Application Displayed Portion-----------------------------------------

#Reading modeldata from Github
rsvp_url = 'https://raw.githubusercontent.com/crbrandt/chef-shur/main/Data/rsvps.csv'
rsvp = pd.read_csv(rsvp_url, error_bad_lines=False)


##Header and Logo
col_title = st.beta_columns([4,1])
with col_title:
  st.title('yes.chef')
  st.markdown(' ## say yes to chef, if you choose to attend')
  st.markdown('  Last updated: Thursday, January 6th, 2022')  
  st.image("https://w7.pngwing.com/pngs/184/60/png-transparent-chef-s-uniform-hat-toque-hat.png")
  
st.write("#")
# highlight('NFL Week ' + str(1))


# In[5]:


#Getting current week number

current_week_num =0

season_start = datetime.strptime('2021-09-07', '%Y-%m-%d').date()




# In[7]:





# In[8]:





# In[9]:




disclaimer('Note: This model does not currently account for players being out due to COVID or injury.')

# In[50]:


st.markdown('___')
Rankings = st.beta_expander('Statistics and Power Rankings')
with Rankings:
    st.markdown('Team Statistics Sorted by Power Ranking')
   


# In[31]:


# Bottom info bar ------------------------------------------------------------------------
st.markdown('___')
about = st.beta_expander('About')
with about:
    '''
    Thank you for visiting the NFL Game Predictor, developed by Cole Brandt. For more information, please visit my [Github repository] (https://github.com/crbrandt/NFLPredictor).
    
    Feel free to support via Venmo, @ColeBrandt
    
    Spreads from MGM Sportsbook, scraped from VegasInsider.com. All images sourced from sportslogos.net. 
    
    [Contact Me] (mailto:cole.r.brandt@gmail.com)
    '''
    
st.image("https://w7.pngwing.com/pngs/184/60/png-transparent-chef-s-uniform-hat-toque-hat.png",
    width= 100, caption='2023 Cole Brandt')


# In[ ]:





# In[10]:





# In[11]:




##Creating Text format options with base and team colors
def highlight(text):
     st.markdown(f'<p style="text-align: center;color:#013369;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
def teamcolor(text):
     if 'Arizona' in text:
         st.markdown(f'<p style="text-align: center;color:#97233F;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Atlanta' in text:
         st.markdown(f'<p style="text-align: center;color:#A71930;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Baltimore' in text:
         st.markdown(f'<p style="text-align: center;color:#241773;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Buffalo' in text:
         st.markdown(f'<p style="text-align: center;color:#00338D;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Carolina' in text:
         st.markdown(f'<p style="text-align: center;color:#0085CA;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Chicago' in text:
         st.markdown(f'<p style="text-align: center;color:#C83803;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Cincinnati' in text:
         st.markdown(f'<p style="text-align: center;color:#FB4F14;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Cleveland' in text:
         st.markdown(f'<p style="text-align: center;color:#FF3C00;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Dallas' in text:
         st.markdown(f'<p style="text-align: center;color:#003594;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Denver' in text:
         st.markdown(f'<p style="text-align: center;color:#FB4F14;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Detroit' in text:
         st.markdown(f'<p style="text-align: center;color:#0076B6;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Green Bay' in text:
         st.markdown(f'<p style="text-align: center;color:#203731;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Houston' in text:
         st.markdown(f'<p style="text-align: center;color:#A71930;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Indianapolis' in text:
         st.markdown(f'<p style="text-align: center;color:#002C5F;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Jacksonville' in text:
         st.markdown(f'<p style="text-align: center;color:#006778;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Kansas City' in text:
         st.markdown(f'<p style="text-align: center;color:#E31837;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Las Vegas' in text:
         st.markdown(f'<p style="text-align: center;color:#A5ACAF;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Chargers' in text:
         st.markdown(f'<p style="text-align: center;color:#0080C6;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Rams' in text:
         st.markdown(f'<p style="text-align: center;color:#003594;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Miami' in text:
         st.markdown(f'<p style="text-align: center;color:#008E97;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Minnesota' in text:
         st.markdown(f'<p style="text-align: center;color:#4F2683;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'New England' in text:
         st.markdown(f'<p style="text-align: center;color:#002244;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'New Orleans' in text:
         st.markdown(f'<p style="text-align: center;color:#D3BC8D;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Giants' in text:
         st.markdown(f'<p style="text-align: center;color:#0B2265;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Jets' in text:
         st.markdown(f'<p style="text-align: center;color:#125740;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Eagles' in text:
         st.markdown(f'<p style="text-align: center;color:#004C54;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Steelers' in text:
         st.markdown(f'<p style="text-align: center;color:#FFB612;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'San Francisco' in text:
         st.markdown(f'<p style="text-align: center;color:#AA0000;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Seahawks' in text:
         st.markdown(f'<p style="text-align: center;color:#69BE28;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Buccaneers' in text:
         st.markdown(f'<p style="text-align: center;color:#D50A0A;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Titans' in text:
         st.markdown(f'<p style="text-align: center;color:#4B92DB;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Washington' in text:
         st.markdown(f'<p style="text-align: center;color:#773141;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     else:
         st.markdown(f'<p style="text-align: center;color:#575757;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
def color(text):
     st.markdown(f'<p style="color:#013369;font-size:20px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)
def accuracy(text):
     st.markdown(f'<p style="color:#013369;font-size:15px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)


# In[12]:





# In[13]:





# In[14]:


# preds_url = 'https://raw.githubusercontent.com/crbrandt/NFLPredictor/main/Data/preds.csv'
# preds = pd.read_csv(preds_url, error_bad_lines=False)
#preds


# In[15]:





# In[16]:


#df_weather[df_weather['Home_Team'] == 'Los Angeles Rams'].iat[0,2]
#len(preds['Predicted_Difference'])
#df_weather


# In[17]:





# In[18]:


#preds['Weather']


# In[19]:





# In[ ]:


#df_full.head()


# In[20]:





# In[21]:





# In[22]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




