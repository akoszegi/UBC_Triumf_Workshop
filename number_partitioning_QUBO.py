# import packages that are needed
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector

# partition the numbers of the set {4, 9, -5} into two sets with equal sum
# Define the problem as a Python dictionary
Q = {(4, 4): -64, 
    (9, 9): 36, 
    (-5, -5): 260, 
    (4, 9): 288, 
    (4, -5): -160,
    (9, -5): -360
    }

# specify the chain_strength
chain_strength = 100

# for QUBO problems, formulate in terms of a Q dictionary instead of h and J
# note that the dictionary doesn't have to use numbers as the indices. It could 
# instead use letters or names
# in the Q dictionary, need to specify both coupling and linear bias terms


sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
response = sampler.sample_qubo(Q, num_reads = 100, chain_strength = chain_strength)

# Show the problem visualization on the QPU 
# inspector.show(response)


print("QPU response")
print(response)

