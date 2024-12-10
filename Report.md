# Final Project Report
## Assessing the Impact of Climate Change on Agricultural Productivity

**Project URL**: TODO

**Video URL**: [Video Link](https://drive.google.com/file/d/16m7-kxxpcep9zdES6fj_2sQ3NMhoz9K5/view?usp=drive_link)

Climate change poses significant challenges to the agricultural sector, affecting crop yields, farmer incomes, and food security globally. Understanding the relationship between climate variables such as temperature, precipitation, and CO₂ emissions and their effect on crop yield is crucial for developing effective adaptation strategies. This project focuses on analyzing the impact of climate change on agricultural productivity across regions and crop types, with a particular emphasis on how climate-driven changes in yields influence farmers' economic outcomes.

We utilize a comprehensive dataset that includes climate metrics (e.g., average temperature, total precipitation, CO₂ emissions) along with crop yield for ten major countries. By integrating this dataset with producer price data from the FAO, we assess the economic consequences of climate-induced productivity changes. Our methodology involves exploratory data analysis and visualization to evaluate the effects of climate variables on crop yields and farmer incomes.

The proposed solution provides actionable insights through a combination of explainable analysis and an interactive dashboard. The dashboard enables stakeholders to explore trends in temperature, precipitation, and yield, as well as analyze economic disparities across regions. Our results highlight temperature thresholds beyond which yields decline, the sensitivity of crops to erratic precipitation, and the disproportionate economic impact across the globe.

By linking climate impact variables to crop yield, this project empowers policymakers and farmers with data-driven recommendations to improve the agricultural revenue generated in the face of ongoing climate change.

## Introduction
Climate change is among the most pressing challenges of our time, with profound implications for global food security. Changes in temperature, precipitation patterns, and the frequency of extreme weather events significantly affect agricultural productivity, altering crop yields and, consequently, farmer incomes. Understanding these impacts is crucial for devising strategies to mitigate risks, improve climate resilience, and ensure sustainable agricultural practices.

This project aims to analyze the relationships between climate variables (e.g., temperature, precipitation, CO₂ emissions) and agricultural productivity, with a focus on crop yield. Additionally, we assess the economic consequences of climate-driven changes in productivity by linking crop yield data with agricultural price data. Our goal is to provide actionable insights to policymakers, researchers, and farmers to adapt to changing climate conditions.

## Related Work
Climate change is profoundly influencing agricultural production and food systems across the globe. The rising temperatures, shifts in precipitation patterns, and increased frequency of extreme weather events are altering crop yields, agricultural incomes, and global trade. Several studies have highlighted these challenges and underscored the need for region-specific adaptation strategies to mitigate the negative consequences of climate change on agriculture.

Porfirio et al. (2018) [1] investigate how climate change may reshape global agricultural trade patterns, affecting food supply and markets. By coupling global crop models with economic models, their study suggests that under high CO₂ emissions scenarios, the agricultural trade network will become more centralized, with a few regions dominating the markets. In contrast, under a carbon mitigation scenario, the trade network becomes more distributed, potentially reducing vulnerabilities to climate or institutional shocks. This finding emphasizes that mitigating CO₂ emissions benefits the environment and can enhance the stability of global agricultural trade, thus contributing to food security and economic resilience.

Pulighe et al. (2024) [2] focus on Italy, where the Mediterranean climate makes agriculture highly vulnerable to climate change. Their scoping review of the impact of climate change on Italian agriculture covers viticulture, fruit and vegetable production, and dairy cattle farming. They find that rising temperatures, altered precipitation patterns, and extreme weather events are already affecting crop yields and income, with significant regional disparities observed. The study stresses the importance of localized assessments and adaptation strategies tailored to specific crops and farming systems, as these factors can vary significantly across regions.

Yuan et al. (2024) [3] provide a comprehensive review of the broader global impacts of climate change on agricultural production. The authors emphasize that global warming is one of the most significant threats to agricultural systems, influencing various environmental factors such as temperature, precipitation, wind speed, and the occurrence of extreme weather events. These factors disrupt crop growth cycles, increase pest and disease pressures, and ultimately affect crop yields and quality. The review highlights the need for adaptive strategies to ensure the sustainable development of agricultural production in the face of these changes.

Together, these studies underscore the need for a multi-faceted approach to understanding the complex interactions between climate change, agricultural production, and economic outcomes. They highlight the urgency of developing context-specific adaptation strategies that account for regional climate variability and the potential socio-economic consequences for farmers. These insights align closely with the objectives of the current research, which seeks to assess how climate-induced changes in agricultural productivity influence both crop yields and farmer incomes, offering guidance for policy development in the context of climate resilience.
## Methods

### Data Collection and Preprocessing

### 1. Datasets
- **Primary Dataset**: "Climate Change Impact on Agriculture" from Kaggle ([Link](https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture)). This dataset provides climate variables such as temperature, precipitation, CO₂ emissions, extreme weather events, and crop yield metrics across regions.
- **Secondary Dataset**: Producer Prices dataset from FAO ([Link](https://bulks-faostat.fao.org/production/Prices_E_All_Data_(Normalized).zip)). This dataset includes agricultural prices received by farmers for various crops across 180 countries since 1991, enabling an economic perspective on agricultural productivity.

### 2. Preprocessing
- **a. Standardizing Columns:**  Country names and column formats were harmonized across datasets to enable merging. Irrelevant or redundant columns were removed.
- **b. Handling Missing Values:** The FAO dataset contained missing or incomplete data, which was addressed by removing columns with high null ratios and imputing smaller gaps where necessary.
- **c. Data Integration:** Both datasets were merged based on shared attributes such as country, year, and crop type to form a comprehensive dataset. This combined data includes crop yields, climatic variables, and producer prices, enabling cross-dimensional analysis of climate impacts on agricultural productivity and farmer incomes.

### 3. Exploratory Data Analysis
To better understand relationships within the data, several statistical and visualization techniques were employed:
- **a. Correlation Matrix**: Revealed strong relationships between temperature, precipitation, and crop yields, highlighting critical climate variables impacting agricultural productivity.
- **b. Statistical Descriptions**: Provided insights into regional variations in crop productivity, soil health, and climate conditions, offering valuable context for further analysis.

### 4. Interactive Dashboard
An interactive dashboard was developed to provide a dynamic way to explore climate impacts and their effects on agricultural productivity. The dashboard is designed to cater to multiple user needs:
- **a. Crop Yield Distribution:** A global map allows users to explore crop yield distribution across countries for a selected year and crop type. For instance, the map highlights regions like India and Brazil for high sugarcane productivity.
- **b. Climate Variable Relationships:** Scatter plots dynamically illustrate the relationships between crop yields and key climate variables, such as temperature. Scatter plots help identify optimal temperature ranges for crop yields and thresholds where yields begin to decline. Addionally, a line graph is displayed to show the trend of increase in temperature throughout the years.
- **c. Economic Trends:** Bar charts visualize how the economic impact of these crops vary with change in precipitation, temperature, and amount of CO₂ emissions, enabling insights into economic disparities and climate-driven market shifts.

### 5. Visualization Techniques

The visualizations in the dashboard were built using **Plotly** and rendered in **Streamlit**:

- **World Map Visualization**:  
  Displays crop yield distribution for selected crop types and years. A choropleth map visualizes yield metrics, with color intensity indicating productivity levels across countries.
- **Scatter Plots**:  
  Scatter plots with trend lines demonstrate how climate variables (e.g., temperature) correlate with crop yields.
- **Line Graph**:  
  Portrays the temporal change in temperature to get an idea of why and how the crop yield changes throughout the years.
- **Bar Charts**:  
  Economic impacts are visualized through bar charts, grouping producer prices and economic impacts by climate variable ranges (e.g., temperature ranges of 15–25°C). Each chart includes legends for better interpretability.


### 6. Prediction Model

To complement the analysis and visualization, we implemented a **Decision Tree Regression Model** to predict the economic impact of climate factors on agricultural productivity. This model leverages environmental variables such as **average temperature (°C)**, **precipitation (mm)**, and **CO₂ emissions (MT)** as input features to estimate economic outcomes for farmers.

#### Model Implementation
- **Input Features**: The model takes three climate-related factors:
  - Average Temperature (°C)
  - Total Precipitation (mm)
  - CO₂ Emissions (MT)
- **Algorithm**: A Decision Tree Regressor was chosen for its ability to handle nonlinear relationships and provide interpretable results.

#### Interactive Prediction Tool
An interactive **Prediction Model** tab was developed in the dashboard to enable stakeholders to estimate economic impacts dynamically:
- **Inputs**: Users can adjust sliders to input specific values for average temperature, precipitation, and CO₂ emissions.
- **Output**: The dashboard calculates and displays the predicted economic impact based on the provided inputs, offering an intuitive and actionable interface for exploring climate-related economic outcomes.

This prediction capability enhances the system by allowing users to simulate various climate scenarios and understand their potential impacts on agricultural economics. For example, users can explore how a rise in temperature or changes in precipitation levels might affect farmer incomes, enabling data-driven decision-making for climate adaptation.

## Results

Our system produced a variety of interactive visualizations that comprehensively address the challenge of understanding climate change’s impact on agricultural productivity and its economic implications. 

One of the key visualizations, the global crop yield distribution map, highlights variations in productivity across countries for selected crops and years. For example, an analysis of sugarcane yields in 2017 shows high productivity in countries like India and Brazil, while arid or drought-prone regions exhibit lower yields. This visualization offers policymakers and farmers a global perspective, enabling them to identify high-performing regions and areas that require targeted interventions.

The line chart showcasing temperature changes over the years in the United States reveals a gradual but consistent warming trend. Although year-to-year fluctuations are evident, the trend line demonstrates an overall increase in average temperature over the past three decades. Such visualizations underline the pressing need for strategies to address the adverse effects of rising temperatures on crop productivity, such as introducing heat-resistant crop varieties or adjusting planting schedules.

The scatter plot illustrating the relationship between temperature and crop yield provides additional clarity. It demonstrates that moderate temperature ranges, typically between 10°C and 25°C, are associated with higher yields, while extreme temperatures, either too low or too high, result in diminished productivity. This insight is particularly valuable for identifying critical thresholds beyond which yields are adversely affected, enabling farmers and policymakers to adapt agricultural practices to mitigate these effects.

The economic trends visualizations further highlight the significant consequences of climate variability. Bar charts depict how economic impacts vary with temperature, precipitation, and CO₂ emissions. For instance, extreme rainfall events correspond to economic instability. These visualizations not only shed light on regional disparities but also provide a foundation for implementing targeted measures to stabilize farmer incomes and address climate-induced economic inequities. Overall, the system's ability to integrate climatic and economic datasets provides a multifaceted understanding of the problem, supported by accessible and interactive visualizations that aid in data-driven decision-making. Additionally, the prediction model achieved a high validation R² score of **0.97**, indicating excellent predictive accuracy and strong alignment between predicted and observed outcomes in the validation dataset.

## Discussion

This project offers valuable insights into the complex relationships between climate change, agricultural productivity, and economic stability. By combining data from multiple sources and presenting it in an interactive dashboard, the system equips policymakers, researchers, and farmers with the tools needed to analyze and adapt to climate impacts effectively. One of the most significant insights derived from this work is the critical role of climate variables in driving agricultural productivity. For example, the scatter plot analysis demonstrates that crops are highly sensitive to temperature thresholds, and the line chart on U.S. temperature trends underscores the urgent need to address the effects of rising temperatures on food security.

The inclusion of economic analyses further amplifies the system's utility by linking climate-induced changes in crop yields to farmer incomes. The bar charts reveal disparities in economic outcomes across regions and crop types, highlighting how climate variability disproportionately affects smallholder farmers in developing countries. This insight underscores the importance of implementing income stabilization policies, such as crop insurance or targeted subsidies, to mitigate the financial risks faced by vulnerable farming communities.

Beyond these findings, the system enables new practices for climate adaptation. By dynamically visualizing relationships between climate variables and crop yields, it empowers users to identify optimal conditions for specific crops. This allows for the development of tailored strategies, such as selecting climate-resilient crops or optimizing irrigation practices in water-scarce regions. Additionally, the interactive dashboard makes it easy for users to explore the data in depth, fostering transparency and accelerating decision-making processes.

From an observational standpoint, the system’s usability and interactivity are its key features. The ability to filter data by year, crop type, and climate variable makes complex datasets accessible, fostering engagement among policymakers and researchers. The use of trend lines in scatter plots and line charts enhances interpretability, ensuring that users can draw actionable insights with confidence. Overall, the system serves as a powerful tool for exploring the impacts of climate change on agriculture, providing a foundation for data-driven understanding and future research. Its broader implications extend to ensuring food security, addressing economic disparities to help farmers improve agricultural revenue in the face of global warming.

## Future Work

While our system effectively addresses the relationships between climate change, agricultural productivity, and economic outcomes, there are several avenues for extending and refining the application to further enhance its utility and impact.

One significant area for future work involves incorporating more granular datasets. For example, integrating detailed soil health metrics and land use patterns could provide a deeper understanding of how specific agronomic factors interact with climate variables to influence crop yields. Soil quality, fertility, and water retention capacity are critical determinants of agricultural productivity, and their inclusion could refine the model’s predictions and recommendations.

Another promising direction is the incorporation of climate projection data. Leveraging predictive climate models would allow the system to forecast future changes in temperature, precipitation, and CO₂ levels, enabling stakeholders to anticipate long-term impacts on agricultural productivity and prepare adaptive strategies. These forecasts could also be linked with economic projections to provide insights into future farmer incomes and market dynamics.

Additionally, integrating satellite and remote sensing data would offer real-time monitoring capabilities for key indicators like vegetation health, drought conditions, and water availability. This would enhance the system’s relevance for decision-making in scenarios requiring immediate action, such as responding to extreme weather events or managing water resources during droughts.

The system could also be extended to include regional case studies and adaptation strategies. By focusing on specific regions, the dashboard could provide localized insights and tailored recommendations, such as suggesting drought-resistant crops for arid regions or identifying optimal planting schedules based on historical weather patterns.

Another area for refinement is the development of more sophisticated economic models to quantify the financial impacts of climate change on agriculture. For example, incorporating market dynamics, supply chain disruptions, and trade policies could provide a more comprehensive view of how climate-induced changes in agricultural productivity affect global and local economies.

Finally, enhancing the system’s user interface and interactivity could make it even more accessible to non-technical stakeholders. Features like natural language queries, where users can ask questions in plain language and receive tailored visualizations or insights, would significantly broaden the application’s usability. Additionally, providing customizable reports based on user inputs could make the system more actionable for policymakers, researchers, and farmers.

## References
[1]	Porfirio, L.L., et al. “Economic Shifts in Agricultural Production and Trade Due to Climate Change.” Palgrave Communications, vol. 4, no. 111, 2018, https://doi.org/10.1057/s41599-018-0164-y.

[2]	Pulighe, G., et al. “Climate Change Impact on Yield and Income of Italian Agriculture System: A Scoping Review.” Agricultural Economics, vol. 12, no. 23, 2024, https://doi.org/10.1186/s40100-024-00317-7. 

[3]	Yuan, X., et al. “Impacts of Global Climate Change on Agricultural Production: A Comprehensive Review.” Agronomy, vol. 14, no. 7, 2024, p. 1360, https://doi.org/10.3390/agronomy14071360.
