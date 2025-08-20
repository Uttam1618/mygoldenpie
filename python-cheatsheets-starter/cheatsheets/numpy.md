# NumPy Cheat Sheet

```python
import numpy as np
```
## Create
```python
np.array([1,2,3])
np.zeros((3,4)); np.ones(5); np.full((2,2), 7)
np.arange(0,10,2)     # 0..8 step 2
np.linspace(0,1,5)    # 5 points between 0..1
```
## Inspect / Shape
```python
a.shape; a.ndim; a.dtype; a.size
a.astype(np.float32)
```
## Index / Slice / Fancy
```python
a[0]; a[:3]; a[::2]; a[1:4, 2:5]
a[[0,2,4]]; a[a>0]      # boolean mask
```
## Reshape / Combine
```python
a.reshape(2, -1)
np.vstack([a,b]); np.hstack([a,b])
a.T; a.ravel()
```
## Math / Broadcasting
```python
a + 5; a * b; np.exp(a); np.log(a+1e-9)
a.mean(); a.std(); a.sum(axis=0)
```
## Random
```python
rng = np.random.default_rng(42)
rng.integers(0,10,size=5)
rng.normal(loc=0, scale=1, size=(2,3))
```
## Linear Algebra
```python
np.dot(A,B); A @ B
np.linalg.inv(A); np.linalg.eig(A)
np.linalg.solve(A, b)
```