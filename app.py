import streamlit as st
import time

# CSS by andfanilo, learned from DataProfessor's Pomodoro App code
# Source: https://discuss.streamlit.io/t/creating-a-nicely-formatted-search-field/1804
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')
#remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')



#===========================================#
#              Streamlit Code               #
#===========================================#

# App inspired by this post on Greg McKeown's blog 
# https://gregmckeown.com/30-second-habit-lifelong-impact/ 

st.title('The 30-Second Habit App')

with st.expander('Write down the most important things'):
    st.markdown('''
        This app takes the inspiration from an Essentialist practice introduced in Greg McKeown's [blog](https://gregmckeown.com/30-second-habit-lifelong-impact/) 
        in which you spend 30 seconds writing down the most 
        important points after every experience, meeting or event. 
        Practice here to see its impacts.'''
    )

# Define callback function to handle button clicks
def handle_click():
    # We want to clear st.session_state.text once button is clicked?  
    if 'text' in st.session_state:
        st.session_state.text = ''

# Show button
clicked = st.button('Start', on_click=handle_click)

# Show text area
st.text_area('', placeholder='Little writing space for you:)', 
                 key='text', help='Remember to save your summary digitally')

# This will get the value of the text_area widget as summary at the end
st.write(st.session_state.text)

# Timer
# Created by adapting from:
# https://github.com/dataprofessor/pomodoro-app

t1 = 30
if clicked:
    # Clear text area whenever user clicks the Start button 
    if st.session_state.text:
        handle_click() # st.session_state.text also works here?
        
    with st.empty(): 
        while t1:
            mins, secs = (0, t1)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f'⏳ {timer}')
            time.sleep(1)
            t1 -= 1
        st.success(f"Great. You've completed the 30-second habit with a lifelong impact!🥳")






