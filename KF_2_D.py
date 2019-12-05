import pandas as pd
import numpy as np
data = pd.read_csv("GPS.csv")
data_2=pd.read_csv("Accelerometer.csv")
position=data["Longitude"]
acceleration=data_2["X"]



#assumptions
delta_t=1
pos_error=26
vel_error=6
measure_pos_error=23
measure_vel_error=7
#measurement error matrix
R=np.array([[measure_pos_error**2, 0],
            [0, measure_vel_error**2]])
#measurement transmission
C=np.identity(2)

#covariance transmission matrix
H=np.identity(2)

#state transmission matrix
A=np.array([[1, delta_t],
            [0 , 1]])

#inital/previous state matrix X
init_state=np.array([[position[0]],
            [0.5*delta_t*acceleration[0]]])

#input transmission matrix
B = np.array([[0.5 * delta_t**2],
                [delta_t]])

#initial/previous process covariance matrix
Pk=np.array([[pos_error**2, 0],
             [0, vel_error**2]])

for i in range(len(position)):
    # first step detrmine the current state
    current_state = A.dot(init_state) + B.dot(acceleration[i])
    # second step
    # predict the process covariance matrix
    pk = np.dot(A.dot(Pk), A.transpose())
    # third step
    # calculate kalman gain
    k = pk.dot(H.transpose()) / (H.dot(pk).dot(H.transpose()) + R)
    # fourth step
    # new measurement value
    new_measure = C.dot(np.array([[position[i]],[0.5*delta_t*acceleration[i]]]))
    # fifth step
    #calculate the new state
    # assign it to initial state to be able to use it in the new iteration
    init_state = current_state + k.dot(new_measure - H.dot(current_state))
    # 6step
    # update the process covariance matrix
    Pk = (np.identity(2) - k.dot(H)).dot(pk)












#plot the measurements and the estimations
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(x, y, s=1, c='b', label='mesurement')
ax1.scatter(x, kal, s=1, c='r', label='kalman_values')
plt.legend(loc='upper left');
plt.show()
