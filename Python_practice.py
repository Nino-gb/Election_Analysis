counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

 




voting_data= [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]



counties_dict = {"Arapahoe": 422829, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


