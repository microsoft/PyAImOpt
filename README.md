# Examples for the PyAIMOpt Python package
## Introduction

`PyAIMOpt` provides a Python interface to access the
Microsoft Research Analog Iterative Machine (AIM) Service.
The AIM Service receives optimization problems expressed
in the [QUMO]() formulation,
and uses advanced algorithms to find good solutions for that problem.
This repository contains simple examples that demonstrate
the API to access the service, and also examples of modeling
problems as QUMO.
You can also use this repo to provide feedback (including bugs,
and suggestions) to the project using the [Issues](https://github.com/microsoft/PyAImOpt/issues) page.

## License

Please see the LICENSE file. The package depends on a number of external packages.
The list of those packages and their corresponding licences can be found in the [NOTICE.html](file:///NOTICE.html) file.

## Authentication

Access to the AIM service is restricted to authorized individuals who have been successfully authenticated according to IETF OAUTH2 standards: our sample python scripts achieve this with emphasis on least intrusive user experience.

## Installation

We are working towards a public release of this project and an accompanying public python wheel file, but in the interim you may download and install manually using the python "pip" installer as follows.

Access via a browser is needed to complete the authentication protocol required by github for access to github project prior to its public version. Failure to get the right will result in an http 404 error displayed on the browser.

If the browser succeeds to authenticate you with github, then on the right hand side of the displayed page will be a "Releases" section in which appears one or more items named something like "PyAimOpt v0.6.0", one of which will be flagged in green as "latest". The "latest" is the one you want: click on it to observe its contents, then click on the wheel file (the one whose name ends with ".whl") and take not of where your browser puts the file on your PC (for example on Windows it will be in your personal "downloads" folder as displayed by Windows File Explorer).

Having downloaded the wheel file, you can instal it into your python environment using the python pip installer. For example you might enter:
pip install pyaimopt-0.6.0-py3-none-any.whl


## Getting Started

You need a working installation of Python;
currently we support versions `3.9`, `3.10`, and `3.11` in `Windows`, `Windows WSL`, and `Linux`.
Very likely the examples will work on other platforms;
please let us know, though the [Issues]() channel, of problems you encounter.

We strongly suggest that you create a virtual environment for your work
(instead of using your default `Python` installation).
One way to create and activate the virtual environment is as follows:

With PowerShell:

```PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

With bash:

```bash
python -m venv venv
source venv/bin/activate
```

Install the main `PyAIMOpt` package:

```PowerShell
pip install pyaimopt -i <PACKAGE_SOURCE_URL>
```

As part of getting access to the AIM Service, you will receive a `.aimenv.conf` file
that will give you access to the service.
Copy the file locally (but, avoid committing to your source control system),
and then set the environmental variable `AIM_SETTINGS_ENV` to point to
(the full path) of that file. Replace `<fullpath>` with the directory where you downloaded
the `.aimenv.conf` file.

With PowerShell:

```PowerShell
$Env:AIM_SETTINGS_ENV="<fullpath>\.aimenv.conf"
```

With bash:

```bash
export AIM_SETTINGS_ENV=<fullpath>/.aimenv.conf
```

Please make sure that indeed the file exists, and the environment variable has been set correctly,
by checking that the command below does not generate an error and the output is not empty.

With PowerShell:

```PowerShell
type $Env:AIM_SETTINGS_ENV
```

With bash:

```bash
cat $AIM_SETTINGS_ENV
```

If everything has been set correctly, you should have access to the `aim` command line utility.
Run the following command to verify that you have indeed access to the service:

```PowerShell
aim list
```

This call should not fail, and should return a list of problems submitted in your account.
Initially, this list will be empty, and you should see:

> No jobs

If there have already been problems submitted with that account you should see the list
of them, e.g.:

> Jobs:\
> Job c6cc4af8-3651-4de0-b028-a6c73d283c6a: JobStatus.COMPLETED\
> Job ed3a9871-5633-457b-a328-4661a61cd613: JobStatus.COMPLETED\
> ...

You can try submitted a small problem to check that the system is working correctly:

```PowerShell
aim submit
```

This will return a unique, fresh id for the job you have submitted
(e.g., "cfab81b9-d0c7-427e-9ee0-c9b9f198319f").
While the job is being process you should be seeing the status as `SUBMITTED`:

> Job cfab81b9-d0c7-427e-9ee0-c9b9f198319f: JobStatus.SUBMITTED

When the job gets completed, the status will change to `COMPLETED`,
and then you should be able to retrieve the results with:

```PowerShell
aim retrieve cfab81b9-d0c7-427e-9ee0-c9b9f198319f
```

## Example problems

The repo contains examples of how to formulate `QUMO` problems
and how to solve them using the `AIM` service.
In summary, the examples are arranged in the following directories:

- `NotebooksVisualStudioCode\`:
  Example inputs written for the interactive notebook experience in Visual Studio Code.
  You could run directly from the command line, but you will not see the associated
  documentation.

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

## Security

Microsoft takes the security of our software products and services seriously, which includes all source code repositories managed through our GitHub organizations, which include [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet), [Xamarin](https://github.com/xamarin), and [our GitHub organizations](https://opensource.microsoft.com/).

If you believe you have found a security vulnerability in any Microsoft-owned repository that meets [Microsoft's definition of a security vulnerability](https://docs.microsoft.com/en-us/previous-versions/tn-archive/cc751383(v=technet.10)), please report it to us as described below.

## Reporting Security Issues

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them to the Microsoft Security Response Center (MSRC) at [https://msrc.microsoft.com/create-report](https://msrc.microsoft.com/create-report).

If you prefer to submit without logging in, send email to [secure@microsoft.com](mailto:secure@microsoft.com).  If possible, encrypt your message with our PGP key; please download it from the [Microsoft Security Response Center PGP Key page](https://www.microsoft.com/en-us/msrc/pgp-key-msrc).

You should receive a response within 24 hours. If for some reason you do not, please follow up via email to ensure we received your original message. Additional information can be found at [microsoft.com/msrc](https://www.microsoft.com/msrc).

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the possible issue:

  * Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
  * Full paths of source file(s) related to the manifestation of the issue
  * The location of the affected source code (tag/branch/commit or direct URL)
  * Any special configuration required to reproduce the issue
  * Step-by-step instructions to reproduce the issue
  * Proof-of-concept or exploit code (if possible)
  * Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

If you are reporting for a bug bounty, more complete reports can contribute to a higher bounty award. Please visit our [Microsoft Bug Bounty Program](https://microsoft.com/msrc/bounty) page for more details about our active programs.

## Preferred Languages

We prefer all communications to be in English.

## Policy

Microsoft follows the principle of [Coordinated Vulnerability Disclosure](https://www.microsoft.com/en-us/msrc/cvd).

## Contact Information

Please refer to the SUPPORT.md file.

