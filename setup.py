from setuptools import setup, find_packages

VERSION = "0.1.3"
EXTRAS_REQUIRE = {
    "tests": ["pytest", "mock"],
    "lint": ["flake8==3.9.2", "flake8-bugbear==21.4.3"],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="flask-classful-apispec",
    version=VERSION,
    description="Auto docs generation from marshmallow schema for flask classfy",
    long_description=read("README.rst"),
    author="Rijan adhikari",
    author_email="rijanadhikari@gmail.com",
    url="https://github.com/dev-rijan/flask-classful-apispec",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["apispec==5.1.1", "flask-classful==0.14.2"],
    python_requires=">=3.6",
    extras_require=EXTRAS_REQUIRE,
    license="MIT",
    zip_safe=False,
    keywords=[
        "flask-classfull",
        "flask-classful-swagger",
        "apispec",
        "swagger",
        "openapi",
        "specification",
        "documentation",
        "spec",
        "rest",
        "api",
        "web",
        "flask",
        "frameworks",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="tests",
    project_urls={
        "Issues": "https://github.com/dev-rijan/flask-classful-apispec/issues",
    },
)
