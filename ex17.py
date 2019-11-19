from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

print(f"First, we now look at what is in the {from_file} \n"
      , open(from_file).read())

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, CTRL-C to abort.")
input("RETURN or ^C: ")

open(to_file, "w").write(indata)

print("Alright, all done.")

print(f"Here is the content of {to_file} \n"
      , open(to_file).read())
