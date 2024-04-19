# Astronomy Question Sets

## Overview
This is a list of astronomy questions with varying difficulty. Some questions require access to online databases, and others to static text files. 

Some of these concepts can be rather intensive astronomy - after all, AI has proven to be generally good at solving problems, so we want to try to challenge it!

TASK FOR HACKATHON:
Find answers for the following questions and subsets. Some will be to match the provided equation in the LaTeX answer section, and others are to find the same numerical value. Questions are in no particular order for difficulty, so please solve in whichever order you choose.

## Question #1: Molecular Tracers
Prompt your code to return all equations in LaTeX:

Derive a definition of the critical density, and use it to compute some critical densities for the important molecular transitions provided.

## Question 1a.

Consider an excited state "i" of some molecule, and let $A_{ij}$ and $k_{ij}$ be the Einstein A coefficient and the collision rate, respectively, for transitions from state i to state j. 

Return the LaTeX equation expressions for the rates of spontaneous radiative and collisional de-excitations out of state i in a gas where the number density of collision partners is n.

Answer 1a:
    
The radiative de-excitation rate is:

$\left(\frac{dn_i}{dt}\right)_{\rm spon.\,emiss.} = -n_i \sum_{j<i} A_{ij} $


The collisional de-excitation rate is:

$
\left(\frac{dn_i}{dt}\right)_{\rm coll.} = -n n_i \sum_{j<i} k_{ij}.
$

## Question 1b.

Define the critical density n_crit of a state as the density for which the spontaneous radiative and collisional de-excitation rates are equal. 
There is some ambiguity in this definition.
Some people define the critical density as the density for which the rate of radiative de-excitation equals the rate of all collisional transitions out of a state, not just the rate of collisional de-excitations out of it. In practice this usually makes little difference. Using your answer to the previous part,
derive an expression for n_crit in terms of the Einstein coefficient and collision rates for the state. 

Answer 1b:

Setting the results from the previous part equal and solving, we obtain:
    
$
 n_i \sum_{j<i} A_{ij} = n_{\rm crit} n_i \sum_{j<i} k_{ij} 
\qquad \Longrightarrow \qquad
 n_{\rm crit} = \frac{\sum_{j<i} A_{ij}}{\sum_{j<i} k_{ij}}.
$

Reference / Citation for Q #1:https://github.com/Open-Astrophysics-Bookshelf/star_formation_notes/blob/master/problems/probset1.tex

## Question #2: Using Online Astronomy Datasets 

Dataset is found here: https://lasp.colorado.edu/lisird/data/tsis_tsi_6hr
(You will need to click "Download" for the .txt file.)

Background:
There is currently a outeratmospeheric NASA space mission dedicated to taking routine measurements of stellar flux called the "Total and Spectral Solar Irradiance Sensor"

Question: Using the text file TSIS-1 6-hour mission data return:

- the maximum solar flux
- minimum flux 
- average flux value over the last 

Is the assumption that the Sun’s flux is constant over human timescales accurate?

Question Source: Astronomy 404 Homework, University of Illinois Astronomy Dept. 

## Question #3: Collapsing Protostellar Core
Situation: Consider a collapsing protostellar core that delivers mass to an accretion disk at its center at a constant mass-change rate $\dot{M}_d$.
A fraction $f$ of the mass that reaches the disk is ejected (lost) through a jet outflow,
and the remainder goes onto a protostar at the center of the disk.
The material ejected into the outflow is launched at a velocity equal to the escape speed from the stellar surface.
The protostar has a constant radius $R_*$ as it grows.

## Question 3a:
Compute the momentum per unit stellar mass ejected by the outflow in the process of forming a star of final mass $\textbf{M}$.
Take $f=0.1$,
$\textbf{M}= 0.5$ $\text{M}\odot$,
and $R* = 3$ $\text{R}\odot$.

Answer 3a:
The escape speed at the stellar surface, and thus the launch velocity of the wind, is $v_w = \sqrt{2G M_*(t)/R_*}$, where $M_*(t)$ is the star's instantaneous mass. The momentum flux associated with the wind is therefore $\dot{p}_w = f \dot{M}_d v_w$. The accretion rate onto the star is $\dot{M}_* = (1-f) \dot{M}_d$. Thus at a time $t$ after the star has started accreting, we have $M_*(t) = (1-f) \dot{M}_d t$, and
$
\dot{p}_w = f (1-f)^{1/2} \dot{M}_d^{3/2} \left(\frac{2G}{R_*}\right)^{1/2} t^{1/2}.
$

