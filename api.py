import slumber

class api():

	def __init__(self, key):
		self.elo = slumber.API("http://elophant.com/api/")
		self.key = key
	
	def status(self):
		return self.elo.status.get(key=self.key)
		
	def items(self):
		return self.elo.v1.items.get(key=self.key)

	def champions(self):
		return self.elo.v1.champions.get(key=self.key)

	def summoner_by_name(self, name, region):
		return self.elo.v1(region).getSummonerByName.get(summonerName=name, key=self.key)

	def get_ranked_stats(self, id, region, season="CURRENT"):
		return self.elo.v1(region).getRankedStats.get(accountId=id, season=season, key=self.key)

	def get_in_progress_game_info(self, name, region):
		return self.elo.v1(region).getInProgressGameInfo.get(summonerName=name, key=self.key)

	def get_most_played_champions(self, id, region):
		return self.elo.v1(region).getMostPlayedChampions.get(accountId=id, key=self.key)

	def get_mastery_pages(self, id, region):
		return self.elo.v1(region).getMasteryPages.get(summonerId=id, key=self.key)

	def get_rune_pages(self, id, region):
		return self.elo.v1(region).getRunePages.get(summonerId=id, key=self.key)

	def get_recent_games(self, id, region):
		return self.elo.v1(region).getRecentGames.get(accountId=id, key=self.key)

	#this one is different.  ill do it later
	def get_summoner_names(self, ids, region):
		return self.elo.v1(region).getRecentGames.get(summonerIds=",".join(ids), key=self.key)

	def get_player_stats(self, id, region, season="CURRENT"):
		return self.elo.v1(region).getPlayerStats.get(accountId=id, season=season, key=self.key)

	def get_team_by_id(self, id, region):
		return self.elo.v1(region).getTeamById.get(teamId=id, key=self.key)

	def get_team_by_tag_or_name(self, tag, region):
		return self.elo.v1(region).getTeamByTagOrName.get(tagOrName=tag, key=self.key)

	#needs to be tested
	def get_team_end_of_game_stats(self, teamId, gameId, region):
		return self.elo.v1(region).getTeamEndOfGameStats.get(teamId=id, gameId=gameId, key=self.key)

	def get_team_ranked_stats(self, id, region):
		return self.elo.v1(region).getTeamRankedStats.get(teamId=id, key=self.key)

	#not working
	def get_summoner_team_info(self, id, region):
		print "warning.  probably doesn't work.  elophant.api.api.get_summoner_team_info"
		return self.elo.v1(region).getSummonerTeamInfo.get(summonerId=id, key=self.key)


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
