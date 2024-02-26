from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

ext_modules = cythonize(
    [
        Extension(
            "ExoVista.wrapImage",
            sources=["ExoVista/wrapImage.pyx", "ExoVista/Image.cpp"],
            language="c++",
        ),
        Extension(
            "ExoVista.wrapIntegrator",
            sources=["ExoVista/wrapIntegrator.pyx", "ExoVista/Integrator.cpp"],
            language="c++",
        ),
    ]
)

setup(
    name="ExoVista",
    version="2.4",
    packages=find_packages(),
    ext_modules=ext_modules,
    package_data={"ExoVista": ["data/*"]},
    include_package_data=True,
)
