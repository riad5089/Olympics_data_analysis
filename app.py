import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
df=pd.read_csv(r"C:\Users\Abdur rahim nishad\ml project\Olympics_data_analysis\athlete_events.csv")
region_df=pd.read_csv(r'C:\Users\Abdur rahim nishad\ml project\Olympics_data_analysis\noc_regions.csv')

df=preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
user_menu=st.sidebar.radio(
    "Select an Option",
    ("Medal Tally","Overall Analysis","Country_wise Analysis","Athlete wise Analysis")

)
# st.dataframe(df)
# if user_menu=="Medal Tally":
#     st.header("Medal Tally")
#     years,country=helper.country_year_list(df)
#     selected_year=st.sidebar.selectbox("Selected Year",years)
#     selected_country = st.sidebar.selectbox("Selected country", country)
#     medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
#     if selected_year == 'Overall' and selected_country=='Overall':
#         st.title("Overall Tally")
#     if selected_year != 'Overall' and selected_country == 'Overall':
#         st.title("Medal Tally in" + str(selected_year)+ " Olympics")
#     if selected_year == 'Overall' and selected_country != 'Overall':
#         st.title(selected_country + " Oveall performace")
if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu =='Overall Analysis':
    editions=df['Year'].unique().shape[0] - 1
    cities=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athletes=df['Name'].unique().shape[0]
    nations=df['region'].unique().shape[0]


    st.title("Top Statistics")
    col1,col2,col3=st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1, col2, col3=st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Athletes')
        st.title(athletes)
    with col3:
        st.header('Nations')
        st.title(nations)
    nation_over_time=helper.data_over_time(df,'region')
    fig = px.line(nation_over_time, x="Edition", y='region')
    st.title("Participaiting Nation over the years")
    st.plotly_chart(fig)

    event_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(event_over_time, x="Edition", y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)


    athletes_over_time = helper.data_over_time(df,'Name')
    fig = px.line(athletes_over_time, x="Edition", y='Name')
    st.title("Athletes over the years")
    st.plotly_chart(fig)


