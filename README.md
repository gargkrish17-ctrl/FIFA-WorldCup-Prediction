
# FIFA World Cup 2026 Prediction
This project developed machine learning models to predict FIFA World Cup match outcomes using historical tournament data and FIFA team rankings. Among all models tested, the tuned Random Forest Classifier achieved the best performance and was selected as the final prediction model.

Feature engineering played an important role in model performance. Goal_Avg_Diff provided a slight improvement for Logistic Regression but reduced the performance of Random Forest, suggesting that its usefulness depends on the learning algorithm. Experience_Diff consistently reduced model accuracy and was therefore excluded from the final feature set.

Hyperparameter tuning using GridSearchCV improved the Random Forest model compared to its default configuration, highlighting the importance of model optimization. The final model was then used to generate Home Win, Away Win, and Draw probabilities for FIFA World Cup 2026 fixtures.

Overall, the project demonstrates how historical performance data, FIFA rankings, and carefully selected engineered features can be combined to build an effective sports outcome prediction system.
