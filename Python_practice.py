# print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
# counties.append("El Paso")
# print(counties)
# print(type(counties))
# print(len(counties))
# print(counties[1])
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
# print(counties_dict)
# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())
# print(counties_dict["Denver"])
# print(counties_dict.get("Denver"))
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# print(voting_data[2]["county"])
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("what is the total vote in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print(f'I recieved {percentage_votes: .2f} % of the total votes')
# if counties[1] == "Denver" :
#     print(counties[1])
# if "Arapahoe" in counties or " El Paso" in counties:

#     print("Arapahoe or El Paso is in the list of counties.")

# else:

#     print("Arapahoe and El Paso are not in the list of counties.")

# x = 0

# while x < 5:
#     print(x)
#     x = x + 1

# for county in counties:
#     print(county)

# for i in range(5):
#     print(i)

# for i in range(len(counties)):
#     print(counties[i])

for county in counties_dict.keys():
    print(county)

for n_votes in counties_dict.values():
    print(n_votes)

for county in counties_dict:
    print(f'{county}:{counties_dict[county]}')

print(counties_dict.items())

for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters')

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)