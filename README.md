# Consistent-representations-of-and-conversions-between-3D-rotations
These programs implement explicit rotation conversion algorithms (commonly used in Materials Science community.) are described. For each conversion, the section title provides a shorthand indicator of the conversion, with the first two letters describing the input representation, and the last two characters the output representation.\
Each program has some unit tests.\
The following conventions are followed:\
Convention 1. When dealing with 3D rotations, all Cartesian reference frames will be
right-handed.\
Convention 2. A rotation angle ω is taken to be positive for a counterclockwise rotation
when viewing from the end point of the rotation axis unit vector nˆ towards the origin.\
Convention 3. Rotations will be interpreted in the passive sense.\
Convention 4. Euler angle triplets are implemented using the Bunge convention.\
Convention 5. The rotation angle ω is limited to the interval [0, π].\
