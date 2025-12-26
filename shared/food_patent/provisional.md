# PROVISIONAL PATENT APPLICATION

**Title:** Systems and Methods for Automated Preparation of Granular Starch-Based Food Products via Hydro-Thermal Agitation with Closed-Loop Sensor Control

---

## CROSS-REFERENCE TO RELATED APPLICATIONS

[0001] None.

---

## FIELD OF THE INVENTION

[0002] This invention relates to food processing apparatuses and methods, and more specifically to automated systems for preparing granular starch-based foods using coordinated electromagnetic heating, peripheral fluid injection, vertical mechanical agitation, and closed-loop sensor feedback.

---

## BACKGROUND OF THE INVENTION

[0003] Granular starch-based foods such as couscous present a fundamental processing challenge: the starch granules must be hydrated and gelatinized without fusing into a cohesive mass.

[0004] Traditional artisanal preparation requires skilled manual intervention, including repeated fluffing with fingers or forks to separate granules during and after steaming.

[0005] Industrial systems utilizing extrusion create uniform pellets but destroy the porous structure of true rolled couscous.

[0006] Domestic appliances employ either rotary blades that shear delicate hydrated granules, or passive steaming that permits agglomeration under the weight of the food mass.

[0007] Microwave heating offers rapid energy transfer but produces non-uniform temperature distributions, resulting in hot spots that burn some regions while others remain undercooked.

[0008] No existing system provides: controlled hydration from the periphery to counteract microwave center-heating; vertical mechanical agitation that separates granules without shearing them; lipid pre-coating to form amylose-lipid complexes that reduce stickiness; closed-loop control using real-time sensing of viscosity and temperature; and active retrogradation cooling to set texture while maintaining granule separation.

---

## SUMMARY OF THE INVENTION

[0009] The invention provides an automated food processing system comprising a resonant cavity containing a microwave energy source, a removable vessel of microwave-transparent material, a circumferential liquid distribution manifold positioned at the upper perimeter of the vessel, a vertical reciprocating agitation assembly with interchangeable tool heads, a multi-sensor suite including infrared temperature sensors and a torque sensor, and a control unit implementing closed-loop feedback.

[0010] The system executes a staged algorithm comprising lipid intercalation, gradient hydration, gelatinization with continuous fluffing, and active retrogradation cooling.

[0011] Torque rheometry provides real-time viscosity estimation, enabling automatic clump detection and corrective agitation.

---

## BRIEF DESCRIPTION OF THE DRAWINGS

[0012] FIG. 1 is a cross-sectional view of the apparatus showing the resonant cavity, vessel, agitation assembly, circumferential manifold, and sensor positions.

[0013] FIG. 2 is a detail view of the circumferential liquid distribution manifold showing plan view and nozzle angle configuration.

[0014] FIG. 3 shows the vertical reciprocating agitation assembly including the drive mechanism and operating modes.

[0015] FIG. 4 is a process control algorithm flowchart showing the four-phase cooking cycle with sensor checkpoints.

[0016] FIG. 5 is a closed-loop sensor control system block diagram showing feedback control with torque, temperature, and humidity sensing.

---

## DETAILED DESCRIPTION OF THE INVENTION

### System Architecture

[0017] Referring to FIG. 1, the apparatus comprises a resonant cavity (100) configured for 2.45 GHz microwave frequency, with a magnetron (10) coupling electromagnetic energy into the cavity via a waveguide (12).

[0018] A cooking vessel (20) is disposed within the cavity, the vessel being a removable container of borosilicate glass or high-temperature polymer having a slightly conical bottom to center granules under gravity.

[0019] A circumferential liquid distribution manifold (30) is positioned at the superior rim of the vessel, fed by a peristaltic pump capable of volumetric precision of plus or minus one milliliter.

[0020] A plurality of nozzles are oriented at fifteen to thirty degrees relative to the vertical vessel wall, directing fluid streams onto the wall rather than directly onto the food mass, thereby creating a laminar falling film that hydrates the periphery.

[0021] An agitation assembly (40) comprises a drive unit positioned outside the cavity, coupled to a shaft (42) extending through a wave choke into the cavity.

[0022] The assembly provides two degrees of freedom: Z-axis reciprocation (50) via a linear actuator driving the tool head vertically at frequencies from 0.5 to 10 Hz, and theta-axis indexing (52) via a stepper motor providing rotational positioning at zero to thirty RPM.

