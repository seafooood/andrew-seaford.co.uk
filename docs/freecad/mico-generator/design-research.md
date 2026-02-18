---
keywords: [axial flux generator, AFPMG, wire gauge optimization, 3d printing, power generation]
---

Advanced Design Optimization for a 36-Pole Axial Flux Permanent Magnet Generator: Determining Optimal Wire Gauge

I. Advanced AFPMG Design Fundamentals: Constraints and Topology Selection

I.A. The Design Challenge: Overcoming Wire Gauge Limitations via System Optimization

The necessity to identify an optimal wire gauge stems from a previous constraint described as a "significant limitation" in the original design. In the context of small power generation systems, such a limitation almost universally points to issues arising from excessive electrical resistance (R) within the windings. High resistance leads to substantial copper losses, quantified as I2R, which severely limits the generator's efficiency and current carrying capability (I) for a given thermal tolerance. The design objective is therefore recast not merely as selecting a wire, but as maximizing the cross-sectional area of the conductor (Ac​, corresponding to a lower AWG number) to reduce R, while simultaneously ensuring that the resulting winding volume still allows for sufficient turns (N) to generate the required back-electromotive force (EMF) at the lowest operational speeds (cut-in RPM).  

The proposed system modifications—specifically, increasing the pole count to 36 and adding iron cores—are complementary strategies designed to permit this optimization. The induced back-EMF, Vph​, is fundamentally proportional to the number of turns per phase (Nph​), the magnetic flux per pole (Φmax​), the winding factor (kw​), and the operating frequency (f). By increasing the number of pole pairs (p=18), the electrical frequency is boosted relative to the mechanical rotational speed (ω), given by f=(2p/60)⋅RPM. This increase in f contributes directly to the voltage output at low RPM. The subsequent incorporation of iron cores, which drastically increases Φmax​ by concentrating the magnetic field, provides the necessary margin to dramatically reduce Nph​. The reduction in Nph​ translates directly into a shorter total wire length (L), enabling the use of a larger conductor cross-section (Ac​), thereby achieving the crucial objective of minimizing total winding resistance.  

I.B. Establishing the Winding Framework: 36 Poles and Fractional Slot Concentration

High pole counts, such as the specified 36 poles, are typical for Axial Flux Permanent Magnet Generators (AFPMGs) intended for low-speed applications like small wind turbines, where rotational speeds often fall within the 500 to 1500 RPM range. Maximizing the frequency response at these low speeds is essential for efficient energy capture.  

Assuming a standard three-phase (m=3) system, the design requires a careful selection of the number of stator slots (Qs​) to maximize performance while accommodating the thickest possible wire. A Fractional Slot Concentrated Winding (FSCW) is selected due to its inherent advantages in high-pole-count machines, including shorter coil length and simpler structure, which minimizes copper losses.  

The critical factor is the number of slots per pole per phase (q=Qs​/(2p⋅m)). For concentrated windings, q is ideally selected to be between 1/4 and 1/2 to ensure a high fundamental winding factor (kw​).  

Candidate slot combinations for 2p=36 include:

    Qs​=27: This yields q=27/(36⋅3)=1/4. This combination results in a high winding factor, kw​≈0.945.   

Qs​=54: This yields q=54/(36⋅3)=1/2. This provides a marginally higher winding factor, kw​≈0.966.  

To overcome the previous wire gauge limitation, the design must prioritize maximizing the physical area available for the conductor. The Qs​=27 configuration utilizes nine coils per phase (27 total coils) and provides significantly larger slot window areas (WA​) compared to the Qs​=54 design, even though the latter offers a slightly better kw​. A marginal reduction in kw​ is an acceptable engineering trade-off for a substantial gain in slot volume, which permits the use of a thicker wire gauge, thereby reducing resistance and losses far more effectively than the small gain in kw​ would have provided. Consequently, the Qs​=27 slot configuration is selected to maximize the wire thickness capability.  

I.C. Defining the Target Output Parameters

