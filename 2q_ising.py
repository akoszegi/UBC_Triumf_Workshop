# import packages that are needed
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector as inspector

# h specifies the local biases applied to each variable (qubit in this case)
h = {0: -1, 1: 1} 

# J specifies the coupling between two variables (in this case, adjacent qubits)
J = {(0, 1): -1} 

sampler = EmbeddingComposite(DWaveSampler())

# Run the problem on the sampler and print the results

response = sampler.sample_ising(h, J, num_reads = 10)
# Show the problem visualization on the QPU 
#inspector.show(response)

print("QPU response")
print(response)


# would like to add something in here about how to access various parts of the solution