import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import plotly.express as px
from statsmodels.tsa.holtwinters import ExponentialSmoothing

st.set_page_config(layout="wide")
# Read data
climate_data = pd.read_csv('./datasets/climate_change_impact_on_agriculture_2024.csv')

st.title(":green[Climate and Crops Dashboard]")


tab1, tab2, tab3, tab4 = st.tabs(["Global Overview", "Temperature Trends", "Economic Impact", "Prediction Model"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        selected_year = st.slider("Select Year", int(climate_data['Year'].min()), int(climate_data['Year'].max()), step=1)
    with col2:
        selected_crop = st.selectbox("Select Crop Type", climate_data['Crop_Type'].unique())

    ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
        background: rgb(1 1 1 / 0%); } </style>''', unsafe_allow_html = True)


    Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        background-color: rgb(128, 128, 128); box-shadow: rgb(255, 255, 255 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)

        
    Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
                                    { color: rgb(255, 255, 255); } </style>''', unsafe_allow_html = True)
        

    col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{
        background: linear-gradient(to right, rgb(1, 120, 1) 0%, 
                                    rgb(1, 120, 1) {selected_year}%, 
                                    rgba(151, 166, 195, 0.25) {selected_year}%, 
                                    rgba(151, 166, 195, 0.25) 100%); }} </style>'''

    ColorSlider = st.markdown(col, unsafe_allow_html = True)   

    filtered_data = climate_data[(climate_data['Year'] == selected_year) & (climate_data['Crop_Type'] == selected_crop)]
    country_yield = filtered_data.groupby("Country", as_index=False)["Crop Yield (Metric Tonne/HA)"].mean()

    st.subheader(f"Crop Yield by Region in {selected_year} for {selected_crop}")
    fig = px.choropleth(
        country_yield,
        locations="Country",
        locationmode="country names",
        color="Crop Yield (Metric Tonne/HA)",
        hover_name="Country",
        # color_continuous_scale="YlGn",  # Earthy tones
        color_continuous_scale = ["#8B4513", "#e6965a", "#a6bd88", "#006400", "#004502"],
        title=f" ",
        range_color=(country_yield["Crop Yield (Metric Tonne/HA)"].min(),
                    country_yield["Crop Yield (Metric Tonne/HA)"].max())
    )

    # Update layout for an earthy look
    fig.update_layout(
        title=dict(x=0.5, font=dict(size=18)),  # Centered title
        geo=dict(
            showframe=True,  # Adds border around the entire world map
            framecolor="grey",  # World map border in grey
            showcoastlines=True,  # Show coastlines
            coastlinecolor="grey",  # Coastline color grey
            # showland=True,  # Show land
            # landcolor="white",  # Land color
            showlakes=True,  # Show lakes
            lakecolor="rgba(0,0,0,0)",  # Lake color
            projection_type="natural earth",  # Natural map projection
            bgcolor="rgba(0,0,0,0)",  # Transparent map background
            showcountries=True,  # Show country borders
            countrycolor="grey",  # Country borders in grey
        ),
        autosize=True,  # Automatically adjust the size of the chart
        height=700  
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    climate_data = pd.read_csv('./datasets/merged_climate_agriculture_data.csv')

    usa_data = climate_data[climate_data['Country'] == 'USA']

    # Group by Year to calculate the average temperature
    usa_temp_data = usa_data.groupby('Year', as_index=False)['Average_Temperature_C'].mean()

    # Create a scatter plot with a trend line
    fig_usa_temp = px.scatter(
        usa_temp_data,
        x='Year',
        y='Average_Temperature_C',
        title="<b>Temperature Changes Over Years in USA</b>",
        labels={'Average_Temperature_C': 'Average Temperature (°C)', 'Year': 'Year'},
        template="plotly",
        trendline="ols"  # Add Ordinary Least Squares (OLS) regression trend line
    )

    # Customize traces
    fig_usa_temp.data[0].update(marker=dict(color="darkorange", size=6), mode="markers", name="Data Points")
    fig_usa_temp.update_traces(mode="lines", name="Data Points")  # Customize data points line+markers
    fig_usa_temp.data[-1].update(line=dict(color="lightgreen", width=2), name="Trend Line")  # Customize trend line color and legend

    # Customize layout
    fig_usa_temp.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        legend_title="Legend",
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)  # Position legend
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig_usa_temp, use_container_width=True)



    fig_temp_yield = px.scatter(
        climate_data,
        x='Average_Temperature_C',
        y='Crop_Yield_MT_per_HA',
        title="<b>Effect of Temperature on Crop Yield</b>",
        labels={
            'Average_Temperature_C': 'Average Temperature (°C)',
            'Crop_Yield_MT_per_HA': 'Crop Yield (MT/HA)'
        },
        template="plotly",
        # trendline="ols",  # Add a trendline to show the relationship
        color_discrete_sequence=["green"]  # Customize marker color
    )

    # Customize traces
    # fig_temp_yield.data[-1].update(line=dict(color="red", width=2), name="Trend Line")  # Customize trend line
    fig_temp_yield.update_traces(marker=dict(size=8), name="Data Points")  # Customize marker size

    # Customize layout
    fig_temp_yield.update_layout(
        title_font_size=20,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        legend_title="Legend",
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)  # Position legend
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig_temp_yield, use_container_width=True)

with tab3:
    choice = st.selectbox("Choose Climate Variable", ['Temperature', 'Precipitation', 'CO2 Emissions'])
    col_1, col_2, col_3 = st.columns(3)
    if climate_data is not None:
        if choice == 'Temperature':
            bins = [-float('inf'), 15, 25, 35, float('inf')]  # Temperature ranges
            labels = ['Low (<=15°C)', 'Moderate (15-25°C)', 'Warm (25-35°C)', 'Hot (>35°C)']
            climate_data['Temperature_Range'] = pd.cut(climate_data['Average_Temperature_C'], bins=bins, labels=labels)

            # Group the data by Crop Type and Temperature Range to find the economic impact for each group
            econ_impact_temp_data = climate_data.groupby(['Crop_Type', 'Temperature_Range'], as_index=False)['Economic_Impact_Million_USD'].mean()

            # Create a bar chart for economic impact by crop type and temperature range
            fig_temp_impact = px.bar(
                econ_impact_temp_data,
                x="Crop_Type",  # Crop type on the X-axis
                y="Economic_Impact_Million_USD",  # Economic impact on the Y-axis
                color="Temperature_Range",  # Color by temperature range
                title="<b>Economic Impact by Crop Type and Temperature Range </b>",
                labels={"Economic_Impact_Million_USD": "Economic Impact (Million USD)", "Crop_Type": "Crop Type", "Temperature_Range": "Temperature Range"},
                template="plotly",
                height=700,
                barmode="group",
                color_discrete_map={
                    'Low (<=15°C)': '#8B4513',  
                    'Moderate (15-25°C)': '#e6965a',  
                    'Warm (25-35°C)': '#228B22',  
                    'Hot (>35°C)': '#006400'  
                }
            )
            st.plotly_chart(fig_temp_impact, use_container_width=True)

        if choice == 'Precipitation':
            precip_bins = [-float('inf'), 200, 500, 800, float('inf')]
            precip_labels = ['Low (<=200 mm)', 'Moderate (200-500 mm)', 'High (500-800 mm)', 'Very High (>800 mm)']
            climate_data['Precipitation_Range'] = pd.cut(climate_data['Total_Precipitation_mm'], bins=precip_bins, labels=precip_labels)
            econ_impact_precip_data = climate_data.groupby(['Crop_Type', 'Precipitation_Range'], as_index=False)['Economic_Impact_Million_USD'].mean()

            # Bar chart for Precipitation Economic Impact
            fig_precip_impact = px.bar(
                econ_impact_precip_data,
                x="Crop_Type",
                y="Economic_Impact_Million_USD",
                color="Precipitation_Range",
                title="<b>Economic Impact</b><br>by Crop Type and Precipitation Range",
                labels={"Economic_Impact_Million_USD": "Economic Impact (Million USD)", "Crop_Type": "Crop Type", "Precipitation_Range": "Precipitation Range"},
                template="plotly",
                height=700,
                barmode="group",
                color_discrete_map={
                    'Low (<=200 mm)': '#8B4513',  
                    'Moderate (200-500 mm)': '#e6965a',  
                    'High (500-800 mm)': '#228B22',  
                    'Very High (>800 mm)': '#006400'  
                }
            )
            st.plotly_chart(fig_precip_impact, use_container_width=True)

        if choice == 'CO2 Emissions':
            # CO2 Emissions: Create bins for better understanding
            co2_bins = [-float('inf'), 2, 5, 10, float('inf')]
            co2_labels = ['Low (<=2 MT)', 'Moderate (2-5 MT)', 'High (5-10 MT)', 'Very High (>10 MT)']
            climate_data['CO2_Range'] = pd.cut(climate_data['CO2_Emissions_MT'], bins=co2_bins, labels=co2_labels)    

            # Group data for CO2-based economic impact chart
            econ_impact_co2_data = climate_data.groupby(['Crop_Type', 'CO2_Range'], as_index=False)['Economic_Impact_Million_USD'].mean()

            # Bar chart for CO2 Economic Impact
            fig_co2_impact = px.bar(
                econ_impact_co2_data,
                x="Crop_Type",
                y="Economic_Impact_Million_USD",
                color="CO2_Range",
                title="<b>Economic Impact</b><br>by Crop Type and CO2 Emissions Range",
                labels={"Economic_Impact_Million_USD": "Economic Impact (Million USD)", "Crop_Type": "Crop Type", "CO2_Range": "CO2 Emissions Range"},
                template="plotly",
                height=700,
                barmode="group",
                color_discrete_map={
                    'Low (<=2 MT)': '#8B4513', 
                    'Moderate (2-5 MT)': '#e6965a', 
                    'High (5-10 MT)': '#228B22', 
                    'Very High (>10 MT)': '#006400'  
                }
            )
            st.plotly_chart(fig_co2_impact, use_container_width=True)

        # # Display all charts
        # with col_1:
            
        # with col_2:
            
        # with col_3:
            

    else:
        st.write("Data is not loaded. Please load your dataset to visualize the chart.")

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
dataset = climate_data[['Average_Temperature_C','Total_Precipitation_mm', 'CO2_Emissions_MT','Economic_Impact_Million_USD']]
X = dataset.drop(['Economic_Impact_Million_USD'], axis=1) #Environmental factors
y = dataset['Economic_Impact_Million_USD']  # Target column

features = X.columns

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_dt = DecisionTreeRegressor(random_state=42)

model_dt.fit(X_train, y_train)

with tab4:
    st.title(":green[Predict Economic Impact]")

    st.subheader("Enter the environmental factors to predict economic impact")

    # User input fields
    avg_temp = st.number_input("Average Temperature (°C)", min_value=float(X['Average_Temperature_C'].min()), max_value=float(X['Average_Temperature_C'].max()), value=float(X['Average_Temperature_C'].mean()))
    precipitation = st.number_input("Precipitation (mm)", min_value=float(X['Total_Precipitation_mm'].min()), max_value=float(X['Total_Precipitation_mm'].max()), value=float(X['Total_Precipitation_mm'].mean()))
    co2_emissions = st.number_input("CO2 Emissions (MT)", min_value=float(X['CO2_Emissions_MT'].min()), max_value=float(X['CO2_Emissions_MT'].max()), value=float(X['CO2_Emissions_MT'].mean()))

    # Prediction button
    if st.button("Predict Economic Impact"):
        # Prepare input for prediction
        input_data = pd.DataFrame([[avg_temp, precipitation, co2_emissions]], columns=features)
        
        # Make prediction
        prediction = model_dt.predict(input_data)[0]
        
        # Display the result
        st.markdown(
                    f"""
                    <div style="background-color: #d4edda; padding: 20px; border-radius: 5px;">
                        <h2 style="color: #155724; text-align: center;">
                            Predicted Economic Impact: ${prediction:,.2f} Million USD
                        </h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    

    



