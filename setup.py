from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in a3sola_solar_management/__init__.py
from a3sola_solar_management import __version__ as version

setup(
	name="a3sola_solar_management",
	version=version,
	description="Custom App for a3sola Solar Management",
	author="Misma",
	author_email="ms@acube.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
