# Environmental Impact of Food Production
## A Spatial Data Science Analysis of Global Food Emissions

![Global Food Emissions Map](reports/figures/global_map.png)


## Overview

This project analyzes global food production emissions using spatial data science and machine learning techniques.

By integrating FAOSTAT production data (1961–2022) with environmental footprint datasets, this study identifies geographic emission hotspots, product-level environmental impacts, and country-level emission patterns.

The final Random Forest regression model achieved:

- R² Score: 99.93%
- Mean Absolute Percentage Error (MAPE): 4.02%

The analysis reveals that nearly half of global food-production emissions originate from only five countries.

1 Brazil 19,440 16.4% ████████████████████████████████</br>
2 India 15,445 13.0% ██████████████████████████████</br>
3 China 10,219 8.6% ████████████████████</br>
4 United States 6,070 5.1% ███████████</br>
5 Indonesia 3,715 3.1% ██████</br>
6 Pakistan 2,784 2.3% █████</br>
7 Thailand 2,585 2.2% █████</br>
8 Mexico 1,768 1.5% ███</br>
9 Australia 1,319 1.1% ██</br>
10 France 1,269 1.1% ██</br>


</br>

</br></br></br>




[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Spatial Data Science](https://img.shields.io/badge/Spatial-Data_Science-green.svg)](https://github.com/)
[![Regression R²=0.999](https://img.shields.io/badge/Regression-R²_0.999-brightgreen.svg)]()

> **Predicting and mapping environmental impacts of global food production using spatial regression analysis**

## 📋 Executive Summary

This project integrates **FAOSTAT agricultural production data** (1961-2022, 200+ countries) with **product-level environmental footprints** to answer critical questions about food system emissions.

### Key Achievements

| Metric | Result |
|--------|--------|
| **Variance Explained** | 99.93% (R² = 0.9993) |
| **Prediction Accuracy** | 4.02% MAPE |
| **Data Coverage** | 14,045 country-years, 1961-2022 |
| **Top 5 Countries Share** | 47.7% of global emissions |

### 🎯 Key Finding

> **Food production emissions are hyper-concentrated in Asia and South America, driven by a small number of high-intensity products (coffee, chocolate, beef), with just 5 countries accounting for nearly half of global emissions.**

---

## 📊 Visual Highlights

| Top 10 Emitting Countries | Global Emissions Heatmap |
|:-------------------------:|:------------------------:|
| ![Top 10](outputs/figures/top_10_countries.png) | ![Spatial Map](outputs/figures/spatial_emissions_map.png) |

| Emissions Trend (1961-2022) | Feature Importance |
|:---------------------------:|:------------------:|
| ![Trend](outputs/figures/emissions_trend.png) | ![Features](outputs/figures/feature_importance.png) |

---

## 🔍 Research Questions

1. **What** are the environmental impacts of food production?
2. **Where** are these emissions produced geographically?
3. **Can we predict** emissions from production patterns alone?
4. **Which countries and products** should be prioritized for mitigation?

---

## 📁 Repository Structure
