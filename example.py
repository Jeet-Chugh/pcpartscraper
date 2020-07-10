# This is an import statement in one line, that imports both Modules
from pcpartscraper.scraper import Part,Query

# Instantiate the Part with a url
# first URL points to an Intel i5-2400 Processor
# second URL points to an AMD Ryzen 5 2600 Processor
intel_cpu = Part('/product/jxJwrH/intel-cpu-bx80623i52400')
amd_cpu = Part('/product/jLF48d/amd-ryzen-5-2600-34ghz-6-core-processor-yd2600bbafbox')

# Create a list of parts, if you want to loop through their information
parts_list = [intel_cpu,amd_cpu]

# Define a function that loops through the information to see what the methods can provide
def info_loop(p_list):
    print('This is an example for the Part Class')
    for part in parts_list:
        print(part.name())
        print(part.type())
        print(part.amazon_link())
        print(part.price())
        print(part.advanced_specs())
        print(part.url())
        print(part.rating())
        print(part.reviews(1))
        print('\n')
# Call the info_loop function
info_loop(parts_list)

# Now lets try the Query function
print('We are now testing the Query Function')

ryzen_fives = Query('ryzen 5',results=3,exclude_laptops=True,pages=1)
# Here you see that we want a list of 3 results, on the first result page, excluding laptops.
print(ryzen_fives)

# We can loop through our list, or directly index it
print(ryzen_fives[0].name())

for ryzen in ryzen_fives:
    print(ryzen.name())

# Now lets make a functional program that finds cheap Cooler Master Parts
# This program finds the 20 results on the first page for Cooler Master parts
# If the part has an amazon link and is under $50
# With such a simple program, you can now see how powerful this can be when using many filters
cooler_master_parts = Query('cooler master',20,False,1)
for part in cooler_master_parts:
    if part.price() != None and part.amazon_link() != None and part.price() < 50:
        print('Buy the {part} for {price} at {az_link} \n'.format(part=part.name(),price=part.price(),az_link=part.amazon_link()))
# Congratulations! You have a working program. Now lets see what you can make by yourself!