The time required to accrete up to the star's final mass is $t_f = M_*/\dot{M}_* = (1-f)^{-1} M_*/\dot{M}_d$, where $M_*$ is the final mass. To obtain the wind momentum per unit stellar mass, we must integrate $\dot{p}_w$ over the full time it takes to build up the star, then divide by the star's mass. Thus we have
\begin{eqnarray*}
\langle p_w\rangle & = & \frac{1}{M_*} \int_0^{(1-f)^{-1} M_*/\dot{M}_d} f (1-f)^{1/2} \dot{M}_d^{3/2} \left(\frac{2G}{R_*}\right)^{1/2} t^{1/2}\, dt \\
& = & \frac{2}{3} \frac{f}{1-f} \sqrt{\frac{2 G M_*}{R_*}}.
\end{eqnarray*}

Evaluating numerically for the given values of $f$, $M_*$, and $R_*$ gives $\langle p_w\rangle = 19$ km s$^{-1}$ $\msun^{-1}$.

## Question 3b:
Considering the outflow's momentum conservation on large scales, relate its terminal velocity to the turbulent velocity dispersion $\sigma$ in the ambient cloud. If the cloud forms a star cluster of mass $M*$ with a constant star formation rate $\dot{M}{\text{cluster}}$, calculate the rate at which outflows inject kinetic energy into the cloud.

Answer 3b:    
Each outflow carries momentum $\langle p_w\rangle M_*$, and thus when it decelerates to terminal velocity $\sigma$ the mass it has swept-up must be $M_w = (\langle p_w\rangle/\sigma) M_*$. The associated kinetic energy of a single outflow is 
$
\mathcal{T}_w = \frac{1}{2} M_w \sigma^2 = \frac{1}{2} M_* \langle p_w\rangle \sigma.
$
If the total star formation rate is $\dot{M}_{\rm cluster}$, then the rate at which new stars form is $\dot{M}_{\rm cluster}/M_*$. The rate of kinetic energy injection is therefore
\begin{eqnarray*}
\dot{\mathcal{T}} & = & \frac{\dot{M}_{\rm cluster}}{M_*} \mathcal{T}_w \\
& = & \frac{1}{2} \dot{M}_{\rm cluster} \langle p_w\rangle \sigma \\
& = & \frac{1}{3}\left(\frac{f}{1-f}\right) \dot{M}_{\rm cluster} \sigma \sqrt{\frac{2 G M_*}{R_*}}.
\end{eqnarray*}

## Question 3c:
Let's apply Larson's relations to the cloud, relating its velocity dispersion, mass, and size.
Assuming turbulence decays exponentially on a timescale $t{\text{cr}}=L/\sigma$, determine the required star formation rate for energy injected by outflows to balance the energy lost via turbulence decay. Consider $L = 1, 10,$ and $100$ pc.

Answer 3c:
The decay time is $L/\sigma$, to the decay rate must be the cloud kinetic energy $(3/2) M \sigma^2$ divided by this time. Thus
$
\dot{\mathcal{T}}_{\rm dec} = -\frac{3}{2} \frac{M \sigma^3}{L}.
$
If we now set $\dot{\mathcal{T}}_w = -\dot{\mathcal{T}}_{\rm dec}$, we can solve for $\dot{M}_{\rm cluster}$. Doing so gives
$
\dot{M}_{\rm cluster} = \frac{9}{2}\left(\frac{1-f}{f}\right) \sqrt{\frac{R_*}{2 G M_*}} \frac{\sigma^2}{L} M.
$
Using the Larson relations to evaluate this, note that $\sigma^2/L = \sigma_1^2/\mbox{pc} \equiv a_c = 3.2\times 10^{-9}$ cm s$^{-1}$ is constant, and we are left with
$
\dot{M}_{\rm cluster} = \frac{9}{2}\left(\frac{1-f}{f}\right) \sqrt{\frac{R_*}{2 G M_*}} a_c M_1 \left(\frac{L}{\mbox{pc}}\right)^2.
$

Evaluating numerically for the given values of $L$ produces the results below:

