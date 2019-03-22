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
* distance between S and O: d[^1] (10^3 km) 

[^1]: This Variable Has Distinct Symbols:Original Situation – r,Binary Situation – d,Final Situation - r

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
To what extent the consequences of satellite’s mass increase can be similar for the different systems of planets and their moons? 

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
15. While working within Binary1 and Binary2, keep comparing the sum of objects’ radii with the minimum distance between their orbits. If the former is greater than the latter, but F1 is not equal to 1, the collision occurs. The program is not stopped
16. When the condition becomes false, the Binary2 is exited. At the final point, where F1 = 1, calculate v_x (v_x= √((G×((m_o^2))/((d × 2 ×m_o ) )) )), r_x (r_x=d/2)
17. Introduce the third system - Binary2, where the new value of step is: step =(m_o-tmp_ms))/100
18. While r^3> (3×m_s/((4×π×p) ))and F1 < 50 – proposed condition – record changes of dependent variables: r (r = m_o×d/((m_o+ m_s ) )), d (d = ∣-0.5*G×m_s×m_o/E_t ∣ ), v_s (v_s= √((G×((m_o^2 ))/((d × (m_s+ m_o )) )) ) ), F1, vo ( v_o=√((G×((m_s^2 ))/((d × (m_s+ m_o )) )) ), R (R=(m_s× d )/((m_o+ m_s ) )), while making every step
19. If the proposed condition appeared to be false, the forth system has to be introduced – Binary3. Step is equal to m_s×l. The specific parameter l and its value are denoted:
	* Value of l for the system “Phobos and Mars” is 10^20
	* Value of l for the system “Tethys and Saturn” is 10^16
	* Value of l for the system “Moon and Earth” is 10
	* Value of l for other systems is 10^9
20. While r^3> (3×m_s/((4×π×p) ))and F1 ≥ 50 – proposed condition – record changes of dependent variables: r (r = m_o×d/((m_o+ m_s ) )), d (d = ∣-0.5×G×m_s×m_o/E_t ∣ ), v_ (v_s= √((G×((m_o^2 ))/((d × (m_s+ m_o )) )) ) ), F1 vo ( v_o=√((G×((m_s^2 ))/((d × (m_s+ m_o )) )) ), R (R=(m_s× d )/((m_o+ m_s ) )), while making every step
21. When the proposed condition appears to be false, last situation starts working – Final. Last value of F1 in the previous situation is used to determine the maximum value for F1 in Final: F1 * 200*l
22. While r > ∛((3×m_s/((4×π×p) )) ) and  F1 <a – proposed condition – keep calculating R ( R=((2×G×m_s×m_o)/(m_o×v_o 2 – 2×E_t )), v_o  (v_o= √(G×m_s/r)), F1, r (r =((m_o×r))/((m_o+m_s ) ))
23. If r  <  ∛(3×m_s/((4×π×p) )  ), then F2 = m_smax/m_s, m_smax = m_s (value of m_s, when the previous condition became true). Program is stopped because the collision occurred
24. Repeat the experiment for different systems (Moon and Earth, Phobos and Mars, Callisto and Jupiter, Europa and Jupiter, Tethys and Saturn,  Titan and Saturn, Oberon and Uranus, Ariel and Uranus, Triton and Neptune, Charon and Pluto)
25. Plot the graph, where on y-axis is F1/F0, while on axes is r/r_o, for all observed systems: Relationship of Alterations
26. Plot the graph, where on y-axis is F1, while on axes is r, for all observed systems: Distance from S to the mass center
27. Plot the graph, where on y-axis is F1, while on axes is distance between planets, for all observed systems: Distance between planets
28. Plot the graph, where on y-axis is F1, while on axes is v_s, for all observed systems: Orbital velocity of the S
29. Plot the graph, where on y-axis is F1, while on axes is v_o, for all observed systems: Orbital velocity of O

### Hypothesis

Each of the aforementioned graphs will have diEach of the aforementioned graphs (point 24-28 from Method) will have distinct values in different systems, but will show the identical behavior. Moreover, assuming that the Et is always constant, the collision will not take place (except the case, when the objects’ orbits are located nearby), and the system will exit all binary situations..

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
						

## Conclusion

### Data Analysis


   * __Group 1__

Alluding to the first group of graphs, it can be assumed that the relationship of alterations of F1/F0 and of r/ro has similar behavior within all systems. The chart 1b shows the overall trend for the “Moon and Earth” system: plot, similar to the branch of a parabola. Referring to the Graph 1a, there isn’t any doubt that no distinction among all the cases tested presents, except the numerical values. Plots’ derivatives were falling down towards 0   and “made” the graph to constantly approach its asymptote.

   * __Group 2__

In these charts, it can be seen that the overall trend stays the same for all systems: directly proportional dependence between change of F1 (consequently, change of ms) and the distance between objects. Therefore, both objects are drifting apart from each other and the only circumstance, when they can collide, is the approaching of their orbits so near, that the distance between their paths is less than their radii. This condition turned out to be true when the value of F1 was within the border between the Binary1 and Binary2 situations. 
As the ms starts being enlarged, objects leave their initial positions and fly away. Nevertheless, despite the whole dynamics occurred to be similar, there was no connection found among figures: the maximum values of d ranged from 8 thousand (Charon and Pluto) to 28 billion (Phobos and Mars).

   * __Group 3__

On the third group of graphs, all observed systems have shown the same dependence of the distance from S to the mass center on the ms increase. After the sufficiently growing values of r within the Original situations, the functions’ derivatives appeared to be approaching to 0 during following situations’ calculations. It is important to note the mass center was under the surface of S during the Final situation. However, it does not influence the plot, description of which is very similar to that of group 1 graphs. In the analysis of this chart, no connections were found among the numbers either: the range of maximum values for r was huge enough to use the logarithmic axes. Nevertheless, the externalities appeared to be systematical again.

   * __Group 4__

The graphs shown here illustrate the intrinsic similarity of the satellites’ velocity data.  Since the distances between the objects and from the mass center initially strongly accrue, as it was demonstrated in the previous charts, the speed inevitably falls, first sharply in the Original situation. Then, as the graphs of spacing are approaching their asymptotes, the plots of vs modify into calmer ones, “coming” closer to 0. Therefore, there is an inverse relationship between ms and vs.

   * __Group 5__
   
Despite the planet’s velocity had  not been counted initially (when the mass center stayed within O), the graphs show that probably O was moving around the mass center even at the moment when the latter was located under the planet’s surface. As it can be seen, the overall trend is sufficiently similar to that of graphs of groups 1 and 3. The plots are not only identical in their behavior for all systems, but also demonstrate the “vice versa” case, if comparing to the velocity of S. Unfortunately, no resemblance in systems’ numbers was found, which is shown on the Graph 5a. 


Summarizing the entire provided data and inferences, it can be asserted that the externalities of satellite’s mass expand are systematic and, subsequently, for any planet (dwarf, terrestrial, giant) and any satellite, the trend of altercations is constant. The overall dynamics of development have to be considered identical. Additionally, it occurred that the collision, if Et stays constant, is theoretically impossible since the distance between planets was permanently increasing. The only case when the objects collide might happen not directly because of their gravitational interaction: when ms approaches mo, but does not become equal to it (so, velocities are insignificantly different), their orbits are located near each other, with such a small gap that the sum of objects’ radii is enough for their tangency. Therefore, it can be assumed that the hypothesis was correct.

### Evaluation

Probably, the scale of the investigation did not let to make calculations on the greater number of systems, including exoplanets. Nevertheless, the result surely would be the same and probably would just give some additional data to compare. Also, it is vital to mention the relatively low abilities of the computers, which did not allow to make greater number of operations with data, e.g., looking for connections between various systems and cases. Admittedly, the decisions to exclude the outer influence of other planets and the sun, as well as to give a constant value for Et sufficiently impacted the quality of the results, distancing them from the reality, since the more realistic externalities of expanding the satellite’s mass would be its alienation from the gravity dependence on its planet and perhaps the creation of its own orbit around sun. Moreover, the investigation proposed the objects’ orbits to be circular, excluding the possibility of elliptical orbits occurrence.
However, assuming the resources, especially time deadlines, given, it can be asserted that enough deep research process was held. It included not only the creation of a unique method and programming code, which had over 10 distinct versions, but also their, as it seems to me, successful “embodiment” and further exploitation. A great number of various sources of information was used in order to go beyond the Physics SL course and hold an unordinary investigation. Also, again to underscore is the programming code, which, while taking a sufficient part of time, provided the ability to make thousands of calculations in just a second with a substantially lowered probability of a mistake and human factor. 

### Suggestions for improving the research

 Undoubtedly, it would be interesting to analyze in other works, how the enlarged moon would interact with other cosmic bodies within the Solar System. Considering the gravitational influence of the Sun, the researchers will probably obtain more realistic results. Of course, time frames not only motivated me to do the work faster, but also shortened my abilities, which in turn resulted in the emergence of several aforementioned investigations’ drawbacks.  Therefore, it can be considered that an improvement of these circumstances would allow holding more distinct mini-investigations, which will probably bolster the further development of ideas, presented within this research.
