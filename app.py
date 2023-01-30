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
                   page_icon='https://i.ibb.co/hDRKYT4/png-transparent-chef-s-uniform-hat-toque-hat-removebg-preview.jpg',
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


#st.title('yes.chef')
auth = 'undefined' 

while auth != True:
  with st.form(key='my_form'):
	  guest_id = st.text_input(label="guest id", key='guest_id')
    password = st.text_input(label="password", key='password')
	  submit_button = st.form_submit_button(label='submit')

  
  if guest_id == 'test' and password == 'test':
    auth = True
  elif guest_id == 'test1' and password == 'test1':
    auth = True
  else:
    st.write('Invalid.')
 

while auth == True:
  st.markdown(' ## say yes to chef, if you choose to attend')
  st.image("https://i.ibb.co/hDRKYT4/png-transparent-chef-s-uniform-hat-toque-hat-removebg-preview.jpg")
  #st.markdown('  Last updated: Thursday, January 6th, 2022')  

  st.write("#")
  # highlight('NFL Week ' + str(1))


  # In[5]:


  #Getting current week number

  current_week_num =0

  season_start = datetime.strptime('2021-09-07', '%Y-%m-%d').date()




  # In[7]:





  # In[8]:





  # In[9]:




  # disclaimer('Note: This model does not currently account for players being out due to COVID or injury.')

  # In[50]:


  #st.markdown('___')
  #Rankings = st.beta_expander('Statistics and Power Rankings')
  #with Rankings:
      #st.markdown('Team Statistics Sorted by Power Ranking')



  # In[31]:
  st.button('Yes, Chef')
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")
st.write("#")

# Bottom info bar ------------------------------------------------------------------------
#st.markdown('___')
about = st.beta_expander('About')
with about:
    st.image("https://i.ibb.co/hDRKYT4/png-transparent-chef-s-uniform-hat-toque-hat-removebg-preview.jpg",
    width= 100, caption='2023 Cole Brandt')

st.write("#")



# In[ ]:





# In[10]:





# In[11]:




##Creating Text format options with base and team colors

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