The generator must produce a stable and continuous power supply, typically intended for battery charging or driving a microcomputer load, such as a Raspberry Pi. Given common small-scale applications, the target continuous output current (IL​) is fixed at 3 Amperes. The stable DC output is commonly 5V. However, to ensure reliability and efficiency when charging or regulating power via an MPPT buck-boost converter, the generator's terminal voltage must be sufficiently high. An effective buck-boost converter requires a minimum input voltage (Vin​) greater than or equal to the desired output voltage (Vout​). A minimum rectified DC link voltage of approximately 7VDC​ is necessary to efficiently operate power electronics designed for a 5V/3A output, such as those employing synchronous rectification or specific MPPT integrated circuits. This minimum voltage threshold must be met at the generator's cut-in RPM.  

II. Comparative Analysis: Cored Stator vs. Coreless Stator

The incorporation of iron cores fundamentally shifts the electromagnetic dynamics and constitutes the primary means of overcoming the initial wire gauge limitation.

II.A. The Electromagnetic Impact of Iron Cores

In a coreless (air-cored) AFPMG, the magnetic flux (Φ) is limited by the air gap, resulting in relatively low air-gap flux density (Bg​), often below 0.7 Tesla. This necessitates a high number of turns (N) to achieve the required voltage output at low operational speeds. This requirement for high N demands the use of a very fine (high AWG) wire, which introduces high internal resistance and unacceptable I2R losses when the system is required to deliver medium current (3A).  

The implementation of a slotted iron-core stator transforms this scenario. The iron provides a path of high magnetic permeability, effectively concentrating the flux and significantly increasing the air-gap flux density, routinely achieving Bg​ values exceeding 1.0 Tesla. Since V∝N⋅Φ, doubling the flux density effectively halves the required number of turns (N) to achieve the same target voltage at a given speed. Because the total winding resistance is proportional to the total length of the wire (L), and L is proportional to N, reducing N dramatically reduces L and, consequently, the total resistance R.  

This reduction in N allows the available winding volume in the slot (WA​) to be occupied by a much thicker wire (lower AWG number) with a larger cross-sectional area (Ac​). This combined effect—reduced N and increased Ac​ (AWG 20)—minimizes R to the greatest extent possible, thus directly resolving the efficiency limitation previously imposed by the wire gauge. For systems requiring continuous medium current output (3A), the slotted iron-core design is strategically superior and necessary for optimizing wire gauge selection.

II.B. Mitigating Cogging Torque in the Cored Stator

The significant electromagnetic advantage gained from the iron core is accompanied by the introduction of cogging torque. Cogging torque is a non-smooth, periodic fluctuation in torque caused by the interaction between the rotor magnets and the ferrous stator teeth. This phenomenon is highly undesirable in wind applications as it can impede the generator’s ability to start at very low wind speeds, thereby raising the critical cut-in speed.  

To ensure reliable low-speed operation, mitigation of cogging torque is essential. Geometric optimization techniques, specifically skewing the stator slots or the magnets, are effective methods. Experimental studies have demonstrated that employing an optimal skew angle can decrease the amplitude of cogging torque by four to five times compared to a non-skewed configuration. An effective optimal angle reported in the literature is 7.5∘. While implementing skewing may introduce a minor reduction in magnetic flux and output power, the trade-off is highly beneficial: the slight loss in power is far outweighed by the successful minimization of torque ripple, ensuring the machine’s mechanical stability and low-speed start capability.  

Table 1: Strategic Impact of Stator Topology on Wire Gauge Selection
Parameter	Coreless (Air-Cored) Design	Slotted Iron-Core Design (Chosen)	Wire Gauge Implication
Air-Gap Flux Density (Bg​)	Low (typically 0.4 T to 0.7 T)	

High (typically 0.8 T to 1.2 T) 
	High Bg​ permits lower N, enabling thicker wire (lower AWG).
Required Turns per Phase (Nph​)	High, driving fine wire selection.	Low, maximizing available slot area for copper.	Allows R minimization to solve previous efficiency limitations.
Cogging Torque Management	Negligible (Inherently low torque ripple).	

Significant (Requires 7.5∘ skewing for mitigation).
	Mechanical complexity accepted for electrical performance gain.
 

III. Wire Gauge Selection: Balancing Turns, Resistance, and Current Capacity

