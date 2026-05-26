| Hyperparameter | Values | Best value |
| --- | --- | --- |
| Retained spectral modes (streamwise direction) | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 6 |
| Retained spectral modes (azimuthal angle) | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 | 8 |
| Neurons per Fourier block | 2, 4, 7, 10, 15, 20, 30, 50, 100 | 30 |
| Tucker retention ratio/% Activation function | 1, 5, 10, 15, 25, 50, 75, 100 Identity, ReLU, ReLU6, LeakyReLU, | 10 |
|  | PReLU, ELU, CELU, SELU, GELU, SiLU, Mish, MishTanh, Sigmoid, Hardsigmoid, Hardtanh, Hardswish, Tanhshrink, Softshrink, Hardshrink, Softplus, Softsign, LogSigmoid | GELU |
| Number of Fourier layers | 2, 4, 6, 8, 10 | 4 |
| MLP after each Fourier layer | Yes, No | Yes |