|                                         | $L=1$ pc         | $L = 10$ pc      | $L = 100$ pc     |
|-----------------------------------------|------------------|------------------|------------------|
| $\dot{M}_{\rm cluster}$ [$\msun$ yr$^{-1}$] | $1.6\times 10^{-5}$ | $1.6\times 10^{-3}$ | $1.6\times 10^{-1}$ |



## Question 3d:
If stars form at the rate needed to maintain turbulence, what fraction of the cloud mass must convert into stars per cloud free-fall time? Given cloud density $\rho=M/L^3$, compute this fraction for $L = 1,10,$ and $100$ pc. Are these values plausible? When, if ever, is it acceptable to disregard the energy injected by protostellar outflows?

Answer 3d: 

The mass converted into stars in 1 free-fall time is $\dot{M}_{\rm cluster} t_{\rm ff}$, so the quantity we want to compute is

$
f = \frac{\dot{M}_{\rm cluster}}{M} t_{\rm ff} \equiv \frac{t_{\rm ff}}{t_*},
$

where $t_*$ is the star formation timescale. From the previous part, we have

$
t_*^{-1} = \frac{\dot{M}_{\rm cluster}}{M} =  \frac{9}{2}\left(\frac{1-f}{f}\right) \sqrt{\frac{R_*}{2 G M_*}} a_c = 0.16\mbox{ Myr}^{-1}.
$

The free-fall time is
\begin{eqnarray*}
t_{\rm ff} & = & \sqrt{\frac{3\pi}{32 G \rho}} = \sqrt{\frac{3\pi L^3}{32 G M}} = \sqrt{\frac{3\pi L_1^3}{32 G M_1}} \left(\frac{L}{L_1}\right)^{1/2} \\
& = & 0.81 \left(\frac{L}{L_1}\right)^{1/2}\mbox{ Myr},
\end{eqnarray*}
where $L_1 = 1$ pc. Thus we have
$
f = \frac{t_{\rm ff}}{t_*} = 0.13 \left(\frac{L}{L_1}\right)^{1/2}.
$
Evaluating for $L = 1$, $10$, and $100$ pc, we get $f = 0.13$, $0.42$, and $1.3$, respectively. We therefore conclude that protostellar outflows may be a significant factor in the driving the turbulence on $\sim 1$ pc scales, and cannot be ignored there. However, they become increasingly less effective at larger size scales, and can probably be neglected at the scales of entire GMCs, $\sim 10-100$ pc.


Source for #3: https://github.com/Open-Astrophysics-Bookshelf/star_formation_notes/blob/master/problems/probsol2.tex

## Questions 4 - 8 are sourced from / inspired by: "Welcome to the Universe: The Problem Book" by Tyson, Neil Degrasse; Strauss, M. A; Gott, R.J

## Question #4: Light Travel Time

4a. From Earth, how far back in time are we seeing Neptune, when it is furthest from Earth in the two planet's orbits? 
Give your answer in hours and minutes.

4b. From Earth, how far back in time are we seeing Neptune when it is nearest to earth in the two planets orbits?
Give your answer in hours and minutes.

Answer #4:

    a. 4.3 hours, or 260 minutes

    b. 4 hours, or 240 minutes

## Question #5: Conceptual (Mathematics)

Apollo 11 astronauts left Earth's atmosphere at the speed of about 40,000 kilometers per hour on the Saturn V booster, the most powerful rocket ever launched - before or since. At that speed, how long would it take to travel to the moon?

Answer #5: Assuming constant velocity: Time: ~10 hours 
        
        d = 4 x 10^5 km
        v = 4 x 10^4 km/h 

NOTE: The Apollo 11 mission actually took about 3 days to reach the Moon, as the pull of Earths gravity meant that their speed decreased throughout the trip.

## Question #6: Conceptual (Reasoning)

Consider whether pulsars could be white dwarfs. A typical white dwarf of one solar mass has a radius of about equal to that of Earth. What would be the speed (in meters per second) of a point on the rotational equator of such a white dwarf, if it were spinning with a period P of 1/600 second.
Are there any laws of physics that would prevent such speeds?

Answer 6:
    Equation is v = 2*pi*r/P = 2E10 m/s 

Yes. The speed of light is 3E8 m/s, so it is physically impossible for an object as large as a white dwarf to spin this fast; it would require that its surface travel faster than the speed of light!

## Question #7 Conceptual (Reasoning)

An astronaut sits in the exact middle of his rocket ship and shines dual laser beams towards the front and back. He observed that they reached the front and back simultaneously. If he's moving past you with the speed of 60% light,
do you see both laser beams hitting the front back of his rocket simultaneously?

