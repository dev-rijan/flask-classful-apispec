from setuptools import setup, find_packages

VERSION = "0.1.9"
EXTRAS_REQUIRE = {
    # [FIXME] latest version of flask is mot supported by flask classful, so added as test dependencies
    "tests": ["pytest", "mock", "marshmallow", "flask==2.1.2", "Werkzeug==2.1.2"],
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
    long_description_content_type="text/markdown",
    author="Rijan adhikari",
    author_email="rijanadhikari@gmail.com",
    url="https://github.com/dev-rijan/flask-classful-apispec",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["apispec[yaml] >= 5.1.1", "flask-classful == 0.14.2", "packaging >= 21.3"],
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
