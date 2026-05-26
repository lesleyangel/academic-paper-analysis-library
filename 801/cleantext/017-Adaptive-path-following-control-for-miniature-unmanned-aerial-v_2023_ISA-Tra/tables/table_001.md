| Symbols and Definitions | $P$ | MAV's guidance path |  |
| --- | --- | --- | --- |
| $c s ^ { i }$ Inertial Reference Frame |  | $p$ | Orientation location |
| $c s ^ { b }$ | MAV-fixed Reference Frame | $\pmb { \varepsilon } = \left\{ x _ { g } , y _ { g } , z _ { g } \right\} ^ { T }$ | Tracking error |
| $C S ^ { g }$ | Route Reference Frame | Angle of heading $\psi$ |  |
| $V _ { u }$ | MAV's vector of velocity | $\left[ { \pmb x } ( k ) , { \pmb y } ( k ) , { \pmb z } ( k ) \right] ^ { T }$ | MAV's position in $c s ^ { i }$ |
| $\gamma$ | Angle of flight path | $V _ { u }$ | The magnitude of $V _ { u }$ |
| $\phi$ | Bank angle | $x _ { g }$ | Steering tracking error |
| $F ^ { p }$ | Route error Reference Frame | $y _ { g }$ | Side tracking error |
| $\left( \dot { p } _ { n } , \dot { p } _ { e } , \dot { p } _ { d } \right) ^ { T }$ | MAV's vector of location in $c s ^ { i }$ | $z _ { g }$ | Height tracking error |
| $\mathbf { \Psi } ( u , \nu , w ) ^ { T }$ | MAV's vector of velocity in $C S ^ { b }$ | $\dot { \chi }$ | Heading angular velocity |
| $[ x _ { p } , y _ { p } , z _ { p } ]$ | Location of point on MAV's guidance path | $\omega$ Magnitude | $\boldsymbol { \mathrm { o f } } \dot { \chi }$ $P _ { s } ( \pmb { a } , \pmb { w } )$ |
| $[ \chi , h _ { d } , \nu _ { a } ]$ | Guidance command | $\pmb { a }$ $w$ | Starting point of Direction vector of $P _ { s } ( \pmb { a } , \pmb { w } )$ |
| $P _ { s } ( \pmb { a } , \pmb { w } )$ | Straight-line path | $\boldsymbol { e } _ { w }$ | Tracking error in Route error Reference Frame |
| $\gamma ^ { c } , \phi ^ { c }$ | Command of and $: \gamma$ $\phi$ |  | $P _ { s } ( \pmb { a } , \pmb { w } )$ |
| $k _ { p a t h }$ | Constant related to curvature of $P _ { s } ( \pmb { a } , \pmb { w } )$ | $\chi _ { w }$ Heading angle of |  |
| $V _ { g }$ | Magnitude of velocity in $C S ^ { g }$ | $\pmb { c } = ( c _ { n } , c _ { e } , c _ { d } ) ^ { T }$ Center of $P _ { c }$ |  |
| $P _ { c }$ | Arc path | $\lambda$ | Direction of rotation of $P _ { c }$ |
| $\rho$ | Magnitude of radius of $P _ { c }$ | $d$ | Distance among center of $P _ { c }$ and that of MAV |
| $h ^ { c }$ | Altitude command to track $P _ { c }$ | $\varphi$ | Phase angle of $P _ { c }$ Heading angle of $P _ { c }$ |
| $k _ { o r b i t }$ | Constant related to $P _ { c }$ | $\chi$ | Climb rate of the helical path |
| $k _ { \rho }$ | Constant adjustment parameter of $P _ { c }$ | $\mu$ |  |
| $\rho _ { h }$ | Radius of the helical path | $[ x ^ { h } ( t ) , y ^ { h } ( t ) , z ^ { h } ( t ) ]$ | Position of a point on at time t Current position of the MAV on the helical path |
| $[ x _ { c h } , y _ { c h } , z _ { c h } ]$ | Center of the helical path | $S _ { M } = \left[ x _ { m } , y _ { m } , z _ { m } \right]$ | Horizontal projection of helical path |
| $\gamma _ { h }$ | Flight-path angle of the helical path | $^ o$ ${ \cal S } _ { M 0 }$ | Projective point of $s _ { M }$ |
| $S _ { 1 } , S _ { 2 } , S _ { 3 }$ | Three individual points on the helical path | $d _ { \theta }$ | The shortest vertical distance from MAV to the helical path |
| $S _ { 0 }$ | The projective point of $s _ { 1 }$ | $\xi _ { \phi _ { 0 } }$ | Current yaw angle of the MAv |
| $d _ { \phi }$ | Distance from $S _ { M 0 }$ to $S _ { 0 }$ | $\varpi$ | Direction of the helical path |
| $\xi _ { \phi _ { c } }$ | The desired yaw angle to convergence to the helical path |  |  |
| $k _ { h }$ | Constant adjustment parameter of helical path | $\pmb { \theta } = \left( \tau _ { \nu } , \tau _ { \gamma } , \tau _ { \psi } \right) ^ { T }$ | Actual value of autopilot parameters |
| $\pmb { \theta } _ { 0 }$ | Nominal value of autopilot parameters | $\pmb { \mu } ^ { c }$ | Command of speed, angle of flight-path, and angle of bank Tracking velocity deviation vector |
| $\pmb { \mu }$ | State vector of MAV | $\pmb { \eta }$ |  |
| ${ \pmb \xi }$ | Tracking deviation vector | $\widehat { \pmb { \theta } } ^ { \prime } = ( \widehat { \tau } _ { \nu } , \widehat { \tau } _ { \gamma } , \widehat { \tau } _ { \psi } ) ^ { T }$ | Estimation of $\mathbf { \nabla } _ { \pmb { \theta } }$ |
| $\pmb { \omega }$ $\xi$ | Velocity vector of wind disturbance | $T e$ | Integral tracking error |
| $\varGamma$ | Comprehensive score of algorithms Weight value | $\overline { { T } } e$ | Mean of integral tracking error |
