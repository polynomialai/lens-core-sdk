import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lens_core_sdk",
    version="0.2.0",
    author="Prakhar Kaushik",
    author_email="prakhar.k@polynomial.ai",
    description="Core Lens SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polynomialai/lens-core-sdk",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["requests==2.26.0", "python-dotenv==0.19.0"],
    python_requires=">=3.6",
)
