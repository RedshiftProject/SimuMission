# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

simu_downwind = pd.read_csv('Downwind.csv',header=0, sep = ';', engine='python')
simu_downwind_balistic = pd.read_csv('Downwind_balistic.csv',header=0, sep = ';', engine='python')

i_sortie_rampe = 32
i_fin_poussee = 206
i_apogee = 553

## =============================================================================
## 
## 
## 
## =============================================================================
angle_of_attack = np.array(list(simu_downwind.loc[i_sortie_rampe:i_apogee,'Angle of attack (°)']))
force_coeff = np.array(list(simu_downwind.loc[i_sortie_rampe:i_apogee,'Normal force coefficient (?)']))

for i in range(0,len(angle_of_attack)):
    
    angle_of_attack[i] = math.radians(angle_of_attack[i])

lift_gradient = force_coeff / angle_of_attack

stability_moment = lift_gradient * simu_downwind.loc[i_sortie_rampe:i_apogee,'Stability margin calibers (?)']

total_forces = simu_downwind.loc[:,'Thrust (N)'] + simu_downwind.loc[:,'Drag force (N)'] + ( simu_downwind.loc[:,'Mass (g)'] * simu_downwind.loc[:,'Gravitational acceleration (m/s²)'] / 1000 )

## =============================================================================
## 
## =============================================================================
#

fig = plt.figure()
fig.add_axes()
plt.tight_layout()
plt.grid()
plt.title('Profile of flight')
plt.xlabel('Lateral distance (m)')
plt.ylabel('Altitude (m)')
plt.axis('equal')
plt.xlim([0,4000])

plt.plot(simu_downwind.loc[:,'Lateral distance (m)'], simu_downwind.loc[:,'Altitude (m)'] , linewidth = 1, label = 'Nominal case')
plt.plot(simu_downwind_balistic.loc[:,'Lateral distance (m)'], simu_downwind_balistic.loc[:,'Altitude (m)'] , linewidth = 1, label = 'Balistic flight')
            
