# Project

> # `pyaimopt`: Python Wrapper for the AIM optimization service

`pyaimopt` is a package that provides access to the Analog Iterative Machine (`AIM`) optimization service.
The `AIM` optimizer accepts problems in the quadratic unconstrained mixed optimization (`QUMO`) format.
The `QUMO` format is a generalization of the quadratic unconstrained binary optimization (`QUBO`) format,
and allows for the optimization of continuous variables in addition to binary variables.
The `AIM` optimizer is a stochastic optimization algorithm that uses a combination of gradient descent and
annealing to find the global minimum of a given objective function.
In addition to `QUMO` and `QUBO` problems, the `AIM` optimizer can also be used to solve `MaxCut` and `Ising`
problems.

## Table of Contents

- [`pyaimopt`: Python Wrapper for the AIM optimization service](#pyaimopt-python-wrapper-for-the-aim-optimization-service)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Authentication](#authentication)
  - [Contributing](#contributiing)
  - [Usage Examples](#usage-examples)

  - [Documentation](#documentation)
  - [License](#license)
  - [Contact Information](#contact-information)

## License

Please see the LICENSE file. The package depends on a number of external packages.
The list of those packages and their corresponding licences can be found in the [NOTICE.html](file:///NOTICE.html) file.



## Prerequisites

The package requires Python 3.10 or higher. It is recommended to use a virtual environment to install the package.


## Installation

We are working towards a public release of this project and an accompanying python wheel file, but in the interim you may download and install using the python "pip" installer as follows.

First, you need to download a copy of our wheel file using a browser to open the PyAImOpt project in github from https:\\github.com\microsoft\PyAImOpt

Access via a browser is needed to complete the authentication protocol required by github for access to github project prior to its public version. Failure to get the right will result in an http 404 error diplayed on the browser.

If the browser succeeds to autheticate you with github, then on the right hand side of the displayed page will be a "Releases" section in which appears one or more items named something like "PyAimOpt v0.6.0", one of which will be flagged in green as "latest". The "latest" is the one you want: click on it to observe its contents, then click on the wheel file (the one whose name ends with ".whl") and take not of where yout browser puts the file on your PC (for example on Windows it will be in your personal "downloads" folder as displayed by Windows File Explorer).

Having downloaded the wheel file, you can instal it into your python environment using the python pip installer. For example you might tpe:
pip install pyaimopt-0.6.0-py3-none-any.whl

You can check successful installation by running the following command:

```bash
aim status
```

It should return the version of the installed package and the status of the AIM service.

## Authentication

Access to the AIM service is restricted to authorized individuals who have been successfully authenticated according to IETF OAUTH2 standards: our sample python scripts achieve this with emphasis on least intrusive user experience.


## Contributing

Initially, this project is not accepting contributions, but we do welcome feedback and suggestions. 

In the event that we accept contributions in future, we anticpate that contributions will require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.


## Contact Information

Please refer to the SUPPORT.md file.

