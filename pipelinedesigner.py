# PIPELINE DESIGNER PROFESSIONAL EDITION
# Created by: B.C. Prabhakar
# Freelance Oil and Gas Pipeline Engineering Consultant
# Email: prabhubc@gmail.com

print("="*80)
print("OIL & GAS PIPELINE DESIGN TRAINING TOOL")
print("For Young Engineers - Career Development")
print("="*80)
print("\nCreated by: B.C. Prabhakar")
print("Freelance Oil and Gas Pipeline Engineering Consultant")
print("Email: prabhubc@gmail.com")
print("\nPurpose: Train young engineers in pipeline design fundamentals")
print("Disclaimer: For educational purposes only")
print("="*80)

def calculate_flow_velocity():
    """Calculate flow velocity in pipeline"""
    print("\n" + "="*80)
    print("FLOW VELOCITY CALCULATOR")
    print("="*80)
    
    try:
        print("\nEnter pipeline parameters:")
        diameter = float(input("Pipe Diameter (mm, e.g., 200): "))
        flow_rate = float(input("Flow Rate (m³/hr, e.g., 100): "))
        
        # Calculations
        diameter_m = diameter / 1000  # Convert to meters
        radius = diameter_m / 2
        area = 3.1416 * radius * radius  # πr²
        flow_m3s = flow_rate / 3600  # Convert to m³/s
        velocity = flow_m3s / area
        
        print(f"\n" + "="*80)
        print("RESULTS:")
        print(f"Pipe Diameter: {diameter} mm")
        print(f"Flow Rate: {flow_rate} m³/hr")
        print(f"Cross-sectional Area: {area:.6f} m²")
        print(f"Flow Velocity: {velocity:.2f} m/s")
        
        # Professional recommendations
        print("\n" + "="*80)
        print("B.C. PRABHAKAR'S RECOMMENDATIONS:")
        if velocity < 1.0:
            print("• Velocity is LOW - Check pump capacity")
            print("• Consider smaller diameter pipe")
        elif velocity > 3.0:
            print("• Velocity is HIGH - Risk of erosion")
            print("• Consider larger diameter pipe")
        else:
            print("• Velocity is OPTIMAL (1-3 m/s range)")
        
        print("\nFor desert pipelines, add 10% margin for temperature effects.")
        print("Consult: prabhubc@gmail.com for project-specific advice")
        print("="*80)
        
        input("\nPress Enter to return to menu...")
        
    except ValueError:
        print("\nERROR: Please enter numbers only (e.g., 200, 100.5)")
        input("Press Enter to try again...")
        calculate_flow_velocity()

def pressure_drop_estimator():
    """Estimate pressure drop in pipeline"""
    print("\n" + "="*80)
    print("PRESSURE DROP ESTIMATOR")
    print("="*80)
    
    try:
        print("\nEnter pipeline parameters:")
        length = float(input("Pipeline Length (km, e.g., 25): "))
        diameter = float(input("Pipe Diameter (mm, e.g., 200): "))
        flow_rate = float(input("Flow Rate (m³/hr, e.g., 100): "))
        
        # Simplified pressure drop calculation
        # ΔP = (f * L * ρ * v²) / (2 * D) - simplified for training
        velocity = flow_rate / (diameter * diameter * 0.000000785)  # Simplified
        pressure_drop = (0.02 * length * 1000 * 850 * velocity * velocity) / (2 * (diameter/1000))
        pressure_drop_bar = pressure_drop / 100000
        
        print(f"\n" + "="*80)
        print("ESTIMATED RESULTS:")
        print(f"Pipeline Length: {length} km")
        print(f"Pipe Diameter: {diameter} mm")
        print(f"Flow Rate: {flow_rate} m³/hr")
        print(f"Estimated Pressure Drop: {pressure_drop_bar:.1f} bar")
        print(f"Pressure Drop per km: {pressure_drop_bar/length:.2f} bar/km")
        
        # Pump power estimation
        if pressure_drop_bar > 0:
            pump_power = (flow_rate/3600) * pressure_drop_bar * 100000 / 1000
            print(f"Estimated Pump Power: {pump_power:.1f} kW")
        
        print("\n" + "="*80)
        print("PROFESSIONAL NOTES:")
        print("• Add 15-20% margin for fittings and valves")
        print("• Desert temperatures affect fluid viscosity")
        print("• Consider booster stations for >10 bar pressure drop")
        print("\nFor accurate design calculations, contact:")
        print("B.C. Prabhakar - prabhubc@gmail.com")
        print("="*80)
        
        input("\nPress Enter to return to menu...")
        
    except ValueError:
        print("\nERROR: Please enter numbers only")
        input("Press Enter to try again...")
        pressure_drop_estimator()

