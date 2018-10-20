import io

from setuptools import find_packages, setup

setup(
    name='ai_nad_api',
    version='1.0.0',
    license='GPL',
    maintainer='Guillem96',
    maintainer_email='guillem.orellana@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
        ],
    },
)