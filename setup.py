from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

setup(
	name="vehicle_service_management",
	version="0.0.1",
	description="Vehicle Service Management app for ERPNext V15",
	author="Balaji",
	author_email="balaji@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
