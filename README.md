                                                 INTERNATIONAL BACCALAUREATE
                                                      DIPLOMA PROGRAMME



 **Internal Assessment in Physics SL** 



# Externalities of Satellite’s mass expansion


Research Question: **To what extent the consequences of a satellite’s mass increase can be similar for different systems of planets and their moons?**

*May 2019*





## Introduction

### Review of the investigation:

#### 1. Abstract 

Throughout the following research, mass (S) of the moon will be being increased from its original initial value to the maximum of the particular taken range or to the maximum mass. Maximum mass is the mass, which will result in the tangent of the surfaces of S and its planet (O). Otherwise, it is also possible that the graph of difference between distance from S to O and radius of S will stay positive at infinity, meaning that the objects will never collide. In this case, the calculations will be stopped at the particular ms/mo within last system. All operations will be performed by the program written especially for the study by its author in Python programming language.

#### 2. Variables:

* mass of S: m_s (10^22 kg)
* mass of O: m_o (10^22 kg)
* velocity of S: v_s (10^3 km/s)
* velocity of O: v_o (10^3 km/s)
* initial distance between S and O: r_o (10^3 km)
* distance between S and O: d[^1]  (10^3 km) 

[^1]:This variable has distinct symbols in different situations: Original – r, Binary – d, Final - r

* distance from S to the mass center: r (semi-major axis) (10^3 km)
* distance from O to the mass center: R (10^3 km)
* density of S: ρ (10^10 kg/km^3)
* radius of O: r_s (10^3 km)
* initial m_s/ initial m_o: F0
* specific parameter: l
* m_s/m_o: F1 
* m_smax/ m_o: F2 

#### 3. Five situations explored (in order of appearance): 

* Original— initial conditions, all required data is taken from open sources. Further calculations are based on the formulas of conserved total energy within the system and of first cosmic velocity.

* Binary1  — following model, when the rise of ms leads to the shift of the mass center out of O, leading to an occurrence of two orbits (shown in Illustration2), where the nearer one is of the Object’s. 

* Binary2 — third situation, where the ms becomes larger than mo. Nevertheless, both objects are still moving simultaneously on two different orbits (Illustration 3). Formulas are the same, as for the Binary1. The maximum value here for F1 is 50.

* Binary3 – fourth system, identical to previous one, except the scale of calculations: step is attached to the new parameter “l”, which makes it possible to skip the colossal difference between Binary2 and Final by substantially increasing the value of the step. It allows to deal with the computes’ limitations by reducing the number of calculations The system operates within Binary3, as long as the mass center locates not within S.

* Final – last system, when the mass center gets under the surface of S. O is moving around S, having velocity (v_o). A specific range is given to this system, which helps to track the behavior of the variables at the infinity and to avoid endless calculations.

### Background
Constantly-evolving area of exploring the outer universe makes the entire world community pay high attention not only to the studies of exoplanets  and exomoons , but also to the searches for connections between the results of scientists’ investigations of similar systems. It seems that space  still covers a number of secrets, making the public feel excited of new assumptions: presence of parallel universes, white holes, wormholes and emerging theories, such as Big Freeze. Having a strong desire to even though insignificantly contribute to the process of exploring this area, I decided to devote my IA to the previously not researched topic (at least, I have not found any analogies), implementing my knowledge from computer science in order to adopt this work for requests of other investigators. 
When I was working on “PHet.Colorado” program, I found an interesting simulation where the laws of gravitation were shown. However, what was remarkable is that the double growth of moon’s mass led to its collision with Earth. When I asked my Physics teacher does it really work that way and he answered that the real-life situation is more comprehensive and complicated, I decided to create an investigation with a purpose not only to identify the more truthful state of things, but also to contain my research in the look for the correlation between changes within one variable and subsequent alterations of dependent variables. 

### Research question

To what extent the consequences of a satellite’s mass increase can be similar for the different systems of planets and their moons? 

### Aim

To clearly identify the externalities of expanding satellite’s mass within the planet-moon system and occurrence or absence of the several distinct variables’ relationships.

## Main Body of the Investigation

### Materials

* Calculator
* program, written in Python programming language
* programs: Excel, Numbers, Pages    
* wikidata.org 

### Method

