from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
X,Y,Z,value = [],[],[],[]
table = open("4_columns.csv").readlines()[1:]
for line in table:
    x,y,z,val = line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3].strip()
    X.append(int(x))
    Y.append(int(y))
    Z.append(int(z))
    value.append(int(val))
    

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
#surf = ax.plot_surface(X,Y,value)
surf =ax.scatter(X,Y,value)
plt.show()
plt.savefig("demo.png")