def wall_thickness_calculator():
    """Calculate minimum wall thickness"""
    print("\n" + "="*80)
    print("WALL THICKNESS CALCULATOR (ASME B31.4 Basis)")
    print("="*80)
    
    try:
        print("\nBased on formula: t = (P × D) / (2 × S × F) + CA")
        print("t = Wall thickness (mm)")
        print("P = Design pressure (bar)")
        print("D = Pipe diameter (mm)")
        print("S = Material strength (MPa)")
        print("F = Design factor (0.72 for desert)")
        print("CA = Corrosion allowance (mm)")
        
        pressure = float(input("\nDesign Pressure (bar, e.g., 30): "))
        diameter = float(input("Pipe Diameter (mm, e.g., 200): "))
        
        # Convert pressure to MPa
        pressure_mpa = pressure * 0.1
        
        # Material properties
        print("\nMaterial Options:")
        print("1. API 5L Grade B (S = 290 MPa)")
        print("2. API 5L X42 (S = 290 MPa)")
        print("3. API 5L X52 (S = 360 MPa)")
        print("4. API 5L X65 (S = 450 MPa)")
        
        material_choice = input("\nSelect material (1-4, default 1): ").strip()
        if material_choice == '2':
            strength = 290
        elif material_choice == '3':
            strength = 360
        elif material_choice == '4':
            strength = 450
        else:
            strength = 290
        
        design_factor = 0.72
        corrosion = 1.5  # mm for desert
        
        # Calculate thickness
        thickness = (pressure_mpa * (diameter/1000)) / (2 * strength * design_factor)
        thickness_mm = thickness * 1000
        total_thickness = thickness_mm + corrosion
        
        # Manufacturing tolerance
        final_thickness = total_thickness * 1.125
        
        print(f"\n" + "="*80)
        print("CALCULATION RESULTS:")
        print(f"Design Pressure: {pressure} bar")
        print(f"Pipe Diameter: {diameter} mm")
        print(f"Material Strength: {strength} MPa")
        print(f"Calculated Thickness: {thickness_mm:.2f} mm")
        print(f"With Corrosion Allowance: {total_thickness:.2f} mm")
        print(f"With Manufacturing Tolerance: {final_thickness:.2f} mm")
        
        # Standard thickness selection
        standard_sizes = [3.2, 4.0, 4.5, 5.0, 5.6, 6.3, 7.1, 8.0, 9.0, 10.0]
        selected = min((t for t in standard_sizes if t >= final_thickness), default=10.0)
        
        print(f"\nSELECT Standard Size: {selected} mm")
        print(f"Schedule: {'Schedule 40' if selected <= 5.0 else 'Schedule 80' if selected <= 8.0 else 'Schedule 160'}")
        
        print("\n" + "="*80)
        print("B.C. PRABHAKAR'S DESERT RECOMMENDATIONS:")
        print("• Use minimum 1.5mm corrosion allowance for desert")
        print("• FBE coating mandatory for corrosion protection")
        print("• Consider higher grade material for sour service")
        print("• Always verify with ASME B31.4 latest edition")
        print("\nFor professional design review: prabhubc@gmail.com")
        print("="*80)
        
        input("\nPress Enter to return to menu...")
        
    except ValueError:
        print("\nERROR: Please enter valid numbers")
        input("Press Enter to try again...")
        wall_thickness_calculator()