1. Create a code in Python, which uses all the necessary data to hold indispensable mathematical operations, based on the formulas from Physics (all further steps are held within the created code).
2. Generate a file with the initial values of required variables for the program.
3. Calculate the values of necessary constants according to the proposed measuring system (e.g, G = 0.000000667).
4. Calculate m_s/ m_o = F0.
5. From the data gathered, determine the Et (total energy within the system, constant): E_t= (m_s×v_s^2)/2)– G×m_s×m_o/r_o.
6. Identify the initial value of ms with the system’s constant: tmp_ms.
7. Identify the initial value of r with the system’s constant: r_o.
8. Identify the initial value of F1 with the system’s constant: F0.
9. Count the initial step: step =(m_o-m_s)/100000.
10. While rs  >  R – proposed condition – (R = m_s×r/(m_o+m_s )), the system operates in the Original situation. Continue adding steps and counting new values of vs  (v_s= √((G×m_o/r)),  r  (r=((2×G×m_s×m_o)/(m_s×v_s 2 – 2×E_t ))),  R , F1, until the proposed condition is true. 
11. If rs > r, then F2 = m_smax/m_o, m_smax = m_s (value of m_s, when the previous condition became true). Program is stopped because the collision occurred.
12. When R obtains a greater value than rs, the Binary1 has to be introduced
13. New value for step: step = (m_o-tmp_ms_ ))/1000
14. While F1 ≤ 1 – proposed condition – continue adding steps and simultaneously finding out and recording changes of r (r = m_o×d/(m_o+ m_s )), d (d = ∣-0.5×G×m_s×m_o/E_t ∣ ), v_s (v_s= √((G×m_o^2 ))/((d×(m_s+ m_o )) )) ) ), F1, v_o (v_o=√((G×((m_s^2 ))/((d × (m_s+ m_o)) ))) , R (R=(m_s× d )/((m_o+ m_s ) )),.
15. When the condition becomes false, the Binary2 is exited. At the final point, where F1 = 1, calculate v_x (v_x= √((G×((m_o^2))/((d × 2 ×m_o ) )) )), r_x (r_x=d/2)
16. Introduce the third system - Binary2, where the new value of step is: step =(m_o-tmp_ms))/100
17. While r^3> (3×m_s/((4×π×p) ))and F1 < 50 – proposed condition – record changes of dependent variables: r (r = m_o×d/((m_o+ m_s ) )), d (d = ∣-0.5*G×m_s×m_o/E_t ∣ ), v_s (v_s= √((G×((m_o^2 ))/((d × (m_s+ m_o )) )) ) ), F1, vo ( v_o=√((G×((m_s^2 ))/((d × (m_s+ m_o )) )) ), R (R=(m_s× d )/((m_o+ m_s ) )), while making every step
18. If the proposed condition appeared to be false, the forth system has to be introduced – Binary3. Step is equal to m_s×l. The specific parameter l and its value are denoted:
	*Value of l for the system “Phobos and Mars” is 10^20
	*Value of l for the system “Tethys and Saturn” is 10^16
	*Value of l for the system “Moon and Earth” is 10
	*Value of l for other systems is 10^9
19. While r^3> (3×m_s/((4×π×p) ))and F1 ≥ 50 – proposed condition – record changes of dependent variables: r (r = m_o×d/((m_o+ m_s ) )), d (d = ∣-0.5×G×m_s×m_o/E_t ∣ ), v_ (v_s= √((G×((m_o^2 ))/((d × (m_s+ m_o )) )) ) ), F1 vo ( v_o=√((G×((m_s^2 ))/((d × (m_s+ m_o )) )) ), R (R=(m_s× d )/((m_o+ m_s ) )), while making every step
20. When the proposed condition appears to be false, last situation starts working – Final. Last value of F1 in the previous situation is used to determine the maximum value for F1 in Final: F1 * 200*l
21. While r > ∛((3×m_s/((4×π×p) )) ) and  F1 <a – proposed condition – keep calculating R ( R=((2×G×m_s×m_o)/(m_o×v_o 2 – 2×E_t )), v_o  (v_o= √(G×m_s/r)), F1, r (r =((m_o×r))/((m_o+m_s ) ))
22. If r  <  ∛(3×m_s/((4×π×p) )  ), then F2 = m_smax/m_s, m_smax = m_s (value of m_s, when the previous condition became true). Program is stopped because the collision occurred
23. Repeat the experiment for different systems (Moon and Earth, Phobos and Mars, Callisto and Jupiter, Europa and Jupiter, Tethys and Saturn,  Titan and Saturn, Oberon and Uranus, Ariel and Uranus, Triton and Neptune, Charon and Pluto)
24. Plot the graph, where on y-axis is F1/F0, while on axes is r/r_o, for all observed systems: Relationship of Alterations
25. Plot the graph, where on y-axis is F1, while on axes is r, for all observed systems: Distance from S to the mass center
26. Plot the graph, where on y-axis is F1, while on axes is distance between planets, for all observed systems: Distance between planets
27. Plot the graph, where on y-axis is F1, while on axes is v_s, for all observed systems: Orbital velocity of the S
28. Plot the graph, where on y-axis is F1, while on axes is v_o, for all observed systems: Orbital velocity of O
29. Plot the graph, where on y-axis is F1, while on axes is R, for all observed systems: Distance from O to the mass center

### Hypothesis

Each of the aforementioned graphs will have distinct values in different systems, but will show the identical behavior. Moreover, assuming that the Et is always constant, the collision will not take place, and the system will exit binary situation.

### Initial Data
System                | m_o, kg×10^22 | m_s, kg×1022 | r_o, 103 km | v_s, 103 km/s | ρ, 1013 kg/km3 | rs, 103 km 
:-------------------- |:------------:|:-----------:|:----------:|:------------:|:--------------:|------------:
Moon and Earth	      |  597	     |  7,35	   |  384,4	| 0,00102      | 0,000003346	| 6,371
Mars and Phobos       |	62,4	     |  0,00000107 |   9,4	| 0,00214      | 0,000001876	| 3,389
Jupiter and Callisto  |	189820	     |  10,759	   |  1882,7	| 0,00821      | 0,000001834	| 69,911
Jupiter and Europa    |	189820	     |  4,799	   |  670,9	| 0,01374      | 0,000003013	| 69,911
Saturn and Titan      | 56834	     |  13,452	   |  1221,87	| 0,00557      | 0,000001879	| 58,232
Saturn and Tethys     |	56834	     |  0,06174	   |  294,619	| 0,01135      | 0,000000984	| 58,232
Uranus and Oberon     |	8681	     |  0,3014	   |  583,52	| 0,00315      | 0,00000163	| 25,362
Uranus and Ariel      |	8681	     |  0,1353	   |  191,02	| 0,00551      | 0,00000159	| 25,362
Neptune and Triton    |	10241,3	     |  2,14	   |  354,759	| 0,00439      | 0,00000206	| 24,622
Pluto and Charon      |	1,303	     |  0,1586	   |  19,591	| 0,00021      | 0,000001702	| 1,187
						