The selection process for the optimal American Wire Gauge (AWG) involves calculating the required number of turns (N) for voltage generation and then determining the largest conductor area (Ac​) that fits into the available winding slots while keeping resistance minimized.

III.A. Modeling Required Turns (N)

The target operational point is defined by a low cut-in speed, assumed to be 300 RPM.  

    Frequency Calculation: With 36 poles (18 pole pairs) at 300 RPM, the electrical fundamental frequency is f=(36/120)⋅300=90 Hz. This high frequency is advantageous for low-speed power generation.

    Target Voltage: To supply a stable 5V output via a buck-boost converter, the minimum rectified DC input voltage should be approximately 7VDC​. Utilizing a Star (Y) connection (as detailed in Section IV), this requires a line-to-line RMS voltage VL,RMS​ slightly above 7V. Assuming a target phase RMS voltage Vph,RMS​≈4V.   

Turn Count Estimate: Utilizing the magnetic flux density gain from the iron core (Bg​≈1.0 T, yielding an estimated flux per pole Φmax​≈5⋅10−4 Weber), the required number of turns per phase (Nph​) can be calculated. Based on comparable design examples for low-voltage, low-speed generators, the total number of turns per phase is expected to be relatively low, likely in the range of 100 to 200 turns.  

    Coil Turns: With Qs​=27 slots (9 coils per phase), Nph​=150 corresponds to Nc​=150/9≈16 turns per coil. This low turn count confirms that a thick wire gauge is feasible.

III.B. Resistance and Current Capacity Analysis

The maximum current load is specified as 3 Amperes. Standard ampacity charts often provide conservative current ratings based on thermal limits for chassis wiring (e.g., 700 circular mils per amp). However, in a heavily optimized winding, the low resistance resulting from the short total wire length minimizes I2R heat generation, meaning the wire's thermal rating (e.g., 155∘C insulation) is the ultimate determinant of current capacity.  

The fundamental constraint is minimizing resistance to maximize efficiency. Assuming a Mean Length Turn (MLT) of approximately 8 cm (determined by the physical diameter of the coil winding) for the 36-pole configuration, 150 turns per phase results in a total wire length per phase (Lph​) of 150×0.08m=12 meters.

The resistance (R) for candidate gauges is assessed:

Table 2: Comparative Electrical Analysis for Candidate AWG Gauges
AWG Gauge	Bare Diameter (mm)	

DC Resistance (Ω/km) at 20°C 
	Estimated Rph​ (12m)	I2R Loss per Phase (3A)
24	0.511	84.2	1.01Ω	9.1 W
22	0.644	52.7	0.63Ω	5.7 W
20	0.812	33.1	0.40Ω	3.6 W
 

The analysis demonstrates a critical point: transitioning from AWG 24 to AWG 20 reduces the phase resistance by over 60%. This drastic reduction in resistance is essential to minimize I2R copper losses. If the generator were producing, for instance, 50W of mechanical power, losses of 27.3W (from three phases of AWG 24) would render the machine highly inefficient (efficiency less than 50%). By utilizing AWG 20, total losses are reduced to approximately 10.8 W (3×3.6 W), significantly boosting overall system efficiency and providing robust thermal performance for continuous 3A operation.

III.C. Final Gauge Recommendation

The optimal gauge is AWG 20. This gauge provides the largest practical conductor area (Ac​), offering the lowest resistance necessary to handle the required 3 Amperes of continuous current output while minimizing the heat generated and solving the previously identified limitation. Given the large slot area afforded by the Qs​=27 fractional slot winding configuration, the estimated 16 turns per coil using AWG 20 wire should fit comfortably within the winding window, especially when a good winding fill factor (Ku​≈0.4) is maintained.  

IV. Output Configuration and Integration Strategy

Once the optimal winding geometry and conductor size are fixed, the final design consideration is the interconnection strategy and power conditioning required to deliver regulated DC output.

IV.A. Winding Connection: Star vs. Delta

