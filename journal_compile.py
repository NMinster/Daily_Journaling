import os

# Set the directory containing the text files
text_files_dir = r"C:\Users\NM\journal"

# Create a dictionary to store the text content of each file, keyed by the file date
text_files = {}

# Loop through each file in the directory
for filename in os.listdir(text_files_dir):
    # Check if the file is a text file (ends in ".txt")
    if filename.endswith(".txt"):
        # Extract the date from the filename
        file_date = filename.split(".")[0]
        
        # Open the file and read the contents
        with open(os.path.join(text_files_dir, filename), "r") as f:
            text_content = f.read()
            
        # Store the text content in the dictionary, keyed by the file date
        text_files[file_date] = text_content

# Sort the dictionary by date
sorted_text_files = dict(sorted(text_files.items()))

# Create a string to hold the journal content
journal_content = ""

# Loop through each entry in the sorted dictionary and append the text content to the journal
for date, text in sorted_text_files.items():
    journal_content += "{}\n{}\n\n".format(date, text)

# Write the journal content to a file
with open("journal.txt", "w") as f:
    f.write(journal_content)
    
# Print a message to indicate the journal has been saved
print("Journal saved to journal.txt")
