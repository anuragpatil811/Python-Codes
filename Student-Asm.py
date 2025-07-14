# Embedded Assembly Code in the Python Program
assembly_code = """
START   0
LOAD    R1, GRADES
LOAD    R2, STUDENTS
MOV     R3, LENGTH
SORT    R1, R2, R3
STORE   R2, SORTED_STUDENTS
STORE   R1, SORTED_GRADES
END
"""

# Sample input data: students and grades
student_numbers = [101, 102, 103, 104]
grades = [75, 85, 65, 95]

# Length of the tables
table_length = len(student_numbers)

# 1. Symbol Table
symbol_table = {
    "START": 0,
    "GRADES": 100,
    "STUDENTS": 104,
    "LENGTH": 108,
    "SORTED_STUDENTS": 112,
    "SORTED_GRADES": 116,
    "END": None
}

# 2. Literal Table (Not used in this example)
literal_table = {}

# 3. Table of Incomplete Instructions (For forward references)
incomplete_instructions = []

# 4. Intermediate Code Representation
intermediate_code = []
instruction_address = 0

# Parse Assembly Code
for line in assembly_code.strip().split("\n"):
    # Strip the line and split into parts
    parts = line.split()
    
    # Skip empty lines or lines that don’t have enough parts
    if not parts:
        continue
    
    # Check if the line starts with a label (labels are alphabetical identifiers)
    label = parts[0] if len(parts) > 1 and parts[1].isalpha() else None
    
    # Determine the mnemonic (operation code) and operands based on the label presence
    if label:
        mnemonic = parts[1] if len(parts) > 1 else None
        operands = parts[2:] if len(parts) > 2 else []
    else:
        mnemonic = parts[0] if len(parts) > 0 else None
        operands = parts[1:] if len(parts) > 1 else []

    # Append instruction to intermediate code
    intermediate_code.append((instruction_address, label, mnemonic, operands))
    instruction_address += 1

# 5. Machine Code Conversion
machine_code = []
mnemonic_to_opcode = {
    "LOAD": "01",
    "MOV": "02",
    "SORT": "03",
    "STORE": "04",
    "END": "FF"
}

for instruction in intermediate_code:
    address, label, mnemonic, operands = instruction
    if mnemonic in mnemonic_to_opcode:
        opcode = mnemonic_to_opcode[mnemonic]
        operand_addresses = [symbol_table.get(op, "??") for op in operands]
        machine_code.append(f"{address:02d} {opcode} {' '.join(map(str, operand_addresses))}")

# 6. Sorting Logic (Assembly Operation Simulated in Python)
def sort_students_by_grades(students, grades):
    combined = list(zip(students, grades))
    sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)  # Sort by grades descending
    sorted_students, sorted_grades = zip(*sorted_combined)
    return list(sorted_students), list(sorted_grades)

# Perform sorting
sorted_students, sorted_grades = sort_students_by_grades(student_numbers, grades)

# Output results
print(f"Original Student Numbers: {student_numbers}")
print(f"Original Grades: {grades}")
print(f"Sorted Student Numbers: {sorted_students}")
print(f"Sorted Grades: {sorted_grades}")
print("\nSymbol Table:", symbol_table)
print("Literal Table:", literal_table)
print("Table of Incomplete Instructions:", incomplete_instructions)
print("\nIntermediate Code:")
for entry in intermediate_code:
    print(entry)
print("\nMachine Code:")
for code in machine_code:
    print(code)