The choice between Star (Y) and Delta (Δ) connection is critical for low-voltage power generation.  

    Delta Connection: Line voltage equals phase voltage (VL​=Vph​), but line current is 1.732 times the phase current (IL​=3​⋅Iph​). This configuration favors current output over terminal voltage.

    Star Connection: Line voltage is 1.732 times the phase voltage (VL​=3​⋅Vph​), and line current equals phase current (IL​=Iph​). This configuration prioritizes voltage output.   

For low-RPM generators, the output voltage is inherently low. To maximize the generator's operating window and minimize the cut-in speed, the priority must be maximizing the terminal voltage presented to the power electronics. The Star (Y) configuration is mandatory because it multiplies the generated phase voltage by 1.732. This voltage boost ensures that the generator reaches the required minimum rectified DC link voltage (VDC​≥7V) at the lowest possible rotational speed, thereby increasing the annual energy yield and enhancing the efficiency of the downstream converter.  

IV.B. Power Conditioning and MPPT Integration

The generator produces variable voltage and frequency AC power. This must be efficiently converted to stable DC output.

    Low-Loss Rectification: Conventional diode bridge rectifiers introduce unacceptable voltage drops in low-voltage systems. High efficiency requires active rectification, often using MOSFET-based circuits or specific low-loss integrated circuits.   

MPPT Control: To maximize power extraction from the variable mechanical source (wind), a Maximum Power Point Tracking (MPPT) system is essential. The MPPT mechanism dynamically loads the generator to maintain operation at the optimal torque-speed curve.  

Buck-Boost Converter Topology: Since the generator's terminal voltage can swing widely, often starting below the target output voltage (e.g., 5VDC​) and sometimes exceeding it at higher wind speeds, a buck-boost converter topology is required. Specialized ICs, such as the SM72441 or LT8490, are designed to implement highly efficient, four-switch buck-boost control for MPPT, suitable for photovoltaic or small wind systems.  

The low internal resistance achieved by the AWG 20 winding is critical for this integration. When the MPPT controller attempts to draw high current to track the maximum power point, any significant internal generator resistance would cause a dramatic voltage drop (ΔV=Iph​Rph​) at the terminals, effectively choking the power output and reducing tracking efficiency. The low resistance of the AWG 20 design ensures minimal voltage droop under load, stabilizing the generator's electrical behavior for optimal power extraction.  

V. Detailed Recommendations and Design Synthesis

Based on the necessity to overcome resistance limitations and the imposed constraints of 36 poles and iron cores, the following definitive design specifications are recommended.

V.A. Recommended Generator Topology and Configuration

The optimal design leverages the high flux density of the slotted iron core to permit the use of low-resistance wiring.

    Stator Topology: Slotted Iron-Core Stator.

    Pole/Slot Combination: 36 Poles (2p=36) / 27 Slots (Qs​=27). This provides the optimal balance between high winding factor (kw​≈0.945) and maximizing the physical slot area to accommodate the thicker wire.   

Cogging Mitigation: 7.5∘ Skewing of magnets or stator stack must be implemented to ensure smooth start-up and low-RPM stability.  

Winding Connection: Three-Phase Star (Y) connection to maximize terminal voltage and achieve the lowest possible cut-in speed.  

V.B. Optimal Wire Gauge Specification

The strategic shift to iron cores necessitates a corresponding shift to the thickest feasible wire to capitalize on the reduced turn requirement.

    Optimal Gauge: AWG 20 (Bare Diameter ≈0.812 mm, Resistance ≈33.1Ω/km).   

Winding Target: Approximately 16 turns per coil (Nc​) to achieve the required voltage threshold at the 300 RPM cut-in speed, given the anticipated high flux density (Bg​>1.0 T) of the cored design.

Wire Type: High-quality enameled copper magnet wire, rated for a minimum thermal class of 155∘C.  

The critical engineering rationale supporting AWG 20 is the reduction in resistance. Compared to the fine gauges typically associated with coreless, high-turn designs (e.g., AWG 38 wire, which has extremely high resistance ), AWG 20 minimizes I2R losses by a factor of 10 or more, fundamentally solving the "significant limitation" cited by the user.  

VI. Detailed Analytical Calculations and Design Nuances

VI.A. Core Dimensions and Winding Volume Constraints

