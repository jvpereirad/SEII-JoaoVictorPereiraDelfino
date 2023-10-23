# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import matplotlib.pyplot as plt 
import numpy as np

x1 = np.arange(0, 1000, 1)
#print(x1)

plt.plot(x1, x1**2)
plt.show()
# -


