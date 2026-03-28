import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid') 
def three_d_surface(x, y):
    """calculate height z based on x and cordinates."""
    return np.sin(np.sqrt(x**2 + y**2))
x_values = np.linspace(-6, 6, 40)
y_values = np.linspace(-6, 6, 40)
x, y =np.meshgrid(x_values, y_values)
z = three_d_surface(x, y)
fig = plt.figure(figsize=(10, 8))
ax =fig.add_subplot(111, projection ='3d')
surface = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none', alpha=0.9)
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10, label='height (z)')
ax.set_xlabel('x distance')
ax.set_ylabel('y distance')
ax.set_zlabel('z height')
ax.set_title('topography of the data: A 3D surface plot', fontsize=14)
ax.view_init(elev=20, azim=35)
plt.tight_layout()
plt.show()