def crossing_design_guide():
    """Guide for pipeline crossings"""
    print("\n" + "="*80)
    print("PIPELINE CROSSING DESIGN GUIDE")
    print("Based on B.C. Prabhakar's Field Experience")
    print("="*80)
    
    print("\nTypes of Crossings:")
    print("1. Road Crossings")
    print("2. Nalla (Dry River) Crossings")
    print("3. Railway Crossings")
    print("4. Canal Crossings")
    
    choice = input("\nSelect crossing type (1-4): ").strip()
    
    if choice == '1':
        print("\n" + "="*80)
        print("ROAD CROSSING REQUIREMENTS")
        print("="*80)
        print("\nMinimum Requirements:")
        print("• Burial Depth: 1.2 meters minimum")
        print("• Casing: Steel casing for heavy traffic roads")
        print("• Protection: Concrete sleeves for major highways")
        print("• Warning Tape: 300mm above pipeline")
        
        print("\nB.C. Prabhakar's Recommendations:")
        print("• Use HDPE casing for corrosion resistance")
        print("• Install cathodic protection test stations")
        print("• Consider future road widening")
        print("• Obtain proper permits from road authority")
        
    elif choice == '2':
        print("\n" + "="*80)
        print("NALLA CROSSING REQUIREMENTS")
        print("="*80)
        print("\nMinimum Requirements:")
        print("• Burial Depth: 1.5 meters minimum")
        print("• Scour Protection: Extra 0.5m depth in sandy nallas")
        print("• Weight Coating: Concrete coating for stability")
        print("• Alignment: Perpendicular crossing preferred")
        
        print("\nB.C. Prabhakar's Desert Experience:")
        print("• Flash floods in desert can cause severe scour")
        print("• Use riprap protection at entry/exit points")
        print("• Consider Horizontal Directional Drilling (HDD)")
        print("• Monitor after monsoon seasons")
        
    elif choice == '3':
        print("\n" + "="*80)
        print("RAILWAY CROSSING REQUIREMENTS")
        print("="*80)
        print("\nMinimum Requirements:")
        print("• Burial Depth: 1.8 meters minimum")
        print("• Casing: Steel casing mandatory")
        print("• Permits: Special railway authority permits")
        print("• Inspection: Railway engineer supervision required")
        
    else:
        print("\n" + "="*80)
        print("CANAL CROSSING REQUIREMENTS")
        print("="*80)
        print("\nMinimum Requirements:")
        print("• Burial Depth: 2.0 meters minimum")
        print("• Weight Coating: Heavy concrete coating")
        print("• Anchor Blocks: At both sides of canal")
        print("• Protection: Anti-buoyancy measures")
    
    print("\n" + "="*80)
    print("For detailed crossing design and permits:")
    print("Contact: B.C. Prabhakar")
    print("Email: prabhubc@gmail.com")
    print("="*80)
    
    input("\nPress Enter to return to menu...")

def about_consultant():
    """Display consultant information"""
    print("\n" + "="*80)
    print("B.C. PRABHAKAR - PIPELINE ENGINEERING CONSULTANT")
    print("="*80)
    
    print("\nProfessional Profile:")
    print("• Freelance Oil and Gas Pipeline Engineering Consultant")
    print("• Specialization: Desert pipeline design and construction")
    print("• Experience: Multiple cross-country pipeline projects")
    print("• Location: Available for projects worldwide")
    
    print("\nServices Offered:")
    print("• Pipeline design review and optimization")
    print("• Crossing design (road, railway, nalla, canal)")
    print("• Material selection and specification")
    print("• Construction supervision and quality assurance")
    print("• Training programs for engineering teams")
    print("• Feasibility studies and cost estimation")
    
    print("\nTechnical Expertise:")
    print("• ASME B31.4 / B31.8 compliance")
    print("• API 5L pipe specifications")
    print("• Desert pipeline corrosion protection")
    print("• HDD (Horizontal Directional Drilling)")
    print("• Pipeline integrity management")
    
    print("\nContact Information:")
    print("• Email: prabhubc@gmail.com")
    print("• Available for consulting projects")
    print("• Training sessions for engineering teams")
    print("• Design review and technical audits")
    
    print("\n" + "="*80)
    print("This tool is part of B.C. Prabhakar's commitment to")
    print("engineering education and knowledge sharing.")
    print("="*80)
    
    input("\nPress Enter to return to menu...")

def main_menu():
    """Main menu function"""
    while True:
        print("\n" + "="*80)
        print("PIPELINE DESIGNER - MAIN MENU")
        print("="*80)
        print("\n1. Calculate Flow Velocity")
        print("2. Estimate Pressure Drop")
        print("3. Calculate Wall Thickness")
        print("4. Crossing Design Guide")
        print("5. About Consultant")
        print("6. Exit Program")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            calculate_flow_velocity()
        elif choice == '2':
            pressure_drop_estimator()
        elif choice == '3':
            wall_thickness_calculator()
        elif choice == '4':
            crossing_design_guide()
        elif choice == '5':
            about_consultant()
        elif choice == '6':
            print("\n" + "="*80)
            print("Thank you for using Pipeline Designer!")
            print("\nRemember:")
            print("• This is a training tool for educational purposes")
            print("• Always verify designs with senior engineers")
            print("• Follow applicable codes and standards")
            print("\nFor professional consultation:")
            print("B.C. Prabhakar")
            print("Freelance Oil and Gas Pipeline Engineering Consultant")
            print("Email: prabhubc@gmail.com")
            print("\nSafe engineering practices save lives!")
            print("="*80)
            break
        else:
            print("\nPlease enter a number between 1 and 6")

# Start the application
if __name__ == "__main__":
    print("\nLoading Pipeline Design Professional Tool...")
    main_menu()
