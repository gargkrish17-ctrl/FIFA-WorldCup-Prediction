#FIFA WORLD CUP PREDICTION
- Gaussian Naive Bayes achieved the best classification performance among all tested models.
- Reducing feature dependency improved Naive Bayes performance by better aligning the data with its independence assumption, while KNN remained the weakest-performing model.
- Experience_Diff consistently reduced model performance, indicating that historical World Cup participation alone was not a strong predictor of match outcomes and introduced noise rather than useful information.
- GridSearchCV improved Random Forest performance compared to the baseline model, though it did not surpass Naive Bayes.
- Naive Bayes and Random Forest produced similar Home Win % and Away Win % trends, but differed noticeably in their Draw % probability forecasts.
