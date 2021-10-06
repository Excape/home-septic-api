from setuptools import find_packages, setup

setup(
    name="home_septic_api",
    version="1.0.0",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["flask", "flask-restplus", "requests"],
)
