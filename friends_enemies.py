# import packages that are needed
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector

# simple constraint satisfaction, with friendly relationships between A,B and C,D and unfriendly between B,D
Q = {('A', 'A'): 1, 
    ('B', 'B'): 0, 
    ('C', 'C'): 1, 
    ('D', 'D'): 0, 
    ('A', 'B'): -2,
    ('A', 'C'): 0,
    ('A', 'D'): 0,
    ('B', 'C'): 0,
    ('B', 'D'): 2,
    ('C', 'D'): -2
    }

# specify the chain_strength
chain_strength = 2

# for QUBO problems, formulate in terms of a Q dictionary instead of h and J
# note that the dictionary doesn't have to use numbers as the indices. It could 
# instead use letters or names
# in the Q dictionary, need to specify both coupling and linear bias terms

sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
response = sampler.sample_qubo(Q, num_reads = 100, chain_strength = chain_strength)

# Show the problem visualization on the QPU 
inspector.show(response)

print("QPU response")
print(response)

