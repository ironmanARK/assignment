import time # to time the execution
import numpy as np
import matplotlib.pyplot as plt
def load_data(data_path):
    data=np.loadtxt(data_path,delimiter=',')
    return data

def initialise_centers(data, K, init_centers=None):
    if init_centers is None:
        indices = np.random.choice(data.shape[0],size=K,replace= False)
        return data[indices]
    else:
        return np.array(init_centers)

def initialise_labels(data):
    n = data.shape[0]
    labels = np.ones(n)
    return labels

def calculate_distances(data, centers):
    distances = np.linalg.norm(data[:, np.newaxis] - centers, axis=2)
    return distances

def update_labels(distances):
    labels = np.argmin(distances, axis=1)
    return labels

def update_centers(data, labels, K):
    cluster_sums = np.zeros((K, data.shape[1]))
    cluster_counts = np.zeros(K)
    np.add.at(cluster_sums, labels, data)
    np.add.at(cluster_counts, labels, 1)
    centers= cluster_sums /cluster_counts[:, np.newaxis]
    return centers

def check_termination(labels1, labels2):
    if labels1.all() == labels2.all() :
        return True
    else :
        return False
## DON'T CHANGE ANYTHING IN THE FOLLOWING FUNCTION
def kmeans(data_path:str, K:int, init_centers):
    '''
    Input :
        data (type str): path to the file containing the data
        K (type int): number of clusters
        init_centers (type numpy.ndarray): initial centers. shape = (K, 2) or None
    Output :
        centers (type numpy.ndarray): final centers. shape = (K, 2)
        labels (type numpy.ndarray): label of each data point. shape = (N,)
        time (type float): time taken by the algorithm to converge in seconds
    N is the number of data points each of shape (2,)
    '''
    data = load_data(data_path)    
    centers = initialise_centers(data, K, init_centers)
    labels = initialise_labels(data)

    start_time = time.time() # Time stamp 

    while True:
        distances = calculate_distances(data, centers)
        labels_new = update_labels(distances)
        centers = update_centers(data, labels_new, K)
        if check_termination(labels, labels_new): break
        else: labels = labels_new
 
    end_time = time.time() # Time stamp after the algorithm ends
    return centers, labels, end_time - start_time 

def visualise(data_path, labels, centers):
    data = load_data(data_path)

    # Scatter plot of the data points
    plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

    ### Set title as 'K-means clustering'
    plt.title('K-means Clustering')
    ### Set xlabel as 'Longitude'
    plt.xlabel('Longitude')
    ### Set ylabel as 'Latitude'
    plt.ylabel('Latitude')
    ### Save the plot as 'kmeans.png'
    plt.savefig('kmeans.png')

    ## DO NOT CHANGE THE FOLLOWING LINE
    return plt
### After you have completed the above functions, run the following code to generate the plot
data_path = 'spice_locations.txt'
K, init_centers = 2, None
centers, labels, time_taken = kmeans(data_path, K, init_centers)
print('Time taken for the algorithm to converge:', time_taken)
visualise(data_path, labels, centers)