import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x     = np.arange(1, 6)
y     = np.array([1.0, 2.1, 1.8, 3.2, 2.9])
yerr  = np.array([0.2, 0.15, 0.3, 0.25, 0.2])

fig, ax = plt.subplots(figsize=(6, 4))
ax.errorbar(
    x, y, yerr=yerr,
    fmt="o",            # markers only (no connecting line)
    markersize=6,
    linestyle="",
    capsize=5,          # length of the little “caps”
    capthick=1.5,       # thickness of caps
    elinewidth=1.2,     # thickness of the error bar itself
    alpha=0.9,          # subtle transparency
    zorder=3            # keep markers above grid
)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Example of nice error bars")
ax.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
