# Changes in the columns the earlier July->October report never compared

The earlier report (docs/repd/2026q3/changes-jul-to-oct, previous = derived project_identity_v6.json) compared 19 columns; 33 official columns were not compared. Counts below are retained refs (14,648) whose value changed, from clean.py output July vs clean.py output October, classified by scripts/indep_diff.py.

| Column | Real change | of which filled (blank->value) | blanked (value->blank) | Formatting only (whitespace/spacing/separator/numeric form) |
|---|---|---|---|---|
| Storage Type | 2 | 0 | 0 | 0 |
| Storage Co-location REPD Ref ID | 6 | 5 | 0 | 0 |
| Share Community Scheme | 0 | 0 | 0 | 0 |
| CHP Enabled | 0 | 0 | 0 | 0 |
| CfD Allocation Round | 0 | 0 | 0 | 0 |
| RO Banding (ROC/MWh) | 0 | 0 | 0 | 0 |
| FiT Tariff (p/kWh) | 0 | 0 | 0 | 0 |
| CfD Capacity (MW) | 0 | 0 | 0 | 0 |
| Turbine Capacity (MW) | 7 | 1 | 2 | 0 |
| No. of Turbines | 4 | 0 | 2 | 0 |
| Height of Turbines (m) | 6 | 0 | 3 | 0 |
| Mounting Type for Solar | 19 | 0 | 18 | 0 |
| Development Status | 373 | 0 | 0 | 0 |
| Are they re-applying (New REPD Ref) | 10 | 10 | 0 | 0 |
| Are they re-applying (Old REPD Ref) | 0 | 0 | 0 | 0 |
| Address | 0 | 0 | 0 | 2555 |
| Post Code | 3 | 0 | 0 | 0 |
| X-coordinate | 27 | 0 | 0 | 0 |
| Y-coordinate | 28 | 0 | 0 | 0 |
| Appeal Reference | 5 | 5 | 0 | 0 |
| Secretary of State Reference | 0 | 0 | 0 | 0 |
| Type of Secretary of State Intervention | 0 | 0 | 0 | 0 |
| Judicial Review | 0 | 0 | 0 | 0 |
| Offshore Wind Round | 0 | 0 | 0 | 0 |
| Appeal Lodged | 5 | 5 | 0 | 0 |
| Appeal Withdrawn | 0 | 0 | 0 | 0 |
| Appeal Refused | 0 | 0 | 0 | 0 |
| Appeal Granted | 13 | 13 | 0 | 0 |
| Secretary of State - Intervened | 0 | 0 | 0 | 0 |
| Secretary of State - Refusal | 0 | 0 | 0 | 0 |
| Secretary of State - Granted | 0 | 0 | 0 | 0 |
| Heat Network Ref | 0 | 0 | 0 | 0 |
| Solar Site Area (sqm) | 19 | 2 | 1 | 3474 |


## Coordinates (aggregate)
28 retained records changed X and/or Y: under 100 m 1; 100 m to 1 km 4; 1 to 10 km 7; 10 to 100 km 2; over 100 km 14.
9 of the over-100 km moves are battery records whose X and Y were transposed in July and are corrected in October.
Secretary of State dates, reference and intervention type, Judicial Review, Appeal Withdrawn and Appeal Refused: 0 changes.
Address: 0 substantive changes (521 differ only by line-break/spacing removal).