[0023] A tool head (44) is interchangeable and may comprise a fork array with multiple vertical tines for granular foods, a pestle for impact processing, or a whisk for liquid batters.

[0024] An IR matrix sensor (60) monitors surface temperature distribution, a torque sensor (62) measures motor current or shaft strain as a proxy for food viscosity, and a humidity sensor (64) monitors steam evolution rate.

[0025] A thermal regulation element (70) comprising a Peltier thermoelectric element or forced-air system provides active cooling during retrogradation.

### Circumferential Manifold Operation

[0026] Referring to FIG. 2, the manifold (30) creates a radial hydration gradient that counteracts the microwave tendency to overheat the food center.

[0027] By injecting water at the perimeter, the system pre-heats the water as it traverses the microwave-irradiated vessel wall, hydrates the driest peripheral regions first, and establishes centripetal moisture wicking toward the hotter center.

### Vertical Reciprocating Agitation

[0028] Referring to FIG. 3, the agitation assembly operates in three modes.

[0029] Mode A provides tumble and coat operation with slow rotation at five to ten RPM and minimal vertical stroke, used during lipid intercalation.

[0030] Mode B provides de-agglomeration with high-frequency vertical reciprocation at three to five Hz with stationary or slowly indexing rotation, creating vertical channels for steam venting and mechanically breaking nascent clumps.

[0031] Mode C provides lift and fluff operation with a compound motion wherein the tines descend, rotate ten to fifteen degrees to engage the lower layer, then retract vertically, lifting bottom material to the surface.

### Closed-Loop Sensor Control

[0032] Referring to FIG. 5, the control unit implements a multi-input feedback loop using torque rheometry as the primary feedback mechanism.

[0033] The agitator motor current correlates with food viscosity, with the system recognizing three phases: low torque when granules flow freely, rising torque as amylose leaks and surface viscosity increases, and stabilized or dropping torque as granules separate.

[0034] A sudden torque spike indicates localized clumping, triggering the controller to increase Z-axis frequency, target additional water injection, and reduce microwave power.

[0035] The IR matrix identifies hot spots, and if localized temperatures exceed a threshold, the controller pauses microwave emission, engages Mode C agitation, and injects water for evaporative cooling.

### Couscous Preparation Algorithm

[0036] Phase 1 comprises lipid intercalation wherein dry semolina is combined with oil at a ratio of approximately one to fifteen to one to twenty-five by volume to weight, the agitator operates in Mode A, and the microwave pulses at ten percent duty cycle to warm the oil and initiate amylose-lipid complex formation.

[0037] Phase 2 comprises gradient hydration wherein the manifold injects water or broth in pulses at a ratio of approximately one to one to one point five to one by volume to weight, the microwave operates at fifty percent power, and the agitator operates in Mode B at two to three Hz.

[0038] Phase 3 comprises gelatinization wherein the microwave power is modulated to maintain ninety-five to ninety-eight degrees Celsius, the agitator operates in Mode C to circulate layers, and the phase ends when steam rate drops below threshold, torque stabilizes, and IR shows uniform surface temperature.

[0039] Phase 4 comprises active retrogradation cooling wherein the microwave is off, cooling is activated, and the agitator operates at maximum Z-frequency of four to five Hz to reduce temperature from ninety-eight degrees to forty-five degrees Celsius within five minutes while preventing inter-granular bonding.

### Alternative Embodiments

[0040] An industrial continuous tunnel embodiment replaces the batch vessel with a microwave-transparent conveyor belt passing through a tunnel resonant cavity, with transverse gantries carrying reciprocating rake arrays.

[0041] A biryani mode limits the agitator Z-stroke to the upper portion of the vessel, allowing fluffing of a rice layer without disturbing a meat or sauce layer below.

[0042] A mochi mode replaces the fork tool head with a solid pestle, with the linear actuator operating in high-force impact mode.

---

## CLAIMS

1. (Original) An automated food processing apparatus comprising: a resonant cavity configured to contain electromagnetic radiation from a microwave energy source; a vessel disposed within said cavity for receiving a granular food product, said vessel being substantially transparent to microwave radiation; a fluid distribution system comprising a manifold disposed circumferentially about an upper perimeter of said vessel, said manifold comprising a plurality of nozzles oriented to direct fluid onto an interior wall surface of said vessel; an agitation assembly comprising a drive shaft extending into said cavity and a tool head coupled to said drive shaft, wherein said agitation assembly is configured to execute a vertical reciprocating motion along a longitudinal axis of said drive shaft; and a control unit operatively coupled to said microwave energy source, said fluid distribution system, and said agitation assembly.