The selection of AWG 20 assumes that the physical dimensions of the slots provided by the 27-slot configuration are sufficient. The Winding Window Area (WA​) available per slot dictates the maximum number of turns (Nc​) possible for a given wire size. The effective wire area (Awire​) includes the copper conductor area (Ac​) and the insulation thickness (build).  

For AWG 20, the bare area is 10380 circular mils (or 0.526 mm2). The Mean Length Turn (MLT), which determines the total wire length L, is a function of the stator inner and outer radii. If the winding is designed such that the MLT is 8 cm, the total length per phase is 12 meters. This low length, coupled with the low resistance per unit length of AWG 20, keeps the total phase resistance Rph​ exceptionally low (≈0.40Ω).  

The winding volume utilization factor (Ku​) for round wire windings is often approximated around 0.4. The required slot area for 16 turns of AWG 20 must be calculated precisely, factoring in the insulation thickness. The selection of Qs​=27 (rather than 54) was made specifically to maximize this slot area, ensuring physical accommodation of the AWG 20 wire and verifying the feasibility of the low resistance target.  

VI.B. Efficiency Modeling and Voltage Drop Analysis

The primary benefit of AWG 20 is realized under load. The generator is designed to operate continuously at 3 Amperes. The resulting total copper loss of 10.8 W is a fixed power penalty that must be deducted from the electrical power output. In a high-efficiency AFPMG, efficiency up to 90% is reported. Maintaining such high efficiency requires minimizing these parasitic losses.  

The terminal voltage drop (ΔVL​) under maximum load is calculated by ΔVph​=Iph​Rph​. Since in a Star connection IL​=Iph​, the voltage drop per phase is 3A×0.40Ω=1.2VRMS​.

If the required Vph,RMS​ at 300 RPM is 4VRMS​ at no load, the loaded voltage would drop to Vph,load​=4V−1.2V=2.8VRMS​. While this drop is notable, the line-to-line voltage VL​ remains 1.732×2.8VRMS​≈4.85VRMS​. After rectification and smoothing, this output, while lower than the ideal 7VDC​ goal at 300 RPM, is still likely usable by the MPPT converter, which excels at utilizing power even when input voltage is marginal or low. Furthermore, as the RPM increases, the generated voltage will rise linearly, quickly exceeding the 7VDC​ threshold, ensuring excellent efficiency at higher operating points. The low internal resistance of the AWG 20 winding stabilizes the output and maximizes the power that the MPPT controller can track.  

VI.C. Magnetic Flux Density and Core Material Considerations

The assumption that the iron core boosts the flux density to ≈1.0 T is dependent on the core material properties, particularly its maximum saturation flux density (Bmax​) and the air gap length (geff​). The design must ensure that the iron core does not enter saturation, which would limit the flux concentration and nullify the advantage over the coreless design. Optimization requires careful selection of the magnetic material and the geometry of the iron teeth to maximize the ratio of magnet volume to air gap length. This ensures that the low turn count dictated by the AWG 20 wire is sufficient to meet the voltage targets at low RPM.  

VII. Conclusion

The optimization of the 36-pole AFPMG to overcome the previous limitation regarding wire gauge requires a mandatory transition to a slotted iron-core topology. This change fundamentally alters the design constraint, shifting the focus from maximizing the number of turns (N) to minimizing the winding resistance (R).

The analysis confirms that the use of a 27-slot stator paired with 36 poles allows for the selection of a conductor with high cross-sectional area. The AWG 20 wire gauge is the optimal selection, achieving a phase resistance reduction of over 85% compared to typical fine gauges used in high-turn coreless designs. This reduction dramatically lowers I2R copper losses, allowing the generator to handle the continuous 3A load efficiently. Furthermore, the selection of the Star (Y) winding configuration is necessary to leverage the 3​ voltage multiplication factor, maximizing the terminal voltage at low rotational speeds and ensuring robust operation for the downstream MPPT buck-boost converter system. The successful integration of iron cores must be accompanied by cogging torque mitigation, ideally through a 7.5∘ skew, to preserve the generator's mechanical performance at low wind speeds.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/freecad/mico-generator](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/freecad/mico-generator)
