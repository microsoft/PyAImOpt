"""
maxcut.py

Example of console script to run max-cut solver on graphs provided as input files.
"""

from typing import List, NamedTuple
from uuid import UUID
import argparse
import glob
import logging
import os
import sys

import networkx as nx
import pyaimopt as aim

from pyaimopt.solver import Solver
from pyaimopt.workspace import Workspace

__DEFAULT_TIMEOUT__ = 100           # seconds
__DEFAULT_PRECISION__ = "Float32"

_logger = logging.getLogger(__name__)


Submission = NamedTuple("Submission", [("Filename", str), ("JobId", UUID)])


def _get_all_files(filenames: List[str]) -> List[str]:
    """
    Get all files matching the given list of filenames

    :param filenames: The list of filenames
    :returns: The list of matching files
    """
    files = []
    for filename in filenames:
        files.extend(glob.glob(filename))

    # remove directories from list
    files = [f for f in files if not os.path.isdir(f)]

    return files


def _parser() -> argparse.Namespace:
    """
    Create the command line parser
    """

    if __name__ == "__main__":
        cmdline = "python maxcut.py"
    else:
        cmdline = sys.argv[0]

    usage = f"""
    To submit a single file:
    \t {cmdline} <filename>
    """

    parser = argparse.ArgumentParser(
        description="Run max-cut solver on graphs provided as input files.",
        prog="python maxcut.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=usage,
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
        "--halt-on-error",
        help="Halt execution on first error",
        action="store_true",
        dest="halt_on_error",
        default=False,
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
        "-l",
        "--list",
        help="File to store the list of submitted problems",
        type=str,
        default="submissions.txt",
        dest="list",
    )

    parser.add_argument(
        "filename",
        help="Input file containing the graph to solve",
        nargs="+",
        type=str,
    )

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    return args


def _process_file(filename: str, solver: Solver, timeout: int):
    """
    Process a single file

    :param filename: The name of the file to process
    :param solver: The solver to use
    :param timeout: The timeout for the solver
    :returns: The id of the submitted problem
    """

    print(f"Processing file: {filename}")
    with open(filename) as f:
        _logger.debug("Reading graph from file %s", filename)
        next(f)
        graph = nx.read_edgelist(f, nodetype=int, data=(("weight", float),))
        problem = aim.MaxCut.mk_from_graph(graph)
        pid = solver.submit(problem, timeout)
        _logger.info("Submitted problem from file %s with id %s", filename, pid)
        return pid


def main():
    """
    Main entry point for this script
    """

    if len(sys.argv) == 1:
        sys.argv.append("--help")

    args = _parser()

    workspace = aim.create_azure_workspace()
    solver = aim.Solver(workspace)
    precision = getattr(aim.Precision, args.precision)
    _logger.debug("Setting precision to %s", precision)
    solver.set_precision(precision)

    files_to_process = _get_all_files(args.filename)
    ids: List[Submission] = []
    for f in files_to_process:
        _logger.info("Processing file %s", f)

        if not os.path.isfile(f):
            _logger.error("File %s does not exist", f)
            if args.halt_on_error:
                _logger.info("Halting execution due to error")
                sys.exit(1)
            else:
                _logger.debug("Ignoring error and continuing execution")
                continue

        pid = _process_file(f, solver, args.timeout)
        ids.append(Submission(f, pid))

    header = "Filename, JobId, Input"
    body = "\n".join([f"{os.path.basename(s.Filename)}, {s.JobId}, {s.Filename}" for s in ids])
    if not os.path.isfile(args.list):
        with open(args.list, "w") as f:
            f.write(header + "\n")

    with open(args.list, "a") as f:
        f.write(body)

    print("Submitted problems:")
    listing = "\n".join([header, body])
    print(listing)

    _logger.info("Waiting for all problems to complete")


if __name__ == "__main__":
    main()
