import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (4, 4) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

## Plot Training Sample and Mesh
def plot_classifier(Xtr, ytr, alpha = 0.2, alpha_pt = None, fn = None, h = 0.01, file = None):

    fig = plt.figure(figsize = (4, 4))
    
    if fn:
        
        xx, yy = np.meshgrid(np.arange(-1.3, 1.3, h),np.arange(-1.3, 1.3, h))
        Z = fn(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)

        plt.contourf(xx, yy, Z, cmap=plt.cm.viridis, alpha = alpha)


    if alpha_pt: alpha = alpha_pt
    plt.scatter(Xtr[:, 0], Xtr[:, 1], c=ytr, s=40, cmap=plt.cm.viridis, alpha = alpha, linewidth = 0.1)
    
    plt.xlim([-1.3, 1.3])
    plt.ylim([-1.3, 1.3])
    
    if file: fig.savefig(file, bbox_inches='tight', pad_inches=0.1)



## Define a Spiral Dataset
def spiral_data(K, N = 1000, D = 2, noise_level = 0.4):

    X = np.zeros((N*K,D))
    y = np.zeros(N*K, dtype='uint8')
    for j in range(K):

        ix = range(N*j,N*(j+1))

        spiral = np.linspace(0, 1.5 * np.pi,N)
        offset = 2 * np.pi * j / K
        noise  = np.random.randn(N)*noise_level

        theta  = spiral + noise + offset

        r = np.linspace(0.0,1,N) # radius    

        X[ix] = np.c_[r*np.sin(theta), r*np.cos(theta)]
        y[ix] = j # class
        
    return X, y


## Define a blob dataset.
def blob_data(X = 2, Y = 2, N = 1000, D = 2, correlated = 0.5, noise_level = 1.0):

    K = X * Y
    
    par = np.zeros((N*K,D))
    cat = np.zeros(N*K, dtype='uint8')
    
    xstart = -0.5 if X > 1 else 0
    ystart = -0.5 if Y > 1 else 0
    
    xx, yy = np.meshgrid(np.linspace(xstart, 0.5, X), 
                         np.linspace(ystart, 0.5, Y))
    
    for j, (xctr,yctr) in enumerate(zip(xx.ravel(), yy.ravel())):

        ix = range(N*j,N*(j+1))

        corr = np.random.randn(N) * correlated 
        uncorr_x = np.random.randn(N) * (1 - correlated)
        uncorr_y = np.random.randn(N) * (1 - correlated)

        x = (corr + uncorr_x) * noise_level + xctr
        y = (corr + uncorr_y) * noise_level + yctr

        r = np.linspace(0.0,1,N) # radius    

        par[ix] = np.c_[x, y]
        cat[ix] = j 
        
    return par, cat
