# Keras (tf.keras) Cheat Sheet

Keras is bundled with TensorFlow as `tf.keras`.

```python
import tensorflow as tf
from tensorflow import keras
```
## Sequential Example
```python
model = keras.Sequential([
    keras.layers.Dense(128, activation="relu", input_shape=(X.shape[1],)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax")
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.1)
```
## Callbacks
```python
cb = [
    keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
    keras.callbacks.ModelCheckpoint("best.keras", save_best_only=True)
]
model.fit(X_train, y_train, epochs=50, callbacks=cb)
```