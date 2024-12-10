# Final Project Proposal

**GitHub Repo URL**: https://github.com/CMU-IDS-Fall-2024/final-project-f24-ids-group-14

**Project Proposal**: Assessing the Impact of Climate Change on Agricultural Productivity

**Team Members**: Akhil Dua, Akshita Gupta, Krishnaprasad Vijayshankar, Mahima Jagadeesh Patel

### Problem Description

The agricultural sector is critically affected by climate change, with increasing temperatures, unpredictable precipitation patterns, and extreme weather events posing significant challenges to crop yield and food security. This project aims to evaluate the impact of climate change on agricultural productivity across different regions, with a specific focus on identifying factors that most significantly affect crop yields. By understanding these relationships, we can offer insights to policymakers and farmers on optimizing agricultural practices and improving food security in the face of climate change. Combining this dataset with agricultural price data enables us to assess how climate-induced yield changes affect farmers' incomes, offering insights to guide policies for economic stability and climate resilience in agriculture.

### Dataset

This dataset explores the impact of climate change on agricultural productivity across various regions. It includes data on temperature, precipitation, and crop yields to understand how shifting climate patterns affect agriculture.

The main dataset, Climate Change Impact on Agriculture ([Kaggle link](https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture)), examines how climate factors such as temperature, precipitation, CO₂ emissions, and extreme weather events impact crop yields across various regions. Key features include crop type, irrigation access, fertilizer use, soil health, and adaptation strategies, providing a comprehensive view of climate's role in agricultural productivity.

