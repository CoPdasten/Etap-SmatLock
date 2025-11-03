from setuptools import setup, find_packages

setup(
    name="etap-smartlock",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'PyQt5',
    ],
    entry_points={
        'console_scripts': [
            'etap-smartlock=etap_smartlock.main:main',
        ],
    },
    author="Eyup ATILGAN",
    description="Etap Smart Lock System",
    python_requires='>=3.6',
)
