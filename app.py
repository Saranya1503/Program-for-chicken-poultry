import math

LEG_WEIGHT = 0.25
WING_WEIGHT = 0.25
FLESH_WEIGHT = 1.0

PARTS_PER_CHICKEN = {
    "leg": 2,
    "wing": 2,
    "flesh": 1
}

def process_order(legs_needed, wings_needed, flesh_needed):
    total_weight = (legs_needed * LEG_WEIGHT) + (wings_needed * WING_WEIGHT) + (flesh_needed * FLESH_WEIGHT)
    chickens_for_legs = math.ceil(legs_needed / PARTS_PER_CHICKEN["leg"])
    chickens_for_wings = math.ceil(wings_needed / PARTS_PER_CHICKEN["wing"])
    chickens_for_flesh = math.ceil(flesh_needed / PARTS_PER_CHICKEN["flesh"])

    total_chickens_needed = max(chickens_for_legs, chickens_for_wings, chickens_for_flesh)

    total_legs = total_chickens_needed * PARTS_PER_CHICKEN["leg"]
    total_wings = total_chickens_needed * PARTS_PER_CHICKEN["wing"]
    total_flesh = total_chickens_needed * PARTS_PER_CHICKEN["flesh"]

    remaining_legs = total_legs - legs_needed
    remaining_wings = total_wings - wings_needed
    remaining_flesh = total_flesh - flesh_needed

    remaining_leg_weight = remaining_legs * LEG_WEIGHT
    remaining_wing_weight = remaining_wings * WING_WEIGHT
    remaining_flesh_weight = remaining_flesh * FLESH_WEIGHT

    print("\n======= ORDER SUMMARY =======")
    print(f"Total weight of order     : {total_weight:.2f} kg")
    print(f"Whole chickens needed     : {total_chickens_needed}")
    print("\nRemaining parts after fulfilling order:")
    print(f"  Legs  : {remaining_legs}  ({remaining_leg_weight:.2f} kg)")
    print(f"  Wings : {remaining_wings}  ({remaining_wing_weight:.2f} kg)")
    print(f"  Flesh : {remaining_flesh}  ({remaining_flesh_weight:.2f} kg)")
    print("=============================")

print(" Chicken Order System ")
legs = int(input("Enter number of legs needed      : "))
wings = int(input("Enter number of wings needed     : "))
flesh = int(input("Enter number of flesh portions   : "))

process_order(legs, wings, flesh)
