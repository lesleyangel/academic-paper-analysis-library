| Hyperparameter | Values | Best value |
| --- | --- | --- |
| Number of historical measurements | 0, 1, 3, 5, 7, 10 | 3 |
| Historical measurement interval /s | 1, 3, 5, 7, 10, 25, 50, 75 | 25 |
| Retained spectral modes (length) | 1, 2, 3, 4, 5, 7, 10, 15 | 5 |
| Retained spectral modes (width) | 1, 2, 3, 4, 5, 7, 10, 15 | 4 |
| Retained spectral modes (thickness) | 1, 2, 3, 5, 7, 10, 15 | 2 |
| Neurons per Fourier block | 2, 5, 10, 15, 20, 30, 50, 100 | 100 |
| Tucker retention ratio/% Activation function | 1, 5, 10, 15, 25, 50, 75, 100 Identity, ReLU, ReLU6, LeakyReLU, PReLU, | 15 ReLU6 |
|  | ELU, CELU, SELU, GELU, SiLU, Mish, MishTanh, Sigmoid, Hardsigmoid, Hardtanh, Hardswish, Tanhshrink, Softshrink, Hardshrink, Softplus, Softsign, |  |
| Number of Fourier layers | LogSigmoid 2,4,6, 8, 10 | 4 |
| MLP after each Fourier layer | Yes, No | Yes |
