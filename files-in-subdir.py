import os

with os.scandir('images') as entries:
  print("###############_start_###############")
  for entry in entries:
    # List all files in a directory using os.listdir
    basepath = "images/" + entry.name
    for entry1 in os.listdir( basepath):
      if os.path.isfile(os.path.join(basepath, entry1)):
        print(entry1)

    print("_____________________________________")

print("################_end_################")
