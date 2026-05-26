| Input: Flight states at the current and the previous two moments, ${ \pmb x } ( t - 2 ) , { \pmb x } ( t - 1 ) ,$ |
| --- |
| x(t) |
| aerodynamic forces and moments at the previous two moments, ${ \mathbf { } } y ( t - 2 ) , { \mathbf { } } y ( t - 1 )$ |
| Output: Flight state parameters along the trajectory |
| While $t \leq t _ { e n d }$ do |
| 1: Construct the model input at t instant, $\pmb { S } ( t ) =$ |
| [x(t − 2), x(t − 1), x(t), y(t − 2), y(t − 1)]T |
| 2: Predict the aerodynamic forces and moments y(t) at time ${ t } , { \pmb y } ( t ) = \Psi _ { D N N } ( { \pmb S } ( t ) , { \pmb \xi } )$ |
| 3: Calculate the change of states Δx based on the Eq. (11) to Eq. (14) |
| 4: Update the flight states at time instant t + 1, denoted as x(t + 1) |
| 5: Update the time step, $t = t + 1$ |
| End while |
