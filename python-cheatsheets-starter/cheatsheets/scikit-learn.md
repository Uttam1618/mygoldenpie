# scikit-learn Cheat Sheet

```python
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```
## Train / Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
```
## Pipeline + Scale + Model
```python
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000))
])
pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
print(accuracy_score(y_test, pred))
```
## Cross-Validation
```python
cv = cross_val_score(pipe, X, y, cv=5, scoring="accuracy").mean()
```
## Grid Search
```python
param_grid = {"clf__C":[0.1,1,10]}
grid = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```
## Metrics
```python
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
```
## Persist Model
```python
import joblib
joblib.dump(grid.best_estimator_, "model.joblib")
model = joblib.load("model.joblib")
```