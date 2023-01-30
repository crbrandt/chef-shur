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

if auth != True:
	with st.form(key='my_form'):
		guest_id = st.text_input(label="guest id", key='guest_id')
		password = st.text_input(label="password", key='password')
		submit_button = st.form_submit_button(label='submit')
		if (len(guest_id) != 0 OR len(password) != 0) AND auth != True:
			st.write('Invalid')
		else:
			st.write('')
		
	if guest_id == 'test' and password == 'test':
		auth = True
	elif guest_id == 'test1' and password == 'test1':
		auth = True
	else:
		auth = False		
	
else:
	st.write('#')
 

	
	

if auth == True:
	st.markdown(' ## say yes to chef, if you choose to attend')
	st.write("#")
	st.button('Yes, Chef')
else:
	st.write("#")
	

st.image("https://i.ibb.co/hDRKYT4/png-transparent-chef-s-uniform-hat-toque-hat-removebg-preview.jpg")	

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
