from setuptools import setup, find_packages

setup(
    name="ais_assault_harness",
    version="0.1.0",
    description="A modular framework for adversarial red-teaming and vulnerability testing of LLMs.",
    author="IntegralPilot",
    author_email="linux479@duck.com",
    url="https://github.com/IntegralPilot/ais-assault-harness",
    packages=find_packages(),
    install_requires=[
        "nltk>=3.8.1",
        "pytest>=7.0.0"
    ],
    license="Apache-2.0",
    python_requires=">=3.7",
)
