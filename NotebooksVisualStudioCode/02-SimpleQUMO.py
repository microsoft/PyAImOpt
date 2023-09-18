# %% [markdown]
# # Simple QUMO Examples
#
# This notebook demonstrates how to construct and solve
# a simple QUMO problem. The construction of QUMO will
# use the QUMO builder.

# %%
# Import the AIM Python Package
from time import sleep
import pyaimopt as aim

# %% [markdown]
# ## Construct the QUMO problem
#
# For the construction of the QUMO problem,
# we will use the QUMO builder.
# This allows to construct the problem incrementally
# by adding the quadratic and (optionally) linear terms,
# and specifying the variables that are continuous.

# %%
bld = aim.QumoBuilder()

# Add the quadratic terms
bld.add(-22 / 9, 0, 1)
bld.add(-4 / 9, 0, 2)
bld.add(-10 / 3, 0, 5)
bld.add(-170 / 9, 1, 2)
bld.add(-5, 1, 3)
bld.add(-5, 1, 4)
bld.add(-20 / 3, 1, 5)
bld.add(-5, 2, 3)
bld.add(-5, 2, 4)
bld.add(-20 / 3, 2, 5)
bld.add(-5 / 2, 3, 3)
bld.add(-5 / 2, 4, 4)
bld.add(-5 / 2, 5, 5)

# Add linear terms
bld.add(26 / 9, 0)
bld.add(64 / 3, 1)
bld.add(58 / 3, 2)
bld.add(10, 3)
bld.add(10, 4)
bld.add(50 / 3, 5)

# Mark some variables as boxed continuous
bld.set_continuous(3)
bld.set_continuous(4)
bld.set_continuous(5)

qumo = bld.build()

# %% [markdown]
# ## Create the environment for solving the problem.
#
# This is composed of a workspace, which can be used to
# communicate with the AIM service (e.g. to query the status of a job,
# to download results), and a solver, which can be used to
# configure the solution process (e.g. to specify required precision).

# %%
workspace = aim.create_azure_workspace()
solver = aim.Solver(workspace)
# The following is not required, since Float16 is the default precision
solver.set_precision(aim.Precision.Float16)

TIME_LIMIT = 10  # seconds

# %% [markdown]
# ## Solve the problem
#
# ### Submit the problem and wait for solution

# %%

solution = solver.solve(qumo, TIME_LIMIT)
print(solution)
print(solution.result.output)

#%% [markdown]
# ### Submit and retrieve solution later
#
# Alternatively, the problem can be submitted to the AIM service
# and the results can be retrieved later.

# %%
# Submit problem

pid = solver.submit(qumo, 10)
workspace.get_status(pid)

# %%
# Poll until the solution is ready

while (
    workspace.get_status(pid) == aim.JobStatus.RUNNING
    or workspace.get_status(pid) == aim.JobStatus.SUBMITTED
):

    print("waiting for result")
    sleep(5)

# %%
# Retrieve the solution
assert workspace.get_status(pid) == aim.JobStatus.COMPLETED
solution2 = workspace.get_result(pid)
print(solution2.result.output)
