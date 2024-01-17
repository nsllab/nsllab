

import os


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

# Call Django's setup to configure the settings
import django
django.setup()

# from works.models import WeeklyReport
from pages.models import Serendipity


data = {
	"table": "pages_serendipity",
	"rows":
	[
		{
			"user": "관리자",
			"subject": "CEO가 되고 싶은 사람들을 위한 7가지 조언",
			"tcp_ip": "202.31.200.137",
			"write_date": "2006-04-10 19:29:28",
			"update_date": None,
			"visit": 1410,
			"ref": "200604100001"
		},
		{
			"user": "NSL",
			"subject": "사람의 마음을 바꾸는 아홉 가지 방법",
			"tcp_ip": "202.31.200.137",
			"write_date": "2006-04-11 03:20:56",
			"update_date": None,
			"visit": 1473,
			"ref": "200604110001"
		},
		{
			"user": "관리자",
			"subject": "성공을 위한 10가지 충고",
			"tcp_ip": "202.31.200.137",
			"write_date": "2006-04-11 20:42:16",
			"update_date": None,
			"visit": 1586,
			"ref": "200604110002"
		},
		{
			"user": "dskim",
			"subject": "아인슈타인",
			"tcp_ip": "202.31.200.129",
			"write_date": "2006-05-11 16:47:34",
			"update_date": None,
			"visit": 1625,
			"ref": "200605110001"
		},
		{
			"user": "dskim",
			"subject": "긍정적 사고",
			"tcp_ip": "202.31.200.129",
			"write_date": "2006-05-11 16:48:38",
			"update_date": None,
			"visit": 1590,
			"ref": "200605110002"
		},
		{
			"user": "dskim",
			"subject": "시간 관리 잘하기(시간관리 tip120)에서 발췌",
			"tcp_ip": "202.31.200.129",
			"write_date": "2006-05-11 16:49:21",
			"update_date": None,
			"visit": 1627,
			"ref": "200605110003"
		},
		{
			"user": "dskim",
			"subject": "알바트로스",
			"tcp_ip": "202.31.200.129",
			"write_date": "2006-05-11 16:51:49",
			"update_date": None,
			"visit": 1755,
			"ref": "200605110004"
		},
		{
			"user": "dskim",
			"subject": "딕 호잇 (Dick Hoyt)",
			"tcp_ip": "202.31.137.31",
			"write_date": "2007-03-13 09:19:09",
			"update_date": None,
			"visit": 1402,
			"ref": "200703130001"
		},
		{
			"user": "dskim",
			"subject": "There are four things...",
			"tcp_ip": "202.31.137.31",
			"write_date": "2007-03-20 13:36:30",
			"update_date": None,
			"visit": 1506,
			"ref": "200703200001"
		},
		{
			"user": "dskim",
			"subject": "Dying 47-Year-Old Professor Gives Exuberant ‘Last Lecture’",
			"tcp_ip": "202.31.137.31",
			"write_date": "2007-11-23 10:50:54",
			"update_date": None,
			"visit": 1725,
			"ref": "200711230001"
		},
		{
			"user": "dskim",
			"subject": "  Habits and destiny",
			"tcp_ip": "169.237.10.220",
			"write_date": "2008-07-08 03:08:09",
			"update_date": None,
			"visit": 1520,
			"ref": "200807080001"
		},
		{
			"user": "dskim",
			"subject": "  The best and most beautiful things...",
			"tcp_ip": "169.237.10.220",
			"write_date": "2008-10-03 01:57:04",
			"update_date": None,
			"visit": 1475,
			"ref": "200810030001"
		},
		{
			"user": "dskim",
			"subject": "  Endeavor",
			"tcp_ip": "169.237.10.220",
			"write_date": "2008-10-03 03:22:35",
			"update_date": None,
			"visit": 1580,
			"ref": "200810030002"
		},
		{
			"user": "관리자",
			"subject": "  Randy Pausch's Web Site - One of My favorites",
			"tcp_ip": "169.237.10.220",
			"write_date": "2008-10-09 06:00:45",
			"update_date": None,
			"visit": 1660,
			"ref": "200810090001"
		},
		{
			"user": "관리자",
			"subject": "  What lies within us..",
			"tcp_ip": "169.237.10.220",
			"write_date": "2008-10-10 02:37:41",
			"update_date": None,
			"visit": 1635,
			"ref": "200810100001"
		},
		{
			"user": "관리자",
			"subject": "  ‘highly creative’",
			"tcp_ip": "169.237.10.220",
			"write_date": "2009-01-21 06:48:06",
			"update_date": None,
			"visit": 1665,
			"ref": "200901210001"
		},
		{
			"user": "관리자",
			"subject": "  &quotLife is.........&quot",
			"tcp_ip": "202.31.137.31",
			"write_date": "2009-05-17 20:16:45",
			"update_date": None,
			"visit": 1439,
			"ref": "200905170001"
		},
		{
			"user": "관리자",
			"subject": "  What lies witin us..",
			"tcp_ip": "202.31.137.31",
			"write_date": "2009-10-11 19:42:05",
			"update_date": None,
			"visit": 1597,
			"ref": "200910110001"
		},
		{
			"user": "D.-S. Kim",
			"subject": "To know is nothing at all",
			"tcp_ip": "210.223.130.67",
			"write_date": "2010-04-25 17:50:38",
			"update_date": None,
			"visit": 1514,
			"ref": "201004250001"
		},
		{
			"user": "D.-S. Kim",
			"subject": "From Thomas Edison",
			"tcp_ip": "210.223.130.67",
			"write_date": "2010-04-25 17:56:42",
			"update_date": None,
			"visit": 1541,
			"ref": "201004250002"
		},
		{
			"user": "D.-S.Kim",
			"subject": "Minds are like Parachutes.",
			"tcp_ip": "210.223.130.74",
			"write_date": "2010-05-15 23:38:31",
			"update_date": None,
			"visit": 1559,
			"ref": "201005150001"
		},
		{
			"user": "D.-S. Kim",
			"subject": "-Selected paragraph in the middle of &quotTuesdays with Morrie&quot",
			"tcp_ip": "202.31.137.66",
			"write_date": "2010-11-29 21:19:50",
			"update_date": None,
			"visit": 1401,
			"ref": "201011290001"
		},
		{
			"user": "관리자",
			"subject": "Success means",
			"tcp_ip": "202.31.137.66",
			"write_date": "2011-01-21 11:13:26",
			"update_date": None,
			"visit": 1316,
			"ref": "201101210001"
		},
		{
			"user": "관리자",
			"subject": "Steve Jobs Stanford Commencement Speech with scripts",
			"tcp_ip": "202.31.137.66",
			"write_date": "2011-10-06 14:03:46",
			"update_date": None,
			"visit": 1224,
			"ref": "201110060001"
		},
		{
			"user": "관리자",
			"subject": "The only choice is how.",
			"tcp_ip": "202.31.137.66",
			"write_date": "2011-12-06 11:43:10",
			"update_date": None,
			"visit": 1007,
			"ref": "201112060001"
		},
		{
			"user": "관리자",
			"subject": "A soul generated user love",
			"tcp_ip": "202.31.137.38",
			"write_date": "2011-12-08 13:00:15",
			"update_date": None,
			"visit": 960,
			"ref": "201112080001"
		},
		{
			"user": "관리자",
			"subject": "Obstacles are those frightful things you see..",
			"tcp_ip": "202.31.137.167",
			"write_date": "2011-12-09 14:03:28",
			"update_date": None,
			"visit": 1015,
			"ref": "201112090001"
		},
		{
			"user": "아기 프라세티아디",
			"subject": "True wisdom comes to each of us when...",
			"tcp_ip": "202.31.137.197",
			"write_date": "2011-12-12 12:13:20",
			"update_date": None,
			"visit": 1023,
			"ref": "201112120001"
		},
		{
			"user": "탄",
			"subject": "There are two primary choices in life...",
			"tcp_ip": "202.31.137.29",
			"write_date": "2011-12-16 20:55:31",
			"update_date": None,
			"visit": 1006,
			"ref": "201112160001"
		},
		{
			"user": "관리자",
			"subject": "If we knew what it was we were doing..",
			"tcp_ip": "202.31.137.167",
			"write_date": "2011-12-24 12:28:05",
			"update_date": None,
			"visit": 1039,
			"ref": "201112240001"
		},
		{
			"user": "관리자",
			"subject": "The important thing is not to stop questioning..",
			"tcp_ip": "202.31.137.167",
			"write_date": "2011-12-31 11:53:58",
			"update_date": None,
			"visit": 968,
			"ref": "201112310001"
		},
		{
			"user": "관리자",
			"subject": "Any man who reads too much and uses his own brain too little...",
			"tcp_ip": "202.31.137.167",
			"write_date": "2012-01-07 14:09:09",
			"update_date": None,
			"visit": 883,
			"ref": "201201070001"
		},
		{
			"user": "관리자",
			"subject": "Nothing can stop the man with the right mental attitude...",
			"tcp_ip": "202.31.137.167",
			"write_date": "2012-01-14 20:25:28",
			"update_date": None,
			"visit": 900,
			"ref": "201201140001"
		},
		{
			"user": "관리자",
			"subject": "Try not to become a man of success...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-01-27 14:03:43",
			"update_date": None,
			"visit": 994,
			"ref": "201201270001"
		},
		{
			"user": "관리자",
			"subject": "Imagination is more important than knowledge...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-02-03 22:05:34",
			"update_date": None,
			"visit": 926,
			"ref": "201202030001"
		},
		{
			"user": "관리자",
			"subject": "I Love Living Life. I Am Happy. -Nick Vujicic",
			"tcp_ip": "202.31.137.30",
			"write_date": "2012-02-20 14:40:53",
			"update_date": None,
			"visit": 966,
			"ref": "201202200001"
		},
		{
			"user": "관리자",
			"subject": "Everything Happens For A Reason",
			"tcp_ip": "202.31.137.153",
			"write_date": "2012-03-02 14:50:11",
			"update_date": None,
			"visit": 913,
			"ref": "201203020001"
		},
		{
			"user": "관리자",
			"subject": "If A equals success, then the formula is A=X+Y+Z...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-03-16 22:28:45",
			"update_date": None,
			"visit": 911,
			"ref": "201203160001"
		},
		{
			"user": "관리자",
			"subject": "Do you want the Littleprince?",
			"tcp_ip": "202.31.137.36",
			"write_date": "2012-03-19 11:36:36",
			"update_date": None,
			"visit": 869,
			"ref": "201203190001"
		},
		{
			"user": "관리자",
			"subject": "A person who never made a mistake never tried anything new",
			"tcp_ip": "202.31.137.153",
			"write_date": "2012-04-02 17:47:28",
			"update_date": None,
			"visit": 841,
			"ref": "201204020001"
		},
		{
			"user": "관리자",
			"subject": "The Star - Alphonse Daudet -",
			"tcp_ip": "192.168.222.139",
			"write_date": "2012-04-04 20:56:29",
			"update_date": None,
			"visit": 18148,
			"ref": "201204040001"
		},
		{
			"user": "관리자",
			"subject": "Doing easily what others find difficult is talent; doing what is impossible for talent is genius.",
			"tcp_ip": "202.31.137.121",
			"write_date": "2012-04-23 16:02:23",
			"update_date": None,
			"visit": 795,
			"ref": "201204230001"
		},
		{
			"user": "관리자",
			"subject": "Scientific research is based on the idea that ..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-04-29 15:42:55",
			"update_date": None,
			"visit": 730,
			"ref": "201204290001"
		},
		{
			"user": "관리자",
			"subject": "The release of atom power has changed everything except our way of thinking...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-05-14 13:20:39",
			"update_date": None,
			"visit": 777,
			"ref": "201205140001"
		},
		{
			"user": "관리자",
			"subject": "Do not worry about your difficulties in Mathematics..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-06-11 10:25:34",
			"update_date": None,
			"visit": 744,
			"ref": "201206110001"
		},
		{
			"user": "관리자",
			"subject": "Beauty is not in the face...",
			"tcp_ip": "202.31.137.122",
			"write_date": "2012-06-14 10:41:55",
			"update_date": None,
			"visit": 740,
			"ref": "201206140001"
		},
		{
			"user": "관리자",
			"subject": "For to win one hundred victories...",
			"tcp_ip": "202.31.137.122",
			"write_date": "2012-06-18 10:08:30",
			"update_date": None,
			"visit": 765,
			"ref": "201206180001"
		},
		{
			"user": "관리자",
			"subject": "It would be better if you begin to teach others...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-07-02 12:46:22",
			"update_date": None,
			"visit": 749,
			"ref": "201207020001"
		},
		{
			"user": "관리자",
			"subject": "Truth does not become more true user...",
			"tcp_ip": "202.31.137.122",
			"write_date": "2012-07-16 16:57:27",
			"update_date": None,
			"visit": 775,
			"ref": "201207160001"
		},
		{
			"user": "관리자",
			"subject": "The only way to do great work is to love what you do.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-07-30 09:51:31",
			"update_date": None,
			"visit": 693,
			"ref": "201207300001"
		},
		{
			"user": "관리자",
			"subject": "When our ambition is bounded, it leads to work joyfully..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-08-08 01:25:17",
			"update_date": None,
			"visit": 674,
			"ref": "201208080001"
		},
		{
			"user": "관리자",
			"subject": "Education is what remains after one has forgotten everything..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-08-13 20:20:56",
			"update_date": None,
			"visit": 689,
			"ref": "201208130001"
		},
		{
			"user": "관리자",
			"subject": "We can't solve problems user using the same kind of thinking...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-08-20 15:02:51",
			"update_date": None,
			"visit": 667,
			"ref": "201208200001"
		},
		{
			"user": "관리자",
			"subject": "An education isn't how much you have committed to memory..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-08-27 11:50:08",
			"update_date": None,
			"visit": 684,
			"ref": "201208270001"
		},
		{
			"user": "관리자",
			"subject": "Any intelligent fool can make things bigger and more complex...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-09-02 22:22:15",
			"update_date": None,
			"visit": 650,
			"ref": "201209020001"
		},
		{
			"user": "관리자",
			"subject": "A man should look for what is, and not for what he thinks should be.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-09-09 10:50:43",
			"update_date": None,
			"visit": 660,
			"ref": "201209090001"
		},
		{
			"user": "관리자",
			"subject": "Character is like a tree and reputation like a shadow",
			"tcp_ip": "202.31.137.156",
			"write_date": "2012-09-17 11:10:34",
			"update_date": None,
			"visit": 681,
			"ref": "201209170001"
		},
		{
			"user": "관리자",
			"subject": "Learn from yesterday, live for today, hope for tomorrow..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-09-24 13:08:32",
			"update_date": None,
			"visit": 769,
			"ref": "201209240001"
		},
		{
			"user": "관리자",
			"subject": "Every day I remind myself that my inner and outer life..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-10-02 10:08:05",
			"update_date": None,
			"visit": 669,
			"ref": "201210020001"
		},
		{
			"user": "관리자",
			"subject": "Science is a wonderful thing if one does not have to..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-10-08 19:42:30",
			"update_date": None,
			"visit": 689,
			"ref": "201210080001"
		},
		{
			"user": "관리자",
			"subject": "It's not that I'm so smart, it's just that I stay with..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-10-15 13:00:00",
			"update_date": None,
			"visit": 684,
			"ref": "201210150001"
		},
		{
			"user": "관리자",
			"subject": "Anyone who doesn't take truth seriously in small matters..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-10-22 11:20:56",
			"update_date": None,
			"visit": 673,
			"ref": "201210220001"
		},
		{
			"user": "관리자",
			"subject": "If you can't explain it simply, you don't understand..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-10-29 09:48:56",
			"update_date": None,
			"visit": 725,
			"ref": "201210290001"
		},
		{
			"user": "관리자",
			"subject": "The only thing that interferes with my learning..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-11-06 18:58:12",
			"update_date": None,
			"visit": 684,
			"ref": "201211060001"
		},
		{
			"user": "관리자",
			"subject": "Great spirits have always encountered violent opposition..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-11-12 10:08:29",
			"update_date": None,
			"visit": 691,
			"ref": "201211120001"
		},
		{
			"user": "관리자",
			"subject": "Great spirits have often encountered violent..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-11-19 11:46:57",
			"update_date": None,
			"visit": 721,
			"ref": "201211190001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "The most beautiful thing we can experience is..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-11-26 10:40:47",
			"update_date": None,
			"visit": 730,
			"ref": "201211260001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "No problem can be solved from the same level of consciousness that created it.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-12-17 07:43:10",
			"update_date": None,
			"visit": 709,
			"ref": "201212170001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "Try not to become a man of success but rather to become a man of value.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2012-12-24 08:57:12",
			"update_date": None,
			"visit": 664,
			"ref": "201212240001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "It would be better if you begin to teach others only after you yourself have learned something...",
			"tcp_ip": "",
			"write_date": "2013-01-02 10:18:31",
			"update_date": "2013-01-02 10:19:17",
			"visit": 662,
			"ref": "201301020001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "People like us, who believe in physics, know that the distinction..",
			"tcp_ip": "202.31.137.198",
			"write_date": "2013-01-08 21:55:54",
			"update_date": None,
			"visit": 620,
			"ref": "201301080001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "The secret to creativity is knowing how to hide your sources...",
			"tcp_ip": "202.31.137.198",
			"write_date": "2013-01-15 13:17:43",
			"update_date": None,
			"visit": 674,
			"ref": "201301150001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "The true sign of intelligence is not knowledge but imagination.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2013-01-21 19:21:08",
			"update_date": None,
			"visit": 691,
			"ref": "201301210001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "Intellectuals solve problems; geniuses prevent them.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2013-01-28 22:44:07",
			"update_date": None,
			"visit": 619,
			"ref": "201301280001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "It&#39;s not that I&#39;m so smart, it&#39;s just that I stay with problems longer.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2013-02-04 14:23:05",
			"update_date": None,
			"visit": 679,
			"ref": "201302040001"
		},
		{
			"user": "Tung Thanh Le",
			"subject": "A theory can be proved user experiment; but no path leads from experiment to the birth of a theory.",
			"tcp_ip": "202.31.137.198",
			"write_date": "2013-02-14 19:52:32",
			"update_date": None,
			"visit": 682,
			"ref": "201302140001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Education is what remains after one has forgotten everything he learned in school.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-02-19 19:52:45",
			"update_date": None,
			"visit": 648,
			"ref": "201302190001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Live as if you were to die tomorrow. Learn as if you were to live forever.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-02-25 09:06:16",
			"update_date": None,
			"visit": 655,
			"ref": "201302250001"
		},
		{
			"user": "Tran Nhon",
			"subject": "The true sign of intelligence is not knowledge but imagination.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-03-05 21:49:51",
			"update_date": None,
			"visit": 651,
			"ref": "201303050001"
		},
		{
			"user": "Tran Nhon",
			"subject": "In the book of life, the answers aren&#39;t in the back.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-03-11 15:07:48",
			"update_date": None,
			"visit": 686,
			"ref": "201303110001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Intelligence is the wife, imagination is the mistress, memory is the servant.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-03-18 10:35:06",
			"update_date": None,
			"visit": 691,
			"ref": "201303180001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Education does not end at any point in our lives; it is an ongoing journey to be carried with us everyday throughout our lives.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-03-25 11:11:56",
			"update_date": None,
			"visit": 709,
			"ref": "201303250001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Every truth has four corners: as a teacher I give you one corner, and it is for you to find the other three.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-04-01 10:22:07",
			"update_date": None,
			"visit": 658,
			"ref": "201304010001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Love is the triumph of imagination over intelligence.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-04-09 09:52:25",
			"update_date": None,
			"visit": 647,
			"ref": "201304090001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Success is the ability to go from failure to failure without losing your enthusiasm.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-04-16 00:23:37",
			"update_date": None,
			"visit": 724,
			"ref": "201304160001"
		},
		{
			"user": "Tran Nhon",
			"subject": "A discovery is said to be an accident meeting a prepared mind.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-04-24 21:25:56",
			"update_date": None,
			"visit": 685,
			"ref": "201304240001"
		},
		{
			"user": "Tran Nhon",
			"subject": "The first step to getting the things you want out of life is this: Decide what you want.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-05-06 23:52:48",
			"update_date": None,
			"visit": 646,
			"ref": "201305060001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-05-20 09:55:55",
			"update_date": None,
			"visit": 670,
			"ref": "201305200001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Do something every day that you don&#39;t want to do; this is the golden rule for acquiring the habit of doing your duty without pain.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-06-04 16:32:00",
			"update_date": None,
			"visit": 708,
			"ref": "201306040001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Great works are performed, not user strength, but user perseverance.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-06-11 09:44:04",
			"update_date": None,
			"visit": 651,
			"ref": "201306110001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Success usually comes to those who are too busy to be looking for it.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-06-18 10:50:01",
			"update_date": None,
			"visit": 670,
			"ref": "201306180001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Scientific research is based on the idea that everything that takes place is determined user laws of nature, and therefore this holds for the action of people. For this reason, a research scientist will hardly be inclined to be",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-07-11 02:31:43",
			"update_date": None,
			"visit": 894,
			"ref": "201307110001"
		},
		{
			"user": "Tran Nhon",
			"subject": "In an inspirational and practical book, Matt explores the ‘logic of magic’ at work and gives us new tricks to make it happen! Read only if you are ready to behave accordingly!",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-07-16 20:58:34",
			"update_date": None,
			"visit": 709,
			"ref": "201307160001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Men love to wonder, and that is the seed of science.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-08-12 14:19:18",
			"update_date": None,
			"visit": 723,
			"ref": "201308120001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Great works are performed, not user strength, but user perseverance.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-08-19 13:42:29",
			"update_date": None,
			"visit": 659,
			"ref": "201308190001"
		},
		{
			"user": "Tran Nhon",
			"subject": "There is only one success - to be able to spend your life in your own way.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-08-26 10:59:30",
			"update_date": None,
			"visit": 668,
			"ref": "201308260001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Every science begins as philosophy and ends as art.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-09-04 09:24:10",
			"update_date": None,
			"visit": 678,
			"ref": "201309040001"
		},
		{
			"user": "Tran Nhon",
			"subject": "The beginning is the most important part of the work.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-09-09 14:57:12",
			"update_date": None,
			"visit": 646,
			"ref": "201309090001"
		},
		{
			"user": "Tran Nhon",
			"subject": "Accomplishment will prove to be a journey, not a destination.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2013-09-16 10:16:35",
			"update_date": None,
			"visit": 658,
			"ref": "201309160001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "We learn only from those we love.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-09-23 10:09:01",
			"update_date": None,
			"visit": 632,
			"ref": "201309230001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "The man who follows the crowd will usually get no further than the crowd. The man  who walks alone is likely to find himself in places no one has ever been.",
			"tcp_ip": "",
			"write_date": "2013-09-30 09:57:29",
			"update_date": "2013-09-30 09:57:50",
			"visit": 645,
			"ref": "201309300001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "You are what you think. You are what you go for. You are what you do.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-10-07 11:28:11",
			"update_date": None,
			"visit": 623,
			"ref": "201310070001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Life&#39;s battles don&#39;t always go",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-10-14 16:53:11",
			"update_date": None,
			"visit": 625,
			"ref": "201310140001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Why did I want to win? Because I didn&#39;t want to lose!",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-10-21 09:55:25",
			"update_date": None,
			"visit": 644,
			"ref": "201310210001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "The elevator to success is out of order. You&#39;ll have to use the stairs... one step at a time.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-10-28 13:51:22",
			"update_date": None,
			"visit": 647,
			"ref": "201310280001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "A proud man is always looking down on things and people; and, of course, as long as you are looking down, you cannot see something that is above you",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-11-02 15:14:03",
			"update_date": None,
			"visit": 634,
			"ref": "201311020001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Kites rise highest against the wind, not with it.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-11-11 10:10:33",
			"update_date": None,
			"visit": 687,
			"ref": "201311110001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Everyone is trying to accomplish something big , not  realizing that life is made up of little things.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-11-19 10:54:05",
			"update_date": None,
			"visit": 645,
			"ref": "201311190001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Every adversity carries with it the seed of an equal or  greater benefit.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2013-11-25 17:20:34",
			"update_date": None,
			"visit": 659,
			"ref": "201311250001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "The slogan &#34; Press on &#34; has solved and always will solve the problems of human race.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2013-12-02 19:53:08",
			"update_date": None,
			"visit": 655,
			"ref": "201312020001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "It always seems impossible until it&#39;s done",
			"tcp_ip": "202.31.137.112",
			"write_date": "2013-12-09 19:29:24",
			"update_date": None,
			"visit": 692,
			"ref": "201312090001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Nothing is really over until the moment you stop trying.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2013-12-15 12:35:54",
			"update_date": None,
			"visit": 677,
			"ref": "201312150001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Nothing ever achieve without enthusiasm.",
			"tcp_ip": "202.31.137.71",
			"write_date": "2013-12-28 16:22:24",
			"update_date": None,
			"visit": 633,
			"ref": "201312280001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Do all the good you can",
			"tcp_ip": "202.31.137.71",
			"write_date": "2013-12-28 16:25:03",
			"update_date": None,
			"visit": 630,
			"ref": "201312280002"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "If you don&#39;t like something, change it. If you can&#39;t change it, change your attitude. Don&#39;t complain.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-01-07 12:23:02",
			"update_date": None,
			"visit": 672,
			"ref": "201401070001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Everything that is happening at this moment is a result  of the choices you&#39;ve made in the past.",
			"tcp_ip": "",
			"write_date": "2014-01-13 16:07:25",
			"update_date": "2014-01-13 16:07:45",
			"visit": 672,
			"ref": "201401130001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "The important thing is not to stop questioning.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-01-20 15:00:40",
			"update_date": None,
			"visit": 729,
			"ref": "201401200001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Be wise in the use of time",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-01-27 10:25:10",
			"update_date": None,
			"visit": 775,
			"ref": "201401270001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Life is measured user thought and action, not user time.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-02-03 15:50:46",
			"update_date": None,
			"visit": 758,
			"ref": "201402030001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "A heart to resolve, a head to contrive, and two hands to  execute.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-02-10 15:37:44",
			"update_date": None,
			"visit": 802,
			"ref": "201402100001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "The great pleasure in life is doing what people say you  cannot do.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-02-19 23:11:10",
			"update_date": None,
			"visit": 618,
			"ref": "201402190001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Don&#39;t look down. If you have something you must do,  then look forward.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-02-24 20:00:30",
			"update_date": None,
			"visit": 766,
			"ref": "201402240001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Failure doesn&#39;t mean that you can&#39;t do anything,  but simply that you can learn one more thing.",
			"tcp_ip": "202.31.137.112",
			"write_date": "2014-03-03 16:11:23",
			"update_date": None,
			"visit": 691,
			"ref": "201403030001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "The higher your energy level, the more efficient your body.",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-03-10 20:44:43",
			"update_date": None,
			"visit": 766,
			"ref": "201403100001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "The best way to predict future is to create it.",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-03-17 10:28:33",
			"update_date": None,
			"visit": 647,
			"ref": "201403170001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Success is getting what you want. Happiness is wanting what you get.",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-03-24 17:07:39",
			"update_date": None,
			"visit": 732,
			"ref": "201403240001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Strive not to be a success, but rather to be of value.",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-03-31 13:52:21",
			"update_date": None,
			"visit": 754,
			"ref": "201403310001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Conquering any difficulty always gives one a secret joy",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-04-07 20:19:23",
			"update_date": None,
			"visit": 713,
			"ref": "201404070001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "I find my greatest pleasure, and so my reward",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-04-15 00:09:42",
			"update_date": None,
			"visit": 722,
			"ref": "201404150001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Develop success from failures",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-04-21 21:25:38",
			"update_date": None,
			"visit": 700,
			"ref": "201404210001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "People rarely succeed unless...",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-04-28 10:30:46",
			"update_date": None,
			"visit": 709,
			"ref": "201404280001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "To succeed, jump as quickly at opportunities as you do at conclusions.",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-05-06 16:39:31",
			"update_date": None,
			"visit": 816,
			"ref": "201405060001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "You are forgiven for your happiness and your successes only if ...",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-05-12 20:25:29",
			"update_date": None,
			"visit": 820,
			"ref": "201405120001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "For success, attitude is equally as important as ability",
			"tcp_ip": "202.31.137.157",
			"write_date": "2014-05-18 23:56:56",
			"update_date": None,
			"visit": 782,
			"ref": "201405180001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "All successful people men and women are big dreamers.",
			"tcp_ip": "202.31.139.217",
			"write_date": "2014-07-20 14:41:37",
			"update_date": None,
			"visit": 2543,
			"ref": "201407200001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Successful people are always looking for opportunities to help others.",
			"tcp_ip": "202.31.137.137",
			"write_date": "2014-07-28 10:35:14",
			"update_date": None,
			"visit": 662,
			"ref": "201407280001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Do not sleep on your victory!",
			"tcp_ip": "202.31.137.13",
			"write_date": "2014-08-04 10:07:46",
			"update_date": None,
			"visit": 708,
			"ref": "201408040001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Success is not final, failure is not fatal",
			"tcp_ip": "202.31.137.13",
			"write_date": "2014-08-21 22:09:30",
			"update_date": None,
			"visit": 740,
			"ref": "201408210001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "If you want to achieve things in life..",
			"tcp_ip": "202.31.137.13",
			"write_date": "2014-09-01 21:18:29",
			"update_date": None,
			"visit": 683,
			"ref": "201409010001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "If at first you don&#39;t succeed, try, try again.",
			"tcp_ip": "202.31.137.13",
			"write_date": "2014-10-13 14:18:10",
			"update_date": None,
			"visit": 649,
			"ref": "201410130001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "I honestly think it is better to be a failure at something you love",
			"tcp_ip": "202.31.137.13",
			"write_date": "2014-10-27 10:23:57",
			"update_date": None,
			"visit": 709,
			"ref": "201410270001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Formula for success",
			"tcp_ip": "202.31.137.13",
			"write_date": "2014-11-03 10:27:40",
			"update_date": None,
			"visit": 642,
			"ref": "201411030001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Formal education will make you a living; self-education will make you a fortune.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2014-11-10 11:46:16",
			"update_date": None,
			"visit": 664,
			"ref": "201411100001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Flaming enthusiasm, backed up user horse sense and persistence, is the quality that most frequently makes for success.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2014-11-17 18:15:54",
			"update_date": None,
			"visit": 646,
			"ref": "201411170001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Don&#39;t aim for success if you want it; just do what you love and believe in, and it will come naturally.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2014-11-24 11:15:13",
			"update_date": None,
			"visit": 708,
			"ref": "201411240001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Diligence is the mother of good fortune",
			"tcp_ip": "",
			"write_date": "2014-12-02 16:08:07",
			"update_date": "2014-12-02 16:08:22",
			"visit": 688,
			"ref": "201412020001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "After I won the Oscar, my salary doubled..",
			"tcp_ip": "202.31.137.196",
			"write_date": "2014-12-08 10:32:14",
			"update_date": None,
			"visit": 695,
			"ref": "201412080001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Watch a cat when it enters a room for the first time",
			"tcp_ip": "202.31.137.196",
			"write_date": "2014-12-23 09:53:30",
			"update_date": None,
			"visit": 586,
			"ref": "201412230001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "If you set your goals ridiculously high and it&#39;s a failure, you will fail above everyone else&#39;s success.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2014-12-29 10:45:55",
			"update_date": None,
			"visit": 657,
			"ref": "201412290001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Success usually comes to those who are too busy to be looking for it.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-01-05 10:29:50",
			"update_date": None,
			"visit": 606,
			"ref": "201501050001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Things work out best for those who make the best of how things work out.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-01-12 10:56:48",
			"update_date": None,
			"visit": 632,
			"ref": "201501120001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Entrepreneurs average 3.8 failures before final success.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-01-19 10:04:46",
			"update_date": None,
			"visit": 600,
			"ref": "201501190001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "If you are not willing to risk the usual",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-01-26 10:09:08",
			"update_date": None,
			"visit": 660,
			"ref": "201501260001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Take up one idea.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-02-02 09:20:57",
			"update_date": None,
			"visit": 652,
			"ref": "201502020001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "All our dreams can come true if..",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-02-09 11:17:11",
			"update_date": None,
			"visit": 1002,
			"ref": "201502090001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Great spirits have often encountered violent opposition from weak minds.",
			"tcp_ip": "113.177.110.131",
			"write_date": "2015-02-18 16:17:44",
			"update_date": None,
			"visit": 632,
			"ref": "201502180001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Intelligence is the wife....",
			"tcp_ip": "113.168.15.202",
			"write_date": "2015-02-24 10:23:42",
			"update_date": None,
			"visit": 711,
			"ref": "201502240001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Success is walking from failure to failure with no loss of enthusiasm.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-03-02 09:26:01",
			"update_date": None,
			"visit": 701,
			"ref": "201503020001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Whenever you see a successful person",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-03-09 09:55:01",
			"update_date": None,
			"visit": 708,
			"ref": "201503090001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Success is inner peace",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-03-16 09:58:32",
			"update_date": None,
			"visit": 645,
			"ref": "201503160001"
		},
		{
			"user": "Tran Minh Phuong",
			"subject": "Great minds discuss ideas",
			"tcp_ip": "202.31.137.196",
			"write_date": "2015-03-23 09:56:49",
			"update_date": None,
			"visit": 614,
			"ref": "201503230001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "A successful man",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-03-30 11:13:21",
			"update_date": None,
			"visit": 643,
			"ref": "201503300001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "The whole secret of a successful life...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-04-06 10:03:53",
			"update_date": None,
			"visit": 735,
			"ref": "201504060001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Success is...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-04-13 08:33:46",
			"update_date": None,
			"visit": 597,
			"ref": "201504130001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "If you can&#39;t...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-04-20 10:07:03",
			"update_date": None,
			"visit": 724,
			"ref": "201504200001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Start where you are",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-04-27 17:24:54",
			"update_date": None,
			"visit": 735,
			"ref": "201504270001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "I find that...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-05-04 10:04:51",
			"update_date": None,
			"visit": 703,
			"ref": "201505040001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "The starting point",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-05-11 10:23:37",
			"update_date": None,
			"visit": 638,
			"ref": "201505110001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "The only place where...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-05-18 09:25:27",
			"update_date": None,
			"visit": 627,
			"ref": "201505180001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "I find that...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-05-25 21:36:03",
			"update_date": None,
			"visit": 641,
			"ref": "201505250001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "If you genuinely want something...",
			"tcp_ip": "",
			"write_date": "2015-06-01 10:40:38",
			"update_date": "2015-06-01 10:42:07",
			"visit": 634,
			"ref": "201506010001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Motivation is...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-06-08 10:13:35",
			"update_date": None,
			"visit": 4272,
			"ref": "201506080001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "To be successful...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-06-15 08:47:59",
			"update_date": None,
			"visit": 636,
			"ref": "201506150001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Many of life&#39;s failures are...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-06-22 11:05:23",
			"update_date": None,
			"visit": 632,
			"ref": "201506220001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Always bear in mind that...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-06-29 10:23:58",
			"update_date": None,
			"visit": 624,
			"ref": "201506290001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Successful and unsuccessful people...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-07-06 09:53:37",
			"update_date": None,
			"visit": 691,
			"ref": "201507060001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Would you like me to give you a formula for success?",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-07-13 09:14:46",
			"update_date": None,
			"visit": 675,
			"ref": "201507130001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Logic will get you from...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-07-27 11:05:29",
			"update_date": None,
			"visit": 666,
			"ref": "201507270001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Successful people do...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-08-03 09:35:26",
			"update_date": None,
			"visit": 613,
			"ref": "201508030001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Twenty years from now...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-08-10 09:13:33",
			"update_date": None,
			"visit": 664,
			"ref": "201508100001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Take up one idea...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-08-17 11:05:33",
			"update_date": None,
			"visit": 657,
			"ref": "201508170001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Things work out best for...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-08-24 10:08:43",
			"update_date": None,
			"visit": 675,
			"ref": "201508240001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "All our dreams can come true if...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-08-31 09:35:12",
			"update_date": None,
			"visit": 592,
			"ref": "201508310001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Successful people do...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-09-07 09:53:12",
			"update_date": None,
			"visit": 634,
			"ref": "201509070001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Try not to become...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-09-14 09:40:22",
			"update_date": None,
			"visit": 679,
			"ref": "201509140001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "In my experience, there is only one motivation...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-09-21 10:18:46",
			"update_date": None,
			"visit": 660,
			"ref": "201509210001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "If you genuinely want something...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-09-30 09:47:55",
			"update_date": None,
			"visit": 678,
			"ref": "201509300001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Your work is going to fill a large part of your life...",
			"tcp_ip": "59.151.215.100",
			"write_date": "2015-10-05 09:31:26",
			"update_date": None,
			"visit": 729,
			"ref": "201510050001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Without passion, you don’t have energy.",
			"tcp_ip": "",
			"write_date": "2015-10-12 11:02:53",
			"update_date": "2015-10-12 11:04:17",
			"visit": 725,
			"ref": "201510120001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "If you want to succeed...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-10-19 10:31:42",
			"update_date": None,
			"visit": 637,
			"ref": "201510190001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Motivation is what gets you started...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-10-26 10:29:41",
			"update_date": None,
			"visit": 732,
			"ref": "201510260001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Whenever you see a successful person...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-11-02 10:09:30",
			"update_date": None,
			"visit": 684,
			"ref": "201511020001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Patience is a key element of success",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-11-09 10:49:35",
			"update_date": None,
			"visit": 705,
			"ref": "201511090001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Innovation distinguishes...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-11-16 03:09:38",
			"update_date": None,
			"visit": 623,
			"ref": "201511160001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Never give up.",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-11-23 10:16:51",
			"update_date": None,
			"visit": 644,
			"ref": "201511230001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "If you want to make a permanent change...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-11-30 10:31:48",
			"update_date": None,
			"visit": 861,
			"ref": "201511300001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "The distance between insanity and genius...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-12-07 11:10:17",
			"update_date": None,
			"visit": 919,
			"ref": "201512070001"
		},
		{
			"user": "Le Anh Minh",
			"subject": "Happiness lies in...",
			"tcp_ip": "202.31.137.36",
			"write_date": "2015-12-14 11:00:36",
			"update_date": None,
			"visit": 1050,
			"ref": "201512140001"
		},
		{
			"user": "관리자",
			"subject": "Everything has a purpose",
			"tcp_ip": "",
			"write_date": "2016-06-03 12:12:16",
			"update_date": "2016-06-04 21:30:10",
			"visit": 599,
			"ref": "201606030001"
		},
		{
			"user": "관리자",
			"subject": "Innovation is a key",
			"tcp_ip": "",
			"write_date": "2016-06-04 21:38:07",
			"update_date": "2016-06-10 15:08:17",
			"visit": 756,
			"ref": "201606040001"
		},
		{
			"user": "관리자",
			"subject": "That is why it is called the present-Albert Einstein Quotes",
			"tcp_ip": "202.31.137.119",
			"write_date": "2016-06-09 18:57:32",
			"update_date": None,
			"visit": 720,
			"ref": "201606090001"
		},
		{
			"user": "관리자",
			"subject": "&#34;If you cannot do great things, do small things in a great way&#34;",
			"tcp_ip": "",
			"write_date": "2016-06-10 15:06:41",
			"update_date": "2016-06-10 15:13:40",
			"visit": 644,
			"ref": "201606100001"
		},
		{
			"user": "김승한",
			"subject": "&#34;Have more than thou showest, speak less than thou knowest.&#34;",
			"tcp_ip": "202.31.137.116",
			"write_date": "2016-06-17 13:11:56",
			"update_date": None,
			"visit": 857,
			"ref": "201606170001"
		},
		{
			"user": "관리자",
			"subject": "To imagine is everything, to know is nothing at all",
			"tcp_ip": "",
			"write_date": "2016-06-17 13:18:58",
			"update_date": "2016-06-17 13:19:20",
			"visit": 731,
			"ref": "201606170002"
		},
		{
			"user": "김다혜",
			"subject": "The only joy in the world",
			"tcp_ip": "202.31.137.138",
			"write_date": "2016-07-01 15:50:22",
			"update_date": None,
			"visit": 705,
			"ref": "201607010001"
		},
		{
			"user": "Alif Akbar Pranata",
			"subject": "Stay hungry, stay foolish",
			"tcp_ip": "202.31.201.34",
			"write_date": "2016-07-08 13:52:40",
			"update_date": None,
			"visit": 703,
			"ref": "201607080001"
		},
		{
			"user": "관리자",
			"subject": "I am not here to be average, I am here to be awesome",
			"tcp_ip": "202.31.137.34",
			"write_date": "2016-07-15 13:52:43",
			"update_date": None,
			"visit": 679,
			"ref": "201607150001"
		},
		{
			"user": "Nguyen Bach Long",
			"subject": "All our dreams can come true, if we have the courage to pursue them.",
			"tcp_ip": "202.31.137.161",
			"write_date": "2016-07-22 13:27:14",
			"update_date": None,
			"visit": 740,
			"ref": "201607220001"
		},
		{
			"user": "Gereziher",
			"subject": "Remember, today is the tomorrow you worried about yesterday (Dale Carnegie)",
			"tcp_ip": "202.31.137.115",
			"write_date": "2016-07-28 21:41:48",
			"update_date": None,
			"visit": 756,
			"ref": "201607280001"
		},
		{
			"user": "관리자",
			"subject": "Never forget your past. It&#39;s your best teacher.",
			"tcp_ip": "202.31.137.119",
			"write_date": "2016-08-05 11:35:04",
			"update_date": None,
			"visit": 818,
			"ref": "201608050001"
		},
		{
			"user": "임지철",
			"subject": "The letter of Darrel K.Royal",
			"tcp_ip": "",
			"write_date": "2016-08-08 12:13:29",
			"update_date": "2016-08-08 12:23:43",
			"visit": 1174,
			"ref": "201608080001"
		},
		{
			"user": "민동주",
			"subject": "There are no Skill Challenges accepting votes currently.",
			"tcp_ip": "202.31.137.139",
			"write_date": "2016-08-19 07:51:04",
			"update_date": None,
			"visit": 741,
			"ref": "201608190001"
		},
		{
			"user": "차중혁",
			"subject": "user Horace Mann",
			"tcp_ip": "202.31.137.136",
			"write_date": "2016-08-23 00:51:37",
			"update_date": None,
			"visit": 872,
			"ref": "201608230001"
		},
		{
			"user": "김승한",
			"subject": "Nothing is as far away as one minute ago.",
			"tcp_ip": "202.31.137.116",
			"write_date": "2016-08-26 10:25:50",
			"update_date": None,
			"visit": 1001,
			"ref": "201608260001"
		},
		{
			"user": "김다혜",
			"subject": "I can’t understand  why people are frightened of new ideas. I’m frightened of the old ones.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2016-09-01 12:40:58",
			"update_date": None,
			"visit": 2195,
			"ref": "201609010001"
		},
		{
			"user": "Alif Akbar Pranata",
			"subject": "For every minute you are angry, you lose sixty seconds of happiness",
			"tcp_ip": "202.31.201.34",
			"write_date": "2016-09-23 15:01:08",
			"update_date": None,
			"visit": 741,
			"ref": "201609230001"
		},
		{
			"user": "syamsul rizal",
			"subject": "To acquire knowledge, one must study; but to acquire wisdom, one must observe. -Marilyn vos Savant-",
			"tcp_ip": "202.31.207.244",
			"write_date": "2016-10-07 11:03:40",
			"update_date": None,
			"visit": 805,
			"ref": "201610070001"
		},
		{
			"user": "Nguyen Bach Long",
			"subject": "Innovation distinguishes between a leader and a follower",
			"tcp_ip": "202.31.137.161",
			"write_date": "2016-10-16 17:47:34",
			"update_date": None,
			"visit": 771,
			"ref": "201610160001"
		},
		{
			"user": "임지철",
			"subject": "Nothing of me is original. I am the combined effort of everybody I&#39;ve ever known.",
			"tcp_ip": "202.31.130.55",
			"write_date": "2016-10-18 08:28:29",
			"update_date": None,
			"visit": 802,
			"ref": "201610180001"
		},
		{
			"user": "관리자",
			"subject": "If you want to shine like the sun, first you have to burn like it.",
			"tcp_ip": "202.31.137.119",
			"write_date": "2016-10-20 17:34:55",
			"update_date": None,
			"visit": 800,
			"ref": "201610200001"
		},
		{
			"user": "차중혁",
			"subject": "user Edith Wharton",
			"tcp_ip": "",
			"write_date": "2016-11-01 22:07:11",
			"update_date": "2016-11-01 22:07:33",
			"visit": 695,
			"ref": "201611010001"
		},
		{
			"user": "김다혜",
			"subject": "In preparing for battle I have always found that plans are useless, but planning is indispensable.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2016-11-11 10:42:26",
			"update_date": None,
			"visit": 771,
			"ref": "201611110001"
		},
		{
			"user": "김승한",
			"subject": "Just because something doesn&#39;t do what you planned it to do doesn&#39;t mean it&#39;s useless.",
			"tcp_ip": "202.31.137.116",
			"write_date": "2016-11-11 10:46:55",
			"update_date": None,
			"visit": 945,
			"ref": "201611110002"
		},
		{
			"user": "Alif Akbar Pranata",
			"subject": "Life is what happens when you&#39;re busy making your excuses",
			"tcp_ip": "202.31.201.34",
			"write_date": "2016-11-16 20:54:21",
			"update_date": None,
			"visit": 793,
			"ref": "201611160001"
		},
		{
			"user": "Muhamamd Royyan",
			"subject": "Sometimes user losing a battle you find a new way to win the war.",
			"tcp_ip": "202.31.137.196",
			"write_date": "2016-11-18 08:37:11",
			"update_date": None,
			"visit": 831,
			"ref": "201611180001"
		},
		{
			"user": "차중혁",
			"subject": "&#34;Don&#39;t ask ..&#34;user Kimberly Chapman",
			"tcp_ip": "",
			"write_date": "2017-01-05 10:59:42",
			"update_date": "2017-01-05 11:00:04",
			"visit": 776,
			"ref": "201701050001"
		},
		{
			"user": "김승한",
			"subject": "A Day without Laughter is a Day Wasted.",
			"tcp_ip": "202.31.137.116",
			"write_date": "2017-01-05 11:00:19",
			"update_date": None,
			"visit": 953,
			"ref": "201701050002"
		},
		{
			"user": "김다혜",
			"subject": "Believe in  yourself. Have faith in your abilities. Without a humble but reasonable confidence in your own powers you cannot be successful or happy.",
			"tcp_ip": "202.31.137.33",
			"write_date": "2017-01-15 22:24:28",
			"update_date": None,
			"visit": 890,
			"ref": "201701150001"
		},
		{
			"user": "Alif Akbar Pranata",
			"subject": "Remember to enjoy everything. The things that feel good, the things that hurt, rejection, acceptance, it&#39;s all going to make you better, stronger, and more like yourself. Every once in a while I get a reminder of how much I&#39;m okay with just being me.",
			"tcp_ip": "202.31.201.34",
			"write_date": "2017-01-25 16:07:48",
			"update_date": None,
			"visit": 808,
			"ref": "201701250001"
		},
		{
			"user": "Muhamamd Royyan",
			"subject": "Knowledge is not what is memorised knowledge is what benefits.",
			"tcp_ip": "119.56.153.78",
			"write_date": "2017-02-06 00:51:26",
			"update_date": None,
			"visit": 887,
			"ref": "201702060001"
		},
		{
			"user": "이하연",
			"subject": "Experience never gets old. Experience never goes out of fashion.",
			"tcp_ip": "119.56.128.66",
			"write_date": "2017-02-17 01:28:31",
			"update_date": None,
			"visit": 1122,
			"ref": "201702170001"
		},
		{
			"user": "관리자",
			"subject": "The biggest risk is not taking any risk... In a world that changing really quickly, the only strategy that is guaranteed to fail is not taking risks.",
			"tcp_ip": "202.31.137.161",
			"write_date": "2017-03-13 10:09:21",
			"update_date": None,
			"visit": 891,
			"ref": "201703130001"
		},
		{
			"user": "차중혁",
			"subject": "life is long lesson in humility",
			"tcp_ip": "",
			"write_date": "2017-03-31 03:53:40",
			"update_date": "2017-03-31 03:57:28",
			"visit": 941,
			"ref": "201703310001"
		},
		{
			"user": "Muhamamd Royyan",
			"subject": "Don&#39;t Count The Days, Make The Days Count - Muhammad Ali",
			"tcp_ip": "119.56.153.78",
			"write_date": "2017-04-21 06:08:15",
			"update_date": None,
			"visit": 828,
			"ref": "201704210001"
		},
		{
			"user": "Alif Akbar Pranata",
			"subject": "No, I won&#39;t stop. For every minute of the rest of my life I will figt.",
			"tcp_ip": "202.31.137.64",
			"write_date": "2017-04-28 10:27:25",
			"update_date": None,
			"visit": 789,
			"ref": "201704280001"
		},
		{
			"user": "조홍규",
			"subject": "Opportunity is missed user most people because it is dressed in overalls and looks like work.",
			"tcp_ip": "202.31.207.244",
			"write_date": "2017-04-28 16:07:20",
			"update_date": None,
			"visit": 872,
			"ref": "201704280002"
		},
		{
			"user": "PhuPT",
			"subject": "No matter how many mistakes you make or how slow you progress, you are still way ahead of everyone who isn’t trying",
			"tcp_ip": "",
			"write_date": "2017-05-11 11:04:23",
			"update_date": "2017-05-11 11:05:18",
			"visit": 1342,
			"ref": "201705110001"
		},
		{
			"user": "이하연",
			"subject": "The journey is the reward.",
			"tcp_ip": "202.31.137.65",
			"write_date": "2017-05-13 16:59:34",
			"update_date": None,
			"visit": 1024,
			"ref": "201705130001"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "Miracles can be made, but only user sweating",
			"tcp_ip": "202.31.137.115",
			"write_date": "2017-05-14 14:02:33",
			"update_date": None,
			"visit": 965,
			"ref": "201705140001"
		},
		{
			"user": "syamsul rizal",
			"subject": "Teachers open the door, but you must enter user yourself",
			"tcp_ip": "202.31.137.34",
			"write_date": "2017-06-23 11:40:57",
			"update_date": None,
			"visit": 1014,
			"ref": "201706230001"
		},
		{
			"user": "최학희",
			"subject": "The reading of all good books is like a conversation with the finest men of past centruries - Rene Decartes",
			"tcp_ip": "202.31.137.111",
			"write_date": "2017-07-07 05:34:48",
			"update_date": None,
			"visit": 915,
			"ref": "201707070001"
		},
		{
			"user": "Muhamamd Royyan",
			"subject": "Being angry is human. Staying angry is foolish.",
			"tcp_ip": "202.31.137.139",
			"write_date": "2017-07-24 11:21:27",
			"update_date": None,
			"visit": 890,
			"ref": "201707240001"
		},
		{
			"user": "이하연",
			"subject": "So long as a man imagines that he cannot do this or that, so long as he is determined not to do it; and consequently so long as it is impossible to him that he should do it.",
			"tcp_ip": "202.31.137.65",
			"write_date": "2017-08-07 10:21:22",
			"update_date": None,
			"visit": 839,
			"ref": "201708070001"
		},
		{
			"user": "관리자",
			"subject": "But as long as we think positively, I&#39;m sure a solution will appear",
			"tcp_ip": "202.31.137.115",
			"write_date": "2017-08-16 12:58:20",
			"update_date": None,
			"visit": 601,
			"ref": "201708160001"
		},
		{
			"user": "syamsul rizal",
			"subject": "Smile in the mirror. Do that every morning and you’ll start to see a big difference in your life. &#8211; Yoko Ono",
			"tcp_ip": "202.31.137.34",
			"write_date": "2017-08-18 11:47:35",
			"update_date": None,
			"visit": 860,
			"ref": "201708180001"
		},
		{
			"user": "차중혁",
			"subject": "He can do, She can do, Why not me?",
			"tcp_ip": "121.182.234.157",
			"write_date": "2017-08-24 00:09:00",
			"update_date": None,
			"visit": 592,
			"ref": "201708240001"
		},
		{
			"user": "김승한",
			"subject": "Suffering is not holding you, you are holding suffering",
			"tcp_ip": "202.31.136.58",
			"write_date": "2017-08-25 16:36:27",
			"update_date": None,
			"visit": 1134,
			"ref": "201708250001"
		},
		{
			"user": "Ali Moallim",
			"subject": "# It is not beauty when one is clothed with beautiful clothings to beautify one self. # Verily beauty lies in knowledge and morals.",
			"tcp_ip": "",
			"write_date": "2017-08-25 17:43:53",
			"update_date": "2017-08-25 17:44:21",
			"visit": 692,
			"ref": "201708250002"
		},
		{
			"user": "최학희",
			"subject": "To succeed in life, you need two things: ignorance and confidence. -Mark Twain-",
			"tcp_ip": "202.31.137.111",
			"write_date": "2017-09-01 13:27:24",
			"update_date": None,
			"visit": 696,
			"ref": "201709010001"
		},
		{
			"user": "김다혜",
			"subject": "Chance favors only the prepared mind",
			"tcp_ip": "202.31.137.33",
			"write_date": "2017-09-01 15:09:53",
			"update_date": None,
			"visit": 843,
			"ref": "201709010002"
		},
		{
			"user": "Muhamamd Royyan",
			"subject": "It always seems impossible until it&#39;s done - Nelson Mandela",
			"tcp_ip": "119.56.153.78",
			"write_date": "2017-09-08 05:36:47",
			"update_date": None,
			"visit": 698,
			"ref": "201709080001"
		},
		{
			"user": "Alif Akbar Pranata",
			"subject": "Don’t feel stupid if you don&#39;t like what everyone else pretends to love",
			"tcp_ip": "202.31.137.64",
			"write_date": "2017-09-08 16:19:27",
			"update_date": None,
			"visit": 743,
			"ref": "201709080002"
		},
		{
			"user": "Asatilla",
			"subject": "The world is a book, and those who do not travel read only a page",
			"tcp_ip": "192.168.212.39",
			"write_date": "2017-09-18 14:29:17",
			"update_date": None,
			"visit": 796,
			"ref": "201709180001"
		},
		{
			"user": "JEAN CLAUDE SANGANO",
			"subject": "Give me six hours to chop down a tree and I will spend the first four sharpening the axe",
			"tcp_ip": "192.168.210.218",
			"write_date": "2017-09-18 16:22:36",
			"update_date": None,
			"visit": 723,
			"ref": "201709180002"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "You have to believe in yourself.",
			"tcp_ip": "202.31.137.115",
			"write_date": "2017-09-29 14:36:20",
			"update_date": None,
			"visit": 977,
			"ref": "201709290001"
		},
		{
			"user": "Nwadiugwu Williams P",
			"subject": "The Man, The Wife, The Donkey and the Critics.",
			"tcp_ip": "202.31.137.118",
			"write_date": "2017-10-02 10:54:41",
			"update_date": None,
			"visit": 583,
			"ref": "201710020001"
		},
		{
			"user": "이하연",
			"subject": "Never leave till tomorrow that which you can do today.",
			"tcp_ip": "202.31.137.65",
			"write_date": "2017-10-13 11:40:55",
			"update_date": None,
			"visit": 679,
			"ref": "201710130001"
		},
		{
			"user": "Ali Moallim",
			"subject": "A wise mind appreciates simplicity because it is less accessible.",
			"tcp_ip": "",
			"write_date": "2017-10-13 14:22:41",
			"update_date": "2017-10-13 14:23:11",
			"visit": 619,
			"ref": "201710130002"
		},
		{
			"user": "Asatilla",
			"subject": "A smart man learns from his mistakes. A wise one learns from the mistakes of others",
			"tcp_ip": "202.31.137.161",
			"write_date": "2017-10-20 09:34:09",
			"update_date": None,
			"visit": 568,
			"ref": "201710200001"
		},
		{
			"user": "Muhamamd Royyan",
			"subject": "Education is the passport to the future, for tomorrow belongs to those who prepare for it today.",
			"tcp_ip": "202.31.137.139",
			"write_date": "2017-11-28 11:46:24",
			"update_date": None,
			"visit": 560,
			"ref": "201711280001"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "The accumulation of small achievements is the only way to do something incredible - Fumio Sasaki",
			"tcp_ip": "192.168.209.77",
			"write_date": "2017-12-08 14:53:36",
			"update_date": None,
			"visit": 475,
			"ref": "201712080001"
		},
		{
			"user": "Nwadiugwu Williams P",
			"subject": "GOAL SETTINGS: working SMART!",
			"tcp_ip": "202.31.137.118",
			"write_date": "2017-12-08 15:01:07",
			"update_date": None,
			"visit": 496,
			"ref": "201712080002"
		},
		{
			"user": "이하연",
			"subject": "I believe that one of life&#39;s greatest risks is never daring to risk.",
			"tcp_ip": "202.31.137.65",
			"write_date": "2017-12-15 13:20:25",
			"update_date": None,
			"visit": 508,
			"ref": "201712150001"
		},
		{
			"user": "Ali Moallim",
			"subject": "You can not be really strong until you see a funny side to things.",
			"tcp_ip": "202.31.137.117",
			"write_date": "2017-12-15 14:03:06",
			"update_date": None,
			"visit": 501,
			"ref": "201712150002"
		},
		{
			"user": "Asatilla",
			"subject": "If you don&#39;t follow your heart, you might spend the rest of your life wishing you had",
			"tcp_ip": "202.31.137.161",
			"write_date": "2017-12-21 12:51:35",
			"update_date": None,
			"visit": 573,
			"ref": "201712210001"
		},
		{
			"user": "관리자",
			"subject": "Let Your Smile Changes the World, but Do not Let the World Changes your Smile",
			"tcp_ip": "202.31.137.64",
			"write_date": "2018-01-05 14:39:08",
			"update_date": None,
			"visit": 498,
			"ref": "201801050001"
		},
		{
			"user": "JEAN CLAUDE SANGANO",
			"subject": "7 Habits of Highly Effective People first published in 1988, is a business and self-help book written user Stephen R. Covey",
			"tcp_ip": "202.31.137.120",
			"write_date": "2018-01-08 12:06:23",
			"update_date": None,
			"visit": 498,
			"ref": "201801080001"
		},
		{
			"user": "김승한",
			"subject": "Keep your face to the sunshine and you cannot see the shadow.",
			"tcp_ip": "202.31.137.116",
			"write_date": "2018-01-12 11:12:43",
			"update_date": None,
			"visit": 537,
			"ref": "201801120001"
		},
		{
			"user": "김다혜",
			"subject": "Happiness is like a kiss. You must share it to enjoy it.",
			"tcp_ip": "",
			"write_date": "2018-01-12 11:29:50",
			"update_date": "2018-01-12 11:30:09",
			"visit": 526,
			"ref": "201801120002"
		},
		{
			"user": "관리자",
			"subject": "Be afraid of the same mistake, but do not be afraid of a new mistake.  A mistake is an experience.",
			"tcp_ip": "",
			"write_date": "2018-01-19 09:06:58",
			"update_date": "2018-01-20 00:35:21",
			"visit": 521,
			"ref": "201801190001"
		},
		{
			"user": "관리자",
			"subject": "Only I can change my Life. No one else can do it for me!",
			"tcp_ip": "202.31.137.118",
			"write_date": "2018-01-19 15:00:08",
			"update_date": None,
			"visit": 644,
			"ref": "201801190002"
		},
		{
			"user": "Muhamamd Royyan",
			"subject": "If you want to shine like sun, first you have to burn like it - Adolf Hitler",
			"tcp_ip": "202.31.137.139",
			"write_date": "2018-01-26 10:24:13",
			"update_date": None,
			"visit": 561,
			"ref": "201801260001"
		},
		{
			"user": "Ali Moallim",
			"subject": "The world can’t tell you who you are. You’ve just got to figure out who you are and be there, for better or worse.",
			"tcp_ip": "202.31.137.117",
			"write_date": "2018-01-26 14:51:17",
			"update_date": None,
			"visit": 565,
			"ref": "201801260002"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "Accept who you are, and revel in it",
			"tcp_ip": "119.56.151.171",
			"write_date": "2018-02-02 08:56:06",
			"update_date": None,
			"visit": 721,
			"ref": "201802020001"
		},
		{
			"user": "관리자",
			"subject": "The best preparation  for tomorrow is doing your best today",
			"tcp_ip": "202.31.137.161",
			"write_date": "2018-02-09 15:32:34",
			"update_date": None,
			"visit": 487,
			"ref": "201802090001"
		},
		{
			"user": "관리자",
			"subject": "Knowing is not enough, we must apply. Willing is not enough, we must do",
			"tcp_ip": "202.31.137.161",
			"write_date": "2018-02-09 15:42:47",
			"update_date": None,
			"visit": 582,
			"ref": "201802090002"
		},
		{
			"user": "Jean",
			"subject": "Nothing is impossible, the word itself says &#39;I&#39;m possible&#39;!",
			"tcp_ip": "",
			"write_date": "2018-02-23 01:53:19",
			"update_date": "2018-03-23 15:35:38",
			"visit": 2322,
			"ref": "201802230001"
		},
		{
			"user": "이종우",
			"subject": "Never confuse a single defeat with a final defeat",
			"tcp_ip": "",
			"write_date": "2018-02-26 10:26:18",
			"update_date": "2018-02-26 10:26:50",
			"visit": 599,
			"ref": "201802260001"
		},
		{
			"user": "김경선",
			"subject": "If you want to live a happy life , rely on a goal , not a person or thing",
			"tcp_ip": "202.31.137.39",
			"write_date": "2018-03-02 12:53:02",
			"update_date": None,
			"visit": 570,
			"ref": "201803020001"
		},
		{
			"user": "Rizki Rivai Ginanjar",
			"subject": "The roots of education are bitter, but the fruit is sweet",
			"tcp_ip": "",
			"write_date": "2018-03-07 11:13:34",
			"update_date": "2018-03-21 15:02:50",
			"visit": 586,
			"ref": "201803070001"
		},
		{
			"user": "Gaspard Gashema",
			"subject": "Intelligence is the ability to adapt to change",
			"tcp_ip": "",
			"write_date": "2018-03-16 14:53:51",
			"update_date": "2018-03-21 15:08:32",
			"visit": 492,
			"ref": "201803160001"
		},
		{
			"user": "sanjay",
			"subject": "Live and Let Live",
			"tcp_ip": "",
			"write_date": "2018-03-20 15:03:10",
			"update_date": "2018-03-21 15:53:15",
			"visit": 450,
			"ref": "201803200001"
		},
		{
			"user": "Saviour",
			"subject": "There is always big room in reality to accommodate any big dream.",
			"tcp_ip": "202.31.137.130",
			"write_date": "2018-03-23 15:53:01",
			"update_date": None,
			"visit": 527,
			"ref": "201803230001"
		},
		{
			"user": "Alif Akbar Pranata",
			"subject": "I&#39;m thankful for all those bad people in my life. They have shown me exactly who I do not want to be.",
			"tcp_ip": "202.31.137.46",
			"write_date": "2018-03-30 15:32:44",
			"update_date": None,
			"visit": 451,
			"ref": "201803300001"
		},
		{
			"user": "김승한",
			"subject": "That which does not kill us makes us stronger.",
			"tcp_ip": "",
			"write_date": "2018-03-30 15:42:54",
			"update_date": "2018-03-30 15:43:04",
			"visit": 529,
			"ref": "201803300002"
		},
		{
			"user": "김다혜",
			"subject": "Happiness lies first of all in health.",
			"tcp_ip": "",
			"write_date": "2018-04-06 10:21:46",
			"update_date": "2018-04-06 10:22:17",
			"visit": 435,
			"ref": "201804060001"
		},
		{
			"user": "조홍규",
			"subject": "To live a creative life, I must abandon the fear that I might be wrong.",
			"tcp_ip": "202.31.137.197",
			"write_date": "2018-04-06 13:05:56",
			"update_date": None,
			"visit": 460,
			"ref": "201804060002"
		},
		{
			"user": "Thanh",
			"subject": "The successful warrior the average man,  with laser-like focus - Bruce Lee",
			"tcp_ip": "192.168.209.102",
			"write_date": "2018-04-13 15:47:24",
			"update_date": None,
			"visit": 472,
			"ref": "201804130001"
		},
		{
			"user": "Nwadiugwu Williams P",
			"subject": "The glory of rising after each fall.",
			"tcp_ip": "202.31.137.118",
			"write_date": "2018-04-13 16:12:02",
			"update_date": None,
			"visit": 466,
			"ref": "201804130002"
		},
		{
			"user": "관리자",
			"subject": "Tomorrow belongs to those who can hear it coming - David Bowie",
			"tcp_ip": "202.31.137.139",
			"write_date": "2018-04-23 08:53:47",
			"update_date": None,
			"visit": 459,
			"ref": "201804230001"
		},
		{
			"user": "Ali Moallim",
			"subject": "Life is inherently risky.There is only one big risk you should avoid at all costs, and that is the risk of doing nothing.",
			"tcp_ip": "202.31.137.122",
			"write_date": "2018-04-27 10:40:34",
			"update_date": None,
			"visit": 445,
			"ref": "201804270001"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "Detachment is a key. Learn to detach. Do not cling to things, because everything is impermanent.",
			"tcp_ip": "202.31.137.34",
			"write_date": "2018-04-27 14:37:34",
			"update_date": None,
			"visit": 593,
			"ref": "201804270002"
		},
		{
			"user": "이하연",
			"subject": "Laughter is user definition healthy.",
			"tcp_ip": "202.31.137.65",
			"write_date": "2018-05-08 12:41:07",
			"update_date": None,
			"visit": 423,
			"ref": "201805080001"
		},
		{
			"user": "Asatilla",
			"subject": "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
			"tcp_ip": "202.31.137.161",
			"write_date": "2018-05-11 01:42:17",
			"update_date": None,
			"visit": 536,
			"ref": "201805110001"
		},
		{
			"user": "JEAN CLAUDE SANGANO",
			"subject": "&#39;&#39; Success is how you bounce when you hit bottom &#39;&#39; General George Patton",
			"tcp_ip": "202.31.137.120",
			"write_date": "2018-05-18 00:43:37",
			"update_date": None,
			"visit": 450,
			"ref": "201805180001"
		},
		{
			"user": "이종우",
			"subject": "Waste not fresh tears over old griefs.",
			"tcp_ip": "202.31.137.123",
			"write_date": "2018-05-18 16:12:05",
			"update_date": None,
			"visit": 675,
			"ref": "201805180002"
		},
		{
			"user": "Rizki Rivai Ginanjar",
			"subject": "Don&#39;t find fault, find a remedy",
			"tcp_ip": "202.31.137.110",
			"write_date": "2018-06-08 15:17:01",
			"update_date": None,
			"visit": 498,
			"ref": "201806080001"
		},
		{
			"user": "Gaspard Gashema",
			"subject": "If you find a path with no obstacles, it probably does lead anywhere",
			"tcp_ip": "202.31.137.133",
			"write_date": "2018-06-22 10:04:15",
			"update_date": None,
			"visit": 524,
			"ref": "201806220001"
		},
		{
			"user": "김시완",
			"subject": "There is nothing noble in being superior to your fellow man; true nobility is being superior to your former self",
			"tcp_ip": "202.31.137.41",
			"write_date": "2018-07-06 14:27:26",
			"update_date": None,
			"visit": 596,
			"ref": "201807060001"
		},
		{
			"user": "김경선",
			"subject": "Good luck hates idiots",
			"tcp_ip": "",
			"write_date": "2018-07-06 15:36:57",
			"update_date": "2018-07-06 15:37:54",
			"visit": 436,
			"ref": "201807060002"
		},
		{
			"user": "sanjay",
			"subject": "Learning_Behaviour_Stimulation",
			"tcp_ip": "202.31.137.131",
			"write_date": "2018-07-19 11:48:26",
			"update_date": None,
			"visit": 383,
			"ref": "201807190001"
		},
		{
			"user": "Saviour",
			"subject": "What is the meaning of love?",
			"tcp_ip": "202.31.137.130",
			"write_date": "2018-07-25 11:51:30",
			"update_date": None,
			"visit": 495,
			"ref": "201807250001"
		},
		{
			"user": "관리자",
			"subject": "Happiness is not the mere possession of money; it lies in the joy of achievement, in the thrill of creative effort.",
			"tcp_ip": "202.31.137.46",
			"write_date": "2018-07-27 14:57:46",
			"update_date": None,
			"visit": 468,
			"ref": "201807270001"
		},
		{
			"user": "김승한",
			"subject": "It doesn’t matter how slow you go as long as you don’t stop",
			"tcp_ip": "202.31.139.196",
			"write_date": "2018-07-27 15:59:26",
			"update_date": None,
			"visit": 665,
			"ref": "201807270002"
		},
		{
			"user": "김다혜",
			"subject": "There is no path to happiness. The happiness is the path.",
			"tcp_ip": "202.31.137.33",
			"write_date": "2018-08-03 12:28:14",
			"update_date": None,
			"visit": 585,
			"ref": "201808030001"
		},
		{
			"user": "조홍규",
			"subject": "Do not say thirty minutes is the same time as the dust, and it is wise to handle the same thing as dust during that time.",
			"tcp_ip": "202.31.137.197",
			"write_date": "2018-08-06 16:38:30",
			"update_date": None,
			"visit": 524,
			"ref": "201808060001"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "But as long as we think positively, I’m sure a solution will appear. Jonas Jonasson",
			"tcp_ip": "202.31.134.95",
			"write_date": "2018-09-07 14:13:27",
			"update_date": None,
			"visit": 513,
			"ref": "201809070001"
		},
		{
			"user": "Asatilla",
			"subject": "When you want something all the universe conspires in helping you to achieve it!",
			"tcp_ip": "",
			"write_date": "2018-09-10 12:11:34",
			"update_date": "2018-09-10 12:11:58",
			"visit": 541,
			"ref": "201809100001"
		},
		{
			"user": "Ali Moallim",
			"subject": "Time is a created thing.  To say ‘I don&#39;t have time’ is like saying ‘I don&#39;t want to’",
			"tcp_ip": "192.168.210.168",
			"write_date": "2018-09-14 15:56:59",
			"update_date": None,
			"visit": 443,
			"ref": "201809140001"
		},
		{
			"user": "김시완",
			"subject": "The key to everything is patience. You get the chicken user hatching the egg, not user smashing it",
			"tcp_ip": "202.31.134.93",
			"write_date": "2018-09-20 23:21:40",
			"update_date": None,
			"visit": 534,
			"ref": "201809200001"
		},
		{
			"user": "So-Hyang",
			"subject": "A pessimist sees the difficulty in every opportunity; an optimist sees the opportunity in every difficulty.",
			"tcp_ip": "202.31.137.162",
			"write_date": "2018-09-21 12:01:15",
			"update_date": None,
			"visit": 731,
			"ref": "201809210001"
		},
		{
			"user": "sanjay",
			"subject": "In the field of observation, chance favor’s only the prepared mind ~Lois Pasteur",
			"tcp_ip": "202.31.134.90",
			"write_date": "2018-10-05 11:25:23",
			"update_date": None,
			"visit": 529,
			"ref": "201810050001"
		},
		{
			"user": "Gaspard Gashema",
			"subject": "Never limit yourself because of others&#39; limited imagination; never limit others because of your own limited imagination",
			"tcp_ip": "202.31.137.133",
			"write_date": "2018-10-14 14:52:47",
			"update_date": None,
			"visit": 487,
			"ref": "201810140001"
		},
		{
			"user": "Heidy Indrayani",
			"subject": "“Everybody is a genius. But if you judge a fish user its ability to climb a tree, its will live its whole life believing that it is stupid”",
			"tcp_ip": "202.31.137.57",
			"write_date": "2018-10-19 15:41:13",
			"update_date": None,
			"visit": 643,
			"ref": "201810190001"
		},
		{
			"user": "Muhammad Taufiq Rama",
			"subject": "there are many things that can knock you down, but the only thing that can really bring you down is your own attitude.",
			"tcp_ip": "",
			"write_date": "2018-10-26 09:53:54",
			"update_date": "2018-10-26 09:58:31",
			"visit": 395,
			"ref": "201810260001"
		},
		{
			"user": "Nita Hidayati",
			"subject": "The happiness of your life depends upon the quality of your thoughts",
			"tcp_ip": "202.31.137.64",
			"write_date": "2018-10-26 12:01:41",
			"update_date": None,
			"visit": 470,
			"ref": "201810260002"
		},
		{
			"user": "Riesa Krisna Astuti",
			"subject": "“The chances you take, the people you meet, the people you love, the faith that you have. That’s what’s going to define you.”",
			"tcp_ip": "",
			"write_date": "2018-10-30 09:12:08",
			"update_date": "2018-10-30 09:13:19",
			"visit": 867,
			"ref": "201810300001"
		},
		{
			"user": "Saviour",
			"subject": "In order to succeed, your desire for success should be greater than your fear of failure.",
			"tcp_ip": "",
			"write_date": "2018-11-05 22:10:38",
			"update_date": "2018-11-07 21:22:56",
			"visit": 410,
			"ref": "201811050001"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "Anyone who has never made a mistake has never tried anything new.",
			"tcp_ip": "192.168.208.185",
			"write_date": "2018-11-13 16:54:45",
			"update_date": None,
			"visit": 380,
			"ref": "201811130001"
		},
		{
			"user": "Seung-Han",
			"subject": "The only way of discovering the limits of the possible is  to venture a little way past them into the impossible.",
			"tcp_ip": "202.31.134.94",
			"write_date": "2018-11-20 13:47:32",
			"update_date": None,
			"visit": 378,
			"ref": "201811200001"
		},
		{
			"user": "Ali Moallim",
			"subject": "There is a great deal of difference between an eager man who wants to read a book and the tired man who wants a book to read.",
			"tcp_ip": "202.31.134.97",
			"write_date": "2018-11-23 16:40:20",
			"update_date": None,
			"visit": 2673,
			"ref": "201811230001"
		},
		{
			"user": "김다혜",
			"subject": "“When I was 5 years old, my mother always told me that happiness was the key to life. When I went to school, they asked me what I wanted to be when I grew up. I wrote down ‘happy’. They told me I didn’t understand the assignment, and I told them they didn’t understand life.”  ― John Lennon",
			"tcp_ip": "202.31.134.96",
			"write_date": "2018-12-05 22:01:15",
			"update_date": None,
			"visit": 622,
			"ref": "201812050001"
		},
		{
			"user": "Nwadiugwu Williams P",
			"subject": "&#34;Great things often have small beginnings. Be patient!&#34;",
			"tcp_ip": "",
			"write_date": "2018-12-10 19:01:12",
			"update_date": "2018-12-10 19:01:43",
			"visit": 407,
			"ref": "201812100001"
		},
		{
			"user": "Asatilla",
			"subject": "Some people quit due to slow progress… Never grasping the fact that slow progress … is progress.",
			"tcp_ip": "",
			"write_date": "2018-12-13 18:14:40",
			"update_date": "2018-12-13 18:15:22",
			"visit": 381,
			"ref": "201812130001"
		},
		{
			"user": "Thanh",
			"subject": "Books wash away from the soul the dust of everyday life",
			"tcp_ip": "202.31.137.139",
			"write_date": "2018-12-14 15:14:59",
			"update_date": None,
			"visit": 460,
			"ref": "201812140001"
		},
		{
			"user": "So-Hyang",
			"subject": "Always aim at complete harmony of thought and word and deed. Always aim at purifying your thought and everything will be well",
			"tcp_ip": "202.31.137.162",
			"write_date": "2018-12-20 15:11:32",
			"update_date": None,
			"visit": 439,
			"ref": "201812200001"
		},
		{
			"user": "박성화",
			"subject": "Promise me you&#39;ll always remember; You&#39;re breaver than you believe, and stronger than you seem, and smarter than you think",
			"tcp_ip": "202.31.137.138",
			"write_date": "2018-12-21 14:04:35",
			"update_date": None,
			"visit": 489,
			"ref": "201812210001"
		},
		{
			"user": "이종우",
			"subject": "He that is good at making excuses is seldom good at anything else.",
			"tcp_ip": "202.31.137.123",
			"write_date": "2018-12-27 10:57:34",
			"update_date": None,
			"visit": 418,
			"ref": "201812270001"
		},
		{
			"user": "김시완",
			"subject": "Today is the first day of the rest of your life",
			"tcp_ip": "202.31.134.93",
			"write_date": "2019-01-03 13:16:10",
			"update_date": None,
			"visit": 431,
			"ref": "201901030001"
		},
		{
			"user": "Rizki Rivai Ginanjar",
			"subject": "Your Life is The Fruit of Your Own Doing. You Have no One to Blame But Yourself",
			"tcp_ip": "173.245.211.99",
			"write_date": "2019-01-10 13:47:03",
			"update_date": None,
			"visit": 396,
			"ref": "201901100001"
		},
		{
			"user": "Gaspard Gashema",
			"subject": "Most days are not overwhelmingly successful in your life.",
			"tcp_ip": "",
			"write_date": "2019-01-17 10:27:39",
			"update_date": "2019-01-17 18:14:18",
			"visit": 420,
			"ref": "201901170001"
		},
		{
			"user": "sanjay",
			"subject": "Stars Can&#39;t shine without darkness",
			"tcp_ip": "",
			"write_date": "2019-01-17 12:31:18",
			"update_date": "2019-01-17 12:31:37",
			"visit": 423,
			"ref": "201901170002"
		},
		{
			"user": "Kevin Putra Dirganto",
			"subject": "Sometimes it is the people no one can imagine anything of, who do the things no one can imagine.",
			"tcp_ip": "202.31.137.61",
			"write_date": "2019-01-31 20:18:59",
			"update_date": None,
			"visit": 413,
			"ref": "201901310001"
		},
		{
			"user": "Saviour",
			"subject": "The function of education is to teach one to think intensively and to think critically. Intelligence plus character - that is the goal of true education",
			"tcp_ip": "202.31.139.196",
			"write_date": "2019-02-01 15:12:14",
			"update_date": None,
			"visit": 423,
			"ref": "201902010001"
		},
		{
			"user": "Nita Hidayati",
			"subject": "You can’t stop the waves, but you can learn to surf",
			"tcp_ip": "119.56.145.96",
			"write_date": "2019-02-11 07:32:56",
			"update_date": None,
			"visit": 387,
			"ref": "201902110001"
		},
		{
			"user": "Heidy Indrayani",
			"subject": "In theory, there is no difference between theory and practice. But in practice, there is.",
			"tcp_ip": "223.62.190.184",
			"write_date": "2019-02-11 14:52:53",
			"update_date": None,
			"visit": 408,
			"ref": "201902110002"
		},
		{
			"user": "Muhammad Taufiq Rama",
			"subject": "Inspiration comes from within yourself. one has to be positive. when you&#39;re positive, good things happen.",
			"tcp_ip": "119.56.145.96",
			"write_date": "2019-02-15 14:26:29",
			"update_date": None,
			"visit": 446,
			"ref": "201902150001"
		},
		{
			"user": "Riesa Krisna Astuti",
			"subject": "Setting goals is the first step in turning the invisible into the visible",
			"tcp_ip": "",
			"write_date": "2019-02-15 14:39:07",
			"update_date": "2019-03-13 10:58:32",
			"visit": 418,
			"ref": "201902150002"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "“Life does not get better user chance, it gets better user change.” Jim Rohn",
			"tcp_ip": "202.31.134.99",
			"write_date": "2019-02-22 09:59:05",
			"update_date": None,
			"visit": 477,
			"ref": "201902220001"
		},
		{
			"user": "김치윤",
			"subject": "A THING IS A THING, NOT WHAT IS SAID OF THAT THING",
			"tcp_ip": "202.31.134.92",
			"write_date": "2019-03-11 16:31:39",
			"update_date": None,
			"visit": 547,
			"ref": "201903110001"
		},
		{
			"user": "유상호",
			"subject": "Together, even the smallest can achieve the greatest goal.",
			"tcp_ip": "192.168.215.194",
			"write_date": "2019-03-15 14:18:41",
			"update_date": None,
			"visit": 397,
			"ref": "201903150001"
		},
		{
			"user": "Ade Pitra Hermawan",
			"subject": "To improve is to change; to be perfect is to change often",
			"tcp_ip": "202.31.137.124",
			"write_date": "2019-03-15 14:44:27",
			"update_date": None,
			"visit": 432,
			"ref": "201903150002"
		},
		{
			"user": "Alifia Putri Anantha",
			"subject": "You don&#39;t have to be great to start, but you have to start to be great.",
			"tcp_ip": "202.31.134.88",
			"write_date": "2019-03-22 11:05:53",
			"update_date": None,
			"visit": 432,
			"ref": "201903220001"
		},
		{
			"user": "NWAKANMA COSMAS IFEA",
			"subject": "Most people have a desire to look for the exception instead of the desire to become exceptional",
			"tcp_ip": "202.31.134.98",
			"write_date": "2019-03-22 14:52:23",
			"update_date": None,
			"visit": 432,
			"ref": "201903220002"
		},
		{
			"user": "Philip TD",
			"subject": "Your opinion about yourself becomes your reality. ~ 50 Cent",
			"tcp_ip": "",
			"write_date": "2019-03-29 17:24:29",
			"update_date": "2019-03-29 17:26:53",
			"visit": 451,
			"ref": "201903290001"
		},
		{
			"user": "Rubina Akter",
			"subject": "The two most important Days in your LIFE, Are the day you are born, and the day you FIND out WHY",
			"tcp_ip": "",
			"write_date": "2019-04-05 12:36:54",
			"update_date": "2019-04-05 12:44:15",
			"visit": 529,
			"ref": "201904050001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "If you can’t fly, then run, if you can’t run, then walk, if you can’t walk, then crawl, but whatever you do, you have to keep MOVING forward. - Martin Luther King Jr.",
			"tcp_ip": "",
			"write_date": "2019-04-10 12:24:33",
			"update_date": "2019-04-10 12:34:07",
			"visit": 432,
			"ref": "201904100001"
		},
		{
			"user": "Esmot Ara",
			"subject": "&#34;It is never too late to be what you might have been.&#34;-George Eliot",
			"tcp_ip": "202.31.137.125",
			"write_date": "2019-04-11 19:39:49",
			"update_date": None,
			"visit": 631,
			"ref": "201904110001"
		},
		{
			"user": "김다혜",
			"subject": "Just play. Have fun. Enjoy the game.",
			"tcp_ip": "202.31.134.96",
			"write_date": "2019-04-12 14:39:57",
			"update_date": None,
			"visit": 6720,
			"ref": "201904120001"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "&#34;People could behave how they liked, but Allan considered that in general it was quite unnecessary to be grumpy if you had the chance not to&#34; - Jonas Jonasson",
			"tcp_ip": "202.31.134.95",
			"write_date": "2019-04-19 14:05:48",
			"update_date": None,
			"visit": 470,
			"ref": "201904190001"
		},
		{
			"user": "Williams Paul",
			"subject": "&#34;You are rich, when you are content and happy with what you have&#34;",
			"tcp_ip": "202.31.134.91",
			"write_date": "2019-04-19 14:53:22",
			"update_date": None,
			"visit": 481,
			"ref": "201904190002"
		},
		{
			"user": "이종우",
			"subject": "First you take a drink, then the drink takes a drink, Then the drink takes you.",
			"tcp_ip": "202.31.137.123",
			"write_date": "2019-05-03 13:54:05",
			"update_date": None,
			"visit": 439,
			"ref": "201905030001"
		},
		{
			"user": "Asatilla",
			"subject": "The only place success comes before work is in the dictionary",
			"tcp_ip": "202.31.134.210",
			"write_date": "2019-05-03 14:31:26",
			"update_date": None,
			"visit": 444,
			"ref": "201905030002"
		},
		{
			"user": "박성화",
			"subject": "Anyone can be anything",
			"tcp_ip": "202.31.137.138",
			"write_date": "2019-05-09 16:19:28",
			"update_date": None,
			"visit": 488,
			"ref": "201905090001"
		},
		{
			"user": "So-Hyang",
			"subject": "Reading a book and knowing a rich word distinguishes from the end of sorrow to the end of joy one user one of the many emotions that you have",
			"tcp_ip": "202.31.134.89",
			"write_date": "2019-05-15 21:34:09",
			"update_date": None,
			"visit": 437,
			"ref": "201905150001"
		},
		{
			"user": "김시완",
			"subject": "It&#39;s not studying if you&#39;re having fun.",
			"tcp_ip": "202.31.137.61",
			"write_date": "2019-05-17 14:13:51",
			"update_date": None,
			"visit": 428,
			"ref": "201905170001"
		},
		{
			"user": "sanjay",
			"subject": "Push Yourself Beacuse, No One Else Is Going To do it for You",
			"tcp_ip": "202.31.134.90",
			"write_date": "2019-05-23 12:00:58",
			"update_date": None,
			"visit": 452,
			"ref": "201905230001"
		},
		{
			"user": "Gaspard Gashema",
			"subject": "&#34;Conflict is inevitable, but combat is optional&#34; user Max Lucado",
			"tcp_ip": "202.31.137.133",
			"write_date": "2019-06-03 20:24:52",
			"update_date": None,
			"visit": 475,
			"ref": "201906030001"
		},
		{
			"user": "Saviour",
			"subject": "The worst part about being strong is that no one ever asks if you&#39;re okay.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2019-06-24 13:08:32",
			"update_date": None,
			"visit": 388,
			"ref": "201906240001"
		},
		{
			"user": "Rizki Rivai Ginanjar",
			"subject": "Don&#39;t Be Afraid to Give up the Good to Go for the Great",
			"tcp_ip": "202.31.137.110",
			"write_date": "2019-06-26 13:40:30",
			"update_date": None,
			"visit": 412,
			"ref": "201906260001"
		},
		{
			"user": "Nita Hidayati",
			"subject": "Don’t compare your life to others. There’s no comparison between the sun and the moon.  They shine when it’s their time.",
			"tcp_ip": "202.31.137.197",
			"write_date": "2019-06-26 13:44:29",
			"update_date": None,
			"visit": 435,
			"ref": "201906260002"
		},
		{
			"user": "Kevin Putra Dirganto",
			"subject": "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
			"tcp_ip": "205.185.223.171",
			"write_date": "2019-06-27 16:00:22",
			"update_date": None,
			"visit": 405,
			"ref": "201906270001"
		},
		{
			"user": "Heidy Indrayani",
			"subject": "Doubt is a killer you just have to know who you are and what you stand for",
			"tcp_ip": "202.31.137.57",
			"write_date": "2019-07-03 11:45:25",
			"update_date": None,
			"visit": 415,
			"ref": "201907030001"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "&#34;Imagination is everything. It is the preview of life&#39;s coming attractions&#34;. Albert Einstein",
			"tcp_ip": "202.31.134.99",
			"write_date": "2019-07-11 13:27:12",
			"update_date": None,
			"visit": 419,
			"ref": "201907110001"
		},
		{
			"user": "Muhammad Taufiq Rama",
			"subject": "Whatever you do. good or bad, people will always have something negative to say about you and that&#39;s life",
			"tcp_ip": "202.31.137.197",
			"write_date": "2019-07-11 13:46:02",
			"update_date": None,
			"visit": 393,
			"ref": "201907110002"
		},
		{
			"user": "Riesa Krisna Astuti",
			"subject": "do not quench of your inspiration  and your imagination, do not become the slave of your model",
			"tcp_ip": "202.31.134.86",
			"write_date": "2019-07-11 14:45:01",
			"update_date": None,
			"visit": 483,
			"ref": "201907110003"
		},
		{
			"user": "Rubina Akter",
			"subject": "Stop Tring to leave, and you will arrive.Stop seeking and you will see. Stop running away, and you will be found.",
			"tcp_ip": "202.31.134.87",
			"write_date": "2019-07-19 11:57:08",
			"update_date": None,
			"visit": 396,
			"ref": "201907190001"
		},
		{
			"user": "Alifia Putri Anantha",
			"subject": "There should be no boundaries to human endeavor",
			"tcp_ip": "202.31.137.57",
			"write_date": "2019-07-26 14:11:44",
			"update_date": None,
			"visit": 402,
			"ref": "201907260001"
		},
		{
			"user": "Ade Pitra Hermawan",
			"subject": "You can&#39;t go back and change the beginning, but you can start where you are and change the ending.",
			"tcp_ip": "202.31.137.124",
			"write_date": "2019-07-26 15:28:48",
			"update_date": None,
			"visit": 2290,
			"ref": "201907260002"
		},
		{
			"user": "mohtasin golam",
			"subject": "“When other’s advice disturbed you, it’s called arrogance.’’  - Imam Ghazali.",
			"tcp_ip": "202.31.137.55",
			"write_date": "2019-08-01 14:50:22",
			"update_date": None,
			"visit": 391,
			"ref": "201908010001"
		},
		{
			"user": "MD SAJJAD HOSSAIN",
			"subject": "“Life is really simple, but we insist on making it complicated.”  user Confucius",
			"tcp_ip": "202.31.137.138",
			"write_date": "2019-08-09 04:53:01",
			"update_date": None,
			"visit": 437,
			"ref": "201908090001"
		},
		{
			"user": "Philip TD",
			"subject": "If you&#39;re afraid to fail, then you&#39;re probably going to fail. - Kobe Bryant.",
			"tcp_ip": "",
			"write_date": "2019-08-09 15:58:45",
			"update_date": "2019-08-09 16:00:31",
			"visit": 1132,
			"ref": "201908090002"
		},
		{
			"user": "NWAKANMA COSMAS IFEA",
			"subject": "&#34;If you want to go fast, go alone.    If you want to go far, go together.”  &#8211; African Proverb",
			"tcp_ip": "202.31.137.61",
			"write_date": "2019-08-16 22:13:27",
			"update_date": None,
			"visit": 408,
			"ref": "201908160001"
		},
		{
			"user": "김치윤",
			"subject": "&#34;I choose my own feelings. Today, I choose &#39;happiness.&#39;&#34;",
			"tcp_ip": "",
			"write_date": "2019-08-19 13:05:17",
			"update_date": "2019-08-19 13:06:08",
			"visit": 424,
			"ref": "201908190001"
		},
		{
			"user": "김다혜",
			"subject": "They must often change who would remain constant in happiness and wisdom",
			"tcp_ip": "",
			"write_date": "2019-08-22 13:48:13",
			"update_date": "2019-08-22 13:48:31",
			"visit": 380,
			"ref": "201908220001"
		},
		{
			"user": "Williams Paul",
			"subject": "&#34;The greatest danger for most of us is not that our aim is too high and we miss it, but that is too low and we reach it&#34;",
			"tcp_ip": "202.31.134.97",
			"write_date": "2019-08-23 15:23:35",
			"update_date": None,
			"visit": 435,
			"ref": "201908230001"
		},
		{
			"user": "Muhammad Rusyadi",
			"subject": "Being productive and being busy are not necessarily the same thing. Doing things won’t create your success; doing the right things will.",
			"tcp_ip": "117.20.203.76",
			"write_date": "2019-08-30 02:56:00",
			"update_date": None,
			"visit": 360,
			"ref": "201908300001"
		},
		{
			"user": "이종우",
			"subject": "Not allowing change is  a bad plan. - Publilius Syrus -",
			"tcp_ip": "202.31.137.123",
			"write_date": "2019-09-03 15:21:17",
			"update_date": None,
			"visit": 366,
			"ref": "201909030001"
		},
		{
			"user": "So-Hyang",
			"subject": "Everything in your world is created user what you think-Oprah Gail Winfrey",
			"tcp_ip": "118.235.32.142",
			"write_date": "2019-09-07 20:18:12",
			"update_date": None,
			"visit": 703,
			"ref": "201909070001"
		},
		{
			"user": "박성화",
			"subject": "I tried to live everyday as if was the final day of extraordinary, ordinary life",
			"tcp_ip": "223.39.139.56",
			"write_date": "2019-09-07 20:23:50",
			"update_date": None,
			"visit": 494,
			"ref": "201909070002"
		},
		{
			"user": "sanjay",
			"subject": "Showing off is the fool’s idea of glory……",
			"tcp_ip": "202.31.134.90",
			"write_date": "2019-09-19 20:10:17",
			"update_date": None,
			"visit": 397,
			"ref": "201909190001"
		},
		{
			"user": "Rizki Rivai Ginanjar",
			"subject": "The Scientific man does not aim at an immediate result. He does not expect that his advanced ideas will be readily taken up. His work is like that of the planter - for the future. His duty is to lay the foundation for those who are to come and point the way.",
			"tcp_ip": "202.31.134.83",
			"write_date": "2019-09-20 14:50:39",
			"update_date": None,
			"visit": 371,
			"ref": "201909200001"
		},
		{
			"user": "Gaspard Gashema",
			"subject": "Happiness is a choice, not a result. Nothing will make you happy until you choose to be happy. No person will make you happy unless you decide to be happy. Your happiness will not come to you. It can only come from you",
			"tcp_ip": "",
			"write_date": "2019-09-26 21:08:31",
			"update_date": "2019-09-26 21:11:28",
			"visit": 2292,
			"ref": "201909260001"
		},
		{
			"user": "Saviour",
			"subject": "Friendship is the hardest thing in the world to explain. It’s not something you learn in school. But if you haven’t learned the meaning of friendship, you really haven’t learned anything.",
			"tcp_ip": "",
			"write_date": "2019-09-27 13:37:00",
			"update_date": "2019-09-27 13:37:54",
			"visit": 435,
			"ref": "201909270001"
		},
		{
			"user": "Kevin Putra Dirganto",
			"subject": "Learning without thinking is useless, but thinking without learning is very dangerous.",
			"tcp_ip": "220.122.192.49",
			"write_date": "2019-10-04 09:04:50",
			"update_date": None,
			"visit": 358,
			"ref": "201910040001"
		},
		{
			"user": "Nita Hidayati",
			"subject": "The 3 C &#39;s in life, Choice,Chance, and Change. you must make a choice, to take a chance, if you want anything in life to change",
			"tcp_ip": "121.151.244.100",
			"write_date": "2019-10-04 13:24:56",
			"update_date": None,
			"visit": 455,
			"ref": "201910040002"
		},
		{
			"user": "Muhammad Taufiq Rama",
			"subject": "You were born to make mistakes, not to fake perfection",
			"tcp_ip": "59.24.105.32",
			"write_date": "2019-10-11 07:55:50",
			"update_date": None,
			"visit": 396,
			"ref": "201910110001"
		},
		{
			"user": "Heidy Indrayani",
			"subject": "Do what you can&#39;t",
			"tcp_ip": "39.121.103.57",
			"write_date": "2019-10-11 13:22:57",
			"update_date": None,
			"visit": 428,
			"ref": "201910110002"
		},
		{
			"user": "Riesa Krisna Astuti",
			"subject": "Higher IQ is useless if you are lazy and not discipline, the important thing is that you are healthy and want to contribute for a bright future.",
			"tcp_ip": "202.31.137.34",
			"write_date": "2019-10-22 12:27:25",
			"update_date": None,
			"visit": 404,
			"ref": "201910220001"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "If you can see it in your mind, you can hold it in your hand. &#39;&#39;Bob Proctor&#39;&#39;",
			"tcp_ip": "202.31.134.99",
			"write_date": "2019-10-22 13:21:38",
			"update_date": None,
			"visit": 389,
			"ref": "201910220002"
		},
		{
			"user": "mohtasin golam",
			"subject": "Sharing idea is a process of learning",
			"tcp_ip": "202.31.137.55",
			"write_date": "2019-11-01 15:45:28",
			"update_date": None,
			"visit": 437,
			"ref": "201911010001"
		},
		{
			"user": "Ade Pitra Hermawan",
			"subject": "Efforts and courage are not enough without purpose and direction. - John F. Kennedy",
			"tcp_ip": "220.122.192.48",
			"write_date": "2019-11-01 18:48:57",
			"update_date": None,
			"visit": 452,
			"ref": "201911010002"
		},
		{
			"user": "김치윤",
			"subject": "To see the world,  things dangerous to come to,  to see behind walls,  draw closer,  to find each other, and to feel.  That is the purpose of life.",
			"tcp_ip": "192.168.210.25",
			"write_date": "2019-11-05 14:15:10",
			"update_date": None,
			"visit": 919,
			"ref": "201911050001"
		},
		{
			"user": "MD SAJJAD HOSSAIN",
			"subject": "You have to put in the hours because there’s always something which you can improve.”&#160;Roger Federer",
			"tcp_ip": "202.31.137.138",
			"write_date": "2019-11-07 17:49:24",
			"update_date": None,
			"visit": 343,
			"ref": "201911070001"
		},
		{
			"user": "Alifia Putri Anantha",
			"subject": "If you can&#39;t fly, then run, if you can&#39;t run then walk, if you can&#39;t walk, then crawl, but whatever you do, you have to keep moving forward.",
			"tcp_ip": "202.31.137.57",
			"write_date": "2019-11-08 14:31:05",
			"update_date": None,
			"visit": 406,
			"ref": "201911080001"
		},
		{
			"user": "NWAKANMA COSMAS IFEA",
			"subject": "Written dream is a goal, Dated goal is a plan, plan supported with action becomes REALITY",
			"tcp_ip": "202.31.137.61",
			"write_date": "2019-11-15 09:19:42",
			"update_date": None,
			"visit": 966,
			"ref": "201911150001"
		},
		{
			"user": "Philip TD",
			"subject": "Check your ego at the door. The ego can be the great success inhibitor. It can kill opportunities and it can kill success.",
			"tcp_ip": "59.24.108.129",
			"write_date": "2019-11-15 11:33:31",
			"update_date": None,
			"visit": 421,
			"ref": "201911150002"
		},
		{
			"user": "Rubina Akter",
			"subject": "Dreams is not what you see in sleep, Is the thing which does not let you sleep",
			"tcp_ip": "202.31.134.87",
			"write_date": "2019-11-22 15:10:05",
			"update_date": None,
			"visit": 387,
			"ref": "201911220001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "If your always trying to be normal you will never know how amazing you can be - Maya Angelou",
			"tcp_ip": "202.31.134.82",
			"write_date": "2019-11-22 15:25:47",
			"update_date": None,
			"visit": 394,
			"ref": "201911220002"
		},
		{
			"user": "김형진",
			"subject": "Good relationship is not good start one  but end well one",
			"tcp_ip": "202.31.137.139",
			"write_date": "2019-12-02 13:12:04",
			"update_date": None,
			"visit": 445,
			"ref": "201912020001"
		},
		{
			"user": "장민희",
			"subject": "The greatest part of our happiness or misery depends on our dispositions and not on our circumstances - Matha Washington",
			"tcp_ip": "202.31.137.137",
			"write_date": "2019-12-02 13:15:21",
			"update_date": None,
			"visit": 467,
			"ref": "201912020002"
		},
		{
			"user": "Aj",
			"subject": "Don&#39;t ever let someone tell you that you can&#39;t do something. Not even me. You got a dream, you gotta protect it. When people can&#39;t do something themselves, they&#39;re gonna tell you that you can&#39;t do it. You want something, go get it. Period.-Will Smith (The Pursuit of Happyness, film)",
			"tcp_ip": "",
			"write_date": "2019-12-09 07:12:30",
			"update_date": "2019-12-09 07:13:06",
			"visit": 2132,
			"ref": "201912090001"
		},
		{
			"user": "Godwin Tunze",
			"subject": "Once you stop learning, you start dying",
			"tcp_ip": "202.31.137.118",
			"write_date": "2019-12-13 15:07:37",
			"update_date": None,
			"visit": 436,
			"ref": "201912130001"
		},
		{
			"user": "danielle agron",
			"subject": "It is more important to have a happy life than a so called successful life, because success can be defined in so many ways. Just being happy is a success in itself. - Miriam Defensor Santiago",
			"tcp_ip": "202.31.134.81",
			"write_date": "2019-12-15 15:03:19",
			"update_date": None,
			"visit": 403,
			"ref": "201912150001"
		},
		{
			"user": "Gabriel",
			"subject": "A fool and a wise man",
			"tcp_ip": "202.31.134.91",
			"write_date": "2019-12-20 13:35:54",
			"update_date": None,
			"visit": 412,
			"ref": "201912200001"
		},
		{
			"user": "Williams",
			"subject": "Williams - &#34;If you cannot reason beyond petty sentiments, you are a liability to mankind.",
			"tcp_ip": "202.31.134.97",
			"write_date": "2019-12-26 19:08:55",
			"update_date": None,
			"visit": 521,
			"ref": "201912260001"
		},
		{
			"user": "sanjay",
			"subject": "Work out your own salvation. Do not depend on others.",
			"tcp_ip": "202.31.134.90",
			"write_date": "2020-01-09 20:27:25",
			"update_date": None,
			"visit": 386,
			"ref": "202001090001"
		},
		{
			"user": "관리자",
			"subject": "the happiest people are not hose getting more but those giving more",
			"tcp_ip": "202.31.134.96",
			"write_date": "2020-01-10 14:15:43",
			"update_date": None,
			"visit": 379,
			"ref": "202001100001"
		},
		{
			"user": "Gaspard",
			"subject": "When we meet real tragedy in life, we can react in two ways--either user losing hope and falling into self-destructive habits, or user using the challenge to find our inner strength",
			"tcp_ip": "202.31.134.83",
			"write_date": "2020-01-13 21:50:35",
			"update_date": None,
			"visit": 1271,
			"ref": "202001130001"
		},
		{
			"user": "관리자",
			"subject": "The people who are crazy enough to think they can change the world are the ones who do.",
			"tcp_ip": "202.31.134.86",
			"write_date": "2020-01-22 20:17:50",
			"update_date": None,
			"visit": 377,
			"ref": "202001220001"
		},
		{
			"user": "Nita Hidayati",
			"subject": "Shoot for the moon, even if you miss you&#39;ll land among the stars",
			"tcp_ip": "59.24.105.32",
			"write_date": "2020-01-23 09:11:23",
			"update_date": None,
			"visit": 890,
			"ref": "202001230001"
		},
		{
			"user": "Muhammad Taufiq Rama",
			"subject": "your best teacher is your last mistake",
			"tcp_ip": "202.31.137.38",
			"write_date": "2020-01-31 14:43:00",
			"update_date": None,
			"visit": 376,
			"ref": "202001310001"
		},
		{
			"user": "Heidy Indrayani",
			"subject": "Train your main to see the good in every situations",
			"tcp_ip": "39.121.103.57",
			"write_date": "2020-01-31 21:54:01",
			"update_date": None,
			"visit": 401,
			"ref": "202001310002"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "Be a student not a follower. Judge all things and hold fast to that which you believe to be true for you.   &#39;&#39;Jim Rohn&#39;&#39;.",
			"tcp_ip": "202.31.134.99",
			"write_date": "2020-02-07 13:03:26",
			"update_date": None,
			"visit": 407,
			"ref": "202002070001"
		},
		{
			"user": "Riesa Krisna Astuti",
			"subject": "You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.",
			"tcp_ip": "202.31.134.94",
			"write_date": "2020-02-07 15:58:44",
			"update_date": None,
			"visit": 392,
			"ref": "202002070002"
		},
		{
			"user": "Aouto, Ali",
			"subject": "“Don&#39;t be a salad, be the best goddamn broccoli you could ever be” - Felix Kjellberg (Pewdiepie)",
			"tcp_ip": "202.31.134.82",
			"write_date": "2020-02-24 15:23:55",
			"update_date": None,
			"visit": 757,
			"ref": "202002240001"
		},
		{
			"user": "Aj",
			"subject": "You don&#39;t have to understand. You just have to have faith... Faith in destiny.",
			"tcp_ip": "117.20.203.50",
			"write_date": "2020-03-14 13:41:01",
			"update_date": None,
			"visit": 344,
			"ref": "202003140001"
		},
		{
			"user": "Ade Pitra",
			"subject": "The Best Way to Predict Your Future is to Create it",
			"tcp_ip": "202.31.137.55",
			"write_date": "2020-03-16 14:55:18",
			"update_date": None,
			"visit": 372,
			"ref": "202003160001"
		},
		{
			"user": "Cosmas",
			"subject": "Everybody Has Something. The difference is Some Know How to Use it",
			"tcp_ip": "",
			"write_date": "2020-03-20 10:42:19",
			"update_date": "2020-03-20 10:47:42",
			"visit": 2410,
			"ref": "202003200001"
		},
		{
			"user": "mohtasin golam",
			"subject": "Be the change that you wish to see in the world",
			"tcp_ip": "",
			"write_date": "2020-03-20 15:57:03",
			"update_date": "2020-03-22 22:57:21",
			"visit": 359,
			"ref": "202003200002"
		},
		{
			"user": "Alifia Putri Anantha",
			"subject": "Don&#39;t limit your challenges, challenge your limits",
			"tcp_ip": "",
			"write_date": "2020-03-23 15:18:23",
			"update_date": "2020-03-23 15:20:10",
			"visit": 428,
			"ref": "202003230001"
		},
		{
			"user": "Philip TD",
			"subject": "The way to succeed is to DOUBLE your FAILURE RATE.",
			"tcp_ip": "220.122.192.51",
			"write_date": "2020-04-03 02:59:03",
			"update_date": None,
			"visit": 367,
			"ref": "202004030001"
		},
		{
			"user": "Rubina Akter",
			"subject": "Wisely, and slow, They stumble that run fast.",
			"tcp_ip": "202.31.134.87",
			"write_date": "2020-04-13 14:59:58",
			"update_date": None,
			"visit": 428,
			"ref": "202004130001"
		},
		{
			"user": "김형진",
			"subject": "Happiness can be found even in the darkest of times, if one only remembers to turn on the light.",
			"tcp_ip": "202.31.137.139",
			"write_date": "2020-04-17 12:32:08",
			"update_date": None,
			"visit": 459,
			"ref": "202004170001"
		},
		{
			"user": "Gabriel",
			"subject": "Until the lion learns how to write, every story will glorify the hunter",
			"tcp_ip": "14.56.242.225",
			"write_date": "2020-04-17 19:11:06",
			"update_date": None,
			"visit": 435,
			"ref": "202004170002"
		},
		{
			"user": "danielle agron",
			"subject": "Nothing in this world is difficult, but thinking makes it seem so.",
			"tcp_ip": "202.31.137.137",
			"write_date": "2020-04-23 18:36:15",
			"update_date": None,
			"visit": 385,
			"ref": "202004230001"
		},
		{
			"user": "Godwin Tunze",
			"subject": "Whether you think you can, or think you can’t you’re right",
			"tcp_ip": "",
			"write_date": "2020-04-24 07:06:58",
			"update_date": "2020-04-24 07:08:13",
			"visit": 421,
			"ref": "202004240001"
		},
		{
			"user": "김치윤",
			"subject": "What does not destroy me makes me stronger",
			"tcp_ip": "",
			"write_date": "2020-04-29 13:46:06",
			"update_date": "2020-04-29 13:48:35",
			"visit": 651,
			"ref": "202004290001"
		},
		{
			"user": "Mareska Pratiwi Maha",
			"subject": "I never lose. I either win or learn.",
			"tcp_ip": "",
			"write_date": "2020-04-29 14:54:33",
			"update_date": "2020-05-04 17:01:08",
			"visit": 4362,
			"ref": "202004290002"
		},
		{
			"user": "Choi Si Yeong",
			"subject": "The greatest glory in living lies not in never falling, but in rising every time we fall",
			"tcp_ip": "202.31.134.93",
			"write_date": "2020-05-08 03:22:56",
			"update_date": None,
			"visit": 530,
			"ref": "202005080001"
		},
		{
			"user": "Fabliha Bushra Islam",
			"subject": "You can&#39;t cross the sea merely user standing and staring at the water",
			"tcp_ip": "",
			"write_date": "2020-05-08 14:15:00",
			"update_date": "2020-05-08 14:33:42",
			"visit": 488,
			"ref": "202005080002"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "If you shed tears when you miss the sun You also miss the stars",
			"tcp_ip": "37.211.91.13",
			"write_date": "2020-05-10 16:59:51",
			"update_date": None,
			"visit": 450,
			"ref": "202005100001"
		},
		{
			"user": "이종우",
			"subject": "No sweat, No sweet",
			"tcp_ip": "202.31.134.88",
			"write_date": "2020-06-15 11:14:21",
			"update_date": None,
			"visit": 692,
			"ref": "202006150001"
		},
		{
			"user": "Ade Pitra Hermawan",
			"subject": "The Best Investment you can make, is an investment in yourself... The more you learn, the more you&#39;ll earn. - Warren Buffett",
			"tcp_ip": "202.31.137.55",
			"write_date": "2020-06-18 20:58:15",
			"update_date": None,
			"visit": 440,
			"ref": "202006180001"
		},
		{
			"user": "김시완",
			"subject": "Do not doubt. It is also an important ability of studying. The idea of &#34;can do it&#34; is the ability to study.",
			"tcp_ip": "",
			"write_date": "2020-06-26 15:24:20",
			"update_date": "2020-06-26 15:26:58",
			"visit": 360,
			"ref": "202006260001"
		},
		{
			"user": "김경선",
			"subject": "If you get tired, you lose,   if you go crazy, you win",
			"tcp_ip": "202.31.137.39",
			"write_date": "2020-06-26 15:37:35",
			"update_date": None,
			"visit": 353,
			"ref": "202006260002"
		},
		{
			"user": "mohtasin golam",
			"subject": "The greatest glory in living lies not in never falling, but in rising every time we fail.",
			"tcp_ip": "",
			"write_date": "2020-07-03 02:23:50",
			"update_date": "2020-07-03 02:24:38",
			"visit": 359,
			"ref": "202007030001"
		},
		{
			"user": "김치윤",
			"subject": "He who would learn to fly one day must first learn to stand and walk and run and climb and dance;  one cannot fly into flying",
			"tcp_ip": "202.31.134.92",
			"write_date": "2020-07-03 14:33:38",
			"update_date": None,
			"visit": 382,
			"ref": "202007030002"
		},
		{
			"user": "Cosmas",
			"subject": "No matter how smart you are, if you never know how to work with people, you will never be successful (Jack Ma)",
			"tcp_ip": "",
			"write_date": "2020-07-10 12:58:04",
			"update_date": "2020-10-29 09:26:19",
			"visit": 388,
			"ref": "202007100001"
		},
		{
			"user": "Alifia Putri Anantha",
			"subject": "Doubt kills more dreams than failure ever will - Suzy Kassem",
			"tcp_ip": "202.31.137.57",
			"write_date": "2020-07-10 14:16:41",
			"update_date": None,
			"visit": 339,
			"ref": "202007100002"
		},
		{
			"user": "MD SAJJAD HOSSAIN",
			"subject": "A winner is a dreamer , who never gives up----- Nelson Mandela",
			"tcp_ip": "202.31.134.95",
			"write_date": "2020-07-17 00:48:34",
			"update_date": None,
			"visit": 344,
			"ref": "202007170001"
		},
		{
			"user": "Philip TD",
			"subject": "People often say that motivation doesn&#39;t last. Well, neither does bathing -- that&#39;s why we recommend it daily.",
			"tcp_ip": "220.122.192.51",
			"write_date": "2020-07-17 15:47:10",
			"update_date": None,
			"visit": 332,
			"ref": "202007170002"
		},
		{
			"user": "Rubina Akter",
			"subject": "Everything negative pressure and challenges are all an opportunity for me to rise.",
			"tcp_ip": "202.31.134.87",
			"write_date": "2020-07-24 12:07:12",
			"update_date": None,
			"visit": 1291,
			"ref": "202007240001"
		},
		{
			"user": "장민희",
			"subject": "Life is a journey with everyone.  All we can do while we live every day is do our best to enjoy this wonderful trip.",
			"tcp_ip": "",
			"write_date": "2020-07-30 13:52:24",
			"update_date": "2020-07-30 13:55:08",
			"visit": 359,
			"ref": "202007300001"
		},
		{
			"user": "김형진",
			"subject": "Why can&#39;t I love myself?  Because you can&#39;t love others",
			"tcp_ip": "202.31.137.139",
			"write_date": "2020-07-31 10:49:41",
			"update_date": None,
			"visit": 355,
			"ref": "202007310001"
		},
		{
			"user": "Godwin Tunze",
			"subject": "Education is not learning of the facts but the training of the mind to think",
			"tcp_ip": "202.31.134.85",
			"write_date": "2020-08-28 13:45:33",
			"update_date": None,
			"visit": 3404,
			"ref": "202008280001"
		},
		{
			"user": "Aj",
			"subject": "When life puts you in tough situations, don&#39;t say &#34;why me&#34;, say &#34;try me&#34; - anon",
			"tcp_ip": "112.217.167.202",
			"write_date": "2020-08-28 16:20:22",
			"update_date": None,
			"visit": 2530,
			"ref": "202008280002"
		},
		{
			"user": "danielle agron",
			"subject": "A smooth sea never made a skilled sailor",
			"tcp_ip": "220.122.113.64",
			"write_date": "2020-09-04 01:44:07",
			"update_date": None,
			"visit": 304,
			"ref": "202009040001"
		},
		{
			"user": "Gabriel",
			"subject": "Manners Maketh A Man",
			"tcp_ip": "202.31.137.117",
			"write_date": "2020-09-04 15:26:46",
			"update_date": None,
			"visit": 300,
			"ref": "202009040002"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "Luxury and Lies have huge maintenance costs. But Truth and Simplicity are self-maintained without any cost. --APJ Abdul Kalam",
			"tcp_ip": "202.31.134.88",
			"write_date": "2020-09-11 12:30:18",
			"update_date": None,
			"visit": 298,
			"ref": "202009110001"
		},
		{
			"user": "Mareska Pratiwi Maha",
			"subject": "To be or not to be",
			"tcp_ip": "",
			"write_date": "2020-09-11 13:57:14",
			"update_date": "2020-09-11 13:58:27",
			"visit": 329,
			"ref": "202009110002"
		},
		{
			"user": "Simeon",
			"subject": "All achievement, all earned riches, all phenomenal concept, have their beginning in an idea!~~~ Napoleon Hill",
			"tcp_ip": "",
			"write_date": "2020-09-18 10:25:59",
			"update_date": "2020-09-18 10:27:47",
			"visit": 307,
			"ref": "202009180001"
		},
		{
			"user": "Fabliha Bushra Islam",
			"subject": "Now is no time to think of what you do not have. Think of what you can do with what there is",
			"tcp_ip": "202.31.137.124",
			"write_date": "2020-09-18 15:21:41",
			"update_date": None,
			"visit": 312,
			"ref": "202009180002"
		},
		{
			"user": "Yohana Jayanti Aruan",
			"subject": "&#34;You can&#39;t expect to win, unless you know why you lose&#34;",
			"tcp_ip": "36.71.234.18",
			"write_date": "2020-09-25 13:35:14",
			"update_date": None,
			"visit": 352,
			"ref": "202009250001"
		},
		{
			"user": "이종우",
			"subject": "&#34;Life is like playing a violin in public and  learning the instrument  as one goes on&#34;",
			"tcp_ip": "202.31.134.95",
			"write_date": "2020-09-25 13:54:45",
			"update_date": None,
			"visit": 363,
			"ref": "202009250002"
		},
		{
			"user": "Saviour",
			"subject": "When a thing is done, it’s done. Don’t look back. Look forward to your next objective.",
			"tcp_ip": "202.31.137.110",
			"write_date": "2020-09-25 16:02:42",
			"update_date": None,
			"visit": 304,
			"ref": "202009250003"
		},
		{
			"user": "NWAKANMA COSMAS IFEA",
			"subject": "Without a sense of caring, there can be no sense of community-- Anthony Burgess (1993)",
			"tcp_ip": "",
			"write_date": "2020-10-29 09:18:57",
			"update_date": "2020-10-29 09:21:05",
			"visit": 299,
			"ref": "202010290001"
		},
		{
			"user": "Philip TD",
			"subject": "A wise man knows a wise man knows nothin’.",
			"tcp_ip": "220.122.192.51",
			"write_date": "2020-10-30 01:51:53",
			"update_date": None,
			"visit": 301,
			"ref": "202010300001"
		},
		{
			"user": "MD SAJJAD HOSSAIN",
			"subject": "&#34;Setting goals is the first step in turning the invisible into the visible.&#34;------- Tony Robbins - American businessman, author",
			"tcp_ip": "",
			"write_date": "2020-11-09 06:26:38",
			"update_date": "2020-11-09 06:28:04",
			"visit": 290,
			"ref": "202011090001"
		},
		{
			"user": "Rubina Akter",
			"subject": "However difficult life may seem, there is always something you can do and succeed At",
			"tcp_ip": "202.31.134.87",
			"write_date": "2020-11-16 14:59:43",
			"update_date": None,
			"visit": 321,
			"ref": "202011160001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "“Even if there’s nothing here today, there might be something tomorrow. It’s a caring heart that’s important.”",
			"tcp_ip": "202.31.134.86",
			"write_date": "2020-11-18 18:49:49",
			"update_date": None,
			"visit": 343,
			"ref": "202011180001"
		},
		{
			"user": "Godwin Tunze",
			"subject": "You don&#39;t learn to walk user following rules. You learn user doing, and user falling over",
			"tcp_ip": "202.31.134.85",
			"write_date": "2020-11-19 23:49:04",
			"update_date": None,
			"visit": 299,
			"ref": "202011190001"
		},
		{
			"user": "Aj",
			"subject": "Intelligence plus character - that is the goal of true education",
			"tcp_ip": "202.31.134.84",
			"write_date": "2020-11-27 11:33:38",
			"update_date": None,
			"visit": 1179,
			"ref": "202011270001"
		},
		{
			"user": "danielle agron",
			"subject": "The best way to predict the future is to create it - Abraham Lincoln",
			"tcp_ip": "202.31.137.125",
			"write_date": "2020-11-27 15:32:01",
			"update_date": None,
			"visit": 294,
			"ref": "202011270002"
		},
		{
			"user": "Mareska Pratiwi Maha",
			"subject": "&#34;To a great mind nothing is little&#34; -Sherlock Holmes-",
			"tcp_ip": "117.20.203.63",
			"write_date": "2020-12-04 06:13:23",
			"update_date": None,
			"visit": 310,
			"ref": "202012040001"
		},
		{
			"user": "김형진",
			"subject": "If you only read the books that everyone else is reading, you can only think what everyone else is thinking",
			"tcp_ip": "202.31.137.139",
			"write_date": "2020-12-04 14:58:54",
			"update_date": None,
			"visit": 299,
			"ref": "202012040002"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "I walk all day. My roads never end. Journey without any destination shouldn’t have an end.",
			"tcp_ip": "202.31.134.88",
			"write_date": "2020-12-11 13:57:59",
			"update_date": None,
			"visit": 1405,
			"ref": "202012110001"
		},
		{
			"user": "Fabliha Bushra Islam",
			"subject": "Reach high, for stars lie hidden in your soul. Dream deep for every dream precedes the goal",
			"tcp_ip": "202.31.137.124",
			"write_date": "2020-12-11 14:57:25",
			"update_date": None,
			"visit": 277,
			"ref": "202012110002"
		},
		{
			"user": "Simeon",
			"subject": "Any Sufficiently advanced technology is indistinguishable from magic~ Arthur C Clarke, profile of the future 1961",
			"tcp_ip": "202.31.137.140",
			"write_date": "2020-12-18 12:39:12",
			"update_date": None,
			"visit": 490,
			"ref": "202012180001"
		},
		{
			"user": "Ade Pitra",
			"subject": "The Greatest Prison People Live in is The Fear of What Other People Think - JOKER",
			"tcp_ip": "",
			"write_date": "2020-12-18 13:52:32",
			"update_date": "2020-12-18 13:53:31",
			"visit": 274,
			"ref": "202012180002"
		},
		{
			"user": "Chio Aruan",
			"subject": "&#34;I never lose. I either win or learn.&#34; Nelson Mandela",
			"tcp_ip": "118.97.57.13",
			"write_date": "2020-12-18 14:01:01",
			"update_date": None,
			"visit": 276,
			"ref": "202012180003"
		},
		{
			"user": "Alifia Putri Anantha",
			"subject": "Working hard is important. But there’s something that matters even more. Believing in yourself.",
			"tcp_ip": "202.31.137.123",
			"write_date": "2020-12-22 15:48:42",
			"update_date": None,
			"visit": 366,
			"ref": "202012220001"
		},
		{
			"user": "Gabriel Avelino Samp",
			"subject": "It is the time you have wasted for your rose that makes your rose so important.",
			"tcp_ip": "175.176.23.48",
			"write_date": "2020-12-28 15:32:59",
			"update_date": None,
			"visit": 678,
			"ref": "202012280001"
		},
		{
			"user": "장민희",
			"subject": "Life is either a daring adventure or nothing",
			"tcp_ip": "",
			"write_date": "2021-01-04 16:13:39",
			"update_date": "2021-01-04 16:14:22",
			"visit": 277,
			"ref": "202101040001"
		},
		{
			"user": "Saviour",
			"subject": "A mind of moderate capacity which closely pursues one study must infallibly arrive at great proficiency in that study.",
			"tcp_ip": "121.182.237.167",
			"write_date": "2021-01-08 15:38:42",
			"update_date": None,
			"visit": 310,
			"ref": "202101080001"
		},
		{
			"user": "이종우",
			"subject": "The only thing worse than starting something and failing is not starting something. -Seth Godin-",
			"tcp_ip": "202.31.134.95",
			"write_date": "2021-01-08 16:23:03",
			"update_date": None,
			"visit": 338,
			"ref": "202101080002"
		},
		{
			"user": "Cosmas",
			"subject": "Intelligence is the Ability to Adapt to Changes: Stephen Hawking",
			"tcp_ip": "202.31.137.140",
			"write_date": "2021-01-09 12:13:20",
			"update_date": None,
			"visit": 320,
			"ref": "202101090001"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "If you are not in the process of becoming the person you want to be, you are automatically engaged in becoming the person you don’t want to be",
			"tcp_ip": "202.31.134.88",
			"write_date": "2021-01-19 17:07:30",
			"update_date": None,
			"visit": 307,
			"ref": "202101190001"
		},
		{
			"user": "Philip TD",
			"subject": "Time changes everything. That’s what people say, it’s not true. Doing things changes things. Not doing things leaves things exactly as they were. ~ Dr. Gregory House",
			"tcp_ip": "220.122.192.51",
			"write_date": "2021-01-21 03:30:29",
			"update_date": None,
			"visit": 314,
			"ref": "202101210001"
		},
		{
			"user": "Rubina Akter",
			"subject": "Focus means saying no to the hundred other good ideas",
			"tcp_ip": "202.31.134.87",
			"write_date": "2021-01-22 11:37:06",
			"update_date": None,
			"visit": 288,
			"ref": "202101220001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "someone is sitting in the shade today because someone planted a tree long time ago - Warren Buffett",
			"tcp_ip": "202.31.134.86",
			"write_date": "2021-02-01 15:54:27",
			"update_date": None,
			"visit": 323,
			"ref": "202102010001"
		},
		{
			"user": "MD SAJJAD HOSSAIN",
			"subject": "“The secret of getting ahead is getting started.” &#8211; Mark Twain",
			"tcp_ip": "202.31.134.92",
			"write_date": "2021-02-08 17:43:54",
			"update_date": None,
			"visit": 290,
			"ref": "202102080001"
		},
		{
			"user": "mohtasin golam",
			"subject": "One today is worth two tomorrows",
			"tcp_ip": "202.31.134.91",
			"write_date": "2021-02-09 13:17:49",
			"update_date": None,
			"visit": 314,
			"ref": "202102090001"
		},
		{
			"user": "김형진",
			"subject": "What you do not want done to yourself, do not do to others.",
			"tcp_ip": "202.31.137.139",
			"write_date": "2021-02-18 15:54:15",
			"update_date": None,
			"visit": 338,
			"ref": "202102180001"
		},
		{
			"user": "장민희",
			"subject": "If you don&#39;t know where you want to go, that means you can choose any path! _ Alice&#39;s Adventures in Wonderland",
			"tcp_ip": "202.31.137.137",
			"write_date": "2021-02-18 22:27:52",
			"update_date": None,
			"visit": 320,
			"ref": "202102180002"
		},
		{
			"user": "Aj",
			"subject": "Dream as if you’ll live forever, live as if you’ll die today. &#8211; James Dean",
			"tcp_ip": "202.31.137.119",
			"write_date": "2021-02-26 13:07:41",
			"update_date": None,
			"visit": 293,
			"ref": "202102260001"
		},
		{
			"user": "Godwin",
			"subject": "Coming together is the beginning; keeping together is the progress; working together is a success-Henry Ford",
			"tcp_ip": "202.31.134.85",
			"write_date": "2021-02-26 14:22:19",
			"update_date": None,
			"visit": 328,
			"ref": "202102260002"
		},
		{
			"user": "danielle agron",
			"subject": "The most common way people give up their power is user thinking they don&#39;t have any.",
			"tcp_ip": "202.31.137.125",
			"write_date": "2021-03-04 17:22:55",
			"update_date": None,
			"visit": 334,
			"ref": "202103040001"
		},
		{
			"user": "Mareska Pratiwi Maha",
			"subject": "&#34;Some people want it to happen, some wish it would happen, others make it happen&#34; -Michael Jordan",
			"tcp_ip": "117.20.203.63",
			"write_date": "2021-03-10 08:36:14",
			"update_date": None,
			"visit": 880,
			"ref": "202103100001"
		},
		{
			"user": "Chio Aruan",
			"subject": "If you define the problem correctly, you almost have the solution - Steve Jobs",
			"tcp_ip": "103.10.170.220",
			"write_date": "2021-03-26 00:00:12",
			"update_date": None,
			"visit": 270,
			"ref": "202103260001"
		},
		{
			"user": "이재현",
			"subject": "The moment you give up is the end of the match",
			"tcp_ip": "202.31.134.93",
			"write_date": "2021-03-29 12:47:53",
			"update_date": None,
			"visit": 328,
			"ref": "202103290001"
		},
		{
			"user": "Love",
			"subject": "Challenge yourself to be Innovative",
			"tcp_ip": "",
			"write_date": "2021-03-31 15:18:24",
			"update_date": "2021-03-31 16:25:18",
			"visit": 1078,
			"ref": "202103310001"
		},
		{
			"user": "Made Adi Paramartha",
			"subject": "Do it now! Sometimes &#39;later&#39; becomes &#39;never&#39;",
			"tcp_ip": "202.31.137.115",
			"write_date": "2021-04-02 14:16:00",
			"update_date": None,
			"visit": 382,
			"ref": "202104020001"
		},
		{
			"user": "Fabliha Bushra Islam",
			"subject": "Yesterday is History, Tomorrow is a Mystery, but Today is a Gift. That is why it is called The Present",
			"tcp_ip": "202.31.137.124",
			"write_date": "2021-04-02 16:05:00",
			"update_date": None,
			"visit": 964,
			"ref": "202104020002"
		},
		{
			"user": "Syifa Maliah Rachmaw",
			"subject": "Just Keep Swimming",
			"tcp_ip": "",
			"write_date": "2021-04-16 12:07:16",
			"update_date": "2021-04-16 12:08:43",
			"visit": 388,
			"ref": "202104160001"
		},
		{
			"user": "Adinda Riztia Putri",
			"subject": "If people are doubting how far you can go, go so far so you can’t hear them anymore",
			"tcp_ip": "202.31.137.116",
			"write_date": "2021-04-16 14:16:49",
			"update_date": None,
			"visit": 2077,
			"ref": "202104160002"
		},
		{
			"user": "Goodness",
			"subject": "The reward of a work well done is the opportunity to do more work",
			"tcp_ip": "",
			"write_date": "2021-04-22 10:50:53",
			"update_date": "2021-04-22 10:53:56",
			"visit": 358,
			"ref": "202104220001"
		},
		{
			"user": "Yusuf",
			"subject": "You miss 100% of the shots you don&#39;t take.",
			"tcp_ip": "",
			"write_date": "2021-04-22 14:13:40",
			"update_date": "2021-04-22 14:14:49",
			"visit": 383,
			"ref": "202104220002"
		},
		{
			"user": "Simeon Okechukwu Aja",
			"subject": "I.M.P.O.S.S.I.B.L.E means I&#39;M POSSIBLE",
			"tcp_ip": "",
			"write_date": "2021-04-29 14:11:05",
			"update_date": "2021-04-29 16:24:06",
			"visit": 331,
			"ref": "202104290001"
		},
		{
			"user": "Mark",
			"subject": "Better days to come.",
			"tcp_ip": "202.31.137.138",
			"write_date": "2021-04-30 10:25:17",
			"update_date": None,
			"visit": 376,
			"ref": "202104300001"
		},
		{
			"user": "NWAKANMA COSMAS IFEA",
			"subject": "If you want to change the world, go home and love your family ~ Mother Teresa",
			"tcp_ip": "",
			"write_date": "2021-05-07 09:15:17",
			"update_date": "2021-05-07 09:15:43",
			"visit": 326,
			"ref": "202105070001"
		},
		{
			"user": "Saviour",
			"subject": "Success is steady progress toward one’s personal goals",
			"tcp_ip": "202.31.134.207",
			"write_date": "2021-05-07 14:33:13",
			"update_date": None,
			"visit": 301,
			"ref": "202105070002"
		},
		{
			"user": "Godwin Tunze",
			"subject": "If a team is to reach its potential, each player must be willing to subordinate his personal goals to the  good of the team",
			"tcp_ip": "",
			"write_date": "2021-05-14 09:42:40",
			"update_date": "2021-05-14 09:43:21",
			"visit": 326,
			"ref": "202105140001"
		},
		{
			"user": "Rubina Akter",
			"subject": "A winner is a dreamer who never gives up-user Nelson Mandela",
			"tcp_ip": "202.31.134.87",
			"write_date": "2021-06-03 12:58:33",
			"update_date": None,
			"visit": 344,
			"ref": "202106030001"
		},
		{
			"user": "Philip TD",
			"subject": "The only easy day was yesterday. ~ US Navy SEALs",
			"tcp_ip": "202.31.134.95",
			"write_date": "2021-06-03 13:31:56",
			"update_date": None,
			"visit": 380,
			"ref": "202106030002"
		},
		{
			"user": "Aouto, Ali",
			"subject": "&#34; In anger we should refrain both from Speach and action&#34; - pythagoras",
			"tcp_ip": "202.31.137.120",
			"write_date": "2021-06-14 05:52:30",
			"update_date": None,
			"visit": 573,
			"ref": "202106140001"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "Speak A Good Word or Remain Silent",
			"tcp_ip": "202.31.134.88",
			"write_date": "2021-06-14 13:06:29",
			"update_date": None,
			"visit": 250,
			"ref": "202106140002"
		},
		{
			"user": "mohtasin golam",
			"subject": "&#34;Once we accept our limits, we go beyond them&#34;",
			"tcp_ip": "",
			"write_date": "2021-06-21 11:36:41",
			"update_date": "2021-06-21 11:37:05",
			"visit": 331,
			"ref": "202106210001"
		},
		{
			"user": "Rani",
			"subject": "&#34;I could either watch it happen or be a part of it&#34;",
			"tcp_ip": "202.31.137.123",
			"write_date": "2021-07-01 13:23:52",
			"update_date": None,
			"visit": 647,
			"ref": "202107010001"
		},
		{
			"user": "Fabliha Bushra Islam",
			"subject": "The longest way must have its close,- the gloomiest night will wear on to a morning",
			"tcp_ip": "202.31.137.124",
			"write_date": "2021-07-01 14:16:59",
			"update_date": None,
			"visit": 315,
			"ref": "202107010002"
		},
		{
			"user": "Gino",
			"subject": "“&#32536;木求&#40060;” “Don’t climb a tree to catch fish.”  Chinese Proverb",
			"tcp_ip": "202.31.137.119",
			"write_date": "2021-07-08 15:56:04",
			"update_date": None,
			"visit": 260,
			"ref": "202107080001"
		},
		{
			"user": "Simeon Okechukwu Aja",
			"subject": "Every Artist was first an Amateur",
			"tcp_ip": "202.31.134.97",
			"write_date": "2021-07-08 15:59:34",
			"update_date": None,
			"visit": 261,
			"ref": "202107080002"
		},
		{
			"user": "이재현",
			"subject": "Just do it!",
			"tcp_ip": "",
			"write_date": "2021-07-15 12:28:28",
			"update_date": "2021-07-15 12:29:05",
			"visit": 241,
			"ref": "202107150001"
		},
		{
			"user": "Chio Aruan",
			"subject": "“Most manifest sign of abundant intelligence is good planning.” - Imam Ali Ibn Abi Thalib",
			"tcp_ip": "103.140.79.202",
			"write_date": "2021-07-15 12:44:50",
			"update_date": None,
			"visit": 286,
			"ref": "202107150002"
		},
		{
			"user": "Made Adi Paramartha",
			"subject": "Life Begins at the End of Your Comfort Zone - Neale Donald Walsch",
			"tcp_ip": "202.31.137.115",
			"write_date": "2021-07-22 11:32:59",
			"update_date": None,
			"visit": 236,
			"ref": "202107220001"
		},
		{
			"user": "Love",
			"subject": "Successful people don&#39;t have fewer problems. They have determined that nothing will stop them from going forward.",
			"tcp_ip": "202.31.134.89",
			"write_date": "2021-07-22 11:54:11",
			"update_date": None,
			"visit": 299,
			"ref": "202107220002"
		},
		{
			"user": "Adinda Riztia Putri",
			"subject": "Adventure is out there",
			"tcp_ip": "202.31.137.126",
			"write_date": "2021-07-29 06:44:00",
			"update_date": None,
			"visit": 253,
			"ref": "202107290001"
		},
		{
			"user": "Syifa Maliah Rachmaw",
			"subject": "If you can dream it, you can do it",
			"tcp_ip": "202.31.137.116",
			"write_date": "2021-07-29 14:05:54",
			"update_date": None,
			"visit": 292,
			"ref": "202107290002"
		},
		{
			"user": "Goodness",
			"subject": "An Investment in Knowledge pays the best interest",
			"tcp_ip": "",
			"write_date": "2021-08-05 13:07:42",
			"update_date": "2021-08-05 14:19:01",
			"visit": 305,
			"ref": "202108050001"
		},
		{
			"user": "Yusuf",
			"subject": "Never let the fear of striking out keep you from playing the game.",
			"tcp_ip": "",
			"write_date": "2021-08-06 14:04:25",
			"update_date": "2021-08-06 14:04:41",
			"visit": 419,
			"ref": "202108060001"
		},
		{
			"user": "Mark",
			"subject": "Col. Harland Sanders",
			"tcp_ip": "122.199.68.171",
			"write_date": "2021-08-19 09:11:32",
			"update_date": None,
			"visit": 599,
			"ref": "202108190001"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "Walt Disney",
			"tcp_ip": "",
			"write_date": "2021-09-01 17:59:20",
			"update_date": "2021-09-01 18:02:43",
			"visit": 594,
			"ref": "202109010001"
		},
		{
			"user": "Revin",
			"subject": "Success does not belong to a smart person. Success belongs to those who always try.",
			"tcp_ip": "202.31.137.125",
			"write_date": "2021-09-02 13:32:20",
			"update_date": None,
			"visit": 338,
			"ref": "202109020001"
		},
		{
			"user": "Muhammad Rasyid Redh",
			"subject": "Quote user Ir. Soekarno, the First President of Indonesia",
			"tcp_ip": "112.217.167.202",
			"write_date": "2021-09-09 12:15:25",
			"update_date": None,
			"visit": 261,
			"ref": "202109090001"
		},
		{
			"user": "Allwinnaldo",
			"subject": "Allah give me everything, without Allah, we can do nothing - Khabib Nurmagomedov (29-0 MMA Fightrer - Greatest of All Time)",
			"tcp_ip": "112.217.167.202",
			"write_date": "2021-09-09 14:17:50",
			"update_date": None,
			"visit": 228,
			"ref": "202109090002"
		},
		{
			"user": "Vivian Ukamaka Iheko",
			"subject": "Success is not final, Failure is not fatal. It is the courage to continue that counts",
			"tcp_ip": "112.217.167.202",
			"write_date": "2021-09-27 12:15:08",
			"update_date": None,
			"visit": 247,
			"ref": "202109270001"
		},
		{
			"user": "NWAKANMA COSMAS IFEA",
			"subject": "Intelligence, energy, and Integrity are important but INTEGRITY is the BEST.",
			"tcp_ip": "202.31.137.140",
			"write_date": "2021-09-29 12:00:22",
			"update_date": None,
			"visit": 7977,
			"ref": "202109290001"
		},
		{
			"user": "Saviour",
			"subject": "Knowledge is of more value than gold.",
			"tcp_ip": "112.217.167.202",
			"write_date": "2021-09-30 21:25:55",
			"update_date": None,
			"visit": 207,
			"ref": "202109300001"
		},
		{
			"user": "관리자",
			"subject": "A fool thinks himself to be wise, but a wise man knows himself to be a fool",
			"tcp_ip": "202.31.134.87",
			"write_date": "2021-10-06 22:25:01",
			"update_date": None,
			"visit": 219,
			"ref": "202110060001"
		},
		{
			"user": "Philip TD",
			"subject": "Our deeds determine us, as much as we determine our deeds.",
			"tcp_ip": "202.31.134.95",
			"write_date": "2021-10-07 14:55:07",
			"update_date": None,
			"visit": 234,
			"ref": "202110070001"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "You can never cross the ocean until you have the courage to lose sight of the shore-Christopher Columbus",
			"tcp_ip": "",
			"write_date": "2021-10-12 13:40:51",
			"update_date": "2021-10-12 13:41:58",
			"visit": 278,
			"ref": "202110120001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "&#34;Man cannot remake himeself without suffering for he is both the marble and the sculptor&#34;",
			"tcp_ip": "202.31.137.120",
			"write_date": "2021-10-14 12:09:36",
			"update_date": None,
			"visit": 235,
			"ref": "202110140001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "&#34;Our shouting is louder than our actions, Our swords are taller that us, this is out tragedy. in short we wear the cape of civilisation but our souls live in the stone age&#34;",
			"tcp_ip": "202.31.137.120",
			"write_date": "2021-10-14 12:12:39",
			"update_date": None,
			"visit": 249,
			"ref": "202110140002"
		},
		{
			"user": "mohtasin golam",
			"subject": "While there’s life, there is hope.",
			"tcp_ip": "202.31.134.91",
			"write_date": "2021-10-28 13:32:55",
			"update_date": None,
			"visit": 341,
			"ref": "202110280001"
		},
		{
			"user": "장민희",
			"subject": "You can be happy every day, But there are happy things every day.",
			"tcp_ip": "202.31.137.137",
			"write_date": "2021-10-29 13:09:34",
			"update_date": None,
			"visit": 298,
			"ref": "202110290001"
		},
		{
			"user": "Simeon",
			"subject": "He who learns, teaches",
			"tcp_ip": "202.31.134.97",
			"write_date": "2021-11-11 11:31:11",
			"update_date": None,
			"visit": 253,
			"ref": "202111110001"
		},
		{
			"user": "김형진",
			"subject": "No possession doesn&#39;t mean you don&#39;t have anything, but you don&#39;t having unnecessary things",
			"tcp_ip": "202.31.137.139",
			"write_date": "2021-11-11 15:11:21",
			"update_date": None,
			"visit": 262,
			"ref": "202111110002"
		},
		{
			"user": "Chio Aruan",
			"subject": "Intelligence is the ability to adapt to change",
			"tcp_ip": "118.97.57.13",
			"write_date": "2021-11-22 13:07:26",
			"update_date": None,
			"visit": 286,
			"ref": "202111220001"
		},
		{
			"user": "Gabriel Avelino Samp",
			"subject": "Everyone thinks of changing the world, but no one thinks of changing himself.",
			"tcp_ip": "130.105.194.170",
			"write_date": "2021-11-22 16:53:19",
			"update_date": None,
			"visit": 233,
			"ref": "202111220002"
		},
		{
			"user": "Love",
			"subject": "People will Never Forget How You made them Feel",
			"tcp_ip": "202.31.134.85",
			"write_date": "2021-11-25 14:31:11",
			"update_date": None,
			"visit": 227,
			"ref": "202111250001"
		},
		{
			"user": "이재현",
			"subject": "Efficiency is doing things right. Effectiveness is doing the right things.  -Peter F. Drucker-",
			"tcp_ip": "202.31.134.93",
			"write_date": "2021-12-02 06:56:05",
			"update_date": None,
			"visit": 202,
			"ref": "202112020001"
		},
		{
			"user": "Made Adi Paramartha",
			"subject": "Reward Yourself for the Work You&#39;ve Done Daily. It will keep you working harder.",
			"tcp_ip": "202.31.137.115",
			"write_date": "2021-12-02 10:44:27",
			"update_date": None,
			"visit": 210,
			"ref": "202112020002"
		},
		{
			"user": "Syifa Maliah Rachmaw",
			"subject": "&#34;The past can hurt. But the way I see it, you can either run from it or learn from it.&#34;",
			"tcp_ip": "117.20.203.63",
			"write_date": "2021-12-08 22:54:51",
			"update_date": None,
			"visit": 246,
			"ref": "202112080001"
		},
		{
			"user": "Adinda Riztia Putri",
			"subject": "Worrying is like paying a debt you do not owe",
			"tcp_ip": "117.20.203.63",
			"write_date": "2021-12-09 03:08:10",
			"update_date": None,
			"visit": 263,
			"ref": "202112090001"
		},
		{
			"user": "Goodness",
			"subject": "When reading, only read. When eating, only eat. When thinking, only think.",
			"tcp_ip": "202.31.137.127",
			"write_date": "2021-12-16 13:25:44",
			"update_date": None,
			"visit": 271,
			"ref": "202112160001"
		},
		{
			"user": "Yusuf",
			"subject": "Don&#39;t let the fear of losing be greater than the excitement of winning.",
			"tcp_ip": "202.31.137.111",
			"write_date": "2021-12-16 15:27:52",
			"update_date": None,
			"visit": 270,
			"ref": "202112160002"
		},
		{
			"user": "Mark",
			"subject": "Never give up. Today is hard, tomorrow will be worse, but the day after tomorrow will be sunshine.",
			"tcp_ip": "",
			"write_date": "2021-12-23 09:55:39",
			"update_date": "2021-12-23 09:56:41",
			"visit": 416,
			"ref": "202112230001"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "The world isn&#39;t as bad as you think",
			"tcp_ip": "59.151.239.3",
			"write_date": "2021-12-30 02:40:57",
			"update_date": None,
			"visit": 347,
			"ref": "202112300001"
		},
		{
			"user": "Revin",
			"subject": "We all have dreams. But in order to make dreams come into reality, it takes an awful lot of determination",
			"tcp_ip": "112.217.167.202",
			"write_date": "2021-12-30 14:48:05",
			"update_date": None,
			"visit": 313,
			"ref": "202112300002"
		},
		{
			"user": "Muhammad Rasyid Redh",
			"subject": "&#34;It always seems impossible until it&#39;s done&#34;, Nelson Mandela",
			"tcp_ip": "112.217.167.202",
			"write_date": "2022-01-06 13:56:47",
			"update_date": None,
			"visit": 329,
			"ref": "202201060001"
		},
		{
			"user": "Vivian",
			"subject": "&#34; You will never see the end, if you give up in the middle&#34;",
			"tcp_ip": "",
			"write_date": "2022-01-13 15:05:21",
			"update_date": "2022-03-17 11:27:35",
			"visit": 296,
			"ref": "202201130001"
		},
		{
			"user": "관리자",
			"subject": "Let us remember the past with gratitude, live the present with enthusiasm, and look forward to the future with confidence",
			"tcp_ip": "",
			"write_date": "2022-01-20 15:21:38",
			"update_date": "2022-01-20 15:24:35",
			"visit": 270,
			"ref": "202201200001"
		},
		{
			"user": "Philip TD",
			"subject": "I didn&#39;t come this far to only come this far. ~ Anonymous",
			"tcp_ip": "202.31.134.95",
			"write_date": "2022-01-20 15:53:23",
			"update_date": None,
			"visit": 254,
			"ref": "202201200002"
		},
		{
			"user": "김형진",
			"subject": "Gather ye rosebuds while ye may, Old time is still flying And this same flower that smiles today, Tomorrow will be dying",
			"tcp_ip": "192.168.81.36",
			"write_date": "2022-02-24 15:18:21",
			"update_date": None,
			"visit": 271,
			"ref": "202202240001"
		},
		{
			"user": "이재현",
			"subject": "Never mistake motion for action  -Ernest Hemingway-",
			"tcp_ip": "202.31.134.93",
			"write_date": "2022-03-10 15:28:23",
			"update_date": None,
			"visit": 225,
			"ref": "202203100001"
		},
		{
			"user": "Chio Aruan",
			"subject": "“It is easier to do a job right than to explain why you didn’t”―&#160;Martin Van Buren",
			"tcp_ip": "202.31.134.96",
			"write_date": "2022-03-11 16:43:41",
			"update_date": None,
			"visit": 215,
			"ref": "202203110001"
		},
		{
			"user": "Made Adi Paramartha",
			"subject": "&#34;The Zone Is Enjoyable. But When That Joy Becomes An Obsession, One Becomes Disconnected From Life.&#34;",
			"tcp_ip": "8.38.172.78",
			"write_date": "2022-03-17 09:33:09",
			"update_date": None,
			"visit": 216,
			"ref": "202203170001"
		},
		{
			"user": "Love",
			"subject": "“Courage is the most important of all the virtues because, without courage, you can&#39;t practice any other virtue consistently.”",
			"tcp_ip": "112.217.167.202",
			"write_date": "2022-03-17 10:32:38",
			"update_date": None,
			"visit": 240,
			"ref": "202203170002"
		},
		{
			"user": "Adinda Riztia Putri",
			"subject": "After a pitch dark night, comes a new beautiful morning",
			"tcp_ip": "117.20.203.63",
			"write_date": "2022-03-24 11:47:06",
			"update_date": None,
			"visit": 211,
			"ref": "202203240001"
		},
		{
			"user": "Syifa Maliah Rachmaw",
			"subject": "“Everybody should do at least two things each day that he hates to do, just for practice”",
			"tcp_ip": "117.20.203.63",
			"write_date": "2022-03-24 13:37:25",
			"update_date": None,
			"visit": 255,
			"ref": "202203240002"
		},
		{
			"user": "Yusuf",
			"subject": "Many of life&#39;s failures are people who did not realize how close they were to success when they gave up.",
			"tcp_ip": "202.31.137.111",
			"write_date": "2022-03-31 13:37:47",
			"update_date": None,
			"visit": 269,
			"ref": "202203310001"
		},
		{
			"user": "Goodness",
			"subject": "“If you want to be successful, find someone who has achieved the results you want and imitate what they do, and you’ll achieve the same results.”  -Tony Robbins",
			"tcp_ip": "202.31.137.127",
			"write_date": "2022-03-31 14:07:01",
			"update_date": None,
			"visit": 238,
			"ref": "202203310002"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "&#34;Talent wins games, but teamwork and intelligence win championships.&#34; &#8211; Michael Jordan",
			"tcp_ip": "202.31.134.98",
			"write_date": "2022-04-07 11:30:13",
			"update_date": None,
			"visit": 254,
			"ref": "202204070001"
		},
		{
			"user": "Muhammad Rasyid Redh",
			"subject": "“A winner is a dreamer who never gives up” - Nelson Mandela",
			"tcp_ip": "",
			"write_date": "2022-04-14 14:51:43",
			"update_date": "2022-04-14 16:57:51",
			"visit": 221,
			"ref": "202204140001"
		},
		{
			"user": "Revin",
			"subject": "&#34;Learning without thinking will not be useful. But thinking without learning will be more dangerous&#8203;&#34;",
			"tcp_ip": "",
			"write_date": "2022-04-14 14:53:16",
			"update_date": "2022-04-14 16:58:28",
			"visit": 252,
			"ref": "202204140002"
		},
		{
			"user": "Mark",
			"subject": "First you learn, then you remove the &#34;L&#34;",
			"tcp_ip": "",
			"write_date": "2022-04-21 13:22:39",
			"update_date": "2022-04-21 13:25:28",
			"visit": 226,
			"ref": "202204210001"
		},
		{
			"user": "Vivian Ukamaka Iheko",
			"subject": "&#34;I have learned over the years that when one&#39;s mind is made up, this diminishes fear&#34; Rosa Parks",
			"tcp_ip": "202.31.134.84",
			"write_date": "2022-04-28 14:03:26",
			"update_date": None,
			"visit": 231,
			"ref": "202204280001"
		},
		{
			"user": "권영준",
			"subject": "No good sittin&#39; worryin&#39; about it.  What&#39;s comin&#39; will come,  and we&#39;ll meet it when it does.",
			"tcp_ip": "202.31.137.57",
			"write_date": "2022-05-12 12:37:44",
			"update_date": None,
			"visit": 190,
			"ref": "202205120001"
		},
		{
			"user": "Philip TD",
			"subject": "Gratitude makes sense of our past, brings peace for today, and creates a vision for tomorrow.",
			"tcp_ip": "202.31.134.95",
			"write_date": "2022-05-12 14:47:15",
			"update_date": None,
			"visit": 201,
			"ref": "202205120002"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less-Marie Curie",
			"tcp_ip": "202.31.134.88",
			"write_date": "2022-05-17 13:59:45",
			"update_date": None,
			"visit": 215,
			"ref": "202205170001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "&#34;The winner takes it all&#34; - ABBA",
			"tcp_ip": "202.31.137.120",
			"write_date": "2022-05-19 17:01:21",
			"update_date": None,
			"visit": 198,
			"ref": "202205190001"
		},
		{
			"user": "mohtasin golam",
			"subject": "The walk didn&#39;t have to be long strides; bauser steps counted too. Go forward.",
			"tcp_ip": "202.31.134.91",
			"write_date": "2022-05-26 01:13:02",
			"update_date": None,
			"visit": 194,
			"ref": "202205260001"
		},
		{
			"user": "김형진",
			"subject": "Once you smile, the whole world is spring.  Once you sob, your heart is full of sorrow.",
			"tcp_ip": "202.31.134.12",
			"write_date": "2022-05-26 13:38:12",
			"update_date": None,
			"visit": 212,
			"ref": "202205260002"
		},
		{
			"user": "Gabriel Avelino Samp",
			"subject": "You become responsible, forever, for what you have tamed.",
			"tcp_ip": "202.31.137.130",
			"write_date": "2022-06-02 13:46:01",
			"update_date": None,
			"visit": 207,
			"ref": "202206020001"
		},
		{
			"user": "Simeon Okechukwu Aja",
			"subject": "The End: Some conclusion may just be an introduction because Effort Never Dies",
			"tcp_ip": "",
			"write_date": "2022-06-09 13:48:10",
			"update_date": "2022-06-09 13:48:55",
			"visit": 253,
			"ref": "202206090001"
		},
		{
			"user": "Love",
			"subject": "&#34;Love is a fruit in season at all times, and within reach of every hand&#34;",
			"tcp_ip": "",
			"write_date": "2022-06-16 11:20:04",
			"update_date": "2022-06-16 12:22:28",
			"visit": 250,
			"ref": "202206160001"
		},
		{
			"user": "이재현",
			"subject": "I’m a firm believer in goal setting. Step user step. I can’t see any other way of accomplishing anything  -Michael Jordan -",
			"tcp_ip": "",
			"write_date": "2022-06-20 10:17:11",
			"update_date": "2022-06-20 10:17:45",
			"visit": 212,
			"ref": "202206200001"
		},
		{
			"user": "장민희",
			"subject": "When the future is out of sight, Do what you have to do now -Frozen-",
			"tcp_ip": "",
			"write_date": "2022-06-27 15:39:44",
			"update_date": "2022-06-27 15:41:02",
			"visit": 183,
			"ref": "202206270001"
		},
		{
			"user": "Syifa Maliah Rachmaw",
			"subject": "&#34;The difference between ordinary and extraordinary is that little extra&#34;",
			"tcp_ip": "117.20.203.63",
			"write_date": "2022-06-30 00:12:51",
			"update_date": None,
			"visit": 219,
			"ref": "202206300001"
		},
		{
			"user": "Made Adi Paramartha",
			"subject": "A new bauser is like the beginning of all things - wonder, hope, a dream of possibilities",
			"tcp_ip": "180.254.225.175",
			"write_date": "2022-07-03 22:48:16",
			"update_date": None,
			"visit": 181,
			"ref": "202207030001"
		},
		{
			"user": "Adinda Riztia Putri",
			"subject": "Just because you have impostor syndrome, doesn’t mean you are incompetent",
			"tcp_ip": "117.20.203.63",
			"write_date": "2022-07-07 10:47:35",
			"update_date": None,
			"visit": 172,
			"ref": "202207070001"
		},
		{
			"user": "Yusuf",
			"subject": "You miss 100% of the shots you don&#39;t take.",
			"tcp_ip": "202.31.137.111",
			"write_date": "2022-07-07 11:13:19",
			"update_date": None,
			"visit": 177,
			"ref": "202207070002"
		},
		{
			"user": "Goodness",
			"subject": "&#34;When times get tough, we don&#39;t give up. We get up&#34;.",
			"tcp_ip": "202.31.137.127",
			"write_date": "2022-07-14 08:51:56",
			"update_date": None,
			"visit": 211,
			"ref": "202207140001"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "I think that&#39;s the single best piece of advice; constantly thinking about how you could be doing things better & questioning your self. --ELON MUSK--",
			"tcp_ip": "202.31.134.98",
			"write_date": "2022-07-21 12:05:15",
			"update_date": None,
			"visit": 212,
			"ref": "202207210001"
		},
		{
			"user": "Revin",
			"subject": "Treat every places as a school, treat everyone as a teacher",
			"tcp_ip": "104.28.230.54",
			"write_date": "2022-07-21 13:35:15",
			"update_date": None,
			"visit": 213,
			"ref": "202207210002"
		},
		{
			"user": "Rasyid",
			"subject": "&#34;Well begun is half done&#34;",
			"tcp_ip": "117.20.203.27",
			"write_date": "2022-08-04 10:15:01",
			"update_date": None,
			"visit": 166,
			"ref": "202208040001"
		},
		{
			"user": "Vivian",
			"subject": "&#34;My philosophy is that not only are you responsible for your life, but doing the best at this moment put you in the best place for the next moment&#34; Oprah Winfrey",
			"tcp_ip": "202.31.134.87",
			"write_date": "2022-08-04 10:26:33",
			"update_date": None,
			"visit": 186,
			"ref": "202208040002"
		},
		{
			"user": "Philip TD",
			"subject": "When one door of happiness closes, another opens, but often we look so long at the closed door that we do not see the one that has been opened for us.",
			"tcp_ip": "220.122.192.51",
			"write_date": "2022-08-18 14:04:32",
			"update_date": None,
			"visit": 167,
			"ref": "202208180001"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "Umbrella can&#39;t stop the rain, but can make us stand in rain.  Confidence may not bring success, but gives us power to face any challenge in Life",
			"tcp_ip": "202.31.134.88",
			"write_date": "2022-08-22 00:29:27",
			"update_date": None,
			"visit": 176,
			"ref": "202208220001"
		},
		{
			"user": "관리자",
			"subject": "Death is so final, yet life is full of possibilities",
			"tcp_ip": "202.31.134.91",
			"write_date": "2022-08-25 00:46:47",
			"update_date": None,
			"visit": 180,
			"ref": "202208250001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "&#34; Everybody is a genius. But if you judge a fish user its ability to climb a tree, it will live its whole life believing that it is stupid.   - Albert Einstein",
			"tcp_ip": "202.31.137.120",
			"write_date": "2022-08-25 12:10:11",
			"update_date": None,
			"visit": 200,
			"ref": "202208250002"
		},
		{
			"user": "Love",
			"subject": "ATTITUDE",
			"tcp_ip": "202.31.134.85",
			"write_date": "2022-09-01 09:34:36",
			"update_date": None,
			"visit": 174,
			"ref": "202209010001"
		},
		{
			"user": "Simeon",
			"subject": "Leadership is Servanthood",
			"tcp_ip": "202.31.134.97",
			"write_date": "2022-09-14 12:50:25",
			"update_date": None,
			"visit": 247,
			"ref": "202209140001"
		},
		{
			"user": "Made Adi Paramartha",
			"subject": "Any man can be a father but it takes someone special to be a dad",
			"tcp_ip": "",
			"write_date": "2022-09-14 15:50:42",
			"update_date": "2022-09-14 15:51:17",
			"visit": 163,
			"ref": "202209140002"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "We must keep doing whatever we are doing right now even though it is hard since it will be easier and easier each day",
			"tcp_ip": "202.31.134.98",
			"write_date": "2022-09-22 13:44:39",
			"update_date": None,
			"visit": 164,
			"ref": "202209220001"
		},
		{
			"user": "Revin",
			"subject": "Intelligence can be gained through study, expertise could be gained from experience. But, bad attitude is hard to fix.",
			"tcp_ip": "37.19.205.194",
			"write_date": "2022-09-29 15:08:00",
			"update_date": None,
			"visit": 174,
			"ref": "202209290001"
		},
		{
			"user": "Muhammad Rasyid Redh",
			"subject": "An investment in knowledge pays the best interest",
			"tcp_ip": "202.31.137.117",
			"write_date": "2022-09-29 15:11:20",
			"update_date": None,
			"visit": 163,
			"ref": "202209290002"
		},
		{
			"user": "Vivian",
			"subject": "&#34;There is no magic to achievement. It&#39;s really about hard work, choices and persistence&#34; Michelle Obama; Former first lady of United States.",
			"tcp_ip": "202.31.134.87",
			"write_date": "2022-10-06 14:09:40",
			"update_date": None,
			"visit": 178,
			"ref": "202210060001"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "‘’ Failure never makes you a loser but giving up does.’’  Jack ma.",
			"tcp_ip": "",
			"write_date": "2022-10-14 15:05:22",
			"update_date": "2022-10-14 15:05:36",
			"visit": 148,
			"ref": "202210140001"
		},
		{
			"user": "Judith Nkechinyere N",
			"subject": "&#34; If you hear a voice within you say &#39;you cannot paint,&#39;....",
			"tcp_ip": "202.31.134.239",
			"write_date": "2022-10-24 10:11:23",
			"update_date": None,
			"visit": 179,
			"ref": "202210240001"
		},
		{
			"user": "Robin",
			"subject": "&#34;The first step towards getting somewhere is to decide you’re not going to stay where you are&#34;",
			"tcp_ip": "",
			"write_date": "2022-11-24 14:28:18",
			"update_date": "2022-11-24 14:30:50",
			"visit": 83,
			"ref": "202211240001"
		},
		{
			"user": "Nkoro Ebuka Chinaech",
			"subject": "Social masks are double-edged",
			"tcp_ip": "",
			"write_date": "2022-11-24 14:50:55",
			"update_date": "2022-11-24 14:51:48",
			"visit": 74,
			"ref": "202211240002"
		},
		{
			"user": "Nwankwo, Odinachi Ud",
			"subject": "The good thing about science is that it’s true whether or not you believe in it",
			"tcp_ip": "",
			"write_date": "2022-12-01 13:22:18",
			"update_date": "2022-12-01 13:23:57",
			"visit": 64,
			"ref": "202212010001"
		},
		{
			"user": "Javed Ahmed Shanto",
			"subject": "In the field of observation, chance favours only the prepared mind.",
			"tcp_ip": "",
			"write_date": "2022-12-01 13:46:18",
			"update_date": "2022-12-01 13:49:58",
			"visit": 96,
			"ref": "202212010002"
		},
		{
			"user": "Mst Ayesha Khatun",
			"subject": "&#34;People are capable at any time in their lives, of doing what they dream of&#34;",
			"tcp_ip": "",
			"write_date": "2022-12-07 18:31:52",
			"update_date": "2022-12-07 18:35:58",
			"visit": 69,
			"ref": "202212070001"
		},
		{
			"user": "Izuazu Urslla Uchech",
			"subject": "&#34;Nothing in life is to be feared, it is only to be understood. Now is the time to understand more,so that we may fear less&#39;",
			"tcp_ip": "202.31.134.83",
			"write_date": "2022-12-08 13:29:18",
			"update_date": None,
			"visit": 79,
			"ref": "202212080001"
		},
		{
			"user": "Mohamed Abubakar",
			"subject": "Success isnt Overnight",
			"tcp_ip": "202.31.134.97",
			"write_date": "2022-12-12 13:11:57",
			"update_date": None,
			"visit": 77,
			"ref": "202212120001"
		},
		{
			"user": "FATIMA TUJ ZOHORA",
			"subject": "“Be yourself; everyone else is already taken.” ― Oscar Wilde",
			"tcp_ip": "103.111.123.110",
			"write_date": "2022-12-15 11:07:30",
			"update_date": None,
			"visit": 77,
			"ref": "202212150001"
		},
		{
			"user": "Simeon Okechukwu Aja",
			"subject": "Innovation is the combination of OLD Things in NEW ways to produce BETTER Result",
			"tcp_ip": "202.31.134.97",
			"write_date": "2023-01-05 15:48:25",
			"update_date": None,
			"visit": 57,
			"ref": "202301050001"
		},
		{
			"user": "Philip TD",
			"subject": "When one door closes, another opens. Or you can open the closed door. That&#39;s how doors work.",
			"tcp_ip": "202.31.134.95",
			"write_date": "2023-01-05 15:55:51",
			"update_date": None,
			"visit": 66,
			"ref": "202301050002"
		},
		{
			"user": "mohtasin golam",
			"subject": "It ain&#39;t how hard you can hit. It&#39;s how hard you can get hit and keep moving forward.",
			"tcp_ip": "202.31.134.91",
			"write_date": "2023-01-12 14:56:47",
			"update_date": None,
			"visit": 67,
			"ref": "202301120001"
		},
		{
			"user": "Love",
			"subject": "ALL GREAT ACHIEVEMENTS REQUIRE TIME",
			"tcp_ip": "",
			"write_date": "2023-01-19 13:13:36",
			"update_date": "2023-01-19 13:17:30",
			"visit": 70,
			"ref": "202301190001"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "“Human progress is neither automatic nor inevitable… Every step toward the goal of success requires sacrifice, suffering, and struggle; the tireless exertions and passionate concern of dedicated individuals” --Dr. Martin Luther King Jr.--",
			"tcp_ip": "202.31.134.98",
			"write_date": "2023-01-26 10:52:53",
			"update_date": None,
			"visit": 68,
			"ref": "202301260001"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "It&#39;s your road, and yours alone. others may walk it with you, but no one can walk it for you-Rumi",
			"tcp_ip": "202.31.134.88",
			"write_date": "2023-02-01 17:55:22",
			"update_date": None,
			"visit": 48,
			"ref": "202302010001"
		},
		{
			"user": "Adi",
			"subject": "Things Change. And we must Change with Them",
			"tcp_ip": "",
			"write_date": "2023-02-02 13:30:01",
			"update_date": "2023-02-02 13:37:24",
			"visit": 55,
			"ref": "202302020001"
		},
		{
			"user": "Revin",
			"subject": "Regretting Fate will not change the situation. Continue to work and making innovation that makes us valuable",
			"tcp_ip": "117.20.203.64",
			"write_date": "2023-02-09 15:24:43",
			"update_date": None,
			"visit": 53,
			"ref": "202302090001"
		},
		{
			"user": "Rasyid",
			"subject": "“There is nothing permanent except change,” Heraclitus",
			"tcp_ip": "59.151.239.136",
			"write_date": "2023-02-16 12:49:00",
			"update_date": None,
			"visit": 54,
			"ref": "202302160001"
		},
		{
			"user": "Vivian",
			"subject": "&#34;Only the fairy tale equates changelessness with happiness...Permanence means paralysis and death. Only in movement with all its pain is life&#34;. Jacob Burckhardt",
			"tcp_ip": "202.31.134.87",
			"write_date": "2023-02-23 13:14:41",
			"update_date": None,
			"visit": 43,
			"ref": "202302230001"
		},
		{
			"user": "Robin",
			"subject": "“Life is like riding a bicycle, to keep your balance, you must keep moving”  &#8211; Albert Einstein",
			"tcp_ip": "192.168.81.111",
			"write_date": "2023-03-09 09:14:57",
			"update_date": None,
			"visit": 46,
			"ref": "202303090001"
		},
		{
			"user": "Ebuka",
			"subject": "No one is rich enough to buy yesterday but if you hustle hard, tomorrow could be yours...",
			"tcp_ip": "",
			"write_date": "2023-03-09 15:53:52",
			"update_date": "2023-03-09 16:09:29",
			"visit": 37,
			"ref": "202303090002"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "Be a student not a follower. Judge all things and hold fast to that which you believe to be true for you.’’  Jim Rohn.",
			"tcp_ip": "192.168.83.8",
			"write_date": "2023-03-13 10:42:35",
			"update_date": None,
			"visit": 28,
			"ref": "202303130001"
		},
		{
			"user": "Judith Nkechinyere N",
			"subject": "Time is more valuable than money. you can get more money, but you cannot get more time",
			"tcp_ip": "192.168.83.10",
			"write_date": "2023-03-16 10:27:56",
			"update_date": None,
			"visit": 35,
			"ref": "202303160001"
		},
		{
			"user": "Md Javed Ahmed Shant",
			"subject": "If we knew what it was we were doing it would not be called research. would it?",
			"tcp_ip": "",
			"write_date": "2023-03-16 13:59:00",
			"update_date": "2023-03-16 16:03:41",
			"visit": 41,
			"ref": "202303160002"
		},
		{
			"user": "Paul C",
			"subject": "What would you attempt to do if you knew you wouldn&#39;t fail?",
			"tcp_ip": "192.168.64.150",
			"write_date": "2023-03-27 12:55:53",
			"update_date": None,
			"visit": 30,
			"ref": "202303270001"
		},
		{
			"user": "Nwankwo, Odinachi Ud",
			"subject": "Science is about knowing; engineering is about doing",
			"tcp_ip": "192.168.63.48",
			"write_date": "2023-03-28 14:11:08",
			"update_date": None,
			"visit": 24,
			"ref": "202303280001"
		},
		{
			"user": "Urslla",
			"subject": "&#34;Research is a formalised curiosity. It is poking and prying with purpose.&#34; Zora Neale",
			"tcp_ip": "192.168.83.5",
			"write_date": "2023-03-30 12:29:40",
			"update_date": None,
			"visit": 33,
			"ref": "202303300001"
		},
		{
			"user": "이늘솜",
			"subject": "I love myself,  I trust myself : Dear me - Taeyeon",
			"tcp_ip": "",
			"write_date": "2023-04-06 02:52:41",
			"update_date": "2023-04-06 02:56:44",
			"visit": 32,
			"ref": "202304060001"
		},
		{
			"user": "Mohamed Abubakar",
			"subject": "“How do I respond to criticism? Critically. I listen to all criticism critically.“  - Paul Thomas Anderson",
			"tcp_ip": "192.168.61.113",
			"write_date": "2023-04-06 15:59:58",
			"update_date": None,
			"visit": 26,
			"ref": "202304060002"
		},
		{
			"user": "이민선",
			"subject": "The universe is change.our life is what our thoughts make it",
			"tcp_ip": "192.168.65.4",
			"write_date": "2023-04-07 13:59:32",
			"update_date": None,
			"visit": 45,
			"ref": "202304070001"
		},
		{
			"user": "Gifar",
			"subject": "Research is to see what  everybody else has seen, and  to think what nobody else has  thought.",
			"tcp_ip": "192.168.64.39",
			"write_date": "2023-04-13 13:31:15",
			"update_date": None,
			"visit": 37,
			"ref": "202304130001"
		},
		{
			"user": "MD FACKLASUR RAHAMAN",
			"subject": "’Google&#39; is not a synonym for ‘research’",
			"tcp_ip": "192.168.63.81",
			"write_date": "2023-04-13 13:36:01",
			"update_date": None,
			"visit": 46,
			"ref": "202304130002"
		},
		{
			"user": "Mst Ayesha Khatun",
			"subject": "And, when you want something, all the universe conspires in helping you to achieve it.",
			"tcp_ip": "192.168.83.3",
			"write_date": "2023-04-15 16:40:31",
			"update_date": None,
			"visit": 44,
			"ref": "202304150001"
		},
		{
			"user": "SUBHAN MD RAIHAN",
			"subject": "Research is what I&#39;m doing when I don&#39;t know what I&#39;m doing.",
			"tcp_ip": "192.168.63.2",
			"write_date": "2023-04-18 11:56:18",
			"update_date": None,
			"visit": 51,
			"ref": "202304180001"
		},
		{
			"user": "Aouto, Ali",
			"subject": "&#34; The secret of change is to focus all of your energy, not on fighting the old, but on building the new &#34; -Socrates",
			"tcp_ip": "",
			"write_date": "2023-05-11 13:09:49",
			"update_date": "2023-05-11 13:10:43",
			"visit": 32,
			"ref": "202305110001"
		},
		{
			"user": "Love",
			"subject": "Education is the key to unlocking world. It is the passport to freedom",
			"tcp_ip": "192.168.83.14",
			"write_date": "2023-05-11 13:35:07",
			"update_date": None,
			"visit": 37,
			"ref": "202305110002"
		},
		{
			"user": "Adi",
			"subject": "You Are Stronger Than You Think",
			"tcp_ip": "",
			"write_date": "2023-05-18 09:31:01",
			"update_date": "2023-05-18 09:32:04",
			"visit": 37,
			"ref": "202305180001"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "If nothing changes, nothing changes. If you keep doing what you’re doing, you’re going to keep getting what you’re getting. You want change, make some.",
			"tcp_ip": "192.168.83.7",
			"write_date": "2023-05-18 09:52:49",
			"update_date": None,
			"visit": 43,
			"ref": "202305180002"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "“You Never Fail Until You Stop Trying&#34;-Albert Einstein",
			"tcp_ip": "192.168.83.128",
			"write_date": "2023-05-25 17:19:40",
			"update_date": None,
			"visit": 55,
			"ref": "202305250001"
		},
		{
			"user": "DAMIAN TITA",
			"subject": "&#34;I walk slowly, but I never walk backward&#34;, Abraham Lincoln",
			"tcp_ip": "192.168.83.8",
			"write_date": "2023-06-02 12:04:25",
			"update_date": None,
			"visit": 43,
			"ref": "202306020001"
		},
		{
			"user": "Judith Nkechinyere N",
			"subject": "If we knew what it was we were doing, it would not be called research, would it? - Albert Einstein",
			"tcp_ip": "169.150.218.22",
			"write_date": "2023-06-13 16:03:35",
			"update_date": None,
			"visit": 43,
			"ref": "202306130001"
		},
		{
			"user": "Ebuka",
			"subject": "When something is important enough, you do it even if the odds are not in your favor",
			"tcp_ip": "192.168.83.6",
			"write_date": "2023-06-15 17:05:14",
			"update_date": None,
			"visit": 52,
			"ref": "202306150001"
		},
		{
			"user": "Robin",
			"subject": "Most of the important things in the world have been accomplished user people who have kept on trying when there seemed to be no hope at all - Dale Carnegie",
			"tcp_ip": "192.168.64.96",
			"write_date": "2023-06-16 16:05:26",
			"update_date": None,
			"visit": 49,
			"ref": "202306160001"
		},
		{
			"user": "Nwankwo, Odinachi Ud",
			"subject": "“Our lives sometimes depend on computers performing as predicted.” &#8211; Philip Emeagwali",
			"tcp_ip": "192.168.63.48",
			"write_date": "2023-06-29 17:39:43",
			"update_date": None,
			"visit": 42,
			"ref": "202306290001"
		},
		{
			"user": "Urslla",
			"subject": "&#34;Academic research  depends on research and publications&#34; user Philips Zimbardo",
			"tcp_ip": "192.168.83.5",
			"write_date": "2023-06-29 17:46:38",
			"update_date": None,
			"visit": 48,
			"ref": "202306290002"
		},
		{
			"user": "Paul C",
			"subject": "&#34;The only way to truly escape the mundane is for you to constantly keep evolving, whether you choose to aim high or aim low. Enjoy each day for what it is.&#34; - Orihara Izaya",
			"tcp_ip": "192.168.63.116",
			"write_date": "2023-07-12 16:38:47",
			"update_date": None,
			"visit": 49,
			"ref": "202307120001"
		},
		{
			"user": "Mohamed Abubakar",
			"subject": "“It is impossible to live without failing at something unless you live so cautiously that you might as well not have lived at all &#8211; in which case, you fail user default.”  J. K. Rowling",
			"tcp_ip": "192.168.61.113",
			"write_date": "2023-07-13 16:16:10",
			"update_date": None,
			"visit": 47,
			"ref": "202307130001"
		},
		{
			"user": "이늘솜",
			"subject": "Why does anyone get to tell you what you can do in your life? : Elemental,  Wade",
			"tcp_ip": "192.168.64.10",
			"write_date": "2023-07-20 13:47:35",
			"update_date": None,
			"visit": 58,
			"ref": "202307200001"
		},
		{
			"user": "MD FACKLASUR RAHAMAN",
			"subject": "Some books are to be tasted, others to be swallowed, and some few to be chewed and digested.",
			"tcp_ip": "192.168.63.81",
			"write_date": "2023-07-27 13:02:58",
			"update_date": None,
			"visit": 36,
			"ref": "202307270001"
		},
		{
			"user": "이민선",
			"subject": "T&#236;sh&#244;k : There is no eternal light,  so let&#39;s enjoy it when it shines",
			"tcp_ip": "",
			"write_date": "2023-07-27 18:55:59",
			"update_date": "2023-07-27 18:58:13",
			"visit": 40,
			"ref": "202307270002"
		},
		{
			"user": "Love",
			"subject": "It’s not what you’re faced with that’s the problem; it’s what you do with the situation.",
			"tcp_ip": "192.168.83.14",
			"write_date": "2023-08-17 12:59:24",
			"update_date": None,
			"visit": 33,
			"ref": "202308170001"
		},
		{
			"user": "Adi",
			"subject": "Learning without thinking is useless, but thinking without learning is very dangerous",
			"tcp_ip": "",
			"write_date": "2023-08-17 14:05:43",
			"update_date": "2023-08-17 14:06:12",
			"visit": 43,
			"ref": "202308170002"
		},
		{
			"user": "Ahmad Zainudin",
			"subject": "Don&#39;t limit your challenges. Challenge your limits.",
			"tcp_ip": "192.168.83.7",
			"write_date": "2023-08-24 12:12:42",
			"update_date": None,
			"visit": 44,
			"ref": "202308240001"
		},
		{
			"user": "유상호",
			"subject": "Sometimes it is the people who no-one imagines anything of who do the things that no-one can imagine",
			"tcp_ip": "192.168.83.15",
			"write_date": "2023-08-28 17:15:38",
			"update_date": None,
			"visit": 39,
			"ref": "202308280001"
		},
		{
			"user": "Esmot Ara Tuli",
			"subject": "If you get tired, learn to rest not to quit~Bansky",
			"tcp_ip": "",
			"write_date": "2023-09-06 13:03:50",
			"update_date": "2023-09-06 13:04:11",
			"visit": 26,
			"ref": "202309060001"
		},
		{
			"user": "Judith Nkechinyere N",
			"subject": "Discovery consists of seeing what everybody has seen and thinking what nobody has thought - Albert Szent-Gyorgyi",
			"tcp_ip": "",
			"write_date": "2023-09-18 11:40:43",
			"update_date": "2023-09-18 11:41:44",
			"visit": 27,
			"ref": "202309180001"
		},
		{
			"user": "Robin",
			"subject": "The more that you read, the more things you will know. The more that you learn, the more places you&#39;ll go",
			"tcp_ip": "192.168.64.96",
			"write_date": "2023-09-25 17:07:15",
			"update_date": None,
			"visit": 15,
			"ref": "202309250001"
		},
		{
			"user": "Nkoro Ebuka Chinaech",
			"subject": "Trust takes years to build, seconds to break and forever to repair - Dhar Mann",
			"tcp_ip": "192.168.83.6",
			"write_date": "2023-09-25 17:07:40",
			"update_date": None,
			"visit": 19,
			"ref": "202309250002"
		},
		{
			"user": "Izuazu urslla uchech",
			"subject": "After all, the Ultimate goal of all research is not objectivity, but the truth.",
			"tcp_ip": "192.168.83.5",
			"write_date": "2023-10-17 15:33:49",
			"update_date": None,
			"visit": 52,
			"ref": "202310170001"
		},
		{
			"user": "Nwankwo, Odinachi Ud",
			"subject": "The most important skill for a computer scientist is problem-solving. Even if you don’t know all the details of the technology you are using, if you can solve the problem, you can figure out how to do it",
			"tcp_ip": "192.168.63.48",
			"write_date": "2023-10-19 16:23:26",
			"update_date": None,
			"visit": 28,
			"ref": "202310190001"
		},
		{
			"user": "Paul C",
			"subject": "&#34;Failure takes a bigger part in people’s lives than one may think. It’s important to not lose yourself in the emotions from success and failure.&#34; - Faker",
			"tcp_ip": "192.168.63.116",
			"write_date": "2023-10-26 15:08:52",
			"update_date": None,
			"visit": 21,
			"ref": "202310260001"
		},
		{
			"user": "MD FACKLASUR RAHAMAN",
			"subject": "Since we are not robots, we  can&#39;t always perform well.",
			"tcp_ip": "192.168.63.81",
			"write_date": "2023-11-09 10:45:50",
			"update_date": None,
			"visit": 6,
			"ref": "202311090001"
		}
	]
}
def populate():
    for row in data['rows']:
        Serendipity.objects.create(**row)

if __name__ == '__main__':
    populate()
    print("working again")