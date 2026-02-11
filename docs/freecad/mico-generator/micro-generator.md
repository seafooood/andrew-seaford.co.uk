The optimization of the generator design based on your specified components (AWG 20 wire, 36 magnets, and 22 mm bearings) mandates a fundamental shift to a slotted iron-core topology. This change is necessary to reduce winding resistance, allowing the generator to handle the high 3 Ampere current required for the Raspberry Pi system.

Here is a summary of the design requirements and critical dimensions for the two 3D-printed disks.

## Summary of Two-Disk Design Requirements

The system must be engineered as a three-phase, slotted Axial Flux Permanent Magnet Generator (AFPMG) using a Star (Y) winding configuration to maximize voltage at low rotational speeds.[1]

| Component | Function | Key Constraint / Dimension | Source |
|---|---|---|---|
| **Poles** | Number of magnets | 36 poles (18 pole pairs) | Constraint |
| **Slots** | Number of stator teeth/coils | 27 slots (9 coils per phase) | Optimized for AWG 20 winding volume [2] |
| **Magnet Dimensions** | Individual magnet size | `7.1 mm (L) x 2.7 mm (W) x 2 mm (H)` | Constraint |
| **Wire Gauge** | Copper conductor | AWG 20 (Bare Diameter: ≈ 0.812 mm) | Constraint |
| **Air Gap** | Spacing between rotor magnets and stator cores | ≤ 1.5 mm | Critical for maximizing voltage output [2] |
| **Cogging Mitigation**| Required skew angle to ensure low-speed start-up | `$\mathbf{7.5^\circ}$` skew (applied to magnets or stator teeth) | Recommended mitigation [3] |

***

## Disk 1: Rotor (Magnet Disk) Design Specifications

The rotor disk's primary function is to secure the magnets in a precise, alternating magnetic polarity pattern and provide a rigid connection to the turbine shaft via the bearings.

| Parameter | Required Specification | Design Details and Rationale |
|---|---|---|
| **Magnet Count** | 36 pieces | All magnets must be arranged in a continuous ring, with alternating North-South-North-South polarity to maximize flux linkage.[2] |
| **Magnet Pockets** | `7.1 x 2.7 x 2 mm` (plus tolerance) | The disk must be printed with recessed pockets to hold each magnet securely, preventing detachment under centrifugal force. |
| **Skewing** | `$\mathbf{7.5^\circ}$` (recommended) | To reduce cogging torque, the 36 magnets should be installed with a $7.5^\circ$ circumferential offset (skew) relative to the axis of rotation.[3] |
| **Bearing Integration** | Central housing for 22 mm bearings | The disk requires a central hub designed to press-fit the 22 mm bearings, ensuring high radial and axial alignment (minimal wobble).[4] |
| **Material** | High rigidity, moderate thermal resistance | Material such as PETG or ABS is preferred over PLA to maintain dimensional stability, especially the critical air gap.[4] |

***

## Disk 2: Stator (Winding Disk) Design Specifications

The stator disk must be designed to accommodate the iron cores and provide the mandatory structure for the concentrated three-phase windings.

| Parameter | Required Specification | Design Details and Rationale |
|---|---|---|
| **Stator Topology** | Slotted Iron-Core Stator | The disk must contain slots/pockets for 27 laminated iron cores or teeth, which significantly increase the magnetic flux density ($B_g$), enabling the use of the low-resistance AWG 20 wire.[2] |
| **Slot/Tooth Count** | 27 slots | This configuration is optimal for a 36-pole, 3-phase system, offering a high winding factor and maximizing the winding space.[2] |
| **Coil Posts** | 27 posts (9 per phase) | The disk requires 27 posts (or teeth of the iron core) upon which the copper wire is wound in a non-overlapping, "snake-like" concentrated pattern.[5, 6] |
| **Winding Requirement** | $\approx 16$ turns per coil | The posts must provide sufficient winding window area ($W_A$) to accommodate $\mathbf{16}$ continuous turns of AWG 20 insulated magnet wire. This count is estimated to provide the necessary low-RPM voltage output.[7, 8] |
| **Winding Dimensions** | Minimized Mean Length Turn (MLT) | The inner (D_i) and outer (D_o) diameters of the coil posts must be designed to minimize the MLT (the average length of one loop of wire). Minimizing MLT is essential as it directly reduces the total wire length, keeping the crucial total phase resistance (R_ph) low (Target R_ph ≈ 0.40 Ω).[9, 10] |
| **Output Connection** | Three AC wire terminations | The 27 coils must be internally wired into three separate electrical phases, and the three ends connected in a Star (Y) configuration before exiting the housing.[1] |

**Note on Final Dimensions:** The precise radial dimensions (Inner and Outer Diameters, $D_i$ and $D_o$) of the coil posts are interdependent on the magnet placement and the 27-slot geometry. These dimensions must be iteratively calculated to ensure the coil winding area aligns optimally with the passing magnet faces while keeping the MLT minimized.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/freecad/mico-generator](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/freecad/mico-generator)
