import numpy as np
def fetch_medal_tally(df,year,country):
    medal_df=df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag=0
    if year=="Overall" and country=="Overall":
        temp_df=medal_df
    if year=="Overall" and country!="Overall":
        flag=1
        temp_df=medal_df[medal_df["region"]==country]
    if year!="Overall" and country=="Overall":
        temp_df=medal_df[medal_df["Year"]==int(year)]
    if year!="Overall" and country!="Overall":
        temp_df=medal_df[(medal_df["Year"]==int(year)) & (medal_df["region"]==country)]
    if flag==1:
        x= temp_df.groupby("Year").sum()[["Gold","Silver","Bronze"]].sort_values("Year",ascending=True).reset_index()
    else:
        x= temp_df.groupby("region").sum()[["Gold","Silver","Bronze"]].sort_values("Gold",ascending=False).reset_index()

    x["total"] = x["Gold"]+x["Silver"]+x["Bronze"]
    x["Gold"] = x["Gold"].astype("int")
    x["Silver"] = x["Silver"].astype("int")
    x["Bronze"] = x["Bronze"].astype("int")
    return x
def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby("region").sum()[["Gold","Silver","Bronze"]].sort_values("Gold",ascending=False).reset_index()
    medal_tally["total"] = medal_tally["Gold"]+medal_tally["Silver"]+medal_tally["Bronze"]
    medal_tally["Gold"]=medal_tally["Gold"].astype("int")
    medal_tally["Silver"] = medal_tally["Silver"].astype("int")
    medal_tally["Bronze"] = medal_tally["Bronze"].astype("int")
    medal_tally["total"] = medal_tally["total"].astype("int")

    return medal_tally
def country_year_list(df):
    year = df['Year'].unique().tolist()
    year.sort()
    year.insert(0, "Overall")
    country = df['region'].dropna().unique().tolist()
    country.sort()
    country.insert(0, "Overall")
    return year,country
def data_over_time(df,col):
    nation_over_time=df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index().sort_values('index')
    nation_over_time.rename(columns={'index': 'Edition', 'Year': col}, inplace=True)
    return nation_over_time
