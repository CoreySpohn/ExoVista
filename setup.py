from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

ext_modules = cythonize(
    [
        Extension(
            "ExoVista.wrapImage",
            sources=["src/wrapImage.pyx", "src/Image.cpp"],
            language="c++",
        ),
        Extension(
            "ExoVista.wrapIntegrator",
            sources=["src/wrapIntegrator.pyx", "src/Integrator.cpp"],
            language="c++",
        ),
    ]
)

setup(
    name="ExoVista",
    version="2.4",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    ext_modules=ext_modules,
    package_data={"ExoVista": ["data/*"]},
    include_package_data=True,
)
