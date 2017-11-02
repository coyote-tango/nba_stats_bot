import praw
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import difflib
import re
import pprint

# # for a in soup.select(".players-list__names a"):
# # 	players_dict[(a.text.lower().replace(',', ''))] = a['href'].strip('player/')


browser = webdriver.Chrome()


players_dict = {'dellavedova matthew': '203521', 'noah joakim': '201149', 'exum dante': '203957', 'jones jr. derrick': '1627884', 'kleber maxi': '1628467', 'knight brandon': '202688', 'singler kyle': '202713', 'nader abdel': '1627846', 'hayward gordon': '202330', 'ulis tyler': '1627755', 'scott mike': '203118', 'mirotic nikola': '202703', 'booker devin': '1626164', 'redick jj': '200755', 'hill solomon': '203524', 'holmes richaun': '1626158', 'crabbe allen': '203459', 'thornwell sindarius': '1628414', 'huestis josh': '203962', 'terry jason': '1891', 'dorsey tyler': '1628416', 'pachulia zaza': '2585', 'cooke charles': '1628429', 'williams jr. matt': '1628475', 'green jeff': '201145', 'diallo cheick': '1627767', 'aminu al-farouq': '202329', 'osman cedi': '1626224', 'hill george': '201588', 'richardson josh': '1626196', 'wilkins damien': '2863', 'whitehead isaiah': '1627785', 'hamilton daniel': '1627772', 'covington robert': '203496', 'mcdermott doug': '203926', 'carter vince': '1713', 'calderon jose': '101181', 'parsons chandler': '202718', 'mahinmi ian': '101133', 'portis bobby': '1626171', 'patterson patrick': '202335', 'evans jawun': '1628393', 'ouattara yakuba': '1628473', 'monk malik': '1628370', 'carroll demarre': '201960', 'graham treveon': '1626203', 'frazier tim': '204025', 'harris joe': '203925', 'schroder dennis': '203471', 'young nick': '201156', 'rivers austin': '203085', 'johnson stanley': '1626169', 'leonard kawhi': '202695', 'rubio ricky': '201937', 'rabb ivan': '1628397', 'felix carrick': '203467', 'nance jr. larry': '1626204', 'jones damian': '1627745', 'felicio cristiano': '1626245', 'jordan deandre': '201599', 'dragic goran': '201609', 'johnson amir': '101161', 'cook quinn': '1626188', 'stone julyan': '202933', 'holiday justin': '203200', 'murray jamal': '1627750', 'muhammad shabazz': '203498', 'bogdanovic bojan': '202711', 'leuer jon': '202720', 'thomas isaiah': '202738', 'afflalo arron': '201167', 'beverley patrick': '201976', 'irving kyrie': '202681', 'mcroberts josh': '201177', 'siakam pascal': '1627783', 'gasol marc': '201188', 'speights marreese': '201578', "o'bryant iii johnny": '203948', 'ferguson terrance': '1628390', 'onuaku chinanu': '1627778', 'iguodala andre': '2738', 'beasley malik': '1627736', 'johnson joe': '2207', 'white derrick': '1628401', 'bradley avery': '202340', 'hart josh': '1628404', 'felton raymond': '101109', 'ginobili manu': '1938', 'paige marcus': '1627779', 'dedmon dewayne': '203473', 'connaughton pat': '1626192', 'caldwell-pope kentavious': '203484', 'wall john': '202322', 'thompson klay': '202691', 'anderson ryan': '201583', 'bogut andrew': '101106', 'sumner edmond': '1628410', 'poeltl jakob': '1627751', 'markkanen lauri': '1628374', 'morris markieff': '202693', 'satoransky tomas': '203107', 'porzingis kristaps': '204001', 'boucher chris': '1628449', 'whiteside hassan': '202355', 'brussino nicolas': '1627852', 'jackson reggie': '202704', 'paul chris': '101108', 'meeks jodie': '201975', 'kornet luke': '1628436', 'montero luis': '1626242', 'parker tony': '2225', 'paul brandon': '203464', 'georges-hunt marcus': '1627875', 'marjanovic boban': '1626246', 'oladipo victor': '203506', 'griffin eric': '203547', 'arthur darrell': '201589', 'vucevic nikola': '202696', 'jefferson al': '2744', 'cunningham dante': '201967', 'kennard luke': '1628379', 'simmons jonathon': '203613', 'hezonja mario': '1626209', 'cousins demarcus': '202326', 'robinson iii glenn': '203922', 'swanigan caleb': '1628403', 'crawford jamal': '2037', 'kilpatrick sean': '203930', 'lydon tyler': '1628399', 'wilcox cj': '203912', 'poythress alex': '1627816', 'lauvergne joffrey': '203530', 'adams steven': '203500', 'crowder jae': '203109', 'bolomboy joel': '1627762', 'smith jason': '201160', 'valanciunas jonas': '202685', 'gasol pau': '2200', 'aldrich cole': '202332', 'johnson tyler': '204020', 'black tarik': '204028', 'chandler tyson': '2199', 'bullock reggie': '203493', 'wiggins andrew': '203952', 'hield buddy': '1627741', 'dekker sam': '1626155', 'batum nicolas': '201587', 'bazemore kent': '203145', 'powell norman': '1626181', 'noel nerlens': '203457', 'sabonis domantas': '1627734', 'hernangomez willy': '1626195', "russell d'angelo": '1626156', 'young thaddeus': '201152', 'hunter vincent': '1626205', 'randle julius': '203944', 'muscala mike': '203488', 'antetokounmpo giannis': '203507', 'lee courtney': '201584', 'pondexter quincy': '202347', 'durant kevin': '201142', 'waiters dion': '203079', 'beasley michael': '201563', 'butler jimmy': '202710', 'pullen jacob': '1626643', 'adebayo bam': '1628389', 'iwundu wes': '1628411', 'walton jr. derrick': '1628476', 'james lebron': '2544', 'booker trevor': '202344', 'jefferson richard': '2210', 'udoh ekpe': '202327', 'reed davon': '1628432', 'love kevin': '201567', 'gordon aaron': '203932', 'gibson taj': '201959', 'temple garrett': '202066', 'jackson frank': '1628402', 'vanvleet fred': '1627832', 'wade dwyane': '2548', "fox de'aaron": '1628368', 'mcgruder rodney': '203585', "moore e'twaun": '202734', 'mbah a moute luc': '201601', 'teodosic milos': '1628462', 'dinwiddie spencer': '203915', "bembry deandre'": '1627761', 'anthony carmelo': '2546', 'payton elfrid': '203901', 'luwawu-cabarrot timothe': '1627789', 'monroe greg': '202328', 'howard dwight': '2730', 'kaminsky frank': '1626163', 'ennis tyler': '203898', 'mcadoo james michael': '203949', 'clark ian': '203546', 'perrantes london': '1628506', 'green danny': '201980', 'beal bradley': '203078', 'tatum jayson': '1628369', 'mills patty': '201988', 'layman jake': '1627774', 'napier shabazz': '203894', 'babbitt luke': '202337', 'smith jr': '2747', 'oubre jr. kelly': '1626162', 'thompson tristan': '202684', 'sampson jakarr': '203960', 'zeller tyler': '203092', 'dudley jared': '201162', 'koufos kosta': '201585', 'brown jaylen': '1627759', 'ellington wayne': '201961', 'westbrook russell': '201566', 'harrell montrezl': '1626149', 'ferrell yogi': '1627812', 'holland john': '204066', 'allen kadeem': '1628443', 'birch khem': '203920', 'korkmaz furkan': '1627788', 'felder kay': '1627770', 'patton justin': '1628383', 'hernangomez juan': '1627823', 'mccullough chris': '1626191', 'mac sheldon': '1627815', 'horford al': '201143', 'jackson justin': '1628382', 'brown sterling': '1628425', 'harris tobias': '202699', 'capela clint': '203991', 'aldridge lamarcus': '200746', 'davis ed': '202334', 'brewer corey': '201147', 'brown anthony': '1626148', 'george paul': '202331', 'clarkson jordan': '203903', 'sefolosha thabo': '200757', 'miller darius': '203121', 'holiday jrue': '201950', 'grant jerian': '1626170', 'finney-smith dorian': '1627827', 'hood rodney': '203918', 'middleton khris': '203114', 'saric dario': '203967', 'leonard meyers': '203086', 'robinson devin': '1628421', 'snell tony': '203503', 'bledsoe eric': '202339', 'magette josh': '203705', 'okafor jahlil': '1626143', 'zizic ante': '1627790', 'motley johnathan': '1628405', 'bogdanovic bogdan': '203992', 'mckinnie alfonzo': '1628035', 'mclemore ben': '203463', 'williams lou': '101150', 'anderson kyle': '203937', 'nwaba david': '1628021', 'ntilikina frank': '1628373', 'smith ish': '202397', 'zeller cody': '203469', 'nene': '2403', 'nelson jameer': '2749', "o'quinn kyle": '203124', "o'neale royce": '1626220', 'belinelli marco': '201158', 'williams marvin': '101107', 'bryant thomas': '1628418', 'rozier terry': '1626179', 'abrines alex': '203518', 'gay rudy': '200752', 'mcgee javale': '201580', 'neto raul': '203526', 'clavell gian': '1628492', 'selden wayne': '1627782', 'mejri salah': '1626257', 'bird jabari': '1628444', 'walker kemba': '202689', 'ennis iii james': '203516', 'payne adreian': '203940', 'moreland eric': '203961', 'zhou qi': '1627753', 'bender dragan': '1627733', 'stauskas nik': '203917', 'tucker pj': '200782', 'joseph cory': '202709', 'nurkic jusuf': '203994', 'simmons kobi': '1628424', 'harris gary': '203914', 'papagiannis georgios': '1627834', 'mozgov timofey': '202389', 'ross terrence': '203082', 'arcidiacono ryan': '1627853', 'hilliard darrun': '1626199', 'isaac jonathan': '1628371', 'thomas lance': '202498', 'wiley jacob': '1628451', 'barton will': '203115', 'morris monte': '1628420', 'mitchell donovan': '1628378', 'ariza trevor': '2772', 'wright delon': '1626153', 'matthews wesley': '202083', 'collins zach': '1628380', 'valentine denzel': '1627756', 'maker thon': '1627748', 'ilyasova ersan': '101141', 'smith jr. dennis': '1628372', 'dunn kris': '1627739', 'lyles trey': '1626168', 'hammons aj': '1627773', 'harkless maurice': '203090', 'ajinca alexis': '201582', 'ojeleye semi': '1628400', 'costello matt': '1627856', 'drummond andre': '203083', 'johnson wesley': '202325', 'olynyk kelly': '203482', 'johnson dakari': '1626177', 'johnson brice': '1627744', 'giles harry': '1628385', 'warren tj': '203933', 'gallinari danilo': '201568', 'livingston shaun': '2733', 'turner myles': '1626167', 'casspi omri': '201956', 'craig torrey': '1628470', 'grant jerami': '203924', 'anigbogu ike': '1628387', 'larkin shane': '203499', 'bradley tony': '1628396', 'parker jabari': '203953', 'chandler wilson': '201163', 'green draymond': '203110', 'frye channing': '101112', 'barea j.j.': '200826', 'asik omer': '201600', 'zipser paul': '1627835', 'jack jarrett': '101127', 'anderson justin': '1626147', 'lopez robin': '201577', 'kidd-gilchrist michael': '203077', 'smart marcus': '203935', 'brooks aaron': '201166', 'bjelica nemanja': '202357', 'liggins deandre': '202732', 'miles cj': '101139', 'brown bobby': '201628', 'mccaw patrick': '1627775', 'plumlee mason': '203486', 'blue vander': '203505', 'williams troy': '1627786', 'ellenson henry': '1627740', 'jones tyus': '1626145', 'nowitzki dirk': '1717', 'brogdon malcolm': '1627763', 'brooks dillon': '1628415', 'daniels troy': '203584', 'collison darren': '201954', 'baynes aron': '203382', 'rose derrick': '201565', 'roberson andre': '203460', 'hicks isaiah': '1628439', 'cauley-stein willie': '1626161', 'jackson demetrius': '1627743', 'yabusele guerschon': '1627824', 'miller malcolm': '1626259', 'dieng gorgui': '203476', 'acy quincy': '203112', 'dotson damyean': '1628422', 'gortat marcin': '101162', 'allen tony': '2754', 'williams c.j.': '203710', 'lavine zach': '203897', 'collison nick': '2555', 'baldwin iv wade': '1627735', 'caruso alex': '1627936', 'morris marcus': '202694', 'delaney malcolm': '1627098', 'wolters nate': '203489', 'plumlee miles': '203101', 'james mike': '1628455', 'mcconnell t.j.': '204456', 'young joe': '1626202', 'wilson d.j.': '1628391', 'payne cameron': '1626166', 'powell dwight': '203939', 'bacon dwayne': '1628407', 'evans tyreke': '201936', 'allen jarrett': '1628386', 'lowry kyle': '200768', 'henson john': '203089', 'cooley jack': '204022', 'randolph zach': '2216', 'len alex': '203458', 'rondo rajon': '200765', 'nogueira lucas': '203512', 'stephenson lance': '202362', 'artis jamel': '1628503', 'payton ii gary': '1627780', 'davis anthony': '203076', 'jokic nikola': '203999', 'green jamychal': '203210', 'murray dejounte': '1627749', 'jackson josh': '1628367', 'hardaway jr. tim': '203501', 'teletovic mirza': '203141', 'wright brandan': '201148', 'harrison andrew': '1626150', 'richardson malachi': '1627781', 'kuzma kyle': '1628398', 'brown lorenzo': '203485', 'johnson james': '201949', 'millsap paul': '200794', 'ball lonzo': '1628366', 'biyombo bismack': '202687', 'fultz markelle': '1628365', 'derozan demar': '201942', 'winslow justise': '1626159', 'mason frank': '1628412', 'augustin d.j.': '201571', 'tolliver anthony': '201229', 'mudiay emmanuel': '1626144', 'dozier pj': '1628408', 'bell jordan': '1628395', 'caboclo bruno': '203998', 'mathiang mangok': '1628493', 'shumpert iman': '202697', 'davis deyonta': '1627738', 'blakeney antonio': '1628469', 'anunoby og': '1628384', 'leaf tj': '1628388', 'galloway langston': '204038', 'embiid joel': '203954', 'lin jeremy': '202391', 'mccollum cj': '203468', 'collins john': '1628381', 'favors derrick': '202324', 'curry seth': '203552', 'gobert rudy': '203497', 'hollis-jefferson rondae': '1626178', 'turner evan': '202323', 'korver kyle': '2594', 'kanter enes': '202683', 'bertans davis': '202722', 'levert caris': '1627747', 'prince taurean': '1627752', 'ingram brandon': '1627742', 'theis daniel': '1628464', 'harris devin': '2734', 'withey jeff': '203481', 'buycks dwight': '202779', 'deng luol': '2736', 'curry stephen': '201939', 'lopez brook': '201572', 'wilson jamil': '203966', 'lamb jeremy': '203087', 'barnes harrison': '203084', 'west david': '2561', 'carter-williams michael': '203487', 'haslem udonis': '2617', 'looney kevon': '1626172', 'vonleh noah': '203943', 'jones jalen': '1627883', 'teague jeff': '201952', 'labissiere skal': '1627746', 'sessions ramon': '201196', 'gordon eric': '201569', 'mickey jordan': '1626175', 'harden james': '201935', 'white okaro': '1627855', 'bayless jerryd': '201573', 'kuzminskas mindaugas': '1627851', 'young mike': '1628454', 'martin jarell': '1626185', 'jerebko jonas': '201973', 'reed willie': '203186', 'faried kenneth': '202702', 'chalmers mario': '201596', 'lillard damian': '203081', 'taylor isaiah': '1627819', 'fournier evan': '203095', 'chriss marquese': '1627737', 'ibaka serge': '201586', 'griffin blake': '201933', 'forbes bryn': '1627854', 'zubac ivica': '1627826', 'conley mike': '201144', 'porter jr. otto': '203490', 'williams alan': '1626210', 'peters alec': '1628409', 'mack shelvin': '202714', 'baker ron': '1627758', 'towns karl-anthony': '1626157', 'vaughn rashad': '1626173', 'burks alec': '202692', 'ingles joe': '204060', 'simmons ben': '1627732'}
a = [item for item in players_dict if len(item.split()) > 2]

