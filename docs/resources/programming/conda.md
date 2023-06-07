# conda

[conda](https://conda.io){:target="_blank"} is a package manager used to manage dependencies for python projects (with some functionality for R and some other programs). You can [export your environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment){:target="_blank"} for your Git repository.

We recommend that you use conda whenever possible to facilitate reproducibility and reduce package conflicts. If you need to use packages that are not available within conda, try to maintain a similar level of documentation:
what packages did you use, and what versions?

## Installation

conda [installation procedures](https://conda.io/projects/conda/en/latest/user-guide/install/index.html){:target="_blank"} vary slightly depending on on your operating system. We recommend starting with Miniconda and adding packages as needed, as the full Anaconda installation might include a lot of less-necessary packages.

## Usage

Here is a [conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf){:target="_blank"} current as of conda 4.6.

You will generally want to add the `conda-forge` channel to your configuration. After loading an environment:
```shell
conda config --add channels conda-forge
conda config --set channel_priority strict
```

The conda documentation has more information on [managing channels](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html){:target="_blank"}.

## Learn More

* [Managing Python Environments](https://earth-env-data-science.github.io/lectures/environment/python_environments.html){:target="_blank"} from [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html){:target="_blank"}
* [Setting Up and Customizing Python Environments Using Conda](https://waterprogramming.wordpress.com/2018/06/29/setting-up-and-customizing-python-environments-using-conda/){:target="_blank"} from Water Programming.