plt.legend()
plt.savefig( 'Profile of flight', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Total Acceleration')
plt.xlabel('Flight time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.xlim([0,35])

plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Total acceleration (m/s²)'] , linewidth = 1)
            
#plt.legend()
plt.savefig( 'Total Acceleration', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Thrust curve')
plt.xlabel('Flight time (s)')
plt.ylabel('Thrust (N)')
plt.xlim([0,7])

plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Thrust (N)'] , linewidth = 1)
                  
#plt.legend()
plt.savefig( 'Thrust curves', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Margin calibers')
plt.xlabel('Flight time (s)')
plt.ylabel('Stability margin calibers')
plt.xlim([0,30])
plt.ylim([0,6.5])

plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Stability margin calibers (?)'], linewidth = 1)
plt.plot(simu_downwind.loc[:,'# Time (s)'], [2]*len(simu_downwind.loc[:,'# Time (s)']) , color = 'black', linewidth = 1, linestyle = '--' )
plt.plot(simu_downwind.loc[:,'# Time (s)'], [6]*len(simu_downwind.loc[:,'# Time (s)']) , color = 'black', linewidth = 1, linestyle = '--' )

plt.tight_layout()                           
#plt.legend()
plt.savefig( 'Margin calibers', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Lift Gradient')
plt.xlabel('Flight time (s)')
plt.ylabel('Lift Gradient')
plt.xlim([0,30])
plt.ylim([10,42])

plt.plot(simu_downwind.loc[:,'# Time (s)'], [15]*len(simu_downwind.loc[:,'# Time (s)']) , color = 'black', linewidth = 1, linestyle = '--' )
plt.plot(simu_downwind.loc[:,'# Time (s)'], [40]*len(simu_downwind.loc[:,'# Time (s)']) , color = 'black', linewidth = 1, linestyle = '--' )

plt.plot(simu_downwind.loc[:len(lift_gradient)-1,'# Time (s)'], lift_gradient , linewidth = 1)
 
plt.tight_layout()
#plt.legend()
plt.savefig( 'Lift Gradient', papertype = 'a5', dpi = 1080, transparent = True  )

del fig
#
fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Angular rates')
plt.xlabel('Flight time (s)')
plt.ylabel('Angular rate (deg/s)')

plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Pitch rate (°/s)'], label = 'Pitch rate' , linewidth = 1)
plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Yaw rate (°/s)'], label = 'Yaw rate' , linewidth = 1)    
plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Roll rate (°/s)'], label = 'Roll rate' , linewidth = 1)                                    
                  
plt.legend()
plt.savefig( 'Side Angular Rates', papertype = 'a5', dpi = 1080, transparent = True  )


del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Angle of attack')
plt.xlabel('Flight time (s)')
plt.ylabel('Angle (deg)')
plt.xlim([0,20])
plt.ylim([-0.1,5])

plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Angle of attack (°)'] , linewidth = 1)
           
plt.legend()
plt.savefig( 'Angle of attack', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Stability moment coefficient')
plt.xlabel('Flight time (s)')
plt.ylabel('Moment (N/rad.calibers)')
#plt.xlim([0,20])
#plt.ylim([-5,5])

plt.plot(simu_downwind.loc[i_sortie_rampe:i_apogee,'# Time (s)'], stability_moment , linewidth = 1)

plt.tight_layout()                           
plt.legend()
plt.savefig( 'Stability moment coefficient', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Forces on the rocket')
plt.xlabel('Flight time (s)')
plt.ylabel('Force (N)')
plt.xlim([0,27])

plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Thrust (N)'] , linewidth = 1, label = 'Thrust')
plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Drag force (N)'] , linewidth = 1, label = 'Drag Force')
plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Gravitational acceleration (m/s²)']*simu_downwind.loc[:,'Mass (g)']*0.001 , linewidth = 1, label = 'Weight')
                           
plt.legend()
plt.tight_layout()
plt.savefig( 'Forces', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure()
fig.add_axes()
plt.grid()
plt.title('Mach number')
plt.xlabel('Flight time (s)')
plt.ylabel('Mach number')
plt.xlim([0,30])

plt.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Mach number (?)'] , linewidth = 1)
                  
plt.legend()
plt.savefig( 'Mach number', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure(figsize=(10,5))

plt.tight_layout()

forces = fig.add_subplot(1,2,1)
acc = fig.add_subplot(1,2,2)

forces.grid()
acc.grid()

forces.set(title = 'Forces on the rocket', xlabel ='Flight time (s)', ylabel = 'Force (N)', xlim = [0,30] )
acc.set(title = 'Total Acceleration', xlabel ='Flight time (s)', ylabel = 'Acceleration (m/s²)', xlim = [0,30] )


forces.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Thrust (N)'] , linewidth = 1, label = 'Thrust')
forces.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Drag force (N)'] , linewidth = 1, label = 'Drag Force')
forces.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Gravitational acceleration (m/s²)']*simu_downwind.loc[:,'Mass (g)']*0.001 , linewidth = 1, label = 'Weight')

acc.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Total acceleration (m/s²)'] , linewidth = 1)

forces.legend()
plt.savefig( 'Dynamics', papertype = 'a5', dpi = 1080, transparent = True  )

del fig

fig = plt.figure(figsize=(10,5))

plt.tight_layout()

vit = fig.add_subplot(1,2,1)
mach = fig.add_subplot(1,2,2)

vit.grid()
mach.grid()

vit.set(title = 'Velocity to apogee', xlabel ='Flight time (s)', ylabel = 'Velocity (m/s)', xlim = [0,30] )
mach.set(title = 'Mach number', xlabel ='Flight time (s)', ylabel = 'Mach number', xlim = [0,30] )

vit.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Total velocity (m/s)'], linewidth = 1)
                  
mach.plot(simu_downwind.loc[:,'# Time (s)'], simu_downwind.loc[:,'Mach number (?)'], linewidth = 1, color = 'red')

forces.legend()
plt.savefig( 'Kinematics', papertype = 'a5', dpi = 1080, transparent = True  )
































