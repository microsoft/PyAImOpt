# %% [markdown]
# # MaxCut on Simple Graph
#
# This notebook shows how to call the MaxCut solver from the AIM service on a simple graph.
# The graph is constructed using the networkx library.

# %%
# First, import dependencies

from time import sleep
import networkx as nx
import pyaimopt as aim

# %% [markdown]
# ## Create the input graph.
#
# This can be done either explicitly (as an numpy array),
# or with the help of the networkx package as follows.

# %%

G = nx.Graph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)

G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 0)

# %%
# Transform the graph to a max cut problem.
mc = aim.MaxCut.mk_from_graph(G)

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

# %% [markdown]
# ## Solve the problem
#
# ### Submit the problem and wait for solution
# %%

TIME_LIMIT = 10  # seconds
solution = solver.solve(mc, TIME_LIMIT)
print(solution.result.output)

#%% [markdown]
# ### Submit and retrieve solution later
#
# Alternatively, the problem can be submitted to the AIM service
# and the results can be retrieved later.

# %%
# Submit problem

pid = solver.submit(mc, 10)
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

# %%