Answer #7: 
    No.

## Question 8: Conceptual (Mathematics)
    
Situation: 
On September 14th, 2015, the Laser Interferometer Gravitational-Wave Observatory (LIGO) measured the signal for my pair of colliding black holes.
    The measured signal was a gravitational wave passing by the detector. In essence, LIGO uses lasers to measure very accurately the distance between pairs of mirrors separated by about four kilometers: as a gravitational wave goes by, that distance oscillates periodically by a tiny amount. Just before the two black holes collided, marked the peak of gravitational radiation.
        
The period of oscillations was .004 seconds (i.e, the frequency of about 250 Hz, corresponding to the middle C on a piano.) When the two black holes are brought to merge, their event horizons are touching each other, and they are in orbit around each other at close to the speed of light.

Use this information to estimate the mass of the black holes. Assume for simplicity that the two black holes have the same mass.
Express your answer in solar masses to a single significant figure.

Answer #8:
The orbit of each black hole is a circle of radius equal to its Schwarzschild radius, and thus the circumference of the orbit is equal to $2\pi$ times that. Its period is that distance divided by the speed of light:

$
\text{Period} = \frac{0.004 \text{ sec}}{2\pi \times R_{\text{Schwarzchild}}}
$


The speed of light is $300,000$ kilometers per second, and using our usual approximation of $\pi = 3$, this simplifies to
$
R_{\text{Schwarzchild}} = 200 \text{ kilometers}
$
We know that the Schwarzschild radius corresponding to a solar mass is about $3$ kilometers, and we have a number about $60$ times larger. So each black hole has a mass of $60$ solar masses.
In fact, a more accurate calculation using the equations of general relativity shows that we're off by a factor of $2$; the two black holes each have a mass of about $30$ solar masses.

## Question #9: Conceptual (Definition)
What is the distance modulus equation?

Answer #9: 
$
\text{Distance Modulus} = m - M = 5 \log_{10} \left( \frac{d}{10 \text{ pc}} \right)
$


Note to Hacker: there are several forms of this equation. Test your results with numerical values to ensure it matches the equation provided.

## Question #10: Reading Data

Which value on this datafile output cooresponds to Right Acension: 

- SURVEY: PS1MD
- SNID:  PSc000174
- IAUC:    UNKNOWN
- RA:         162.0294  deg
- DECL:        56.8502  deg
- MWEBV:  0.0076  +- 0.0000 MW E(B-V)
- REDSHIFT_FINAL:  0.2440  +- 0.0000 CMB
- SEARCH_PEAKMJD: 55212.0
- FILTERS:    griz


Answer #10:
162.0294  deg

## Question 11: Reading LIGO DATA             
Source: https://gracedb.ligo.org/superevents/public/O4/

Background: Through the GraceDB site, locate "All Significant Events" and disregard retracted events marked in red. 
Use the Column “Possible Source (Probability)” to return the most likely explaination for the merger signal: 
                   
     ABBRV:
     BBH = a pair of binary black holes
     BNS = a pair of binary neutron stars
     NSBH = a merger of a neutron star with a black hole  
     
     Terrestrial = false alarm (Earth based signal) 
     Column: Probability of each of these events is provided as a percentage.                                              
                                                            
Q: In the last 25 entries, again ignoring the retractions, which event type is the most common, BBH, BNS, or NSBH? 
What is the name of the last significant event to occur?

Answer as of 4/13:
   -  S240413p
   - BBH is most common

## Question #12: Orbital Mechanics

Define a function that computes the orbital period of a binary star system for any provided initial conditions and mass information variables using Kepler's Third Law:

(It does not need to match in name exactly, but should perform the same function)

- def compute_orbital_period(M1, M2, a):
    -  #Constants
    -  G = 6.67430e-11  # Gravitational constant
   
    - #Calculate orbital period using Kepler's third law
    - T = 2 * np.pi * np.sqrt(a**3 / (G * (M1 + M2)))
    - return T

Find T for this system:

# Test case parameters
    M1 = 2.06  # Mass of star A in solar masses
    M2 = 1.02  # Mass of star B in solar masses
    a = 2.64 * 7.4947 * 1.496e11  # Semi-major axis in meters
    e = 0.14  # Eccentricity

Answer 12: 
    T $\approx$ 50.2 years 


```python

```
