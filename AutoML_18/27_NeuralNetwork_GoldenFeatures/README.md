# Summary of 27_NeuralNetwork_GoldenFeatures

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 16
- **learning_rate**: 0.01
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.9
 - **shuffle**: True

## Optimized metric
mae

## Training time

8.1 seconds

### Metric details:
| Metric   |    Score |
|:---------|---------:|
| MAE      | 0.734852 |
| MSE      | 0.819039 |
| RMSE     | 0.905007 |
| R2       | 0.199104 |
| MAPE     | 1.65562  |



## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
## True vs Predicted

![True vs Predicted](true_vs_predicted.png)


## Predicted vs Residuals

![Predicted vs Residuals](predicted_vs_residuals.png)



[<< Go back](../README.md)
