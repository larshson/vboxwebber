import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vboxwebber", # Replace with your own username
    version="0.0.1",
    author="larshson",
    author_email="larshson@gmail.com",
    description="A standalone client for VirtualBox webservice API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/larshson/vboxwebber",
    packages=setuptools.find_packages(),
    classifiers=[
		"Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
	install_requires=['zeep']
)
