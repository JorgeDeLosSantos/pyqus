# -*- coding: mbcs -*-
import numpy as np
from numpy import nan

warning = "We suggest you use Matplotlib instead of PyQus Graph module"
import_error_str = """
Please install Matplotlib package (http://matplotlib.org/users/installing.html)

Warning: %s
"""%(warning)
# Print warning everywhere

print(warning)

a = 10

try:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import mpl_toolkits.mplot3d.art3d as art3d
    from matplotlib.patches import Polygon
except ImportError:
    print import_error_str


def plot_dfile(figname,filename,xlabel="X",ylabel="Y",dlm=","):
    """
    Plot a data file with two columns, separated by a delimiter.
    
    Parameters
    ----------
    figname: str
        Name of output picture  i.e. "image.png"
    filename  : str
        Filename   i.e. "data_file.txt"
    xlabel : str
        X-Axis Label  i.e. "Time (s)"
    ylabel : str
        Y-Axis Label  i.e. "Stress (MPa)"
    dlm    : str
        Delimiter  i.e. ","
    """
    D = np.loadtxt(filename, delimiter=dlm)
    XX = D[:,0]
    YY = D[:,1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(XX,YY)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.savefig(figname)


def plot_nodes(figname,nodesfile="nodes.txt",dlm=","):
    """
    Plot nodes, the data file must be contain two columns: 
    X and Y coordinates for each node separated by delimiter dlm.
    
    Parameters
    ----------
    figname   : str
        Name of output picture
    nodesfile : str
        Filename for nodes data   i.e. "data_file.txt"
    dlm       : str
        Delimiter    i.e.  "," or "\t"
    """
    D = np.loadtxt(nodesfile, delimiter=dlm)
    XX = D[:,0]
    YY = D[:,1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(XX,YY,"ko",markersize=1.0)
    plt.axis('equal')
    plt.savefig(figname)


def plot_elements(figname="elements.png",nodesfile="nodes.txt",elementsfile="elements.txt",dlm=","):
    """
    Plot nodes and elements of mesh.
    
    Parameters
    ----------
    figname      : str
        Name of output picture
    nodesfile    : str
        Path of node data file
    elementsfile : str
        Path of elements conectivity file
    dlm          : str
        Delimiter (i.e. ",","\t")
    """
    NC = np.loadtxt(nodesfile, delimiter=dlm)
    EC = np.loadtxt(elementsfile, delimiter=dlm)
    f = plt.figure()
    ax = f.add_subplot(111)
    plt.hold(True)
    for element in EC:
        XX = []
        for node in element:
            if str(node)!="nan":
                XX.append([NC[node-1,0],NC[node-1,1]])
        p = Polygon(XX, True, fc="#00DDDD", ec="#778877")
        ax.add_patch(p)
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(figname)
    

def plot3D_elements(figname="elements.png",nodesfile="nodes.txt",elementsfile="elements.txt",dlm=","):
    """
    Plot nodes and elements of mesh.
    
    Parameters
    ----------
    figname      : str
        Name of output picture
    nodesfile    : str   
        Path of node data file
    elementsfile : str 
        Path of elements conectivity file
    dlm          : str
        Delimiter (i.e. ",","\t")
    """
    NC = np.loadtxt(nodesfile, delimiter=dlm)
    EC = np.loadtxt(elementsfile, delimiter=dlm)
    fig =plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    plt.hold(True)
    for CURE in EC:
        TEC = np.array([
                [CURE[0],CURE[1],CURE[2],CURE[3]],
                [CURE[2],CURE[5],CURE[6],CURE[2]],
                [CURE[5],CURE[4],CURE[7],CURE[6]],
                [CURE[4],CURE[0],CURE[3],CURE[7]],
                [CURE[3],CURE[2],CURE[6],CURE[7]],
                [CURE[0],CURE[4],CURE[5],CURE[1]]])
        for telement in TEC:
            XX,YY,ZZ = ([],[],[])
            for node in telement:
                XX.append(NC[node-1,0])
                YY.append(NC[node-1,1])
                ZZ.append(NC[node-1,2])
            ax.plot_wireframe(XX,YY,ZZ,facecolor="#fefefe")
    ax.set_xlim(np.min(NC[:,0]),np.max(NC[:,0]))
    ax.set_ylim(np.min(NC[:,1]),np.max(NC[:,1]))
    ax.set_zlim(np.min(NC[:,2]),np.max(NC[:,2]))
    ax.view_init(45,120)
    plt.axis('equal')
    plt.axis('off')
    #plt.show()
    plt.savefig(figname)


                
if __name__=='__main__':
    pass
