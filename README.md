# -US-Home-Prices-Analysis-
This repository contains a data science project that analyzes the impact of various national economic indicators on US home prices. Using the S&P Case-Shiller Index as a proxy for home prices for the last 20 years, the project examines factors such as GDP per capita, median household income,subsidies,construction cost and  more to understand their influence on the housing market.

# Steps to build the Project:
  1. **Data Acquisition:**
       * Retrieved the S&P Case-Shiller Home Price Index from the Federal Reserve Economic Data (FRED) website to represent home prices.
       * Compiled data on national economic factors impacting home prices, including GDP per capita, CPI, construction costs, median household income, housing subsidies, and demographic information.

  2. **Data Cleaning and Processing and Visulaization:**
       * Processed the data by addressing missing values, converting date formats, and handling outliers to ensure accuracy
       * Conducted EDA to analyze variable distributions, identify correlations, and visualize historical trends.
       * Visualizing relationship between data features by sns heatmap and pairplot and time series analysis to indtify seasonality.

  3. **Models:**
       * Implemented various regression models, including Linear Regression,Random Forest Regressor and Neural Network on same dataset to figure out best model for prediction.

  4. **Training and evaluation:**
       * Trained each model using tarin dataset, evaluated performance using metrics such as Mean Squared Error (MSE) and R-squared on test dataset.

  5. **Indentifying Influential Features:**
       * Identified feature importance for models like Random Forest. Also identifying best features through correlation matrix. In case of neural network, the number of perceptron are more to increase the variance of the model.

  6. **Outcome:**
     * Identified the most effective model based on its low Mean Squared Error (MSE) and high R-squared values.
     * Drew insights into the key factors that have historically impacted U.S. home prices.

# Results:
![image](https://github.com/user-attachments/assets/6731ff09-ff2e-41b8-84a1-3e1e20ec2870)
* Low MSE value means the the model predictions are accurate.
* High R-squared value signifies that the trends in data can be explained by the selected model.
* Random Forest and Neural Network Model appear to be best predictor model as they have low mean square error and high r-squared value.
* Neural Network Model has slightly high mse value and is more complex and need more computation(1000 epochs) which makes Random Forest Regressor model the best performing model for U.S. house price prediction.
* Linear Regression has high mean squared error which makes it less accurate in prediction over the test dataset despite its high r-squared value.

**Best Model:** The Random Forest regressor model is the best performing model having high r-squared value of 0.9979836509403485 and low mean squared error of 3.5337592863302367.

**Important Features:** The features such as Construction Price, CPI, Subsidies, median_income and Per Capita GDP are the most important features.

Increase in the Construction Material Prices would greatly influence the U.S. house prices and so does the Consumer Price Index which is indicative of period of inflation.

The correlation matrix calculated during EDA also shows the same features as most important.


  


