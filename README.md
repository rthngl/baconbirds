# baconbirds

Code here is a lightly-adapted version of the Tensorflow implementation of CycleGAN written by Harry Yang and Nathan Silberman. 

[Their Original Code](https://github.com/leehomyc/cyclegan-1) | [CycleGAN Project](https://junyanz.github.io/CycleGAN/) | [Zhu et al. 2017](https://arxiv.org/pdf/1703.10593.pdf)


# abstract impressionism and style transfer

CycleGAN has been commonly implemented for style transfer, including patterns (i.e. horses to zebras) and textures (i.e. landscapes as Van Goghs). However, it is limited with respect to geometric changes (dogs to cats or apples to oranges can look a little lopsided, similarly [this notable failure case](https://junyanz.github.io/CycleGAN/images/failure_putin.jpg) demonstrates the limits of semantic segmentation + style transfer)

While somewhat abstracted examples of style transfer can be found ([Boshi et al. 2017](https://arxiv.org/pdf/1701.04928.pdf), [this Northwestern project](https://sally9805.github.io/Neural-Artistic-Style-Transfer/)) they still tend to work better when an overall textural style is applied (Hokusai or Mondrian) rather than an object-distortion style (Picasso).
