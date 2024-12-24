import streamlit as st

# Set up the page configuration and title
st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar with clickable headings (buttons)
st.sidebar.header("Navigation")
home_button = st.sidebar.button("Home")
portfolio_button = st.sidebar.button("Portfolio")
contact_button = st.sidebar.button("Contact")
photos_button = st.sidebar.button("Photos")

# Display content based on the button clicked
if home_button:
    st.title("Welcome to My Portfolio")
    st.write("Hello! I'm a passionate developer with a keen interest in building innovative applications.")
    st.write("On this site, you can explore my portfolio, learn more about me, and see my photos and contact info.")
    st.image("https://via.placeholder.com/800x400", caption="A Placeholder Image for Home", use_column_width=True)

elif portfolio_button:
    st.title("My Portfolio")
    st.write("Here are some of the projects I've worked on:")
    st.write("1. **Project One**: A web application built with Streamlit and Python.")
    st.write("2. **Project Two**: A machine learning project that predicts stock prices using Scikit-learn.")
    st.write("3. **Project Three**: A data visualization dashboard built using Plotly and Dash.")
    st.image("https://via.placeholder.com/800x400", caption="A Placeholder Image for Portfolio", use_column_width=True)

elif contact_button:
    st.title("Contact Me")
    st.write("Feel free to reach out!")
    st.write("Email: example@example.com")
    st.write("LinkedIn: [My LinkedIn](https://www.linkedin.com)")
    st.write("GitHub: [My GitHub](https://github.com)")
    st.write("Phone: 123-456-7890")

elif photos_button:
    st.title("My Photos")
    st.write("Here are some of my favorite photos from my travels and experiences.")
    st.image("https://via.placeholder.com/800x400", caption="Placeholder Image 1", use_column_width=True)
    st.image("https://via.placeholder.com/800x400", caption="Placeholder Image 2", use_column_width=True)
    st.image("https://via.placeholder.com/800x400", caption="Placeholder Image 3", use_column_width=True)
