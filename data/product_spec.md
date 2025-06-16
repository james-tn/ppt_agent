# Production Specification Document    
**Project:** Rebound CAD    
**Title:** FRAME BOM    
**Drawing Number:** (refer to original BOM)    
**Revision:** 0    
**Date:** 24 FEB 2017    
**Drawn by:** JMGN    
**Scale:** 1:40    
**Sheet:** 1/1    
  
---  
  
## 1. Overview  
  
This specification outlines the requirements for the fabrication and assembly of the frame structure shown in the Rebound CAD Frame BOM. The frame consists of multiple steel and stainless steel components, each detailed in the Parts List. All fabrication, welding, and assembly must conform to the specifications below.  
  
---  
  
## 2. Materials  
  
- **Steel:** All components specified as 'STEEL' should use structural grade mild steel (minimum yield strength: 250 MPa), except where otherwise stated.  
- **Stainless Steel:** The `BAR_SM_BRACKET` (Item 21) must be fabricated from stainless steel (grade SS304 or equivalent).  
  
---  
  
## 3. Component List  
  
| Item | Part Number                | Description                | Length / Size | Qty | Material        |  
|------|----------------------------|----------------------------|---------------|-----|----------------|  
| 1    | ICE_H_BEAM                 | 2387 mm beam               | 2387 mm       | 2   | Steel          |  
| 2    | ICE_UPRIGHT                | 1940 mm upright            | 1940 mm       | 4   | Steel          |  
| 3    | MOTOR_H_SUPPORT            | 230 mm support             | 230 mm        | 2   | Steel          |  
| 4    | HALF_END                   | 1224 mm end                | 1224 mm       | 2   | Steel          |  
| 5    | TANK_SIDE_BRACE            | 2095 mm brace              | 2095 mm       | 7   | Steel          |  
| ...  | ...                        | ...                        | ...           | ... | ...            |  
| 21   | BAR_SM_BRACKET             | 51 mm bracket              | 51 mm         | 4   | Stainless Steel|  
| ...  | ...                        | ...                        | ...           | ... | ...            |  
  
*Refer to the full BOM for the complete listing.*  
  
---  
  
## 4. Fabrication Instructions  
  
- All **cutting, drilling, and forming** must use processes compatible with the specified materials.  
- **All welds** should be continuous, unless otherwise specified, and executed per AWS D1.1 (or equivalent local standard).  
- **Sharp edges and burrs** should be removed from all parts.  
- **Galvanization or corrosion protection** is required for all steel components, except stainless steel parts, unless surfaces are designated as machined/mating joints.  
  - Preferred method: powder-coating after fabrication, color and gloss to be determined by the project engineer.  
  
---  
  
## 5. Assembly Instructions  
  
- **Reference Drawing:** Use isometric and callout numbers to coordinate parts in assembly.  
- Fastenings not specified in the BOM are to be selected by the fabricator to match the identified loads and material thickness.  
- During assembly, ensure all vertical and horizontal members are square and plumb to within 1.5mm per meter.  
- Subassemblies (e.g., "TANK_SIDE_BRACE" with adjacent "EXT_UPRIGHT" or "COLUMN_UPRIGHT") must be test-fitted prior to final welding.  
- Stainless steel brackets (Item 21) must be isolated from mild steel with appropriate washers or gaskets to avoid galvanic corrosion.  
  
---  
  
## 6. Quality Requirements  
  
- **Dimensional tolerances:** ±2mm for all lengths unless otherwise specified.  
- **Weld inspection:** Visual inspection for continuity, penetration, and absence of cracks/defects.  
- **Protection:** All parts must be free of rust,