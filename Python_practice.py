#print("Hello World")

# #How many votes did you get
# my_votes = int(input("How many votes did you get in the election> "))
# #Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# #Calculate the percentage of votes you received
# #percentage_votes = (my_votes / total_votes) * 100
# #print("I received " + str(percentage_votes)+ "% of the total votes")
# print(f"I received {my_votes/total_votes *100}% of the total votes.")

# candidate_votes = int(input("How many votes did the canditate get in the election?"))
# total_votes = int(input("What is the total number of votes in the election?"))
# message_to_candidate = (
# f"You received {candidate_votes:,} number of votes"
# f"The total number of votes in the election was {total_votes:,}."
# f"You received {candidate_votes / total_votes *100:.2f}% of the total votes.")

#print(message_to_candidate)


# counties = ["Arapahoe","Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")

# counties = ["Arapahoe","Denver", "Jefferson"]
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties")
#     if "Arapahoe" in counties or "El Paso" in counties:
#         print("Arapahoe or Elpaso is in the list of counties.")
#     else:
#         print("Arapahoe and El Paso are not in the list of counties.")
#     for county in counties:
#         print(county)
#     for i in range(len(counties)):
#         print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#    print(county)
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])
# for county in counties_dict:
#     print(counties_dict.get(county))
# for key, value in counties_dict.items():
#     print(key,value)
for county, voters in counties_dict.items():
#     print((county + " county has") , str((voters)) + (" registered voters"))
      print(f"{county} county has {voters:,}, regeistered voters.")



