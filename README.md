# Global Data on Sustainable Energy (2000-2020)
https://www.kaggle.com/datasets/anshtanwar/global-data-on-sustainable-energy/data


Its a data on customer of a bank is operating in global market.


This is aggregated data, i.e. there are multiple customers per row. Dimensions tend to be earlier columns, measures to the right.

# Questions

## 1. Access to Electricity of Population(%) (By Country with Map Slider)

## 2. Renewable Energy percentage(%) of total final energy consumption (By Country with Map Slider)

## 3. Top 10 Countries with electricity from renewable energy

## 4. Top 10 Countries with most CO2 Emissions

## 5. Compare Electricity production from fossil and renewable source (By Year)

## 6. CO2 Emission and PP Health Expense(USD)

## 7. How Forest is dcreasing from 2000 to 2020

# Visual Presentation
## PPT

[ppt](visual_presentation.pptx)

## Tableau

[Tableau](https://public.tableau.com/app/profile/md.abu.yusuf/viz/Customerbaseglobalretailbank/GlobalretailBankDashboard?publish=yes)

# Summary and conclusions

## After concluded the project I am very much excited to share rich insights and exploration of data on global sustainable energy. In addition, happy to share that I included few more data got through API of World Bank. It makes the original data richer and provides different dimensions to think.

## From the beginning of the project handle the data very carefully. Follow all the processes cleaning, wrangling, EDA, visual report,processing data, model train, test and prediction test score.

## The significant findings are:

### 1. Electricity access to population increases in every country

### 2. Countries are successful to level up renewable energy to  their national grid. Hence, Middle African countries are   
treating as examples.

### 3. The more developed countries emit more CO2 in the environment though they produce significant electricity 
from natural resources. ex: China, USA etc.

### 4. Per person health expenses are gradually increases while CO2 emissions also gradually increases except in the
year 2020 

### 5. Global energy has an impact on forest. Its decreases from 2000 to 2020

### 6. Few features in the data are closely correlated to each other. Findings those through the correlation matrix

### 7. Used three Machine Learning algorithms for two sets of targets and features to find out a appropriate model.    
For both cases Random Forest algorithm performs very well for target 'primary_energy_consumption_per_capita_kwh_person' and 'value_co2_emissions_kt_by_country' 0.885764 and 0.995015  
respectively.