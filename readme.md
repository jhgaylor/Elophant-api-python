An overhaul is coming... I hope :D

#Docs are available again. I'll get this updated and off of slumber.  requests will replace it. I'll possibly also abstract it to an object like form, so instead of making api calls, you request object attributes that get calculated on the fly via sync api calls.

http://www.elophant.com/league-of-legends/api/docs

#usage examples
#a = api(key="###")
# print a.champions()
# print a.items()
# print a.get_player_stats('76833', 'euw')
#print a.get_team_by_id('TEAM-e4936d7b-b80e-4367-a76c-5ccf7388c995', 'na')
#print a.get_team_by_tag_or_name('tsm', 'na')
#print a.get_summoner_names(['76833'])
#print a.get_summoner_team_info('mercenaryRPG', 'na')

#need to install slumber, requests
