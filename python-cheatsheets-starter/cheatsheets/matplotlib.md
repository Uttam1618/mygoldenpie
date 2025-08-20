# Matplotlib Cheat Sheet

```python
import matplotlib.pyplot as plt
```
## Quick Line Plot
```python
plt.plot(x, y)
plt.title("Title"); plt.xlabel("x"); plt.ylabel("y")
plt.legend(["series A"])
plt.show()
```
## Scatter / Bar / Hist
```python
plt.scatter(x, y)
plt.bar(categories, values)
plt.hist(data, bins=30)
```
## Subplots
```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(title="My plot", xlabel="x", ylabel="y")
plt.show()
```
## Save Figure
```python
plt.savefig("figure.png", dpi=200, bbox_inches="tight")
```