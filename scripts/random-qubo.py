"""
Example of creating and submitting a QUBO problem.
The problem constructed here is random;
adjust the construction of the quadratic matrix and the field
to reflect the problem you are interested in.

To construct a QUBO problem, we need a quadratic matrix
and (optionally) a field vector. Both are numpy arrays.
These numpy arrays are used to directly construct the
QUMO instance; since there are no continuous variables,
the problem is effectively QUBO.
"""

import argparse
import logging
import sys
import numpy as np
import pyaimopt as aim


__DEFAULT_TIMEOUT__ = 100           # seconds
__DEFAULT_PRECISION__ = "Float32"

_logger = logging.getLogger(__name__)

#
# The next two methods (_create_random_quadratic and _create_random_field)
# should be replaced with the actual construction of the QUBO problem.
#


def _create_random_quadratic(size: int) -> np.ndarray:
    """
    Create a random quadratic matrix of the given size.
    """
    quadratic = np.random.normal(0, size=(size, size))
    np.fill_diagonal(quadratic, 0)
    quadratic = 0.5 * (quadratic + quadratic.transpose())

    _logger.info("Quadratic matrix:\n%s", quadratic)

    return quadratic


def _create_random_field(size: int) -> np.ndarray:
    """
    Create a random field vector of the given size.
    """
    field = np.random.normal(0, size=size)
    _logger.info("Field vector: %s", field)
    return field

#
# The rest of the methods are common code to create
# and submit the problem.
#


def _create_problem(size: int, has_external_field: bool = False) -> aim.QUMO:
    """
    Create a random QUBO problem of the given size.
    """
    quadratic = _create_random_quadratic(size)
    if has_external_field:
        field = _create_random_field(size)
        _logger.info("Creating problem with external field")
        qubo = aim.QUMO(quadratic, field)
    else:
        qubo = aim.QUMO(quadratic)
        _logger.info("Creating problem without external field")

    return qubo


def _parser() -> argparse.Namespace:
    """
    Create the command line parser
    """

    if __name__ == "__main__":
        cmdline = "python random-qubo.py"
    else:
        cmdline = sys.argv[0]

    usage = f"""
    To submit a QUBO problem:
    \t {cmdline} <size>
    """

    parser = argparse.ArgumentParser(
        description="Run QUBO solver on graphs generated at random.",
        prog="python random-qubo.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=usage,
    )

    parser.add_argument(
        "size",
        help="Size of the problem to create",
        type=int
    )

    parser.add_argument(
        "-d",
        "--debug",
        help="Enable debug logging",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable verbose logging",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    parser.add_argument(
        "--precision",
        help="Precision to use for the solver",
        choices=["Float32", "Float16", "BFloat16", "Float64"],
        default=__DEFAULT_PRECISION__,
        dest="precision",
    )
    parser.add_argument(
        "-t"
        "--timeout",
        help="Timeout for the solver (in seconds)",
        type=int,
        default=__DEFAULT_TIMEOUT__,
        dest="timeout",
    )
    parser.add_argument(
        "-f",
        "--fields",
        help="Enable use of field",
        action="store_true",
    )

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    return args


def main():
    if len(sys.argv) == 1:
        sys.argv.append("--help")

    args = _parser()

    problem = _create_problem(args.size, args.fields)

    workspace = aim.create_azure_workspace()
    solver = aim.Solver(workspace)
    precision = getattr(aim.Precision, args.precision)
    _logger.debug("Setting precision to %s", precision)
    solver.set_precision(precision)

    pid = solver.submit(problem, args.timeout)
    _logger.info("Submitted problem with id %s", pid)


if __name__ == "__main__":
    main()