last_names= [key.split()[0] for key in players_dict.keys()]


repeated_last_names = [item for item in last_names if last_names.count(item) > 1]

reddit = praw.Reddit(client_id='HHZ5FFVA72bOFA',
					 client_secret='d2vtaU2gMLhxZ9x6nfxFtWp-AS0',
					 user_agent= 'This is a test bot',
					 username='CoyoteTango_',
					 password='Bloodline19rd')

subreddit = reddit.subreddit('test')
keyword = 'statsbot'
sleep_time = None

for submission in subreddit.stream.submissions():
	submission.comments.replace_more(limit=0)
	print(submission.title)
	for comment in submission.comments.list():
		comment_content = comment.body.lower().split() #Comment contetn normalized
		if keyword in comment_content:
			player_last_name = comment_content[comment_content.index(keyword) - 1]

			player_stats_list = ['MIN', 'PTS', 'REB', 'AST', 'FG%', '3P%', 'FT%', 'STL', 'BLK', '+/-']
			player_stats = {'MIN': '' , 'PTS': '', 'REB': '', 'AST': '','FG%':'', '3P%':'' , 'FT%':'' , 'STL':'' , 'BLK':'' ,'+/-': ''}
			player_id = ''		
			
			if player_last_name in repeated_last_names:
					
				player_full_name = player_last_name + ' ' +comment_content[comment_content.index(keyword) - 2]	
				try:		
					player_id = players_dict[player_full_name]
					display_name = player_full_name.split()[-1].title()+ ' ' + player_full_name.split()[0].title()
				except:
					
					reply_string = "I've found more than one player with that last name:\n\n"
					for item in players_dict.keys():
						if player_last_name == item.split()[0]:
							reply_string = reply_string +'- ' + item.split()[-1].title() + ' ' + item.split()[0].title() + '\n\n'
					
					reply_string = reply_string +"Please specify the first name to bring 'em stats."
					print(reply_string)			
			else:

				if player_last_name not in [item.split()[0] for item in players_dict.keys()]:
					reply_string = "Sorry, I couldn't find that player, make sure there aren't any typos"
									
				else:
					player_id = {key.split()[0]:players_dict[key] for key in players_dict.keys()}[player_last_name]
					
					for key in players_dict.keys():
						if player_id == players_dict[key]:
							player_full_name = key
					
					display_name = player_full_name.split()[-1].title()+ ' ' + player_full_name.split()[0].title()
					
			if player_id is not '':

				url = 'https://stats.nba.com/player/'+player_id+'/'
				browser.get(url)
				browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")	
				html = browser.page_source
				soup = BeautifulSoup(html, 'html.parser')

				td = soup.select("td.first")[0]
				time.sleep(1)
				stats = td.find_next_siblings('td')[1:]
				stats = [item.text for item in stats]
				
				player_stats['MIN'] = stats[1]
				player_stats['PTS'] = stats[2]
				player_stats['REB'] = stats[14]
				player_stats['AST'] = stats[15]	
				player_stats['FG%'] = stats[5] + '%'
				player_stats['3P%'] = stats[8] + '%'
				player_stats['FT%'] = stats[11]+ '%'
				player_stats['STL'] = stats[17]
				player_stats['BLK'] = stats[18]
				player_stats['+/-'] = stats[-1]

				display_stats =''
				reply_string = '***'+ display_name +'***'+ " stats for 2017-2018 season are the following:\n\n"
				for key in player_stats_list:
			 		display_stats = display_stats + '**'+str(key) + ':** ' + str(player_stats[key]) + '\n\n'
				
				reply_string  =reply_string + display_stats
			print(reply_string)
			# comment.reply(reply_string)
			time.sleep(600)
	# GP - 0
	# MIN - 1
	# PTS - 2''
	# FG% - 5
	# 3P% - 8
	# FT% - 11
	# REB - 14
	# AST - 15	
	# STL - 17	
	# BLK - 18
