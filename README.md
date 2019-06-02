rs_estimators
-------------

A set of scikit-learn compatible python wrappers around rust 

Example of rust-numpy
======================

- Prerequirement

```
sudo pip3 install -r requirements.txt
```

- Build

```
python3 setup.py develop --user
```

- Run

```python
import numpy as np
from rs_estimator import axpy

a = np.array([0.0, 1.0])
b = np.array([2.0, 3.0])
axpy(2.0, a, b)
```
which returns `array([2., 5.])`.
