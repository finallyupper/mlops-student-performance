# Summary of 3_Default_NeuralNetwork_KMeansFeatures

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True

## Optimized metric
mae

## Training time

10.5 seconds

### Metric details:
| Metric   |    Score |
|:---------|---------:|
| MAE      | 0.732283 |
| MSE      | 0.830639 |
| RMSE     | 0.911394 |
| R2       | 0.187761 |
| MAPE     | 1.79277  |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
