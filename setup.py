from setuptools import setup, find_packages

setup(
    name="monarch-pylib",
    version="0.5.0",
    description="",
    author="Ali36Saadat",
    author_email="Ali36Saadat@gmail.com",
    url="https://github.com/ali36saadat/monarch-pylib",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "numba",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
)
