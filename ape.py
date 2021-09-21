import requests
from bs4 import BeautifulSoup
import json
import unidecode
from database_mongo import *
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Create a datetime obj the next time we run the insertion part


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from multiprocessing.dummy import Pool as ThreadPool

# newspapers = ['tribune', 'malayalamanorama', 'telegraph', 'anandabazarpatrika', 'hindu', 'hindustantimes', 'timesofindia', 'dainikjugasankha', 'bodosa', 'loksatta', 'ajit', 'assamrising', 'arunachaltimes', 'niyomiyabarta', 'jansatta', 'i-next', 'dainandinbarta', 'sikkimexpress', 'aawaminews', 'indianexpress', 'kutchmitra', 'deccanherald', 'tripuradarpan', 'dainikkashmirtimes', 'himalayadarpan', 'financialexpress', 'businessstandard', 'deccanchronicle', 'navodayatimes', 'siasatdaily', 'rashtradoot', 'bombaysamachar', 'hitavada', 'hindustan', 'loksatta', 'udayavani', 'samagya', 'dinakaran', 'divyahimachal', 'economictimes', 'jagmarg', 'sakshi', 'adhikar', 'meghalayaguardian', 'oheraldo', 'punjabkesari', 'metrovaartha', 'aj', 'saamnatimes', 'nagalandpost', 'navgujaratsamay', 'hamaramahanagar', 'prajavani', 'millenniumpost', 'arunachalfront', 'aajkaal', 'mirror', 'gomantaktimes', 'businessline', 'kathmandupost', 'andhrajyothy', 'pratidin', 'statesman', 'lokmat', 'bartaman', 'midday', 'himalayantimes', 'aizawlpost', 'punjabitribune', 'dinamalar', 'navabharat', 'thepioneer', 'dailyhindimilap', 'navhindtimes', 'asomaditya', 'vijaykarnataka', 'keralakaumudi', 'ajirdainikbatori', 'kannadaprabha', 'rajasthanpatrika', 'samaya', 'inquilab', 'westerntimes', 'ajitsamachar', 'vijayavani', 'dainikjagran', 'prameya', 'himalibela', 'punjabijagran', 'morungexpress', 'madhyamam', 'naidunia', 'orissabhaskar', 'easternchronicle', 'dainikgomantak', 'mumbaichoufer', 'deshabhimani', 'dailythanthi', 'dainikjanambhumi', 'sakal', 'gujarattoday', 'dailyaftab', 'shillongtimes', 'dainikagradoot', 'prothomalo', 'prabhat', 'dailydesherkatha', 'amarasom', 'assamtribune', 'hindsamachar', 'dharitri', 'gujaratimidday', 'navprabha', 'purvanchalprahari', 'amarujala', 'akhbaremashriq', 'dainiksambad', 'jaihinddaily', 'eisamay', 'northeasttimes', 'navbharattimes', 'kashmiruzma', 'mathrubhumi', 'newstoday', 'tripuratimes', 'dainiknavajyoti', 'maharashtratimes', 'asomiyakhabar', 'dainikbhaskar', 'navakal', 'mizorampost', 'echoofindia', 'sandhyatimes', 'swatantravaartha', 'divyabhaskar', 'asianage', 'peopleschronicle', 'arthiklipi', 'kashmirtimes', 'himachaldastak', 'divyamarathi', 'dawnlitpost', 'poknapham', 'infoindia', 'sambad', 'salamduniya', 'ekdin', 'janmabhoomi', 'pratibadikalam', 'dainikstatesman', 'sandesh', 'dainikdabangdunia', 'dinamani', 'mawphor', 'pudhari', 'dainikprantajyoti', 'sanmarg', 'dainikvishwamitra', 'janpathsamachar', 'statetimes', 'samaydainik', 'telanganatoday', 'samaja', 'dainikherald', 'newindianexpress', 'sangaiexpress', 'namasthetelangana', 'eenadu', 'swadesh', 'prabhatkhabar', 'tarunbharat', 'activetimes', 'asomiyapratidin', 'yuvashakti', 'tripuraobserver', 'financialchronicle', 'dainiksaveratimes', 'dailyexcelsior', 'navarashtra', 'punyanagari', 'vanglaini', 'rashtriyakhabar', 'gujaratsamachar', 'sandhyakal', 'uttarbangasambad', 'yashobhumi', 'pratidinodiadaily']
newspapers = ['tribune', 'malayalamanorama', 'telegraph', 'anandabazarpatrika', 'hindu', 'hindustantimes', 'timesofindia', 'dainikjugasankha', 'loksatta', 'ajit', 'i-next', 'sikkimexpress', 'indianexpress', 'kutchmitra', 'deccanherald', 'dainikkashmirtimes', 'deccanchronicle', 'siasatdaily', 'bombaysamachar', 'hitavada', 'hindustan', 'loksatta', 'udayavani', 'dinakaran', 'divyahimachal', 'economictimes', 'sakshi', 'oheraldo', 'punjabkesari', 'navgujaratsamay', 'prajavani', 'aajkaal', 'mirror', 'businessline', 'andhrajyothy', 'pratidin', 'statesman', 'lokmat', 'bartaman', 'midday', 'punjabitribune', 'dinamalar', 'navabharat', 'navhindtimes', 'vijaykarnataka', 'keralakaumudi', 'kannadaprabha', 'rajasthanpatrika', 'inquilab', 'dainikjagran', 'madhyamam', 'naidunia', 'deshabhimani', 'dailythanthi', 'dainikjanambhumi', 'sakal', 'assamtribune', 'dharitri', 'amarujala', 'dainiksambad', 'eisamay', 'navbharattimes', 'mathrubhumi', 'dainiknavajyoti', 'maharashtratimes', 'dainikbhaskar', 'divyabhaskar', 'kashmirtimes', 'divyamarathi', 'sambad', 'sandesh', 'sanmarg', 'samaja', 'newindianexpress', 'eenadu', 'prabhatkhabar', 'asomiyapratidin', 'dailyexcelsior', 'gujaratsamachar', 'uttarbangasambad']
urls = [
		f'https://{paper}.releasemyad.com/classified-ads/matrimonial/wanted-grooms/'
		f'https://{paper}.releasemyad.com/classified-ads/matrimonial/wanted-brides/'
		]

info_list = []

def main_thread(info):
	temp_dic = {}
	try:
		temp_dic['Ad_content'] = info.span.text
		temp_dic['Ad_content_lower'] = temp_dic['Ad_content'].lower()

		temp_data = info.ul.text.strip()
		temp_data = temp_data.split("\n")
		temp_dic['Categorised_under'] = temp_data[0].split(":")[1]
		temp_dic['Newspaper_name'] = temp_data[1].split(":")[1]
		temp_dic['Published_on'] = temp_data[2].split(":")[1]
		temp_dic['Url'] = url
		insert_data_check(temp_dic)
	except Exception as e:
		print(e)

def thread(url):
	re = requests.get(url).text
	soup = BeautifulSoup(re,'lxml')
	information = soup.find_all('div',class_='ad-row')
	
	pool = ThreadPool(10)
	pool.map(main_thread, information)
	pool.close()
	pool.join()
		

if __name__=="__main__":
	paper = 
	for url in urls:
		
		page_urls = [url+str(x) for x in range(1,400)]

		pool = ThreadPool(10)
		pool.map(thread, page_urls)
		pool.close()
		pool.join()

# with open("data.json","w") as f:
# 	uni = unidecode.unidecode(json.dumps(info_list,indent=4))
# 	f.write(uni)

# hindi newspaper as well