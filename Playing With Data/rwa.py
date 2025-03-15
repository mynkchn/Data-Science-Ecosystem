from random import randint as rnd
import re

memReg = r'D:\Data Science\members.txt'
exReg = r'D:\Data Science\inactive.txt'
fee = ('yes', 'no')

# Function to generate sample files
def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active\n')
        data = '{:^13} {:<11} {:<6}\n'
        for rowno in range(20):
            date = f"{rnd(2015, 2020)}-{rnd(1, 12)}-{rnd(1, 25)}"
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active\n')
        data = '{:^13} {:<11} {:<6}\n'
        for rowno in range(3):
            date = f"{rnd(2015, 2020)}-{rnd(1, 12)}-{rnd(1, 25)}"
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

# Function to clean files
def cleanFiles(currentMem, exMem):
    active_members = []
    inactive_members = []

    with open(currentMem, 'r') as readfile:
        header = readfile.readline()  # Read and store header
        lines = readfile.readlines()

    for line in lines:
        if line.strip():  # Skip empty lines
            parts = line.strip().split()
            member_data = ' '.join(parts) + '\n'  # Reformat data as string
            if parts[-1].lower() == 'no':
                inactive_members.append(member_data)
            else:
                active_members.append(member_data)

    # Rewrite members.txt with only active members
    with open(currentMem, 'w') as writefile:
        writefile.write(header)
        writefile.writelines(active_members)

    # Append inactive members to inactive.txt
    with open(exMem, 'w') as writefile:
        writefile.writelines(header)
        writefile.writelines(inactive_members)

# Generate sample files and clean them
genFiles(memReg, exReg)
cleanFiles(memReg, exReg)

print("File cleaning completed successfully!")
