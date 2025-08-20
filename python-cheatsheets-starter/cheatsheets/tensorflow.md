 # TensorFlow Cheat Sheet

```python
import tensorflow as tf
```
## Build → Compile → Fit
```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X.shape[1],)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)
```
## Evaluate / Predict
```python
model.evaluate(X_test, y_test, verbose=0)
proba = model.predict(X_test)
pred = (proba > 0.5).astype("int32")
```
## Save / Load
```python
model.save("model.keras")        # or .h5
loaded = tf.keras.models.load_model("model.keras")
```
## tf.data (mini)
```python
ds = tf.data.Dataset.from_tensor_slices((X, y)).shuffle(1000).batch(32).prefetch(tf.data.AUTOTUNE)
model.fit(ds, epochs=5)
```