2. (Original) An automated food processing apparatus comprising: a resonant cavity and microwave energy source; a vessel for receiving food product; an agitation assembly configured to mechanically agitate the food product; at least one sensor selected from the group consisting of a torque sensor operatively coupled to said agitation assembly and an infrared temperature sensor array positioned to monitor the food product surface; and a control unit configured to adjust at least one of microwave power, agitation frequency, or fluid injection rate in response to signals from said at least one sensor.

3. (Original) A method for automated preparation of granular starch-based food products, comprising the steps of: coating dry starch granules with a lipid agent while applying pulsed electromagnetic energy to initiate formation of amylose-lipid complexes; dispensing a liquid onto a peripheral region of a granule mass to establish a centripetal moisture gradient while applying electromagnetic heating; mechanically agitating the granules via a vertical reciprocating action that creates interstitial voids within the granule mass; monitoring at least one of temperature distribution, agitator resistance, or steam evolution rate; and cooling the granules while maintaining said vertical reciprocating agitation to induce intra-granular starch retrogradation.

4. (Original) The apparatus of claim 1, further comprising a torque sensor operatively coupled to said agitation assembly, wherein said control unit is configured to detect a torque anomaly indicative of food agglomeration and to increase the frequency of said vertical reciprocating motion in response thereto.

5. (Original) The apparatus of claim 1, further comprising an infrared sensor array positioned to monitor temperature distribution across the surface of the food product, wherein said control unit is configured to modulate microwave power in response to detection of a localized temperature excursion.

6. (Original) The apparatus of claim 1, further comprising a thermal regulation subsystem comprising at least one of a thermoelectric cooling element or a forced-air convection system, wherein said control unit is configured to activate said thermal regulation subsystem subsequent to a gelatinization phase.

7. (Original) The apparatus of claim 1, wherein said tool head comprises a plurality of tines extending substantially parallel to said longitudinal axis and configured to penetrate the granular food product during said vertical reciprocating motion.

8. (Original) The apparatus of claim 1, wherein said tool head is interchangeable and selected from the group consisting of a fork array for granular products, a pestle for impact processing, and a whisk for liquid batters.

9. (Original) The method of claim 3, wherein the step of dispensing liquid comprises dispensing liquid in discrete pulses synchronized with periods of reduced electromagnetic power.

10. (Original) The method of claim 3, wherein the step of monitoring comprises measuring motor current or shaft torque as a proxy for food viscosity, and wherein a sudden increase in measured torque triggers an increase in agitation frequency.

11. (Original) The method of claim 3, wherein the electromagnetic energy is microwave radiation at substantially 2.45 GHz and wherein said vertical reciprocating action operates at a frequency between 0.5 Hz and 10 Hz.

12. (Original) The method of claim 3, wherein the food product is couscous and wherein the method further comprises cooling the product from approximately 98 degrees Celsius to approximately 45 degrees Celsius within five minutes while agitating.

13. (Original) The apparatus of claim 2, wherein said control unit implements a state machine having at least four states corresponding to lipid coating, hydration, gelatinization, and cooling, and wherein transitions between states are triggered by sensor-derived conditions.

14. (Original) The apparatus of claim 1, wherein said plurality of nozzles are oriented at an angle between fifteen and thirty degrees relative to a vertical axis of said vessel wall.

15. (Original) A method for closed-loop control of a food cooking process, comprising: measuring resistance of a mechanical agitator operating within a food mass as a proxy for viscosity; detecting a resistance anomaly indicative of localized agglomeration; increasing agitation frequency in response to said anomaly to break the agglomeration; and resuming normal agitation when measured resistance returns to an expected range.

---

## ABSTRACT

An automated apparatus and method for preparing granular starch-based foods such as couscous. The system combines microwave heating, circumferential fluid injection creating a radial hydration gradient, and vertical reciprocating agitation that separates granules without shear damage. A closed-loop control system uses torque rheometry and infrared temperature sensing to detect food state and adjust processing parameters in real time. The method comprises four phases: lipid intercalation, gradient hydration, gelatinization with de-agglomeration, and active retrogradation cooling. The apparatus produces artisan-quality couscous without manual intervention.

---

*End of Specification*