To enhance this analysis, we’ll incorporate agricultural price data from the FAO’s Producer Prices dataset. This dataset includes prices farmers receive for primary agricultural products across 180 countries since 1991 ([FAO link](https://bulks-faostat.fao.org/production/Prices_E_All_Data_(Normalized).zip)). By linking yield data with pricing, we can assess how climate-driven changes in productivity influence farmers’ income, offering insights into economic stability and resilience strategies in agriculture.

### Research Questions

1. How do climate variables like temperature, precipitation, and CO₂ emissions affect crop yields across different regions?
2. How does climate-driven yield change impact agricultural income, and what are the projected economic consequences for farmers over time?

### Proposed Solution

We propose to create a predictive data science model that evaluates the effect of various climate variables on crop yield across multiple regions. The model will use the dataset, which includes features like temperature, precipitation, and other agronomic and environmental factors, such as CO₂ emissions, irrigation access, pesticide use, and adaptation strategies. Additionally, we plan to incorporate economic impacts and extreme weather events to understand their combined effects on agricultural productivity.

Our project will involve the following steps:

**1. Data Cleaning and Preprocessing:** We will handle missing values, standardize units, and ensure that all numerical and categorical data is properly formatted for analysis.

**2. Exploratory Data Analysis (EDA):** Using EDA techniques, we will identify trends in crop yields, extreme weather patterns, and regional variations in climate and productivity.

**3. Augmenting with Additional Data Sources:** To enhance the dataset, we will integrate agricultural price data from the FAO’s Producer Prices dataset, which includes prices received by farmers for primary crops across various countries. This will allow us to link climate-driven productivity changes with economic outcomes for farmers, offering insights into income fluctuations and enabling us to develop policy recommendations for income stabilization and economic resilience in the face of climate change.

**4. Interactive Dashboard:** We will develop a dashboard to visualize climate impacts, economic outcomes, and adaptation strategy effectiveness, enabling users to interactively explore the data.

**5. Modeling:** We will build a predictive model using explainable machine learning algorithms, enabling us to understand the influence of various climate and agronomic factors on crop yield. 

**6. Interpretability:** By focusing on model interpretability, we aim to provide clear insights into how each feature impacts productivity, supporting data-driven recommendations for climate resilience and agricultural decision-making.

### Conclusion

Our project will result in a comprehensive analysis of the climate variables most affecting agricultural productivity and a predictive model. This will provide actionable insights to help understand climate change impacts on agriculture. 


________________________________________________________________________________________________________________________________________________

### Data Analysis and Sketching

### Data Analysis Overview

The primary dataset, Climate Change Impact on Agriculture, required minimal cleaning as it contained no null values. Statistical analysis was conducted to gain insights into the various columns, providing a clear understanding of the data. In contrast, the secondary dataset, the Food and Agriculture Organization's Producer Price dataset, required more preprocessing. This included renaming countries and columns for consistency, removing unnecessary columns with null values, and retaining only the relevant price-crop relations.


![The above image shows the code to rename the columns](/Images/Preprocessing1.jpeg )
The above image shows the code to rename the columns.


![Merge](/Images/Merge.jpeg )
The above image are the top 5 rows of the merged datasets.


![Description](/Images/Description.jpeg )
Above are the descriptive statistics of the merged dataset.

After preprocessing, the two datasets were merged based on country, year, and crop type to create a comprehensive dataset for further analysis. This merged dataset serves as the foundation for comparing crops across countries and years, with respect to key features such as average temperature, total precipitation, CO2 emission rate, crop yield, and producer price (in USD).

To better understand the relationships between these features, a correlation matrix was created. This analysis provided valuable insights into how these variables interact, guiding the development of strategies and next steps to address the research questions effectively.


![Correlation Matrix](/Images/Correlation_Matrix.jpeg )


### Dashboard Sketching

![Dashboard Sketch](/Images/Dashboard_Sketch.png)

The dashboard includes user inputs such as Year and Crop Type, which apply globally to all sections. These filters allow users to dynamically tailor the visualizations to focus on specific time periods or crop types. The dashboard is divided into four main sections:

1. World Map: Crop Yield Distribution

    Visualization: A world map highlighting crop yield distribution across countries in a selected year for the chosen crop.
    Purpose: Provides a global perspective of agricultural productivity, enabling users to identify high and low yield regions at a glance.
    Implications: The map allows policymakers and stakeholders to:
        Identify regions performing well for a particular crop.
        Highlight areas requiring attention due to poor yields.

2. Scatter Plot: Relationship Between Crop Yield and Climate Variables

    Visualization: A scatter plot displaying the relationship between crop yield and selected climate variables such as precipitation, temperature, and CO2 emissions.
    User Input:Dropdown menu to select the X-axis variable (e.g., Precipitation, Temperature, CO2 Emissions).
    Insights:
        Precipitation: Regions with moderate precipitation levels tend to achieve higher yields, whereas extreme levels often reduce productivity.
        Temperature: Crop yields show sensitivity to temperature ranges, highlighting the importance of suitable climatic conditions.
        CO2 Emissions: Allows exploration of the environmental impacts on agricultural output.
    Implications: Enables researchers to study how climate change variables directly impact productivity and develop targeted adaptation strategies.

3. Bar Graph: Crop Price Variations by Country
    
    Visualization: A horizontal bar graph showing crop price variations for each country based on the selected crop and year.
    Purpose: Facilitates comparison of economic factors influencing agricultural practices globally.
    Implications:
        Helps users identify countries where crops are most valuable.
        Highlights economic disparities and market opportunities for stakeholders.
4. Key Insights Section
    
    Insights Highlighted:
        Highest Yield Region: The country or region achieving the highest yield for the selected crop and year.
        Best Soil Health Index: Regions with optimal soil health contributing to sustainable agriculture.
        Largest Economic Impact: Countries with the highest economic contributions from agriculture.
    Purpose: Provides quick, actionable insights at a glance, summarizing the most critical information for decision-making.

Further enhancements to the dashboard aim to incorporate additional graphs that highlight the relationship between climate variables and farmer welfare, focusing on income derived from agriculture. These visualizations will include line or bar graphs to display trends in farmer income across regions and scatterplots or heatmaps to explore the influence of precipitation, temperature, and CO2 emissions on agricultural income. The goal is to establish a clear connection between environmental conditions and socio-economic outcomes, thereby helping identify vulnerable farming communities and proposing interventions to enhance their well-being.








