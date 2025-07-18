import streamlit as st
import pandas as pd
import requests
import altair as alt 

st.set_page_config(layout="wide", page_title="Country Data Dashboard")

st.title("🌍 Global Country Data Dashboard")
st.markdown("Explore information about countries worldwide using data from the REST Countries API.")

@st.cache_data
def get_all_countries():
    """Fetches a list of all countries from the REST Countries API."""
    # Use necessary fields to avoid 400 Bad Request
    url = "https://restcountries.com/v3.1/all?fields=name,capital,region,subregion,population,area,flag,flags"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for HTTP errors
        countries_data = response.json()
        return countries_data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching country data: {e}")
        return []

all_countries_raw = get_all_countries()

if not all_countries_raw:
    st.warning("Could not load country data. Please check your internet connection or try again later.")
else:
    processed_countries = []
    for country in all_countries_raw:
        try:
            processed_countries.append({
                'Name': country.get('name', {}).get('common', 'N/A'),
                'Official Name': country.get('name', {}).get('official', 'N/A'),
                'Capital': country.get('capital', ['N/A'])[0] if country.get('capital') else 'N/A',
                'Region': country.get('region', 'N/A'),
                'Subregion': country.get('subregion', 'N/A'),
                'Population': country.get('population', 0),
                'Area (km²)': country.get('area', 0),
                'Flag': country.get('flag', 'N/A'), # Emoji flag
                'Flag URL': country.get('flags', {}).get('png', 'N/A') 
            })
        except Exception as e:
            st.warning(f"Skipping a country due to data processing error: {e}. Data: {country.get('name', {}).get('common', 'Unknown')}")
            continue

    countries_df = pd.DataFrame(processed_countries)


    st.sidebar.header("Filter Countries")
    search_query = st.sidebar.text_input("Search by country name:", "").lower()
    
    all_regions = sorted(countries_df['Region'].unique())
    selected_regions = st.sidebar.multiselect("Filter by Region:", all_regions, default=all_regions)

    filtered_df = countries_df[countries_df['Region'].isin(selected_regions)]

    if search_query:
        filtered_df = filtered_df[
            filtered_df['Name'].str.lower().str.contains(search_query) |
            filtered_df['Official Name'].str.lower().str.contains(search_query) |
            filtered_df['Capital'].str.lower().str.contains(search_query)
        ]

    st.subheader("Filtered Country Data")
    if not filtered_df.empty:
        st.dataframe(filtered_df)

        st.write("### Population by Country (Top 20 or all if less than 20)")

        chart_data = filtered_df.sort_values(by='Population', ascending=False).head(20)

        if not chart_data.empty:
            chart = alt.Chart(chart_data).mark_bar().encode(
                x=alt.X('Population', title='Population'),
                y=alt.Y('Name', sort='-x', title='Country'),
                tooltip=['Name', 'Population', 'Region']
            ).properties(
                title='Population of Filtered Countries'
            )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.info("No data to display for population chart with current filters.")
    else:
        st.info("No countries match your current filters.")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("Built with Streamlit and REST Countries API")
    st.sidebar.markdown("Data from restcountries.com")
