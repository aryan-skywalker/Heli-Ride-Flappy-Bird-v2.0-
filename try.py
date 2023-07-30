# Open the text file
with open('leaderboard.txt', 'r') as file:
    # Read the contents of the file
    contents = file.readlines()

# Create an empty list
data = []
def compare_marks(record):
    return int(str(record['marks']).zfill(3))
# Loop through each line of the file
for line in contents:
    # Split the line into name and marks
    name, marks = line.strip().split(',')
    # Create a dictionary with the name and marks as key-value pairs
    record = {'name': name, 'marks': marks}
    # Append the dictionary to the list
    data.append(record)

# Close the file
file.close()
#sorted_data = sorted(data, key=lambda x: x['marks'], reverse=True)
sorted_data = sorted(data, key=compare_marks, reverse=True)
# Print the list
#print(data)
#print(sorted_data)
for record in sorted_data:
    print(record['name'])
    print(record['marks'])
    print()
