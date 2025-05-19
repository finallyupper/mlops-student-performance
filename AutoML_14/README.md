# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_Baseline](1_Baseline/README.md)                           | Baseline       | mse           |       1.01361  |         1.72 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | mse           |       0.897548 |        18.93 |
|              | [3_Default_Xgboost](3_Default_Xgboost/README.md)             | Xgboost        | mse           |       0.815455 |        24.24 |
|              | [4_Default_NeuralNetwork](4_Default_NeuralNetwork/README.md) | Neural Network | mse           |       0.814497 |         7.93 |
|              | [5_Default_RandomForest](5_Default_RandomForest/README.md)   | Random Forest  | mse           |       0.87064  |        24.21 |
| **the best** | [Ensemble](Ensemble/README.md)                               | Ensemble       | mse           |       0.808834 |         0.29 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)

### Features Importance
![features importance across models](features_heatmap.png)



### Spearman Correlation of Models
![models spearman correlation](correlation_heatmap.png)

