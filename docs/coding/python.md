# Python

[Python](https://www.python.org/){:target="_blank"} is a general-purpose programming language, aimed at striking a balance between performance and code interpretability. Python has some high-performance numerical libraries, but is not as performant as languages like C++. However, it is widely used, the code can be easy to read, and it has a large collection of packages.

## Installation

You should install Python 3 (preferably version 3.6 or greater) --- not Python 2. Rather than using the default version installed on whatever system you're using, you should use [conda](/lab-manual/coding/conda/){:target="_blank"}. This allows you to manage multiple installations, as different packages might not be compatible with the same Python version. conda is great at automatically upgrading or downgrading the version as needed.

Some packages may not be available through conda, but in that case, use `pip` to install them from within your conda environment.

## Usage

A good place to start if you don't know any Python is the [Python Fundamentals](https://earth-env-data-science.github.io/lectures/core_python/python_fundamentals.html){:target="_blank"} chapter from Earth and Environmental Data Science. There are also a number of other resources available online, and many specific questions can be or already are answered on [Stack Overflow](https://stackoverflow.com/questions/tagged/python){:target="_blank"}.

Python is a dynamically-typed language, meaning that it automatically assigns types to variables and functions. This means that, by default, it lacks type checking, which can result in bugs. Dynamic typing is also one reason why Python is more user-friendly than a statically-typed language like C++, but is also slower.

## Development Environments

There are a number of good IDEs for Python. A few options:

* [Spyder](https://www.spyder-ide.org/){:target="_blank"}: Lightweight, free, open-source, natively-coded in Python.
* [PyCharm](https://www.jetbrains.com/pycharm/){:target="_blank"}: Fully-functional IDE, though it costs money. We can get you a license if this is the way you want to go.
* [Atom](https://atom.io/): Text editor that can [be turned into a Python IDE](https://hackernoon.com/setting-up-atom-as-a-python-ide-a-how-to-guide-o6dd37ff){:target="_blank"} using several packages.

## Recommended Packages

You'll usually want to include the following in any research conda environment:

* [`numpy`](https://numpy.org/){:target="_blank"}: high-performance library for numerical computing.
* [`scipy`](https://www.scipy.org/){:target="_blank"}: contains functionality for a wide variety of scientific computing tasks, including optimization and statistics.
* [`matplotlib`](https://matplotlib.org/){:target="_blank"}: library for visualization and plotting.

Other packages may make sense depending on your workflow and tasks:

* [`pandas`](https://pandas.pydata.org/){:target="_blank"}: data analysis and manipulation.
* [`xarray`](http://xarray.pydata.org/en/stable/){:target="_blank"}: allows for structured datasets and interfacing with netCDF.
* [`seaborn`](https://seaborn.pydata.org/){:target="_blank"}: adds some additional plotting functionality on top of `matplotlib`, and integrates well with `pandas`.
* [`pyMC3`](https://docs.pymc.io/){:target="_blank"}: probabilistic programming using a variety of methods, including Hamiltonian Monte Carlo and Metropolis-Hastings.
* [`pyStan`](https://pystan.readthedocs.io/en/latest/){:target="_blank"}: Similar to `pyMC3`, but uses the [Stan](https://mc-stan.org/) backend.
* [`TensorFlow`](https://www.tensorflow.org/){:target="_blank"}: machine learning tools and libraries.
* [`mpi4py`](https://mpi4py.readthedocs.io/en/stable/){:target="_blank"}: bindings for parallelization across multiple processors and compute nodes.
* [`mypy`](http://mypy-lang.org/){:target="_blank"}: optional static type-checking, can help reduce errors by clarifying expected inputs and outputs and make it easier for others to work with your code.
* [`black`](https://github.com/psf/black){:target="_blank"}: automates code formatting.

## Learn More
* [Beyond PEP 8 -- Best Practices for Beautiful Intelligible Code](https://www.youtube.com/watch?v=wf-BqAjZb8M&list=LL&index=21){:target="_blank"} by Raymond Hettinger from PyCon 2015.
* [Livecoding Madness - Let's Build a Deep Learning Library](https://www.youtube.com/watch?v=o64FV-ez6Gw){:target="_blank"} by Joel Grus
* [Software Testing and Testing Automation with Python](https://leemangeophysicalllc.github.io/testing-with-python/){:target="_blank"}
* [Python posts](https://waterprogramming.wordpress.com/category/programming/python/){:target="_blank"} from Water Programming.
