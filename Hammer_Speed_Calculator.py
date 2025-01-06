import math
import matplotlib.pyplot as plt

def getHammerSpeed(r_pulley): #function that returns speed of the hammer end at launch
    # --Initial Situation--
    #Given values
    m_counterweight = 0.2122  # kg
    m_hammer = 0.09  # kg
    L_hammer = 0.182 # m
    h_hammer_initial = 0.217  # m
    circumference_pulley = 2*math.pi*r_pulley # m
    rotations_hammer = 0.64 # m
    h_counterweight_initial = circumference_pulley * rotations_hammer  # m
    dist_counterweight_freefall = 1.6 - h_counterweight_initial  # m

    #Initial velocity of counterweight after freefall
    g = 9.81  # m/s^2
    v_counterweight_initial = math.sqrt(2 * g * dist_counterweight_freefall)  # m/s

    #Initial energy calculations
    E_potential_counterweight_initial = m_counterweight * g * h_counterweight_initial  # J
    E_kinetic_counterweight_initial = 0.5 * m_counterweight * v_counterweight_initial**2  # J
    E_potential_hammer_initial = m_hammer * g * h_hammer_initial  # J
    E_kinetic_hammer_initial = 0  # J (initial velocity is 0)

    #Total initial energy
    E_initial = E_potential_counterweight_initial + E_kinetic_counterweight_initial + E_potential_hammer_initial + E_kinetic_hammer_initial  # J

    # --Final Situation--
    #given values, approximating the hammer as a point mass at its COM
    dist_fulcrum_to_COM_of_hammer = 0.128  # m
    E_final = E_initial
    I_hammer = 0.5 * m_hammer * dist_fulcrum_to_COM_of_hammer**2


    #working for w_hammer_final which is final angular velocity of the hammer
            ##we assume that the potential energy of the hammer and weight are exhausted at the final position
            ##we assume that the weight will reach the ground and will be able to accelerate the hammer from its starting point, this assumption is not valid with a tiny pulley radius
        #E_final = E_kinetic_hammer + E_kinetic_counterweight
        #E_kinetic_hammer = E_final - E_kinetic_counterweight
            ## we assume that when the weight hits the ground, the pulley is not slipping or loose, so the angular velocity of the hammer is directly related to the velocity of the counterweight
            ##E_kinetic_counterweight = 0.5 * m_counterweight * v_counterweight_final**2
            ##v_counterweight_final = r_pulley * w_hammer_final
        #E_kinetic_hammer = E_final - (0.5*m_counterweight*(r_pulley*w_hammer_final)**2)
            ##E_kinetic_hammer = 0.5 * (I_hammer) * w_hammer_final**2
        #0.5 * (I_hammer) * w_hammer_final**2 = E_final - (0.5*m_counterweight*(r_pulley*w_hammer_final)**2)
        #I_hammer*w_hammer_final**2 = 2*E_final - (m_counterweight*(r_pulley*w_hammer_final)**2)
        #w_hammer_final**2 = 2 * E_final / (I_hammer + m_counterweight * r_pulley**2)
    w_hammer_final = math.sqrt(2 * E_final / (I_hammer + m_counterweight * (r_pulley ** 2)))

    #final velocity of the counterweight when it hits the ground
    v_counterweight_final = w_hammer_final * r_pulley

    #final linear velocity of the hammer at its most outer surface
    v_linear_hammer_final = w_hammer_final * L_hammer  # m/s

    #calculating minimum radius for counterweight to move the hammer
    RiseHeight_initial = dist_fulcrum_to_COM_of_hammer - 0.7017 * dist_fulcrum_to_COM_of_hammer #0.7017 = sin(45deg) this is used because we are raising the hammer from an angle of 45 degrees
    potential_needed = m_hammer * g * RiseHeight_initial #energy that needs to be supplied by the counterweight for it to be able to raise the hammer to its highest position.

    #SSA 12
    transmissionRatio = r_pulley/dist_fulcrum_to_COM_of_hammer
    #checking if the counterweight has enough force to overpower the hammer at its initial resting position assuming initial velocity of counterweight is 0
    if ((m_counterweight*g)*transmissionRatio < (m_hammer*g*0.7071)): #I'm multiplying the force of the hammer by 0.7071 as it starts at 45 deg
        v_linear_hammer_final = 0 #setting final hammer velocity to 0 as the system would not go into action in this situation
    #SSA 12

    return v_linear_hammer_final

#graphs pulley radius vs hammer speed at launch
r_pulley_values = [i / 10000 for i in range(1, 501, 1)]  # r_pulley from 0.001 m to 0.05 m in steps of 0.005 m
v_linear_hammer_final_values = []

for r_pulley in r_pulley_values:
    v_linear_hammer_final_values.append(getHammerSpeed(r_pulley))

plt.figure(figsize=(8, 6))
plt.plot(r_pulley_values, v_linear_hammer_final_values, linestyle='-', color='b')
plt.title("Final Linear Velocity of Hammer vs. Pulley Radius")
plt.xlabel("Pulley Radius (m)")
plt.ylabel("Hammer Linear Velocity (m/s)")
plt.grid(True)
plt.show()

#displays hammer speed with a pulley radius of 0.038m; the approximate largest radius that can be made with our pulley design
print(getHammerSpeed(0.038))