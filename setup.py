import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as req_file:
    requirements = req_file.readlines()
    requirements = [x.strip() for x in requirements]

setuptools.setup(
    name="instagram-insights",
    version="0.2.7",
    author="Pardhu Madipalli",
    author_email="pardhu.madipalli@gmail.com",
    description="Get insights about best times to post, and the best tags based on likes, views and impressions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PardhuMadipalli/instagram-insights",
    project_urls={
        "Bug Tracker": "https://github.com/PardhuMadipalli/instagram-insights/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    package_data={'insights': ['data/*']},
    data_files=[('.', ['screenshot.png', 'README.md', 'requirements.txt', 'requirements-test.txt'])],
    py_modules = ['constant', 'setup', 'get_insta_insights', 'commons'],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={"console_scripts": ["insta-insights=get_insta_insights:main"]},
)
