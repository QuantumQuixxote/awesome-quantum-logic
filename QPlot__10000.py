from qiskit import *
from qiskit import plot_histogram, matplotlib

circuit = QuantumCircuit(16,16) #Making a circuit with 16 qubits
qr = QuantumRegister(16)
cr = ClassicalRegister(16)
for i in range(16):
    circuit.h(i)
    circuit.measure(i,i)

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 250).result()
counts = result.get_counts()
print(counts)
