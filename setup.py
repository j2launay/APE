import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ape',
    version='0.0.1',
    author='Julien Delaunay',
    author_email='juliendelaunay35000@gmail.com',
    description='Testing installation of Package',
    python_requires='>=3.5',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/j2launay/APE-Ijcai',
    project_urls = {
        "Bug Tracker": "https://github.com/j2launay/APE-Ijcai/issues"
    },
    license='MIT',
    packages=['ape'],
    install_requires=[
        'pandas', 
        'scipy', 
        'pyfolding', 
        'numpy', 
        'matplotlib', 
        'yellowbrick', 
        'scikit_learn'
    ],
)