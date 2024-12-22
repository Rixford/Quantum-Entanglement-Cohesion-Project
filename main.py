import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
c = 3e8  # Speed of light (m/s)
initial_entanglement = 1.0  # Perfect entanglement (1 = fully entangled)
initial_gravity = 1.0  # Starting gravitational intensity
gravitational_growth_rate = 0.05  # Rate of gravitational growth per time step
max_gravitational_pull = 50  # Maximum gravitational potential based on star mass
time_steps = 100  # Simulation steps
base_amplification_rate = 0.005  # Base restoration/amplification factor per time step
reflection_efficiency = 0.1  # Reflection efficiency of Element 115
feedback_efficiency = 0.2  # Feedback efficiency for residual coherence
order_growth_rate = 0.1  # Rate of order growth beyond the event horizon
event_horizon_step = 40  # Define the event horizon step

# Arrays to store results
entanglement_correlations = [initial_entanglement]
gravity_values = []  # Gravitational intensity over time
reflection_factors = []  # Reflection factors over time
order_values = []  # Order dynamics beyond the event horizon

# Reflection factor function
def calculate_reflection_factor(gravity_intensity, efficiency):
    """
    Calculate the reflection factor of Moscovium (Element 115) based on gravitational intensity.
    """
    return 1 / (1 + efficiency * gravity_intensity)

# Simulation loop
for t in range(1, time_steps + 1):
    if t <= event_horizon_step:
        # Pre-event horizon dynamics
        gravity_intensity = min(initial_gravity * np.exp(gravitational_growth_rate * t), max_gravitational_pull)
        gravity_values.append(gravity_intensity)

        # Calculate reflection factor
        reflection_factor = calculate_reflection_factor(gravity_intensity, reflection_efficiency)
        reflection_factors.append(reflection_factor)

        # Current entanglement correlation
        current_entanglement = entanglement_correlations[-1]
        
        # Residual coherence: Use current entanglement as a feedback base
        residual_coherence = max(0, current_entanglement)

        # Adjust amplification dynamically based on residual coherence
        amplification = base_amplification_rate + feedback_efficiency * np.log(1 + residual_coherence)

        # Calculate new entanglement
        new_entanglement = current_entanglement * (1 - gravity_intensity / max_gravitational_pull) + amplification

        # Keep entanglement within bounds [0, 1]
        new_entanglement = max(0, min(new_entanglement, 1))
        entanglement_correlations.append(new_entanglement)
    else:
        # Post-event horizon dynamics
        gravity_values.append(0)  # Gravity dissipates beyond the event horizon
        reflection_factors.append(0)  # Reflection no longer a factor

        # Calculate order dynamics
        order_level = order_growth_rate * (t - event_horizon_step)
        order_values.append(order_level)

        # Stabilize entanglement based on order dynamics
        current_entanglement = entanglement_correlations[-1]
        stabilization_factor = np.exp(-order_level)
        new_entanglement = current_entanglement + (1 - current_entanglement) * stabilization_factor

        # Keep entanglement within bounds [0, 1]
        new_entanglement = max(0, min(new_entanglement, 1))
        entanglement_correlations.append(new_entanglement)

# Plot entanglement stabilization
plt.figure(figsize=(10, 6))
plt.plot(range(time_steps + 1), entanglement_correlations, label="Entanglement Correlation")
plt.axvline(event_horizon_step, color='red', linestyle='--', label="Event Horizon")
plt.title("Entanglement Stabilization with Pre- and Post-Event Horizon Dynamics")
plt.xlabel("Time Steps")
plt.ylabel("Entanglement Correlation")
plt.grid(True)
plt.legend()
plt.show()

# Plot gravitational intensity over time
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(gravity_values) + 1), gravity_values, label="Gravitational Intensity")
plt.axvline(event_horizon_step, color='red', linestyle='--', label="Event Horizon")
plt.title("Gravitational Intensity Over Time (Pre-Event Horizon)")
plt.xlabel("Time Steps")
plt.ylabel("Gravitational Intensity")
plt.grid(True)
plt.legend()
plt.show()

# Plot reflection factor over time
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(reflection_factors) + 1), reflection_factors, label="Reflection Factor (Element 115)")
plt.axvline(event_horizon_step, color='red', linestyle='--', label="Event Horizon")
plt.title("Reflection Factor of Element 115 Over Time (Pre-Event Horizon)")
plt.xlabel("Time Steps")
plt.ylabel("Reflection Factor")
plt.grid(True)
plt.legend()
plt.show()

# Plot order dynamics beyond the event horizon
plt.figure(figsize=(10, 6))
plt.plot(range(event_horizon_step + 1, len(order_values) + event_horizon_step + 1), order_values, label="Order Dynamics")
plt.axvline(event_horizon_step, color='red', linestyle='--', label="Event Horizon")
plt.title("Order Dynamics Beyond the Event Horizon")
plt.xlabel("Time Steps")
plt.ylabel("Order Level")
plt.grid(True)
plt.legend()
plt.show()