# import packages that are needed
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector

# define the parameters to use for the problem
h = {4: 0,
    9: 0,
    -5: 0} 

J = {(4, 9): 72, 
    (4, -5): -40, 
    (9, -5): -90} 

chain_strength = 60

sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results
response = sampler.sample_ising(h, J, num_reads = 100, chain_strength = chain_strength)

# Show the problem visualization on the QPU 
# inspector.show(response)

print("QPU response")
print(response)
