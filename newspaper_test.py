import requests
from bs4 import BeautifulSoup

newspapers = ['tribune', 'malayalamanorama', 'telegraph', 'anandabazarpatrika', 'hindu', 'hindustantimes', 'timesofindia', 'dainikjugasankha', 'loksatta', 'ajit', 'i-next', 'sikkimexpress', 'indianexpress', 'kutchmitra', 'deccanherald', 'dainikkashmirtimes', 'deccanchronicle', 'siasatdaily', 'bombaysamachar', 'hitavada', 'hindustan', 'loksatta', 'udayavani', 'dinakaran', 'divyahimachal', 'economictimes', 'sakshi', 'oheraldo', 'punjabkesari', 'navgujaratsamay', 'prajavani', 'aajkaal', 'mirror', 'businessline', 'andhrajyothy', 'pratidin', 'statesman', 'lokmat', 'bartaman', 'midday', 'punjabitribune', 'dinamalar', 'navabharat', 'navhindtimes', 'vijaykarnataka', 'keralakaumudi', 'kannadaprabha', 'rajasthanpatrika', 'inquilab', 'dainikjagran', 'madhyamam', 'naidunia', 'deshabhimani', 'dailythanthi', 'dainikjanambhumi', 'sakal', 'assamtribune', 'dharitri', 'amarujala', 'dainiksambad', 'eisamay', 'navbharattimes', 'mathrubhumi', 'dainiknavajyoti', 'maharashtratimes', 'dainikbhaskar', 'divyabhaskar', 'kashmirtimes', 'divyamarathi', 'sambad', 'sandesh', 'sanmarg', 'samaja', 'newindianexpress', 'eenadu', 'prabhatkhabar', 'asomiyapratidin', 'dailyexcelsior', 'gujaratsamachar', 'uttarbangasambad']

for paper in newspapers:
	urls = [
				f'https://{paper}.releasemyad.com/classified-ads/matrimonial/wanted-grooms/1',
				f'https://{paper}.releasemyad.com/classified-ads/matrimonial/wanted-brides/1'
			]
	for url in urls:
		try:
			re = requests.get(url).text
			soup = BeautifulSoup(re,'lxml')
			information = soup.find_all('div',class_='ad-row')
			print(paper,information[0].span.text)
		except Exception as e:
			print(url)
			with open('test.txt','a') as f:
				f.write(str(url+'\n'+str(e)+'\n'))