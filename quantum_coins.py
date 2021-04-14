#Code to run a quantum random number generator on a real quantum device.
from qiskit import QuantumCircuit, IBMQ, execute

#Authenticate an account and add for use during this session.
IBMQ.enable_account("YOUR_API_TOKEN")
provider = IBMQ.get_provider(hub='ibm-q')

#Initialize the number of qubits and classical registers
number =3
circuit = QuantumCircuit(number, number)

#Apply an hadamard gate to every qubits
circuit.h(range(number))

#Measure every qubits
circuit.measure(range(number), range(number))

# Set the quantum device and execute the quantum circuit
backend = provider.get_backend('ibmq_belem')
job = execute(circuit, backend, shots=1)

#Get and print results
result = job.result()
print(result.get_counts())
