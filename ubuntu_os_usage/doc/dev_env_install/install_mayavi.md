# ubuntu 安装 mayavi

## pip 安装 mayavi

```
python3 -m virtualenv --no-site-packages 3d-visualize
source 3d-visualize/bin/active
pip3 install mayavi
```

注意: 不要加 sudo, 否则会安装到系统路径的 python 中.  

## 测试代码  

使用下面的测试代码, 检查安装是否成功. 

```py
# Create the data.
from numpy import pi, sin, cos, mgrid
dphi, dtheta = pi/100.0, pi/100.0
[phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)

col = z

# View it.
import mayavi.mlab
fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 480))
mayavi.mlab.points3d(x, y, z,
                         col,   # Values used for Color
                         mode="point",
                         colormap='spectral', # 'bone', 'copper', 'gnuplot', 'spectral'
                         color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                         figure=fig,
                         )
# s = mayavi.mlab.mesh(x, y, z)
mayavi.mlab.show()
```
