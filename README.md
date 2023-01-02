# Used_Car_Prices
Predicting used car prices in New York and California using ANN and Linear Regression

![car](https://github.com/Jayem-11/Used_Car_Prices/blob/main/car.jpg)
photo credits: [Pixabay](http://pixabay.com/)  

## Description: 
The system Predicts used car prices using Artificial Nueral Networks based on data collected from New York and Carlifonia

## Author
- Github [@JM_Rono](https://github.com/Jayem-11)
- Linked_in [@John Michael Rono](https://www.linkedin.com/in/john-michael-rono-26a2b6183/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BGItpY4FbT0mUzd4XQz%2FwxQ%3D%3D)

## Table of Contents
[A Data](#dt) <br>
[B Machine learning](#ml) <br>
[C Deploying](#dp) <br>

## Tech Stack
- Beautiful soup
- Power BI
- PostgreSQL
- Scikit-learn
- Tensorflow
- Keras
- Streamlit


## <span id="dt">A. Data </span>

- Check-out notebook:  [@notebook](https://github.com/Jayem-11/Used_Car_Prices/blob/main/Data/scrap_data_from_web.ipynb)

## 
The used car dataset is obtained from Truecar which is a leading automotive digital marketplace that seeks to make car buying and selling easy, transparent and efficient.

From discovery to delivery, consumers can use TrueCar to explore new and used vehicles from an expansive, cross-brand selection of inventory from our vast network of Certified Dealers.

Founded in 2005, [TrueCar](https://www.truecar.com/) has built a trusted brand and a strong reputation for providing consumers with useful tools, research, market context and pricing transparency as they embark on their car-buying journey. The Company is bringing more of the purchasing process online by allowing consumers to find a new or used vehicle that is right for them, secure financing, sell or trade-in their current vehicle and complete their purchase with a reputable dealer all from the comfort of their home.


##
The Data consist of more than 10,000 entries.
![Jupyter notebook example](https://github.com/Jayem-11/Used_Car_Prices/blob/main/Data/df.png)
## 

### Database 
- I used PostgreSQL to store the data scraped
## 
![Jupyter notebook example](https://github.com/Jayem-11/Used_Car_Prices/blob/main/Data/database.png)

### Data Visualzation with Power BI
- [Link](https://app.powerbi.com/groups/me/reports/c6ea12d6-be64-4ee2-b66f-3773ceaeb40c/ReportSection?bookmarkGuid=902dc690-13cb-4264-a634-939f6cab8e97&bookmarkUsage=1&ctid=0765532a-06c1-4f0f-9f39-394689f5f8fe&fromEntryPoint=export) to PowerBi Dashboard
## 
![Jupyter notebook example](https://github.com/Jayem-11/Used_Car_Prices/blob/main/Data/powerbi_visuals.png)

## 
## <span id="ml">B. Machine Learning </span>

- Check-out notebook:  [@notebook](https://github.com/Jayem-11/Used_Car_Prices/blob/main/Machine_learning/used_car_prices.ipynb)

### Model

The ANN model perforemed better on the data compared to the linear regression model.

### Evaluation

![Jupyter notebook example](https://github.com/Jayem-11/Used_Car_Prices/blob/main/Machine_learning/result.png)


- Since our mean absoulute error is 5802, it means we are off by about 19% from the mean. ANN model is better than Linear regression model since it has a lower error from the mean





























