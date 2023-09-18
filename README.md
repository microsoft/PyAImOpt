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

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
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
