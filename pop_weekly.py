

import os


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

# Call Django's setup to configure the settings
import django
django.setup()

# from works.models import WeeklyReport
from works.models import PostDocReport


data = {
	"table": "works_postdocreport",
	"rows":
	[
		{
			"user": "disciple",
			"fr_dt": "2021-04-09 00:00:00",
			"to_dt": "2021-04-15 00:00:00",
			"paper_progress": "1. IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" under review\r\n\r\n2. KICS, having been accepted, Awaiting final submission.\r\n\r\n3. IEEE Access, preparing a Remain Useful Life (RUL) paper.\r\n\r\n4. IEEE Access, preparing an Automatic Modulation Classification (AMC) paper.",
			"project_progress": "Hanwha systems project",
			"mnth_gls": "1. Complete the simulation works",
			"annl_gls": "1. Publish two SCI/E papers"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-04-11 00:00:00",
			"to_dt": "2021-04-17 00:00:00",
			"paper_progress": "1.  Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Performance Evaluation\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: Target Journal- IEEE Transactions on Vehicular Technology-In Progress",
			"project_progress": "not assigned",
			"mnth_gls": "Complete papers 1 and 2.",
			"annl_gls": "Publish at least two SCI papers"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": "1. JCCI 발표 준비\r\n2. 블록체인\r\n3. 산업용 IoT 내결함성 연구",
			"project_progress": "1. 5G 실증 사업 회의 참석 \r\n2. 스마트 에너지 사업 2차년 일정 미팅",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "disciple",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": "1. IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" under review\r\n\r\n2. KICS, having been accepted, Awaiting final submission.\r\n\r\n3. IEEE Access, preparing a Remain Useful Life (RUL) paper.\r\n\r\n4. IEEE Access, preparing an Automatic Modulation Classification (AMC) paper.\r\n\r\n5. Prepare the paper presentation on JCCI 2021, (2021.04.29 - 2021.04.30)",
			"project_progress": "1. Deal with the NRF BP project, dead line(2021.06.30)\r\n\r\n2. Deal with the NRF Vietnam-Korea project, deadline(2021.05.25)\r\n\r\n3. Deal with etc. documents",
			"mnth_gls": "1. Finish the Hanwha system proposal\r\n\r\n2. Finish simulation works",
			"annl_gls": "1. Two SCI/E papers are published"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": "* JCCI 발표준비\r\n* IEEE communications letters major revision (~05.15)\r\n - Imperfect CSI 및 SIC적용 시뮬레이션 및 수학모델 완료\r\n - 작성 논문에 Imperfect CSI 및 SIC 관련 내용 작성 중",
			"project_progress": "2021.04.23(금) 국방 소프트웨어 신뢰성 교육 출장 (서울 송파구)",
			"mnth_gls": "IEEE Communications letters 리비전 진행(목표 ~80%)",
			"annl_gls": "* Cooperative retransmission NOMA 연구(현재 IEEE CL에 리비전중)\r\n* Multicell NOMA-VLC system에 DQN적용한 CoMP 연구(NOMA-VLC BER 모델 작성 완료)"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Cost-Efficient CNN for Impaired OFDM Signals (IEEE GLOBECOM 2021).\r\n2. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n3. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Geosci. Remote Sens. Lett. - TBD).\r\n4. Accurate LPI Radar Waveform Recognition With CWD-TFA for Deep Convolutional Network (IEEE Wire. Commun. Lett. - Accepted).\r\n...\r\n\r\nN. Reliability of Industrial Internet of Things from System Perspective (Journal: TBD - In revision).",
			"project_progress": "1. Research supervision: \r\n- Mr. Godwin Tunze - Radio Signal Processing.\r\n- Ms. Rubina Akter - Deep Learning.\r\n2. Research collaboration (with Dr. Pham): Intelligent Distributed Cloud",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": "1. Towards Distributed Cloud Intelligence: A Comprehensive Survey (Journal: TBD)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Journal: TBD)",
			"project_progress": "Collaborate with Dr. Thien",
			"mnth_gls": "Finalize the structure of the survey and write journal 1",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": "1. Reinforcement Learning based Resource Management for Fog Computing Environment:\r\nPerspectives and Challenges (Survey-IEEE Internet of things Journal).\r\n2. Our research center research achievements for future collaborations (Magazine paper).\r\n3. Machine Learning-enabled Next Generation Sustainable Industries of Future \r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper)\r\n4. Adaptive Learning and Decision-making for Next-generation IoT-based Smart Grid Systems(Magazine paper)",
			"project_progress": "",
			"mnth_gls": "Finalize an initial draft of the paper (1) with Dr. Tran, Dr. Tariq, and Dr. Sanjay.\r\nPrepare a framework for a magazine paper for our ICT research center work.",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": "Topics\r\n1. Resource Management for Fog Computing-based Reinforcement Learning: Perspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\n2. Machine Learning-enabled Next Generation Sustainable Industries of Future (IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges. (IoT Magazine) \r\n3. Experimental Trial and Validation for 5G Test-bed Case: Vertical Applications for Interconnetecd Multiple Sites. (IEEE Communication Magazine) \r\n4. Adaptive Learning and Decision-making for Next-generation IoT-based Smart Grid Systems(Magazine paper).",
			"project_progress": "Update on the above topics\r\n1. Meeting with Dr. Hoa and rest. Task allocation. Own parts writing started.\r\n   Application of reinforcement learning for resource allocation in Fog computing. \r\n   Open issues of applications of reinforcement learning in Fog computing. \r\n2. Paper structure and contents. \r\n3. Making the topic and organization of the survey paper.   \r\n   Gathering trials and research work performed for 28GHz mmWave case.",
			"mnth_gls": "1. Finish my part of the IoT special issue paper. \r\n\r\n2. Collecting all the previous research done for topic 3 and start writing. (40%).",
			"annl_gls": "1. Two SCI/E papers."
		},
		{
			"user": "william",
			"fr_dt": "2021-04-19 00:00:00",
			"to_dt": "2021-04-23 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036 \r\n(SUBMITTED TO: IEEE Trans. on Broadcasting) \r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).  \r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700 \r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: VT-2021-00671 \r\n(SUBMITTED TO: IEEE Trans. on Vehicular Technology)\r\n\r\nTitle 6: CL2021-0854 \r\n(SUBMITTED TO: IEEE Communications Letters)\r\n\r\nTitle 7: TR 21-0147 \r\n(SUBMITTED TO: IEEE Trans. on Robotics)\r\n\r\nTitle 8: SIPN-00774-2021 \r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: JINT-D-21-00170 \r\n(SUBMITTED TO: Journal of Intelligent & Robotic Systems)\r\n\r\nTitle 10: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 11: Access-2021-10959 \r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 12: ICAIIC International Conference, 2021. [ACCEPTED & ATTENDED]\r\nTitle 13: JCCI, 2021. [ACCEPTED, 발표준비]",
			"project_progress": "Title 1: Under review\r\nTitle 2: ACCEPTED and PUBLISHED\r\nTitle 3: Under review\r\nTitle 4: ACCEPTED and PUBLISHED\r\nTitle 5: Under review\r\nTitle 6: Under review\r\nTitle 7: Under review\r\nTitle 8: Under review\r\nTitle 9: Under review\r\nTitle 10: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after revision.\r\nTitle 11: Under review.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Working with Dr. Hoa Tran on a technical paper and a survey paper.\r\n[2]. Currently at an initial stage and yet to finalize discussions.\r\n\r\n\r\nKUMOH NATIONAL UNIVERSITY RESEARCH LOGBOOK\r\n[1]. Was selected by KIT to work on the IT Convergence Dept. research logbook.\r\n[2]. Finalizing the works as stipulated.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [10] above.\r\n[2]. Mr. Damian's Research TITLES [4] and [11] above.",
			"mnth_gls": "[1]. Detailing and adaptation to all my essential simulation and testbed working tools.\r\n[2]. Working with PosDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-04-23 00:00:00",
			"to_dt": "2021-04-29 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Performance Evaluation\r\n-Final Evaluation and submission \r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: Target Journal- IEEE Transactions on Vehicular Technology\r\n-Final Evaluation and submission \r\n\r\n3. Survey paper with Dr. Hoa and team.",
			"project_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Performance Evaluation\r\n-Final Evaluation and submission \r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: Target Journal- IEEE Transactions on Vehicular Technology\r\n-Final Evaluation and submission \r\n\r\n3. Survey paper with Dr. Hoa and team.",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-04-23 00:00:00",
			"to_dt": "2021-05-29 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (Magazine Paper).\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment:\r\nPerspectives and Challenges (Survey-IEEE Internet of things Journal). \r\n3. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n4. Adaptive Learning and Decision-making for Next-generation IoT-based Smart Grid Systems (Magazine paper).",
			"project_progress": "",
			"mnth_gls": "1. Finalize an initial framework for Regional Innovation at ICT Convergence Research Center magazine paper. \r\n2. Finalize an initial draft of the paper (2) with Dr. Tran, Dr. Tariq, and Dr. Sanjay.",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-04-23 00:00:00",
			"to_dt": "2021-05-29 00:00:00",
			"paper_progress": "Topics\r\n1. Resource Management for Fog Computing-based Reinforcement Learning: Perspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\n2. Experimental Trial and Validation for 5G+ Test-bed Case.\r\n3. Adaptive Learning and Decision-making for Next-generation IoT-based Smart Grid Systems(Magazine paper).",
			"project_progress": "Update on the above topics\r\n1. Subsection completion i.e., Applications of RL in Fog Computing, and started subsection Open Issues of Applications of RL in Fog Computing. \r\n2. Organization of the paper and started gathering related work done for the case.\r\n   Received data from Dr. Aan for the 5G+ testbed case.\r\n   Carry on simultaneously with my own research work.",
			"mnth_gls": "Finish Topic 1.\r\nFinish my previous work too. \r\n(missing some results) such as the Bjontegaard delta (BD) bit-rate saving. \r\nChecking the literature part of Topic 2. (necessary for me)",
			"annl_gls": "Two SCI/E papers."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-04-26 00:00:00",
			"to_dt": "2021-04-30 00:00:00",
			"paper_progress": "1. Towards Distributed Cloud Intelligence: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: TBD)",
			"project_progress": "Finalize the structure and start writing (Related Concepts, Fundamentals, Use Cases and Applications, Research Challenges and Future Directions)",
			"mnth_gls": "Finalize the structure of the survey and write journal 1",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-04-26 00:00:00",
			"to_dt": "2021-04-30 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Cost-Efficient CNN for Impaired OFDM Signals (IEEE GLOBECOM 2021).\r\n2. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n3. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Geosci. Remote Sens. Lett. - Submitted).\r\n4. Reliability of Industrial Internet of Things from System Perspective (Journal: TBD).",
			"project_progress": "1. Research supervision:\r\n- Mr. Godwin Tunze - Radio Signal Processing.\r\n2. Research collaboration (with Dr. Pham): Intelligent Distributed Cloud",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "",
			"fr_dt": "2021-04-26 00:00:00",
			"to_dt": "2021-04-30 00:00:00",
			"paper_progress": "* IEEE communications letters major revision (~05.15)\r\n- System model 수정 내용 작성중",
			"project_progress": "* JCCI 2021 참석 및 발표",
			"mnth_gls": "IEEE Communications letters 리비전 진행(목표 ~80%)",
			"annl_gls": "* Cooperative retransmission NOMA 연구(현재 IEEE CL에 리비전중)\r\n* Multicell NOMA-VLC system에 DQN적용한 CoMP 연구(NOMA-VLC BER 모델 작성 완료)"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-04-26 00:00:00",
			"to_dt": "2021-04-30 00:00:00",
			"paper_progress": "* IEEE communications letters major revision (~05.15)\r\n- System 모델 수정 내용 작성",
			"project_progress": "* JCCI 2021 참석 및 발표",
			"mnth_gls": "IEEE Communications letters 리비전 진행(목표 ~80%)",
			"annl_gls": "* Cooperative retransmission NOMA 연구(현재 IEEE CL에 리비전중)\r\n* Multicell NOMA-VLC system에 DQN적용한 CoMP 연구(NOMA-VLC BER 모델 작성 완료)"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-04-26 00:00:00",
			"to_dt": "2021-04-30 00:00:00",
			"paper_progress": "- JCCI 논문 발표 및 참석 '산업용 IoT 기기의 MMS프로토콜 보안을 위한 블록체인 기술'",
			"project_progress": "- 이노폴리스사업 관련 사업지원 검토\r\n- 하드웨어제작 플랫폼 특허출원진행\r\n * 수정 진행",
			"mnth_gls": "- 특허 1건 출원\r\n- 소프트웨어 등록 1건",
			"annl_gls": "- 국내논문 1편 게재\r\n- 해외논문 1편 투고\r\n- 저서 1권\r\n- 특허출원 6\r\n- 소프트웨어 등록 12"
		},
		{
			"user": "william",
			"fr_dt": "2021-04-26 00:00:00",
			"to_dt": "2021-04-30 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: VT-2021-00671\r\n(SUBMITTED TO: IEEE Trans. on Vehicular Technology)\r\n\r\nTitle 6: CL2021-0854\r\n(SUBMITTED TO: IEEE Communications Letters)\r\n\r\nTitle 7: TR 21-0147\r\n(SUBMITTED TO: IEEE Trans. on Robotics)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: JINT-D-21-00170\r\n(SUBMITTED TO: Journal of Intelligent & Robotic Systems)\r\n\r\nTitle 10: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 11: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 12: ICAIIC International Conference, 2021. [ACCEPTED & ATTENDED]\r\nTitle 13: JCCI, 2021. [ACCEPTED & VIRTUALLY PRESENTED]",
			"project_progress": "Title 1: Under review\r\nTitle 2: ACCEPTED and PUBLISHED\r\nTitle 3: Under review\r\nTitle 4: ACCEPTED and PUBLISHED\r\nTitle 5: Under review\r\nTitle 6: Under review\r\nTitle 7: Under review\r\nTitle 8: Under review\r\nTitle 9: Under review\r\nTitle 10: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after revision.\r\nTitle 11: Under review.\r\n\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Working with Prof. Kim on book/magazine.\r\n[2]. 1st meeting was held and concluded. Briefly discussed the title.\r\n[3]. Currently at an initial stage and yet to finalize discussions.\r\n\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Working with Dr. Hoa Tran on a technical paper and a survey paper.\r\n[2]. 2nd meeting was held last week and concluded. Briefly discussed the modalities and authorship.\r\n[3]. Currently at an initial paper titling stage and yet to finalize discussions.\r\n\r\n\r\nKUMOH NATIONAL UNIVERSITY RESEARCH LOGBOOK\r\n[1]. Finalized the works as stipulated and submitted accordingly.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [10] above.\r\n[2]. Mr. Damian's Research TITLE [11] above.",
			"mnth_gls": "[1]. Detailing and adaptation to all my essential simulation and testbed working tools.\r\n[2]. Working with PosDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-04-30 00:00:00",
			"to_dt": "2021-05-06 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-TBD\r\n\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: Target Journal- IEEE Transactions on Vehicular Technology\r\n-Submitted\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\n \r\n \r\n \r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-04-30 00:00:00",
			"to_dt": "2021-05-06 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (Magazine Paper).\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment:\r\nPerspectives and Challenges (Survey-IEEE Internet of things Journal).\r\n3. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n4. Adaptive Learning and Decision-making for Next-generation IoT-based Smart Grid Systems (Magazine paper).",
			"project_progress": "Work on the following topics:\r\n1. R&D, and Education in ICT Convergence Research Center.\r\n A. Grand ICT Research Center \r\n B. Priority Research Center Project\r\n C. Education and Regional Contribution\r\n D. Industry-Academic Cooperation\r\n E. 4M IT convergence (Military Mobile, Military Material, Military Medical, and \r\n    Material-Civil Convergence)\r\n\r\n2. Challenges and Open Issues of Application of Reinforcement learning-based resource allocation in Fog-RAN.",
			"mnth_gls": "1. Finalize a draft for Regional Innovation at ICT Convergence Research Center (magazine paper).\r\n2. Finalize an initial draft of the paper (2) with Dr. Tran, Dr. Tariq, and Dr. Sanjay.",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-04-30 00:00:00",
			"to_dt": "2021-05-06 00:00:00",
			"paper_progress": "Topic 1: Introducing 5G+ at 28GHz mmWave Test-bed (Survey)\r\nTopic 2: Resource Management for Fog Computing-based Reinforcement Learning: Perspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\nTopic 3: Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual Quality of Compressed Videos",
			"project_progress": "Update on the above topics\r\nTopic 1: Prototype in progress that includes the structure of the paper\r\n         Organization of the paper = Continue.\r\n         Introduction, Related work, Detail of the implementation with hardware \r\n         and future goals for devices as tabular form, the contribution of the \r\n         work and measurement results. \r\nTopic 2: Subsection updated i.e., Applications of RL in Fog Computing, and will start more subsection Open Issues of Applications of RL in Fog Computing.\r\nTopic 3: Missing results 50% done i.e.,  Bjontegaard delta (BD) bit-rate saving.",
			"mnth_gls": "Submission of the Topic 3 \r\nFinalizing Topic 1 for its final structure..........",
			"annl_gls": "2 SCI papers"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-05-03 00:00:00",
			"to_dt": "2021-05-07 00:00:00",
			"paper_progress": "1. 국내저널 논문준비\r\n   (엣지 컴퓨티관련 동향 논문 준비)\r\n2. 하계 통신학회 학술대회 논문준비\r\n   (산업용 통신 프로토콜 변환에 관한 연구)",
			"project_progress": "- 이노 폴리스 사업 제안서 작성 (차주 월 지원계획)\r\n\r\n- 해외 특허, 국내 특허 아이디어 관련 논문 조사",
			"mnth_gls": "- 특허 1건 출원\r\n- 소프트웨어 등록 1건",
			"annl_gls": "- 해외논문 1편 투고\r\n- 저서 1권\r\n- 특허출원 6\r\n- 소프트웨어 등록 12"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-05-03 00:00:00",
			"to_dt": "2021-05-07 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: TBD)",
			"project_progress": "Paper 1: Discuss and write Introduction part (on-going).",
			"mnth_gls": "Finalize an initial draft of paper 1 with Dr. Thien",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-05-03 00:00:00",
			"to_dt": "2021-05-07 00:00:00",
			"paper_progress": "* IEEE communications letters major revision (~05.15)\r\n- 작성 중(차주 Introduction 부분 수정 후 제출 예정)\r\n\r\n* 한국통신학회 논문지 수정 후 제출 완료\r\n- 게재가 (7월 게재 예정)",
			"project_progress": "",
			"mnth_gls": "- IEEE Communications letters 리비전 후 제출(~5월15일)",
			"annl_gls": "* SCIE 논문 2편 목표\r\n- Cooperative retransmission NOMA 연구(현재 IEEE CL에 리비전중)\r\n- Multicell NOMA-VLC system에 DQN적용한 CoMP 연구(NOMA-VLC BER 모델 작성 완료)"
		},
		{
			"user": "william",
			"fr_dt": "2021-05-03 00:00:00",
			"to_dt": "2021-05-07 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: VT-2021-00671\r\n(SUBMITTED TO: IEEE Trans. on Vehicular Technology)\r\n\r\nTitle 6: CL2021-0854\r\n(SUBMITTED TO: IEEE Communications Letters)\r\n\r\nTitle 7: TR 21-0147\r\n(SUBMITTED TO: IEEE Trans. on Robotics)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: JINT-D-21-00170\r\n(SUBMITTED TO: Journal of Intelligent & Robotic Systems)\r\n\r\nTitle 10: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 11: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 12: ICAIIC International Conference, 2021. [ACCEPTED & ATTENDED]\r\nTitle 13: JCCI, 2021. [ACCEPTED & VIRTUALLY PRESENTED]",
			"project_progress": "Title 1: Under review\r\nTitle 2: ACCEPTED and PUBLISHED\r\nTitle 3: Under review\r\nTitle 4: ACCEPTED and PUBLISHED\r\nTitle 5: Under review\r\nTitle 6: Under review\r\nTitle 7: PUBLICATION DECLINED on 2020/05/04. To submit elsewhere.\r\n         -Reworking the paper's system model, readability, and simulations based on review comments.\r\n         -To finalize and re-submit before 11th May, 2021.\r\nTitle 8: Under review\r\nTitle 9: Under review\r\nTitle 10: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after Major revision.\r\nTitle 11: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Working with Prof. Kim on book/magazine.\r\n[2]. Reviewing numerous survey papers was done in this Week.\r\n[3]. To finalize on paper title and abstract by next week.\r\n[4]. To further discuss with Prof. Kim by next week.\r\n\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Working with Dr. Hoa Tran on a technical paper and a survey paper.\r\n[2]. Reviewing numerous survey papers was done in Week 3.\r\n[3]. To finalize on paper title and abstract by next week-end.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [10] above.\r\n[2]. Mr. Damian's Research TITLE [11] above.",
			"mnth_gls": "[1]. Detailing and adaptation to all my essential simulation and testbed working tools.\r\n[2]. Working with PosDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-05-03 00:00:00",
			"to_dt": "2021-05-07 00:00:00",
			"paper_progress": "1. Shaping the future of Logistics \r\n       -> Under review in IETE Technical Review\r\n\r\n2. Survey on IIoT Journal\r\n       -> Already submit in IETE Technical Review\r\n\r\n3. Survey on Reinforcement Learning \r\n       -> Streaming the Introduction, System Model section, Applications \r\n\r\n4. Dynamic Collaborative Task Offloading in Fog Computing Systems\r\n       -> Draft on Algorithms",
			"project_progress": "",
			"mnth_gls": "-) Submit paper # 3 in IEEE Internet of Things Journal\r\n-) Submit paper # 4) in KICS summer 2021 conference",
			"annl_gls": "-) 4-5 International Conference\r\n-) 3-4 SCI Journal (Accepted)"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-05-03 00:00:00",
			"to_dt": "2021-05-07 00:00:00",
			"paper_progress": "1. On the Reliability of Industrial Internet of Things from Systematic Perspectives: Evaluation Approaches, Challenges, and Open Issues (IETE Technical Review - Submitted by Dr. Tran).\r\n2. Automatic Modulation Classification with Cost-Efficient CNN for Impaired OFDM Signals (IEEE GLOBECOM 2021).\r\n3. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n4. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Submitted).",
			"project_progress": "1. Research supervision:\r\n- Mr. Godwin Tunze - Radio Signal Processing.\r\n2. Research collaboration (with Dr. Pham): Intelligent Distributed Cloud",
			"mnth_gls": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments -- in preparation of response letter.",
			"annl_gls": ""
		},
		{
			"user": "disciple",
			"fr_dt": "2021-05-03 00:00:00",
			"to_dt": "2021-05-07 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" 리뷰코멘트 기반 업데이트 진행중\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중 \r\no KICS, having been accepted, 최종 버전 제출 대기중",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30\r\no 한국-베트남 국제협력과제 작성 진행중, 제출일자 : 2021.05.25. // 계획서 수령",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료 및 용역 계획서 완료\r\no IEEE Access 논문 재제출 완료\r\no 국제협력 과제 제출 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-05-07 00:00:00",
			"to_dt": "2021-05-13 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-TBD\r\n\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: Target Journal- IEEE Transactions on Vehicular Technology\r\n-Submitted\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\n\r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-05-07 00:00:00",
			"to_dt": "2021-05-13 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (Magazine Paper).\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment:\r\nPerspectives and Challenges (Survey-IEEE Internet of things Journal).\r\n3. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n4. Adaptive Learning and Decision-making for Next-generation IoT-based Smart Grid Systems (Magazine paper).",
			"project_progress": "Work on the following topics:\r\n1. R&D at ICT Convergence research center\r\nA. Development of ICT for defense\r\nB. Radio communication convergence technology\r\nC. Depp-learning based fault detection and life prediction algorithm\r\nD. Drone control based ICT convergence\r\nE. Digital SoC for IoT/robots\r\nF. Medical nano convergence materials for defense\r\n\r\n2. Routing protocol for low-power and lossy IoT networks. \r\nA. RPL mechanism and control messages sequence.\r\nB. RPL related research work\r\n\r\n3. Real-time responsiveness in RL-enabled fog computing.",
			"mnth_gls": "1. Finalize a draft for Regional Innovation at ICT Convergence Research Center (magazine paper).\r\n2. Finalize an initial draft of the paper (2) with Dr. Tran, Dr. Tariq, and Dr. Sanjay.",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-05-07 00:00:00",
			"to_dt": "2021-05-13 00:00:00",
			"paper_progress": "Topic 1: Introducing 5G+ at 28GHz mmWave Test-bed (Survey)\r\nTopic 2: Resource Management for Fog Computing-based Reinforcement Learning: Perspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\nTopic 3: Machine learning-enabled Next Generation Sustainable Industrial IoT: Current Trends, Challenges, and Future Directions. (IEEE IoT Journal Special Issue on Cloud/Fog/Edge-enabled Big Data Intelligence for IoE)  Maybe can be another special issue. \r\nTopic 4: Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual Quality of Compressed Videos (IEEE/ACM Transaction on Audio, Speech, and Language Processing).\r\nTopic 5: Comparison of SARA Versus RW-TVfor Compressive Sensing of computed tomography.",
			"project_progress": "Update on the above topics\r\nTopic 1: Prototype that includes the structure of the paper.\r\nOrganization of the paper = Done.\r\nIntroduction, Related work, Detail of the implementation with hardware\r\nand future goals for devices as tabular form, the contribution of the\r\nwork and measurement results = Finished with Organization along with material input while results explanation need to be discussed more. \r\nTopic 2: Section will be shared with Dr. Hoa as it's done and then we can make a performance table for the respective section. The writing part of respective section V is done.\r\nTopic 3: Prototype that includes the structure of the paper.\r\nOrganization of the paper = Done.\r\nTopic 4: Missing results 80% done i.e., Bjontegaard delta (BD) bit-rate saving and encoder settings now finished.",
			"mnth_gls": "1. Finishing the paper writing part and checking other testbeds. (Topic 1)\r\n1. The target is to submit Topic 4 by end of this month. IEEE/ACM Transaction on Audio, Speech, and Language Processing.",
			"annl_gls": "2 SCI/SCIE paper\r\nA conference"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-05-10 00:00:00",
			"to_dt": "2021-05-14 00:00:00",
			"paper_progress": "1. On the Reliability of Industrial Internet of Things from Systematic Perspectives: Evaluation Approaches, Challenges, and Open Issues (IETE Technical Review - Submitted by Dr. Tran).\r\n2. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n3. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Submitted).",
			"project_progress": "1. Research supervision:\r\n- Mr. Godwin Tunze - Radio Signal Processing.\r\n2. Research collaboration \r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments -- in preparation of response letter.",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-05-10 00:00:00",
			"to_dt": "2021-05-14 00:00:00",
			"paper_progress": "* IEEE communications letters - major revision (~05.15)\r\n- 제출 완료 (05.13)\r\n\r\n* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~5%)",
			"project_progress": "",
			"mnth_gls": "- IEEE Communications letters 리비전 후 제출 (완료)\r\n- Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n  - Custom environment 제작 완료",
			"annl_gls": "* SCIE 논문 2편 목표\r\n- Cooperative retransmission NOMA 연구(현재 IEEE CL에 Major revision 제출)\r\n- Multicell NOMA-VLC system에 DQN적용한 CoMP 연구"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-05-10 00:00:00",
			"to_dt": "2021-05-14 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: TBD)",
			"project_progress": "Paper 1: Comparison of distributed cloud and related concepts (on-going writing)",
			"mnth_gls": "Finalize an initial draft of paper 1 with Dr. Thien",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2021-05-10 00:00:00",
			"to_dt": "2021-05-14 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: BTS-21-083 (LATEST SUBMISSION)\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 6: CL2021-0854\r\n(SUBMITTED TO: IEEE Communications Letters)\r\n\r\nTitle 7: applsci-1236625 (LATEST SUBMISSION)\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: JINT-D-21-00170\r\n(SUBMITTED TO: Journal of Intelligent & Robotic Systems)\r\n\r\nTitle 10: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 11: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 12: ICAIIC International Conference, 2021. [ACCEPTED & ATTENDED]\r\nTitle 13: JCCI, 2021. [ACCEPTED & VIRTUALLY PRESENTED]",
			"project_progress": "Title 1: Under review\r\n\r\nTitle 2: ACCEPTED and PUBLISHED\r\n\r\nTitle 3: PUBLICATION DECLINED on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations based on the previous review comments.\r\n-To finalize and re-submit before 10th June, 2021.\r\n\r\n\r\nTitle 4: ACCEPTED and PUBLISHED\r\n\r\nTitle 5: Under review. (LATEST SUBMISSION)\r\n-Reworked the paper's system model, readability, and simulations based on previous review comments.\r\n-Finalize and re-submitted on 13th May, 2021.\r\n\r\nTitle 6: Under review\r\n\r\nTitle 7: Under review. (LATEST SUBMISSION)\r\n-Reworked the paper's system model, readability, and simulations based on previous review comments.\r\n-Finalize and re-submitted on 11th May, 2021.\r\n\r\nTitle 8: Under review\r\n\r\nTitle 9: Under review\r\n\r\nTitle 10: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after Major revision.\r\n\r\nTitle 11: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Working with Prof. Kim on book/magazine.\r\n[2]. Reviewing numerous survey papers was done in this Week.\r\n[3]. To finalize on paper title and abstract by next week.\r\n[4]. To further discuss with Prof. Kim by next week.\r\n\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Working with Dr. Hoa Tran on a technical paper and a survey paper.\r\n[2]. Reviewing numerous survey papers was done in Week 3.\r\n[3]. To finalize on paper title and abstract by next week-end.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [10] above.\r\n[2]. Mr. Damian's Research TITLE [11] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-05-10 00:00:00",
			"to_dt": "2021-05-14 00:00:00",
			"paper_progress": "1. 국내저널 논문준비\r\n(엣지 컴퓨티관련 동향 논문\r\n2. 하계 통신학회 학술대회 논문준비\r\n(산업용 통신 프로토콜 변환에 관한 연구 or 블록체인 보안기술)",
			"project_progress": "1. 이노 폴리스 사업 제안서 작성 및 발표",
			"mnth_gls": "- 해외 특허, 국내 특허 아이디어 관련 논문 조사\r\n- 특허 1건 출원\r\n- 소프트웨어 등록 1건",
			"annl_gls": "- 해외논문 1편 투고\r\n- 저서 1권\r\n- 특허출원 6\r\n- 소프트웨어 등록 12"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-05-10 00:00:00",
			"to_dt": "2021-05-14 00:00:00",
			"paper_progress": "1. Shaping the future of Logistics\r\n-> Under review in IETE Technical Review\r\n\r\n2. Survey on IIoT Journal\r\n-> Under review in IETE Technical Review\r\n\r\n3. Survey on Reinforcement Learning\r\n-> Streaming the Introduction, System Model section, Applications\r\n\r\n4. Dynamic Collaborative Task Offloading in Fog Computing Systems\r\n-> Draft on Algorithms",
			"project_progress": "",
			"mnth_gls": "Submit paper # 3 in IEEE Internet of Things Journal\r\nSubmit paper # 4) in KICS summer 2021 conference",
			"annl_gls": "-) 4-5 International Conference\r\n-) 3-4 SCI Journal (Accepted)"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-05-14 00:00:00",
			"to_dt": "2021-05-20 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" 리뷰코멘트 기반 업데이트 진행중\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중\r\no KICS, having been accepted, 최종 버전 제출 대기중\r\no KICS, 하계학술대회 발표논문 준비",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30\r\no 한국-베트남 국제협력과제 작성 진행중, 제출일자 : 2021.05.25. // 계획서 작성 완료\r\no 석사과정 1명 논문 지도",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료 및 용역 계획서 완료\r\no IEEE Access 논문 재제출 완료\r\no 국제협력 과제 제출 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-05-14 00:00:00",
			"to_dt": "2021-05-20 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Physical Communication\r\n\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: \r\nTarget Journal- Wireless Networks\r\n-Update as per Comments\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication",
			"project_progress": "",
			"mnth_gls": "SCI Publication at-least Two",
			"annl_gls": ""
		},
		{
			"user": "B00502",
			"fr_dt": "2021-05-14 00:00:00",
			"to_dt": "2021-05-20 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (Magazine Paper).\r\n2. Learning-based Resource Management for Low-power and Lossy Networks (IEEE Transaction).\r\n3. Reinforcement Learning-based Resource Management for Fog Computing Environment:\r\nPerspectives and Challenges (Survey-IEEE Internet of things Journal).\r\n4. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n5. Reinforcement learning for Adaptive Channel Access in IoT Networks (Conference paper)",
			"project_progress": "Work on the following topics:\r\n1. R&D at ICT Convergence research center\r\nA. Development of a remote health monitoring system for defense\r\nB. Development of medical Bio convergence material for defense\r\nC. Smart battery material for high capacity energy storage\r\nD. High-efficiency energy conversion material for smart battery \r\nE. A study on the reliability of smart battery\r\n\r\n2. Link quality assessment mechanism for low-power and lossy networks\r\nA. Expected transmission counts\r\nB. Energy assessment mechanism \r\nC. Machine learning model for link quality assessment\r\n\r\n3. Challenges for RL-based fog computing.",
			"mnth_gls": "1. Finalize a draft for Regional Innovation at ICT Convergence Research Center (magazine paper).\r\n2. Finalize an initial draft of the paper (3) with Dr. Tran, Dr. Tariq, and Dr. Sanjay.\r\n3. Finalize draft for paper (2). \r\n4. Prepare a draft for KICS summer 2021 conference (paper 5).",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-05-14 00:00:00",
			"to_dt": "2021-05-20 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual Quality of Compressed Videos. (IEEE/ACM Transaction on Audio, Speech, and Language Processing).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography.\r\n3. Introducing 5G+ at 28GHz mmWave Test-bed (Survey)\r\n4. Resource Management for Fog Computing-based Reinforcement Learning: Perspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\n\r\n\r\n\r\n\r\nKICS summer conference.",
			"project_progress": "1. Bjontegaard delta (BD) bit-rate saving plotting for 15 and 30 frame rates and H.265/HEVC and VP9 encoders are done. \r\n   60fps remains for both encoders.\r\n   Correlation coefficients graphs are under the observations.\r\n2. Box plotting for SARA and TV analysis for CT images done.\r\n   The writing part continues in the results and discussion section. \r\n3. Application of the test-bed at our center. Depiction and discussion\r\n   Discussion and learning application as an application of the 5G + 28GHz mmWave, \r\n   (a) group discussion scenario, (b) learning management solution of online \r\n  classes, (c) smart green industrial complex.\r\n4. Section-wise tasks are done.\r\n   Dr. Hoa asked for a tabular explanation. Continue.......",
			"mnth_gls": "Submission of 1.\r\nFinalize a draft for 3.\r\nFinalize a draft with Dr. Hoa and others. \r\n\r\n\r\n\r\nKICS paper submission before the deadline.",
			"annl_gls": "2 SCI/SCIE papers"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-05-17 00:00:00",
			"to_dt": "2021-05-21 00:00:00",
			"paper_progress": "1. On the Reliability of Industrial Internet of Things from Systematic Perspectives: Evaluation Approaches, Challenges, and Open Issues (IETE Technical Review - Submitted by Dr. Tran).\r\n2. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n3. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Submitted).",
			"project_progress": "1. Research supervision:\r\n- Mr. Godwin Tunze - Radio Signal Processing.\r\n2. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments -- in preparation of response letter.",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2021-05-17 00:00:00",
			"to_dt": "2021-05-21 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: TBD)",
			"project_progress": "1. Specify the characteristics of distributed cloud (DC) and in comparison with conventional cloud deployment (e.g., public cloud, private cloud, hybrid cloud, multi-cloud), and related edge paradigms (on-going writing).\r\n2. Survey papers about AI for key technologies enabling 5G distributed cloud, such as SDN, NFV, network slicing",
			"mnth_gls": "Finalize an initial draft of paper 1 with Dr. Thien",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-05-17 00:00:00",
			"to_dt": "2021-05-21 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~10%)\r\n\r\n* KICS 하계학술대회\r\n- 시뮬레이션 작성중",
			"project_progress": "",
			"mnth_gls": "- IEEE Communications letters 리비전 후 제출 (완료)\r\n- Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n  -> Custom environment 적용",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-05-17 00:00:00",
			"to_dt": "2021-05-21 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" 답변서 작성 완료, 차주 제출 예정\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중 \r\no KICS 저널 8월 게재 예정, 최종 버전 제출 대기중\r\no KICS 하계 통신학회 학술대회 논문준비",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30. // 5월 마지막 주 수령 예정\r\no 한국-베트남 국제협력과제 작성 진행중, 제출일자 : 2021.05.25. // 제안서 검토중",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료 및 용역 계획서 완료\r\no IEEE Access 논문 재제출 완료\r\no 국제협력 과제 제출 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "william",
			"fr_dt": "2021-05-17 00:00:00",
			"to_dt": "2021-05-21 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123 (LATEST SUBMISSION)\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: CAL-2021-05-0063 (LATEST SUBMISSION)\r\n(SUBMITTED TO: IEEE Computer Letters)\r\n\r\nTitle 7: applsci-1236625\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: JINT-D-21-00170\r\n(SUBMITTED TO: Journal of Intelligent & Robotic Systems)\r\n\r\nTitle 10: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 11: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 12: ICAIIC International Conference, 2021. [AWAITING PUBLICATION]\r\nTitle 13: JCCI, 2021. [AWAITING PUBLICATION]",
			"project_progress": "Title 1: Under review\r\n\r\nTitle 2: ACCEPTED and PUBLISHED\r\n\r\nTitle 3: PUBLICATION DECLINED on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations based on the previous review comments.\r\n-To finalize and re-submit before 10th June, 2021.\r\n\r\n\r\nTitle 4: ACCEPTED and PUBLISHED\r\n\r\nTitle 5: Under review. (LATEST SUBMISSION)\r\n-Paper was deemed OUT-OF-SCOPE from the previous journal and declined.\r\n-Reworked the paper's system model, readability, and simulations based on previous review comments.\r\n-Finalize and re-submitted on 18th May, 2021.\r\n\r\nTitle 6: Under review (LATEST SUBMISSION)\r\n-Paper was deemed OUT-OF-SCOPE from the previous journal and declined.\r\n-Reworked the paper's system model, readability, and simulations based on previous review comments.\r\n-Finalize and re-submitted on 21st May, 2021.\r\n\r\nTitle 7: Under review.\r\n\r\nTitle 8: Under review\r\n\r\nTitle 9: Under review\r\n\r\nTitle 10: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after Major revision.\r\n\r\nTitle 11: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [10] above.\r\n[2]. Mr. Damian's Research TITLE [11] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-05-17 00:00:00",
			"to_dt": "2021-05-21 00:00:00",
			"paper_progress": "1. 국내저널 논문준비 \r\n  - 엣지 컴퓨팅 동향 논문 준비중\r\n\r\n2. 하계 통신학회 학술대회 논문준비\r\n  - 주제변경: 블록체인 구현관련 논문, 차주금 투고준비\r\n\r\n3. 특허준비 \r\n - 하드웨어 제작플랫폼 특허출원신청(선행조사진행중)\r\n - 새로운 특허 아이디어 검토",
			"project_progress": "1. 공학컨설팅센터 BM개발과제 발표지원 (월24, 서울출장)\r\n2. 스마트에너지 플랫폼 사업 지원",
			"mnth_gls": "- 특허 1건 출원\r\n- 소프트웨어 등록 1건",
			"annl_gls": "- 저서 1권\r\n- 특허출원 6\r\n- 소프트웨어 등록 12\r\n- 과제진행"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-05-17 00:00:00",
			"to_dt": "2021-05-21 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Physical Communication\r\n\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: \r\nTarget Journal- Wireless Networks\r\n-Update as per Comments\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-05-21 00:00:00",
			"to_dt": "2021-05-27 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (Magazine Paper).\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks, IEEE Transaction, (Finalized, ready to submit). \r\n3. Reinforcement Learning-based Resource Management for Fog Computing Environment:\r\nPerspectives and Challenges (Survey-IEEE Internet of things Journal).\r\n4. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n5. Federated learning framework for Intelligent IoT Networks, KICS Summer 2021 (Submitted).",
			"project_progress": "Worked on the following topics:\r\n1. R&D at ICT Convergence research center\r\nA. Realistic remote control system project \r\nB. Prognostic and health management system (PHM)\r\nC. Prediction for combat and disaster \r\nD. Smart storage system in ICT-CRC\r\nE. Civil-Military ICT Convergence Technology for Smart IoT Platform \r\n\r\n2. Federated learning framework for Intelligent IoT Networks\r\nA. Federated learning mechanism\r\nB. Results and Simulation\r\n\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks\r\nA. Experimental results and analysis\r\n\r\n4. Reinforcement Learning-based Resource Management for Fog Computing Environment: Perspectives and Challenges",
			"mnth_gls": "1. Finalize a draft for Regional Innovation at ICT Convergence Research Center (magazine paper).\r\n2. Finalize an initial draft of the paper (3) with Dr. Tran, Dr. Tariq, and Dr. Sanjay.\r\n3. Finalize final draft for paper (2).",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-05-21 00:00:00",
			"to_dt": "2021-05-27 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual \r\n   Quality of Compressed Videos. (IEEE/ACM Transaction on Audio, Speech, and \r\n   Language Processing).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography.\r\n3. Introducing 5G+ at 28GHz mmWave Test-bed. (IEEE Transactions on Education)\r\n4. Resource Management for Fog Computing-based Reinforcement Learning: \r\n   Perspectives and Challenges. (IEEE Internet of Things Journal; Special Issue), (Finalizing process).\r\n5. Deep Learning-based Colorectal Cancer Detection in Endoscopic Images. KICS \r\n   Summer 2021. (Finalized and Submitted).",
			"project_progress": "1. Bjontegaard delta (BD) bit-rate saving plotting for 15, 30, and 60fps for both encoders done. \r\nCorrelation coefficient graphs are under the observations.\r\n2. Box plotting for SARA and TV analysis for CT images done.\r\nThe writing part continues in the results and discussion section.\r\n3. Application of the test-bed at our center. Depiction and discussion\r\nDiscussion and learning application as an application of the 5G + 28GHz mmWave,\r\n(a) group discussion scenario, (b) learning management solution of online\r\nclasses, (c) smart green industrial complex.\r\n4. Finalizing the paper.\r\n5. Finalized and submitted.",
			"mnth_gls": "1. Finalize the paper for submission.\r\n3. Finalize the initial draft.\r\n4. Finalize the paper and submission.",
			"annl_gls": "2 SCI/SCIE"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-05-30 00:00:00",
			"paper_progress": "1- \"Shaping the future of logistics: data-driven technology approaches and strategic management\", IETE Technical Review (under review)\r\n2- \"On the reliability of IIoT systems: perspectives and challenges\", IETE Technical Review (Under Review)\r\n3- \" A resource allocation algorithms for task offloading in Fog-based IoT systems\", KICS Summer 2021 (Finalized, ready to submit)\r\n4- \" Reinforcement Learning based Resource Allocation for Fog Computing Environment\", IEEE IoT journal (On Finalizing process)",
			"project_progress": "",
			"mnth_gls": "-Submit paper #4 in IEEE IoT Journal",
			"annl_gls": "-3-4 SCI Journal"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-05-28 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: IEEE Communications Magazine)",
			"project_progress": "",
			"mnth_gls": "Finalize an initial draft of paper 1 with Dr. Thien",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-05-28 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~30%)\r\n\r\n* KICS 하계학술대회\r\n- 제출 완료",
			"project_progress": "",
			"mnth_gls": "- IEEE Communications letters 리비전 후 제출 (완료)\r\n- Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n-> Custom environment 적용",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-05-28 00:00:00",
			"paper_progress": "1. On the Reliability of Industrial Internet of Things from Systematic Perspectives: Evaluation Approaches, Challenges, and Open Issues (IETE Technical Review - Submitted by Dr. Tran).\r\n2. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n3. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Submitted).",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.\r\nMonthly goals \t1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments -- in preparation of response letter.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "disciple",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-05-28 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" 리뷰코멘트 기반 업데이트 진행중 // 답변서 작성 완료\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중 \r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중\r\no KICS 하계 통신학회 학술대회 논문준비",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30. // 5월 마지막 주 수령 예정\r\no 한국-베트남 국제협력과제 제출완료 //2021.09 중 결과 발표 및 2021.10.01 과제 개시\r\no 한국-프랑스 국제협력과제 검토중",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료 및 용역 계획서 완료\r\no IEEE Access 논문 재제출 완료\r\no 국제협력 과제 제출 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-05-28 00:00:00",
			"paper_progress": "1.국내저널 논문준비\r\n(엣지 컴퓨티관련 동향 논문 준비) - holding\r\n\r\n2. 하계 통신학회 학술대회 논문 투고\r\n(IoT 시스템에서의 블록체인 구현 기술에 관한 연구)",
			"project_progress": "",
			"mnth_gls": "- 특허 1건 출원\r\n- 소프트웨어 등록 1건",
			"annl_gls": "- 해외논문 1편 투고\r\n- 저서 1권\r\n- 특허출원 6\r\n- 소프트웨어 등록 12"
		},
		{
			"user": "william",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-06-28 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: AWPL-05-21-1163 (LATEST SUBMISSION)\r\n(SUBMITTED TO: IEEE Antenna and Wireless Propagation Letters)\r\n\r\nTitle 7: applsci-1236625\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: JINT-D-21-00170\r\n(SUBMITTED TO: Journal of Intelligent & Robotic Systems)\r\n\r\nTitle 10: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 11: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 12: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 13: JCCI, 2021. [AWAITING PUBLICATION]",
			"project_progress": "Title 1: Under review\r\n\r\nTitle 2: ACCEPTED and PUBLISHED\r\n\r\nTitle 3: PUBLICATION DECLINED on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations based on the previous review comments.\r\n-To finalize and re-submit before 10th June, 2021.\r\n\r\n\r\nTitle 4: ACCEPTED and PUBLISHED\r\n\r\nTitle 5: Under review.\r\n\r\nTitle 6: Under review (LATEST SUBMISSION)\r\n-Paper was deemed OUT-OF-SCOPE from the previous journal and declined.\r\n-Reworked the paper's system model, readability, and simulations based on previous review comments.\r\n-Finalized and re-submitted on 28th May, 2021.\r\n\r\nTitle 7: Under review.\r\n\r\nTitle 8: Under review\r\n\r\nTitle 9: Under review\r\n\r\nTitle 10: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after Major revision.\r\n\r\nTitle 11: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [10] above.\r\n[2]. Mr. Damian's Research TITLE [11] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-05-24 00:00:00",
			"to_dt": "2021-06-28 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Physical Communication-Submitted\r\n\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: \r\nTarget Journal- Wireless Networks-Submitted\r\n\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "",
			"fr_dt": "2021-05-28 00:00:00",
			"to_dt": "2021-06-03 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" 리뷰코멘트 기반 업데이트 진행중 // 답변서 작성 완료\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중 \r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중\r\no KICS 하계 통신학회 학술대회 논문준비",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30. // 5월 마지막 주 수령 예정\r\no 한국-베트남 국제협력과제 작성 진행중, 제출일자 : 2021.05.25. // 1차본 업로드 완료\r\no 한국-프랑스 국제협력과제 검토중",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료 및 용역 계획서 완료\r\no IEEE Access 논문 재제출 완료\r\no 국제협력 과제 제출 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-05-28 00:00:00",
			"to_dt": "2021-06-03 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (IEEE Transaction on Education).\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks, IEEE Transaction, (IEEE Transaction).\r\n3. Reinforcement Learning based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey-IEEE Internet of things Journal).\r\n4. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n5. Federated learning framework for Intelligent IoT Networks, KICS Summer 2021 (Submitted).",
			"project_progress": "",
			"mnth_gls": "1. Finalize a draft for paper 1 \"Regional Innovation at ICT Convergence Research Center\".\r\n2. Finalize a draft for paper 2 \"Learning-based Resource Management for Low-power and Lossy IoT Networks\".",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-05-28 00:00:00",
			"to_dt": "2021-06-03 00:00:00",
			"paper_progress": "1. Introducing 5G+ at 28GHz mmWave Test-bed. (IEEE Transactions on Education)\r\n2. Resource Management for Fog Computing-based Reinforcement Learning:\r\nPerspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\n3. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE/ACM Transaction on Audio, Speech, and\r\nLanguage Processing).\r\n4. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography.\r\n5. Deep Learning-based Colorectal Cancer Detection in Endoscopic Images. KICS\r\nSummer 2021.",
			"project_progress": "1. > Testbed results section done.\r\n   > Applications of the testbed at center i.e, learning management and AR/VR \r\n     streaming.\r\n   > K7U industrial-academic collaboration.\r\n   > Google cloud smart factory.\r\n   > Triz PBL.\r\n2. > Status is under review.\r\n3. > Finalised and ready for submission. (11th June). \r\n4. > Ongoing. \r\n5. > Accepted",
			"mnth_gls": "Finished 1 and 3 for finalized submission.",
			"annl_gls": "2 SCI/SCIE journals."
		},
		{
			"user": "thienht",
			"fr_dt": "2021-05-31 00:00:00",
			"to_dt": "2021-06-04 00:00:00",
			"paper_progress": "1. On the Reliability of Industrial Internet of Things from Systematic Perspectives: Evaluation Approaches, Challenges, and Open Issues (IETE Technical Review - Submitted by Dr. Tran).\r\n2. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Submitted Revision).\r\n3. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Submitted).",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.\r\nMonthly goals 1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments -- in preparation of response letter.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2021-05-31 00:00:00",
			"to_dt": "2021-06-04 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: IEEE Communications Magazine)\r\n3. Computation Offloading in Vehicle-assisted Multi-access Edge Computing: A QoE-based Optimization Approach (TBD)",
			"project_progress": "1. Survey papers about AI for key technologies enabling 5G distributed cloud, such as SDN, NFV, network slicing\r\n2. Doing simulation for paper 3",
			"mnth_gls": "Finalize a draft of paper 1 with Dr. Thien\r\nFinish paper 3",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-05-31 00:00:00",
			"to_dt": "2021-06-04 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~30%)\r\n\r\n* Cooperative Retransmission scheme in NOMA\r\n- IEEE communications letters (Major revision -> Rejected)\r\n- Reviewer 의견 반영해서 수정\r\n- 차주 ICT express 제출",
			"project_progress": "- BMS개발 관련 기술이전 문의 진행",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n - 수정 후 ICT express 제출\r\n\r\n* Multicell NOMA-VLC system에 DQN 적용\r\n - DQN기반 시뮬레이터 완료",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "william",
			"fr_dt": "2021-05-31 00:00:00",
			"to_dt": "2021-06-04 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAS-II-10481-2021 (LATEST SUBMISSION)\r\n(SUBMITTED TO: IEEE Transactions on Circuits and Systems II: Express Briefs)\r\n\r\nTitle 7: applsci-1236625\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: JINT-D-21-00170\r\n(SUBMITTED TO: Journal of Intelligent & Robotic Systems)\r\n\r\nTitle 10: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 11: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 12: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 13: JCCI, 2021. [AWAITING PUBLICATION]",
			"project_progress": "Title 1: Under review\r\n\r\nTitle 2: ACCEPTED and PUBLISHED\r\n\r\nTitle 3: PUBLICATION DECLINED on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations based on the previous review comments.\r\n-To finalize and re-submit before 10th June, 2021.\r\n\r\n\r\nTitle 4: ACCEPTED and PUBLISHED\r\n\r\nTitle 5: Under review.\r\n\r\nTitle 6: Under review (LATEST SUBMISSION)\r\n\r\nTitle 7: PUBLICATION DECLINED on 2020/06/04. Resubmission allowed after Major revision.\r\n-Reworking the paper's system model, readability, and simulations based on received review comments.\r\n-To finalize and re-submit on 11th June, 2021.\r\n\r\nTitle 8: Under review\r\n\r\nTitle 9: Under review\r\n\r\nTitle 10: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after Major revision.\r\n\r\nTitle 11: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [10] above.\r\n[2]. Mr. Damian's Research TITLE [11] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-05-31 00:00:00",
			"to_dt": "2021-06-04 00:00:00",
			"paper_progress": "#1: \"Shaping the future of logistics\", IETE Technical Review (Under Review)\r\n#2: \"On reliability of IIoT systems\", IETE Technical Review (Under Review)\r\n#3: \"Reinforcement learning based resource allocation in fog computing\", IEEE IoT journal (Under Review)\r\n#4: \"Parallel Communication and Computation in Fog Computing: A performance analysis\", IEEE IoT Journal ( In preparation)\r\n#5: \" Physical Internet in the Era of Digital Transformation: Perspectives and Challenges\", IEEE IoT Journal ( In preparation)",
			"project_progress": "",
			"mnth_gls": "-Submit paper #4",
			"annl_gls": "3-4 SIC(E) accepted"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-05-31 00:00:00",
			"to_dt": "2021-06-04 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" // 제출완료\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중\r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중\r\no KICS 하계 통신학회 학술대회 제출완료",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30. // 재작성 요청\r\no 한국-베트남 국제협력과제 제출완료 //2021.09 중 결과 발표 및 2021.10.01 과제 개시\r\no 한국-프랑스 국제협력과제 연기.\r\no 개도국지원사업 후보자 조사 중.",
			"mnth_gls": "o IEEE Access 시뮬레이션 완료.\r\no NRF BP 과제 제출 완료.\r\no 개도국지원사업 작성 완료.",
			"annl_gls": "o SCIE 2편 게재"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-05-31 00:00:00",
			"to_dt": "2021-06-04 00:00:00",
			"paper_progress": "1.국내저널 논문준비\r\n(엣지 컴퓨티관련 동향 논문 준비) - holding\r\n2. 하계 통신학회 학술대회 논문 투고\r\n(IoT 시스템에서의 블록체인 구현 기술에 관한 연구)",
			"project_progress": "",
			"mnth_gls": "- 특허 1건 출원\r\n- 소프트웨어 등록 1건",
			"annl_gls": "- 저서 1권\r\n- 특허출원 6\r\n- 소프트웨어 등록 12"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-06-04 00:00:00",
			"to_dt": "2021-06-10 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Physical Communication-Submitted\r\n\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: \r\nTarget Journal- Wireless Networks-Submitted\r\n\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\nTarget Journal IEEE IoT Journal-Submitted\r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication \r\n \r\n5. Inception Based ResNet Autoencoder for B5G in Multipath Fading Channels-Rejected\r\nUpdates per comments",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-06-04 00:00:00",
			"to_dt": "2021-06-10 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (IEEE Transaction on Education).\r\n2. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN 2021, In Preparation)\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks, IEEE Transaction, (IEEE Transaction).\r\n4. Reinforcement Learning based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey-IEEE Internet of things Journal, under review).\r\n5. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n6. Federated learning framework for Intelligent IoT Networks, KICS Summer 2021 (accepted).",
			"project_progress": "",
			"mnth_gls": "1. Finalize a draft for paper 1 \"Regional Innovation at ICT Convergence Research Center\".\r\n2. Finalize paper 2 \"Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning,\" ICUFN 2021. \r\n3. Finalize a draft for paper 3 \"Learning-based Resource Management for Low-power and Lossy IoT Networks\".",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-06-04 00:00:00",
			"to_dt": "2021-06-10 00:00:00",
			"paper_progress": "1. Introducing 5G+ at 28GHz mmWave Test-bed. (IEEE Transactions on Education)\r\n2. Resource Management for Fog Computing-based Reinforcement Learning:\r\nPerspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\n3. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE/ACM Transaction on Audio, Speech, and\r\nLanguage Processing).\r\n4. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography.\r\n5. Deep Learning-based Colorectal Cancer Detection in Endoscopic Images. KICS\r\nSummer 2021.\r\n6. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).",
			"project_progress": "1. > Ongoing with prof. Kim\r\n> K7U industrial-academic collaboration.\r\n> Google cloud smart factory.\r\n2. > Status is under review.\r\n3. > Finalised and ready for submission.\r\n4. > Ongoing.\r\n5. > Accepted.\r\n6. Submitted to ICUFN.",
			"mnth_gls": "Finish 3 and submit it\r\nFinish 4 and submit it",
			"annl_gls": "2 SCI/SCIE journals."
		},
		{
			"user": "thienht",
			"fr_dt": "2021-06-07 00:00:00",
			"to_dt": "2021-06-11 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Under review).",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-06-07 00:00:00",
			"to_dt": "2021-06-11 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~30%) -> 금주 Pending\r\n\r\n* Cooperative Retransmission scheme in NOMA\r\n- ICT express 제출 완료",
			"project_progress": "- BMS 개발 기술이전 관련 문의 진행",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express 제출 완료\r\n\r\n* Multicell NOMA-VLC system에 DQN 적용\r\n- DQN기반 시뮬레이터 완료",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-06-07 00:00:00",
			"to_dt": "2021-06-11 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: IEEE Communications Magazine)\r\n3. Computation Offloading in Vehicle-assisted Multi-access Edge Computing: A QoE-based Optimization Approach (TBD)",
			"project_progress": "1. Compare commercial distributed cloud solutions (paper 1)\r\n2. Doing simulation for paper 3",
			"mnth_gls": "Finalize a draft of paper 1 with Dr. Thien\r\nFinish paper 3",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-06-07 00:00:00",
			"to_dt": "2021-06-11 00:00:00",
			"paper_progress": "1.국내저널 논문준비\r\n(엣지 컴퓨티관련 동향 논문 준비) - holding\r\n\r\n2. 하계 통신학회 학술대회 논문 투고\r\n(IoT 시스템에서의 블록체인 구현 기술에 관한 연구) - 발표준비",
			"project_progress": "etc\r\n1. 해외 특허, 국내 특허 아이디어 관련 논문 조사\r\n\r\n2. 업체 기술컨설팅 관련 업체 연락 \r\n\r\n3. 계약학과 및 산업대학원 모집 지원",
			"mnth_gls": "- 특허 1건 출원\r\n- 소프트웨어 등록 1건",
			"annl_gls": "- 해외논문 1편 투고\r\n- 저서 1권\r\n- 특허출원 6\r\n- 소프트웨어 등록 12"
		},
		{
			"user": "william",
			"fr_dt": "2021-06-07 00:00:00",
			"to_dt": "2021-06-11 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAS-II-10481-2021\r\n(SUBMITTED TO: IEEE Transactions on Circuits and Systems II: Express Briefs)\r\n\r\nTitle 7: applsci-1236625 (LATEST RE-SUBMISSION)\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 10: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 11: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 12: JCCI, 2021. [AWAITING PUBLICATION]",
			"project_progress": "Title 1: Under review\r\n\r\nTitle 2: ACCEPTED and PUBLISHED\r\n\r\nTitle 3: PUBLICATION DECLINED on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations as per review comments.\r\n-To finalize and re-submit before 25th June, 2021.\r\n\r\n\r\nTitle 4: ACCEPTED and PUBLISHED.\r\n\r\nTitle 5: Under review.\r\n\r\nTitle 6: Under review.\r\n\r\nTitle 7: Under review. (LATEST RE-SUBMISSION) \r\n-Reworked the paper's system model, readability, and simulations based on received review comments.\r\n-Finalized and re-summited on 10th June, 2021.\r\n\r\nTitle 8: Under review.\r\n\r\nTitle 9: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after Major revision.\r\n\r\nTitle 10: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [9] above.\r\n[2]. Mr. Damian's Research TITLE [10] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "disciple",
			"fr_dt": "2021-06-07 00:00:00",
			"to_dt": "2021-06-11 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" // 제출완료\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중 \r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중\r\no KICS 하계 통신학회 학술대회 발표준비 // 제출완료",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30. // 5월 마지막 주 수령 예정\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 개도국지원사업 후보자 조사 중.",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료\r\no IEEE Access 시뮬레이션 완료.\r\no NRF BP과제 작성 완료. \r\no NRF 개도국지원사업 작성 완료.",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-06-11 00:00:00",
			"to_dt": "2021-06-17 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Physical Communication-Submitted\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: \r\nTarget Journal- Wireless Networks-Submitted\r\n\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\nTarget Journal IEEE IoT Journal-Submitted\r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication \r\n\r\n5. Inception Based ResNet Autoencoder for B5G in Multipath Fading Channels-Rejected\r\nUpdates per comments",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-06-11 00:00:00",
			"to_dt": "2021-06-17 00:00:00",
			"paper_progress": "1. Introducing 5G+ at 28GHz mmWave Test-bed. (IEEE Transactions on Education)\r\n2. Resource Management for Fog Computing-based Reinforcement Learning:\r\nPerspectives and Challenges. (IEEE Internet of Things Journal; Special Issue)\r\n3. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE/ACM Transaction on Audio, Speech, and\r\nLanguage Processing).\r\n4. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography.\r\n5. Deep Learning-based Colorectal Cancer Detection in Endoscopic Images. KICS\r\nSummer 2021.\r\n6. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).",
			"project_progress": "1. > Ongoing with prof. Kim\r\n2. > Status = Rejected due to regular paper and survey issue. \r\n   > New submission will be >>> Journal of Network and Computer Applications\r\n3. > Ongoing\r\n4. > Ongoing.\r\n5. > Accepted and presented at KICS \r\n6. Submitted to ICUFN.",
			"mnth_gls": "Submission of 2 and 3",
			"annl_gls": "2 SCI/SCIE papers\r\n2 International conferences"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-06-11 00:00:00",
			"to_dt": "2021-06-17 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center (IEEE Transaction on Education).\r\n2. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN 2021, submitted)\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks, IEEE Transaction, (IEEE Transaction).\r\n4. Reinforcement Learning based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey-IEEE Internet of things Journal).\r\n5. Machine Learning-enabled Next Generation Sustainable Industries of Future\r\n(IoF)/ Industrial Internet of Things (IIoT)/ Smart Manufacturing Industries: Current Trends, Challenges, and Future Challenges (Magazine paper).\r\n6. Federated learning framework for Intelligent IoT Networks, KICS Summer 2021 (accepted).",
			"project_progress": "",
			"mnth_gls": "1. Finalize a draft for paper 1 \"Regional Innovation at ICT Convergence Research Center\".\r\n2. Finalize a draft for paper 3 \"Learning-based Resource Management for Low-power and Lossy IoT Networks\".",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2021-06-14 00:00:00",
			"to_dt": "2021-06-18 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: IEEE Communications Magazine)\r\n3. Computation Offloading in Vehicle-assisted Multi-access Edge Computing: A QoE-based Optimization Approach (TBD)",
			"project_progress": "1. Requirements for IDC (paper1)\r\n2. Continue doing simulation and extension for paper 3",
			"mnth_gls": "Finalize a draft of paper 1 with Dr. Thien\r\nFinish paper 3",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-06-14 00:00:00",
			"to_dt": "2021-06-18 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~50%)\r\n- Backpropagation시 gradient graph 에러 확인 및 수정중",
			"project_progress": "* BMS 개발 기술이전 관련 문의 진행\r\n- 벡셀 쪽에서 바로 기술이전 받는 형태로는 수행이 어렵다고 하여, 하드웨어 개발 업체에 벡셀에서 자금 집행후, 하드웨어 업체에서 기술이전을 받는 형태로 진행예정.",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Multicell NOMA-VLC system에 DQN 적용\r\n- DQN기반 시뮬레이터 완료 목표",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-06-14 00:00:00",
			"to_dt": "2021-06-18 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Under review).",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2021-06-14 00:00:00",
			"to_dt": "2021-06-18 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAS-II-10481-2021\r\n(SUBMITTED TO: IEEE Transactions on Circuits and Systems II: Express Briefs)\r\n\r\nTitle 7: applsci-1236625\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: SIPN-00774-2021\r\n(SUBMITTED TO: IEEE Trans. on Signal and Info Processing Over Networks)\r\n\r\nTitle 9: applsci-1031543\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 10: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 11: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 12: JCCI, 2021. [AWAITING PUBLICATION]",
			"project_progress": "Title 1: Under review\r\n\r\nTitle 2: ACCEPTED and PUBLISHED\r\n\r\nTitle 3: PUBLICATION DECLINED on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations as per review comments.\r\n-To finalize and re-submit before 25th June, 2021.\r\n\r\nTitle 4: ACCEPTED and PUBLISHED.\r\n\r\nTitle 5: Under review.\r\n\r\nTitle 6: Under review.\r\n\r\nTitle 7: Under review.\r\n\r\nTitle 8: Under review.\r\n\r\nTitle 9: PUBLICATION DECLINED on 2020/12/14. Resubmission allowed after Major revision.\r\n\r\nTitle 10: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Cosmas's Research TITLE [9] above.\r\n[2]. Mr. Damian's Research TITLE [10] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "disciple",
			"fr_dt": "2021-06-14 00:00:00",
			"to_dt": "2021-06-18 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" // 게재확정, 최종버전 제출\r\no IEEE Access, image-based Automatic Modulation Classification (AMC) 관련 시뮬레이션 진행 중 \r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중\r\no KICS 하계 통신학회 학술대회 발표준비 // 제출완료",
			"project_progress": "o NRF BP 과제 (인도포닥) 작성 진행중, 제출일자 : 2021.06.30. // 90% 작성완료\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 개도국지원사업 후보자 조사 중.",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료\r\no IEEE Access 후속 논문관련 시뮬레이션 완료.\r\no NRF BP과제 작성 완료. \r\no NRF 개도국지원사업 작성 완료.",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-06-14 00:00:00",
			"to_dt": "2021-06-18 00:00:00",
			"paper_progress": "1.국내저널 논문준비\r\n(엣지 컴퓨티관련 동향 논문 준비) - holding\r\n\r\n2. KICS 하계종합발표회 논문발표 준비 및 온라인 발표\r\n(IoT 시스템을 위한 블록체인 구현기술)\r\n\r\n3. 스마트 모니터링 관련 구현관련 연구 진행",
			"project_progress": "1. 이노 폴리스 사업 \r\n- 매주 목 교육참가\r\n\r\n2. 재직자 지원 일반산업대학원 등록홍보 (1명지원)\r\n\r\n3. 특허출원진행중\r\n- 하드웨어 제작 플랫폼",
			"mnth_gls": "- 특허 출원 1건\r\n- 소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-06-18 00:00:00",
			"to_dt": "2021-06-24 00:00:00",
			"paper_progress": "1. Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal-Physical Communication-Submitted\r\n\r\n\r\n2. Double Deep Q-Learning based resource allocation for URLLC in V2V: \r\nTarget Journal- Wireless Networks-Submitted\r\n\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\nTarget Journal IEEE IoT Journal-Submitted\r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication \r\n\r\n5. Inception Based ResNet Autoencoder for B5G in Multipath Fading Channels-Rejected\r\nUpdates per comments",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at-least Two"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-06-18 00:00:00",
			"to_dt": "2021-06-24 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE/ACM Transaction on Audio, Speech, and\r\nLanguage Processing).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography.\r\n3. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).",
			"project_progress": "1. Submitted\r\n2. Will be submitted soon.\r\n3. Submitted",
			"mnth_gls": "",
			"annl_gls": "2 SCI/SCIE Publications."
		},
		{
			"user": "B00502",
			"fr_dt": "2021-06-18 00:00:00",
			"to_dt": "2021-06-24 00:00:00",
			"paper_progress": "1. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal). \r\n2. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n3. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team). \r\n4. Regional Innovation at ICT Convergence Research Center: Education and Research (IEEE Transaction on Education).",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at least two."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-06-21 00:00:00",
			"to_dt": "2021-06-25 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: IEEE Communications Magazine)\r\n3. Computation Offloading in Vehicle-assisted Multi-access Edge Computing: A QoE-based Optimization Approach (TBD)",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2021-06-21 00:00:00",
			"to_dt": "2021-07-25 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAS-II-10481-2021\r\n(SUBMITTED TO: IEEE Transactions on Circuits and Systems II: Express Briefs)\r\n\r\nTitle 7: applsci-1236625\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: JCAS-D-21-00519\r\n(SUBMITTED TO: International Journal of Control, Automation and Systems)\r\n\r\nTitle 9: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 11: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 12: JCCI, 2021. [AWAITING PUBLICATION]",
			"project_progress": "Title 1: Under review\r\n\r\nTitle 2: ACCEPTED and PUBLISHED\r\n\r\nTitle 3: PUBLICATION DECLINED on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations as per review comments.\r\n-To finalize and re-submit before 5th July, 2021.\r\n\r\nTitle 4: ACCEPTED and PUBLISHED.\r\n\r\nTitle 5: Under review.\r\n\r\nTitle 6: Under review.\r\n\r\nTitle 7: Under review.\r\n\r\nTitle 8: Under review.\r\n\r\nTitle 9: PUBLICATION DECLINED on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Damian's Research TITLE [9] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-06-21 00:00:00",
			"to_dt": "2021-06-25 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~60%)\r\n- Backpropagation시 gradient graph 에러 수정 완료\r\n- Overfitting 문제 해결중\r\n  (Batch normalization 및 replay memory 활용한 샘플링 적용)",
			"project_progress": "* BMS 개발 기술이전 관련 진행\r\n- 기술이전 관련 자금처리 협의",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Multicell NOMA-VLC system에 DQN 적용\r\n- DQN기반 시뮬레이터 완료 목표",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-06-21 00:00:00",
			"to_dt": "2021-06-25 00:00:00",
			"paper_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" // 온라인 게재\r\no IEEE Access, \"image-based Automatic Modulation Classification (AMC)\" // 시뮬레이션 진행중\r\no KICS, \"image-based Automatic Modulation Classification (AMC)\" // 시뮬레이션 완료, 국내 논문 작성중\r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중",
			"project_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" 관련 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥) 작성완료, 제출일자 : 2021.06.30. // 1차 버전 업로드 완료\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 개도국지원사업 후보자 조사 중.",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료\r\no IEEE Access 후속 논문관련 시뮬레이션 완료.\r\no NRF BP과제 작성 완료.\r\no NRF 개도국지원사업 작성 완료.",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-06-25 00:00:00",
			"to_dt": "2021-07-01 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE IoT Journal - Major Revision).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Under review).",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-06-25 00:00:00",
			"to_dt": "2021-07-01 00:00:00",
			"paper_progress": "1- \"Shaping the future of logistics\", IETE Technical Review (under review)\r\n2- \"On the reliability of IIoT Systems\", IETE Technical Review (under review)\r\n3- \"Reinforcement Learning based Resource Management for Fog Computing System\", Journal of Network and Computer Applications ( Under review)\r\n4- \" Physical Internet in the Era of Digital Transformation\", IEEE IoT Journal (In progress)",
			"project_progress": "",
			"mnth_gls": "Submit paper #4",
			"annl_gls": "3-4 accepted SCI/E Journals"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-06-25 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography.\r\n3. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n4. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities\r\n5. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues.",
			"project_progress": "1. Submitted\r\n2. Submission (Next week expected) \r\n3. Submitted\r\n4. 80% done, and submission will be done by end of this month.\r\n5. Submitted",
			"mnth_gls": "",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-06-25 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center: Education and Researches (IEEE Transaction on Education)\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n3. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n4. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at least two."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-06-28 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: IEEE Communications Magazine)\r\n3. Computation Offloading in Vehicle-assisted Multi-access Edge Computing: A QoE-based Optimization Approach (ICTC 2021)",
			"project_progress": "Submit 3",
			"mnth_gls": "",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2021-06-28 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAS-II-10481-2021\r\n(SUBMITTED TO: IEEE Transactions on Circuits and Systems II: Express Briefs)\r\n\r\nTitle 7: applsci-1236625\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: JCAS-D-21-00519\r\n(SUBMITTED TO: International Journal of Control, Automation and Systems)\r\n\r\nTitle 9: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 11: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 12: JCCI, 2021. [PUBLISHED]",
			"project_progress": "Title 1: Publication declined on 2021/06/29. Currently revising to re-submit soon.\r\n\r\nTitle 2: Accepted and published.\r\n\r\nTitle 3: Publication declined on 2021/05/11. Resubmission allowed after Major revision.\r\n-Currently reworking the paper's system model, readability, and simulations as per review comments.\r\n-To finalize and re-submit before 5th July, 2021.\r\n\r\nTitle 4: Accepted and published.\r\n\r\nTitle 5: Under review.\r\n\r\nTitle 6: Under review.\r\n\r\nTitle 7: Under review.\r\n\r\nTitle 8: Under review.\r\n\r\nTitle 9: Publication declined on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Damian's Research TITLE [9] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-06-28 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작중 (~70%)\r\n- Deep recurrent Q-learning network(DRQN)을 적용하여 Target error rate에 맞는 전력할당이 가능하게 하였음.\r\n- 관련 내용 ICTC 논문작성 진행중 \r\n- DRQN + CoMP 적용하여 Journal 제출 목표",
			"project_progress": "* BMS 개발 기술이전 관련 진행\r\n- 7월중 기술이전 예정 협의\r\n- 차주 월(7월5일) 11시에 관련 자금 집행 및 기술개발 협의",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Multicell NOMA-VLC system에 DQN 적용\r\n- DQN기반 시뮬레이터 완료 목표",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-06-28 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": "IEEE transactions on vehicular technology, \"image-based Automatic Modulation Classification (AMC)\" // 시뮬레이션 진행중\r\no KICS, \"image-based Automatic Modulation Classification (AMC)\" // 시뮬레이션 완료, 국내 논문 작성중 (70% 완료)\r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중",
			"project_progress": "o IEEE Access, \"Deep Learning-based Robust Automatic Modulation Classification for Cognitive Radio Networks\" 관련 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥) 제출완료 // 8월 중 결과발표\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표",
			"mnth_gls": "o 한화시스템 매칭펀드 서류처리 완료.\r\no IEEE transactions on vehicular technology 후속 논문관련 시뮬레이션 완료.",
			"annl_gls": "o SCIE 논문 2편 게재"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-06-28 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE TCCN).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems (IEEE Comml. Lett. - Under review).\r\n3. Conference paper for ICT2021 - in preparation.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-06-28 00:00:00",
			"to_dt": "2021-07-02 00:00:00",
			"paper_progress": "1. ICTC 논문준비 \r\n (프로토콜 변환관련 주제로 준비중)\r\n\r\n2. 국내논문 준비 \r\n  주제: IIoT 및 엣지 컴퓨팅 서베이",
			"project_progress": "1. 이노폴리스 캠프 참가 \r\n - IP캠프, 특허,디자인, 상표 출원과정 교육\r\n\r\n2. 특허출원진행중\r\n - 하드웨어제작플랫폼\r\n\r\n3. 맞충형기술파트너과제 제안서 지원 (문보트, 과제:이재민)\r\n\r\n4. 강소특구 기술자문사업 지원",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-07-03 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography . (IEEE Access).\r\n3. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n4. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)\r\n5. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (Future Generation Computer Systems)",
			"project_progress": "1. Submitted\r\n2. Submitted\r\n3. Submitted\r\n4. 80% done, and submission will be done by end of this month.\r\n5. Submission is in progress",
			"mnth_gls": "Submission of topic 4 and 5",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-07-03 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n3. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n4. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).\r\n5. Optimization of trickle-timer operation for low-power and lossy IoT devices.",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at least two.\r\nInternational conferences at least two."
		},
		{
			"user": "thienht",
			"fr_dt": "2021-07-05 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE TCCN).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems - accepted in IEEE COMML.\r\n3. Conference paper for ICT2021 - in preparation.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2021-07-05 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAS-II-10481-2021\r\n(SUBMITTED TO: IEEE Transactions on Circuits and Systems II: Express Briefs)\r\n\r\nTitle 7: applsci-1236625\r\n(SUBMITTED TO: Applied Sciences, MDPI)\r\n\r\nTitle 8: JCAS-D-21-00519\r\n(SUBMITTED TO: International Journal of Control, Automation and Systems)\r\n\r\nTitle 9: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 11: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 12: JCCI, 2021. [PUBLISHED]",
			"project_progress": "Title 1: Publication declined on 2021/06/29. Currently revising to re-submit soon.\r\n\r\nTitle 2: Accepted and published.\r\n\r\nTitle 3: Resubmitted and under review process.\r\n\r\nTitle 4: Accepted and published.\r\n\r\nTitle 5: Under review process.\r\n\r\nTitle 6: Under review process.\r\n\r\nTitle 7: Under review process.\r\n\r\nTitle 8: Under review process.\r\n\r\nTitle 9: Publication declined on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Damian's Research TITLE [9] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-07-05 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Distributed Cloud Intelligence for Industrial Internet of Things (Magazine Journal: IEEE Communications Magazine)\r\n3. Optimal Computation Offloading in Vehicle-assisted Multi-access Edge Computing (TBD)",
			"project_progress": "Work on 3",
			"mnth_gls": "",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-07-05 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": "* Multicell NOMA-VLC system에 DQN 적용 CoMP 연구\r\n- DQN custom environment 제작완료\r\n- 관련 내용 ICTC 논문작성(~70%)\r\n- DRQN + CoMP 적용하여 Journal 제출 목표",
			"project_progress": "* BMS 개발 기술이전 관련 진행\r\n- 7월중 기술이전 예정이었으나, 관련 자금 처리 행정 문제로 8월중 진행 예정으로 변경",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- ICTC 작성 및 제출\r\n- 관련 내용 바탕으로 DQN 추가하여 논문 작성(Journal용)",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-07-05 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": "1. ICTC 논문준비 (~7/30)\r\n : 주제 : SEC 사업관련 주제\r\n\r\n2. 구현논문 준비중",
			"project_progress": "1. 이노폴리스 캠프 참가\r\n- 비즈니스모델 캠프\r\n\r\n2. 특허출원진행중\r\n- 하드웨어제작플랫폼 (대기중)",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-07-05 00:00:00",
			"to_dt": "2021-07-09 00:00:00",
			"paper_progress": "o IEEE Communications letters, “image-based Automatic Modulation Classification (AMC)” 관련 시뮬레이션 진행 중 // 90% 완료\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문작성 완료, holding\r\no KICS, having been accepted, // 8월 게재 예정, 최종 버전 제출 대기중",
			"project_progress": "o IEEE Access 게재 논문 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) 제출완료, // 8월 중 결과발표\r\no 인도포닥 Dr. Shrivastava 비자관련 서류구비 완료, 차주 접수예정\r\no 한국-베트남 국제협력과제 제출완료 // 9월 중 결과발표\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o IEEE Communications Letters 투고완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-07-09 00:00:00",
			"to_dt": "2021-07-16 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography. (IEEE Access).\r\n3. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (IEEE Access )\r\n4. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n5. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning\", The 12th International Conference on Ubiquitous and Future Networks. (ICUFN).\r\n6. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Submitted\r\n2. Submitted\r\n3. Submitted\r\n4. Accepted\r\n5. Acceped\r\n6. Ongoing...........",
			"mnth_gls": "Finish with topic 6\r\nICC idea preparation",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-07-09 00:00:00",
			"to_dt": "2021-07-16 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n4. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n5. Optimization of trickle-timer operation for low-power and lossy IoT devices.",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at least two.\r\nInternational conferences at least two."
		},
		{
			"user": "william",
			"fr_dt": "2021-07-12 00:00:00",
			"to_dt": "2021-07-16 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\n\r\nTitle 1: BTS-21-036\r\n(SUBMITTED TO: IEEE Trans. on Broadcasting)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAS-II-10481-2021\r\n(SUBMITTED TO: IEEE Transactions on Circuits and Systems II: Express Briefs)\r\n\r\nTitle 7: Access-2021-24847\r\n(IEEE Access)\r\n\r\nTitle 8: JCAS-D-21-00519\r\n(SUBMITTED TO: International Journal of Control, Automation and Systems)\r\n\r\nTitle 9: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 11: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 12: JCCI, 2021. [PUBLISHED]",
			"project_progress": "Title 1: Publication declined on 2021/06/29. Currently revising to re-submit soon.\r\n\r\nTitle 2: Accepted and published.\r\n\r\nTitle 3: Under review process.\r\n\r\nTitle 4: Accepted and published.\r\n\r\nTitle 5: Under review process.\r\n\r\nTitle 6: Under review process.\r\n\r\nTitle 7: Under review process.\r\n\r\nTitle 8: Under review process.\r\n\r\nTitle 9: Publication declined on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Damian's Research TITLE [9] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-07-12 00:00:00",
			"to_dt": "2021-07-16 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Optimal Computation Offloading in Vehicle-assisted Multi-access Edge Computing (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Work on 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-07-12 00:00:00",
			"to_dt": "2021-07-16 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 기존 CoMP-VLC-NOMA에서 VLC-NOMA 전력할당으로 변경\r\n- 시뮬레이션 수정중(60%)\r\n\r\n* 관련 내용 ICTC 논문작성 및 제출(100%)\r\n- 내용 : Downlink VLC-NOMA BER 성능평가",
			"project_progress": "* BMS 개발 기술이전 관련 진행\r\n- 7월중 기술이전 예정이었으나, 관련 자금 처리 행정 문제로 8월중 진행 예정으로 변경",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- ICTC 작성 및 제출(완료)\r\n- 관련 내용 바탕으로 DQN 추가하여 논문 작성(시뮬레이션 수정중)",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-07-12 00:00:00",
			"to_dt": "2021-07-16 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “image-based Automatic Modulation Classification (AMC)” // 논문 작성중\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중\r\no KICS, 논문게재 대기중, // 8월 게재 예정, 최종 버전 제출 대기중",
			"project_progress": "o IEEE Access 게재 논문 //특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) 제출완료, // 8월 중 결과발표\r\no 인도포닥 Dr. Shrivastava 비자관련 서류구비 완료, 차주 접수예정\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o IEEE Wireless Communications Letters 투고완료",
			"annl_gls": "SCI급 논문 2편 게재"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-07-16 00:00:00",
			"to_dt": "2021-07-23 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography. (IEEE Access).\r\n3. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (IEEE Access )\r\n4. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n5. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning\", The 12th International Conference on Ubiquitous and Future Networks. (ICUFN).\r\n6. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Under review\r\n2. Under review\r\n3. Under review\r\n4. Accepted and final submission completed\r\n5. Accepted and final submission completed\r\n6. Ongoing...........",
			"mnth_gls": "Finish with topic 6\r\nICC idea preparation",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-07-19 00:00:00",
			"to_dt": "2021-07-23 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Optimal Computation Offloading in Vehicle-assisted Multi-access Edge Computing (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Work on 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-07-19 00:00:00",
			"to_dt": "2021-07-23 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “image-based Automatic Modulation Classification (AMC)” 논문 작성 중 // 80% 작성완료\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중\r\no KICS, 논문게재 대기중, // 8월 게재 예정, 최종 버전 제출 대기중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 해외 특허출원 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) 제출완료, // 8월 중 결과발표\r\no 인도포닥 Dr. Shrivastava // 비자신청 완료\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o IEEE Wireless Communications Letters 투고완료.",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "william",
			"fr_dt": "2021-07-19 00:00:00",
			"to_dt": "2021-07-23 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270\r\n(SUBMITTED TO: IET Communications)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAD-2021-0394\r\n(SUBMITTED TO: IEEE Trans. on CAD)\r\n\r\nTitle 7: Access-2021-24847\r\n(IEEE Access)\r\n\r\nTitle 8: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 9: ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 10: JCCI, 2021. [PUBLISHED]",
			"project_progress": "Title 1: Under review process.\r\n\r\nTitle 2: Accepted and published.\r\n\r\nTitle 3: Under review process.\r\n\r\nTitle 4: Accepted and published.\r\n\r\nTitle 5: Under review process.\r\n\r\nTitle 6: Under review process.\r\n\r\nTitle 7: Under review process.\r\n\r\nTitle 8: Publication declined on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Damian's Research TITLE [8] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2021-07-19 00:00:00",
			"to_dt": "2021-07-23 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE TCCN).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems.\r\n3. Conference paper for ICT2021 - in preparation.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-07-19 00:00:00",
			"to_dt": "2021-07-23 00:00:00",
			"paper_progress": "1. ICTC 논문준비 - 작성중 (~7/29)\r\n  - 제목 : Design and Implementation of Smart Energy Platform for Industrial Complex",
			"project_progress": "etc.\t\r\n1. 이노폴리스 캠프 참가\r\n - 우수창업자 경진대회 사업화 과제 공모\r\n\r\n2. 특허출원진행중\r\n- 하드웨어제작플랫폼  초안검토\r\n\r\n3. 맞충형기술파트너과제 제안서 지원 (문보트, 과제:이재민) -> 대기중",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-07-19 00:00:00",
			"to_dt": "2021-07-23 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 시뮬레이션 수정중(80%)",
			"project_progress": "",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- ICTC 작성 및 제출(완료)\r\n- 관련 내용 바탕으로 DNN 추가하여 논문 작성",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-07-26 00:00:00",
			"to_dt": "2021-07-30 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Optimal Computation Offloading in Vehicle-assisted Multi-access Edge Computing (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Work on 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-07-26 00:00:00",
			"to_dt": "2021-07-30 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 시뮬레이션 수정 완료\r\n- 논문 작성 시작",
			"project_progress": "* KICS 국내 논문 게재\r\n* 하계휴가 (2021.07.28~30)",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- ICTC 작성 및 제출(완료)\r\n- 관련 내용 바탕으로 DNN 추가하여 논문 작성",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-07-26 00:00:00",
			"to_dt": "2021-07-30 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n4. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n5. Optimization of trickle-timer operation for low-power and lossy IoT devices.",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at least two.\r\nInternational conferences at least two."
		},
		{
			"user": "william",
			"fr_dt": "2021-07-26 00:00:00",
			"to_dt": "2021-07-30 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270\r\n(SUBMITTED TO: IET Communications)\r\n\r\nTitle 2: https://ieeexplore.ieee.org/document/9360448?source=authoralert\r\n(PUBLISHED ON: IEEE Sensors Letters Journal).\r\n\r\nTitle 3: Sensors-38710-2021\r\n(SUBMITTED TO: IEEE Sensor Journal)\r\n\r\nTitle 4: https://www.sciencedirect.com/science/article/pii/S0140366421000700\r\n(PUBLISHED ON: Elsevier Computer Communications Journal)\r\n\r\nTitle 5: TCE-2021-05-0123\r\n(SUBMITTED TO: IEEE Trans. on Consumer Electronics)\r\n\r\nTitle 6: TCAD-2021-0394\r\n(SUBMITTED TO: IEEE Trans. on CAD)\r\n\r\nTitle 7: Access-2021-24847\r\n(SUBMITTED TO: IEEE Access)\r\n\r\nTitle 8: Access-2021-10959\r\n(SUBMITTED TO: IEEE ACCESS)\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\n\r\nTitle 9: IEEE-ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 10: JCCI, 2021. [PUBLISHED]\r\nTitle 11: IEEE-ICTC International Conference 2021. [SUBMITTED]",
			"project_progress": "Title 1: Under review process.\r\n\r\nTitle 2: Accepted and published.\r\n\r\nTitle 3: Under review process.\r\n\r\nTitle 4: Accepted and published.\r\n\r\nTitle 5: Under review process.\r\n\r\nTitle 6: Under review process.\r\n\r\nTitle 7: Under review process.\r\n\r\nTitle 8: Publication declined on 2020/05/05. Resubmission allowed after Minor revision.\r\n\r\nTitle 11: Submitted on 7/30/2021. Under review.\r\n\r\nCOLLABORATIONS WITH Prof. DS Kim:\r\n[1]. Paper survey works in progress.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.\r\n\r\nMENTORSHIP/RESEARCH SUPERVISION\r\n[1]. Mr. Damian's Research TITLE [8] above.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two/three SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00503",
			"fr_dt": "2021-07-26 00:00:00",
			"to_dt": "2021-07-30 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography. (IEEE Access).\r\n3. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (IEEE Access )\r\n4. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n5. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning\", The 12th International Conference on Ubiquitous and Future Networks. (ICUFN).\r\n6. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Under review\r\n2. Revision in progress\r\n3. Under review\r\n4. Accepted and final submission completed\r\n5. Accepted and final submission completed\r\n6. Ongoing...........",
			"mnth_gls": "Finish with topic 6",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-07-31 00:00:00",
			"to_dt": "2021-08-06 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 교정 및 투고완료\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중\r\no KICS, 논문게재 대기중, // 8월 게재 예정, 최종 버전 제출 대기중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) 제출완료, // 8월 중 결과발표\r\no 인도포닥 Dr. Shrivastava // 비자발급 완료\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-08-01 00:00:00",
			"to_dt": "2021-08-07 00:00:00",
			"paper_progress": "Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal- Physical Communication- Submitted\r\n\r\n2. Fedrate learning based resource allocation for URLLC in V2V: Target Journal- IEEE Transactions on Vehicular Technology\r\n-in revision\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\n\r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communicatiion-Submitted",
			"project_progress": "",
			"mnth_gls": "Complete the paper in revesion",
			"annl_gls": "Submit two SCI papers"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-08-02 00:00:00",
			"to_dt": "2021-08-06 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Optimal Computation Offloading in Vehicle-assisted Multi-access Edge Computing (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Work on 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-08-02 00:00:00",
			"to_dt": "2021-08-06 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문 작성 중(20%)",
			"project_progress": "* 국방규격실 관련 자료 번역(번역후 Arslan 전달)\r\n* Saviour 논문 관련 특허자료 번역\r\n* 강소개발특구 이노폴리스 창업 사업계획서 작성 및 제출",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- ICTC 작성 및 제출(완료)\r\n- 관련 내용 바탕으로 DNN 추가하여 논문 작성 중",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-08-02 00:00:00",
			"to_dt": "2021-08-06 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography. (IEEE Access).\r\n3. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (IEEE Access )\r\n4. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n5. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning\", The 12th International Conference on Ubiquitous and Future Networks. (ICUFN).\r\n6. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Under review\r\n2. Revision completed and submitted\r\n3. Under review\r\n4. Accepted and final submission completed\r\n5. Accepted and final submission completed\r\n6. Ongoing...........",
			"mnth_gls": "Finish with topic 6",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-08-02 00:00:00",
			"to_dt": "2021-08-06 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n4. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n5. Optimization of trickle-timer operation for low-power and lossy IoT devices.",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": "SCI Publication at least two.\r\nInternational conferences at least two."
		},
		{
			"user": "thienht",
			"fr_dt": "2021-08-02 00:00:00",
			"to_dt": "2021-08-06 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE TCCN).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems.\r\n3. Conference paper for ICT2021 - in preparation.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "disciple",
			"fr_dt": "2021-08-02 00:00:00",
			"to_dt": "2021-08-06 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 교정 및 투고완료\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중\r\no KICS, 논문게재 대기중, // 8월 게재 예정, 차주 게재료 납부 처리 예정",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) 제출완료, // 8월 중 결과발표\r\no 인도포닥 Dr. Shrivastava // 비자신청 완료\r\no 포닥 pool 서베이 중\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 센터 Grand ICT 보고서 작업 지원\r\no 사업화 아이템 회의 참석 및 지원",
			"mnth_gls": "o RUL 관련 시뮬레이션 진행 (50%)",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-08-02 00:00:00",
			"to_dt": "2021-08-13 00:00:00",
			"paper_progress": "1. ICTC 2021 논문 제출 완료\r\n   (Design and Implementation of Smart Energy Platform for Industrial Complex\"\r\n\r\n2. 엣지 컴퓨팅 인공지능 성능분석 논문 준비중\r\n\r\n3. SEC 관련 저널 논문 준비",
			"project_progress": "1. 하드웨어 제작 플랫폼 특허 출원 완료\r\n\r\n2. 강소특구 사업\r\n  - 이노폴리스 사업 교육종료\r\n  - ALLSET 패키지 지원",
			"mnth_gls": "특허 1건 출원\r\nSW 1건 등록",
			"annl_gls": "SCI 저널 논문 투고 \r\n특허 등록"
		},
		{
			"user": "william",
			"fr_dt": "2021-08-09 00:00:00",
			"to_dt": "2021-08-13 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\nTitle 1: \r\nCOM-2021-07-0270 [SUBMITTED TO: IET Communications]\r\n\r\nTitle 2: \r\n[PUBLISHED ON: IEEE Sensors Letters Journal].\r\n\r\nTitle 3: \r\nSensors-38710-2021. [SUBMITTED TO: IEEE Sensor Journal]\r\n\r\nTitle 4: \r\n[PUBLISHED ON: Elsevier Computer Communications Journal]\r\n\r\nTitle 5: \r\nTCE-2021-05-0123. [SUBMITTED TO: IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 6: \r\nTCAD-2021-0394. [SUBMITTED TO: IEEE Trans. on CAD]\r\n\r\nTitle 7: \r\nAccess-2021-24847. [SUBMITTED TO: IEEE Access]\r\n\r\nTitle 8: \r\nAccess-2021-10959. [SUBMITTED TO: IEEE ACCESS]\r\n\r\nTitle 9: \r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\nTitle 10: IEEE-ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 11: JCCI, 2021. [PUBLISHED]\r\nTitle 12: IEEE-ICTC International Conference 2021. [SUBMITTED]\r\nTitle 13: IEEE-ICC, 2022 [ON-GOING]",
			"project_progress": "Title [1], [3], [5], [6], and [11]: Under review process.\r\n\r\nTitle [2] & [4]: Accepted and published.\r\n\r\nTitle [7]: Publication declined on 2020/08/06. \r\n- Resubmission allowed after Minor revision.\r\n- Re-working the paper based on the comments received.\r\n- To re-submit soon.\r\n\r\nTitle [8]: MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined on 2020/05/05. \r\n- Resubmission allowed after Minor revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [9] & [13]:\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n- To submit by end of October 2021.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-08-09 00:00:00",
			"to_dt": "2021-08-13 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Optimal Computation Offloading in Vehicle-assisted Multi-access Edge Computing (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Update 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-08-09 00:00:00",
			"to_dt": "2021-08-13 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 심사 중\r\no Remain Useful Maintenance (RUL) // 시뮬레이션 진행중\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중\r\no KICS, 논문게재 대기중 // 8월 게재",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) 제출완료, // 8월 중 결과발표\r\no 인도포닥 Dr. Shrivastava // 비자신청 완료\r\no 한국-베트남 국제협력과제 작성 진행중, 제출완료 // 9월 중 결과발표\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 시뮬레이션 진행 (50%)",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-08-09 00:00:00",
			"to_dt": "2021-08-13 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문 작성 중(20%)\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 시뮬레이션 (30%)",
			"project_progress": "* 강소개발특구 이노폴리스 창업 사업계획서 발표",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- ICTC 작성 및 제출(완료)\r\n- 관련 내용 바탕으로 DNN 추가하여 논문 작성 중\r\n\r\n* Downlink NOMA DNN 활용 전력할당\r\n- 시뮬레이션 작성중",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-08-12 00:00:00",
			"to_dt": "2021-08-13 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography. (IEEE Access).\r\n3. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (IEEE Access )\r\n4. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n5. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning\", The 12th International Conference on Ubiquitous and Future Networks. (ICUFN).\r\n6. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Under review\r\n2. Submitted after revision\r\n3. Under review\r\n4. Preparing the ppt for ICUFN\r\n5. Accepted and final submission completed\r\n6. Ongoing...........",
			"mnth_gls": "Finish with topic 6",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "william",
			"fr_dt": "2021-08-16 00:00:00",
			"to_dt": "2021-08-20 00:00:00",
			"paper_progress": ">>>JOURNAL LIST<<<\r\nTitle 1:\r\nCOM-2021-07-0270 [SUBMITTED TO: IET Communications]\r\n\r\nTitle 2:\r\n[PUBLISHED ON: IEEE Sensors Letters Journal].\r\n\r\nTitle 3:\r\nSensors-38710-2021. [SUBMITTED TO: IEEE Sensor Journal]\r\n\r\nTitle 4:\r\n[PUBLISHED ON: Elsevier Computer Communications Journal]\r\n\r\nTitle 5:\r\nTCE-2021-05-0123. [SUBMITTED TO: IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 6:\r\nTCAD-2021-0394. [SUBMITTED TO: IEEE Trans. on CAD]\r\n\r\nTitle 7:\r\nAccess-2021-24847. [SUBMITTED TO: IEEE Access]\r\n\r\nTitle 8:\r\nAccess-2021-10959. [SUBMITTED TO: IEEE ACCESS]\r\n\r\nTitle 9:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n>>>CONFERENCE LIST<<<\r\nTitle 10: IEEE-ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 11: JCCI, 2021. [PUBLISHED]\r\nTitle 12: IEEE-ICTC International Conference 2021. [SUBMITTED]\r\nTitle 13: IEEE-ICC, 2022 [ON-GOING]",
			"project_progress": "Title [1], [3], [5], [6], and [11]: Under review process.\r\n\r\nTitle [2] & [4]: Accepted and published.\r\n\r\nTitle [7]: Publication declined on 2020/08/06.\r\n- Resubmission allowed after Minor revision.\r\n- Re-working the paper based on the comments received.\r\n- To re-submit by 26th Aug.\r\n\r\nTitle [8]: MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined on 2020/05/05.\r\n- Resubmission allowed after Minor revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [9] & [13]:\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n- To submit by end of October 2021.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-08-16 00:00:00",
			"to_dt": "2021-08-20 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Update 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-08-16 00:00:00",
			"to_dt": "2021-08-20 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 심사 중\r\no Remain Useful Maintenance (RUL) 아이디어 구상 및 시뮬레이션 진행\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 8월 중 결과발표\r\no 인도포닥 Dr. Shrivastava // 비자전달 완료\r\no Gabriel // 비자신청 진행중\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-08-16 00:00:00",
			"to_dt": "2021-08-20 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Multimedia).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography. (IEEE Access).\r\n3. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (IEEE Access )\r\n4. e-Health and Resource Management Scheme for a Deep Learning-based Detection of Tumor in Wireless Capsule Endoscopy Videos (ICUFN).\r\n5. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning\", The 12th International Conference on Ubiquitous and Future Networks. (ICUFN).\r\n6. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)\r\n7. Introducing 5G+ (28GHz) mmWave Campus Test-bed",
			"project_progress": "1. Under review\r\n2. Submitted after revision\r\n3. Under review\r\n4. ICUFN presentation done\r\n5. ICUFN presentation done\r\n6. Ongoing...........\r\n7. Submitted to ICTC",
			"mnth_gls": "Finish with topic 6",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-08-16 00:00:00",
			"to_dt": "2021-08-20 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE TCCN).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems.\r\n3. Densely-Accumulated Convolutional Network for Accurate LPI Radar Waveform Recognition - accepted in GLOBECOM 2021.\r\n3. Conference papers for ICT2021.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-08-16 00:00:00",
			"to_dt": "2021-08-20 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문 작성 중(20%)\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 시뮬레이션 (30%)\r\n- NOMA에서 near-user SIC시에 Residual error 관련 공식 유도중",
			"project_progress": "* 고속 ADC 특허 번역\r\n* 강소개발특구 이노폴리스 창업 지원 선정",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- ICTC 작성 및 제출(완료)\r\n- 관련 내용 바탕으로 DNN 추가하여 논문 작성 중\r\n\r\n* Downlink NOMA DNN 활용 전력할당\r\n- 시뮬레이션 작성중",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-08-16 00:00:00",
			"to_dt": "2021-08-20 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n4. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n5. Optimization of trickle-timer operation for low-power and lossy IoT devices.\r\n6. Introducing 5G+ (28GHz) mmWave Campus Test-bed\r\n7. Overview of ICT Convergence Specialized Research Center in South Korea",
			"project_progress": "",
			"mnth_gls": "Finish with topic 1",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-08-20 00:00:00",
			"to_dt": "2021-08-26 00:00:00",
			"paper_progress": "1. 엣지 컴퓨팅관련 논문 준비중(하드웨어 vs 소프트웨어)",
			"project_progress": "1. 이노폴리스 캠프 특화교육 신청 \r\n2. 센터 사업화 ITEM 회의",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-08-23 00:00:00",
			"to_dt": "2021-08-27 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Update 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-08-23 00:00:00",
			"to_dt": "2021-08-27 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Image Processing).\r\n2. Comparison of SARA Versus RW-TV for Compressive Sensing of computed tomography. (IEEE Access).\r\n3. Reinforcement Learning Based Resource Allocation in Fog Computing Environment: Literature Review, Challenges, and Open Issues. (IEEE Journal of Communications and Networks)\r\n4. Introducing 5G+ (28GHz) mmWave Campus Test-bed (ICTC 2021)\r\n5. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Some editing going on. (Will be submitted soon)\r\n2. Accepted\r\n3. Submitted\r\n4. Submitted\r\n5. On going",
			"mnth_gls": "1. Submission of 1\r\n2. Finish with 5",
			"annl_gls": "2 SCIE"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-08-23 00:00:00",
			"to_dt": "2021-08-27 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n4. Enhancing IEEE 802.15.4 Access Mechanism with Machine Learning (ICUFN).\r\n5. Optimization of trickle-timer operation for low-power and lossy IoT devices.\r\n6. Introducing 5G+ (28GHz) mmWave Campus Test-bed\r\n7. Overview of ICT Convergence Specialized Research Center in South Korea",
			"project_progress": "",
			"mnth_gls": "Finish with topic 1",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-08-23 00:00:00",
			"to_dt": "2021-08-27 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 리비젼 진행\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 // 시뮬레이션 진행\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 8월 31일 재접수 예정\r\no 인도포닥 Dr. Shrivastava // 비자신청 완료, 입국 시기 조율 중\r\no Gabriel 연구원 채용 // 비자신청 완료\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 시뮬레이션 진행 (50%)\r\no 9월 중 IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "william",
			"fr_dt": "2021-08-23 00:00:00",
			"to_dt": "2021-08-27 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2020 - Aug. 2021]<<<\r\nTitle 1:\r\nCOM-2021-07-0270 [SUBMITTED TO: IET Communications]\r\n\r\nTitle 2:\r\n[PUBLISHED ON: IEEE Sensors Letters Journal].\r\n\r\nTitle 3:\r\nSensors-38710-2021. [SUBMITTED TO: IEEE Sensor Journal]\r\n\r\nTitle 4:\r\n[PUBLISHED ON: Elsevier Computer Communications Journal]\r\n\r\nTitle 5:\r\nTCE-2021-05-0123. [SUBMITTED TO: IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 6:\r\nTCAD-2021-0394. [SUBMITTED TO: IEEE Trans. on CAD]\r\n\r\nTitle 7:\r\nAccess-2021-24847. [SUBMITTED TO: IEEE Access]\r\n\r\nTitle 8:\r\nAccess-2021-10959. [SUBMITTED TO: IEEE ACCESS]\r\n\r\nTitle 9:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2020 - Aug. 2021]<<<\r\nTitle 10: IEEE-ICAIIC International Conference, 2021. [PUBLISHED]\r\nTitle 11: JCCI, 2021. [PUBLISHED]\r\nTitle 12: IEEE-ICTC International Conference 2021. [SUBMITTED]\r\nTitle 13: IEEE-ICC, 2022 [ON-GOING]",
			"project_progress": "Title [1], [3], [5], [6], and [11]: Under review process.\r\n\r\nTitle [2] & [4]: Accepted and published.\r\n\r\nTitle [7]: Under review process\r\n- Resubmission was completed.\r\n\r\nTitle [8]: MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined on 2020/05/05.\r\n- Resubmission allowed after Minor revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [9] & [13]:\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n- To submit by end of October 2021.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-08-23 00:00:00",
			"to_dt": "2021-08-27 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문 작성 중(20%)\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 시뮬레이션 (60%)\r\n- NOMA에서 near-user SIC시에 Residual error 관련 공식 유도 완료",
			"project_progress": "",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- DNN 기반 전력 할당 알고리즘 시뮬레이션 완료\r\n\r\n* Downlink NOMA DNN 활용 전력할당\r\n- 시뮬레이션 완료",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-08-23 00:00:00",
			"to_dt": "2021-08-27 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE TCCN).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems.\r\n3. Densely-Accumulated Convolutional Network for Accurate LPI Radar Waveform Recognition - accepted in GLOBECOM 2021.\r\n3. Conference papers for ICT2021.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-08-27 00:00:00",
			"to_dt": "2021-09-02 00:00:00",
			"paper_progress": "1. \"Physical Internet in the Era of Digital Transformation: Perspectives and Open Issues\", IEEE Access (Under Review)\r\n2. \"On reliability of IIoT systems from systematic perspectives\", IETE Technical Review (Resubmission and Under Review)\r\n3. \"Shaping the Future of logistics: Data-driven Technology and Strategic Management\", IETE Technical Review (Under Review)\r\n4. \" Reinforcement learning based resource allocation in fog computing: Perspective and Challenges\", Journal of Communication and Networks (Under Review)\r\n5. \" Performance Analysis of Fog computing systems with Parallel computation\", IOT Journal ( In progress)",
			"project_progress": "Summer Vacation Plan: 30-31 August, 2021 (02 days)",
			"mnth_gls": "- 01 SCI accepted\r\n-Paper 5: finished and submit",
			"annl_gls": "03-04 SCI accepted"
		},
		{
			"user": "sanjay",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "Dragonfly Interaction Algorithm for Optimization of the Queuing Delay in Industrial Wireless Networks: Target Journal- Physical Communication- Submitted\r\n\r\n2. Federate learning based resource allocation for URLLC in V2V: Target Journal- IEEE Transactions on Vehicular Technology\r\n-in revision\r\n\r\n3. Survey paper with Dr. Hoa and team. \r\n\r\n\r\n\r\n4. CR-NOMA based cooperative V2X Communication\r\nTarget Journal-Vehicle Communication-Submitted",
			"project_progress": "",
			"mnth_gls": "Complete the paper in revision",
			"annl_gls": "Submit two SCI papers"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문 작성 중(20%)\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 시뮬레이션 (100%)",
			"project_progress": "* 프로그램 등록 신청\r\n* BMS 기술이전계약 완료",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- ICT express, under review\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- DNN 기반 전력 할당 알고리즘 시뮬레이션 완료\r\n\r\n* Downlink NOMA DNN 활용 전력할당\r\n- 시뮬레이션 완료",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "william",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n           >>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 8: IEEE-ICTC International Conference 2021. [SUBMITTED]\r\nTitle 9: IEEE-ICC, 2022 [ON-GOING]",
			"project_progress": "Title [1]-[5], and [8]: Under review process.\r\n\r\nTitle [6]: MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined on 2021/05/05.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [7] & [9]:\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n- To submit by end of October 2021.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00503",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Image Processing).\r\n2. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Updated\r\n2. Updated",
			"mnth_gls": "Submit both papers",
			"annl_gls": "2 SCIE"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Reinforcement Learning-based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issue (Survey with Dr. Hao and Team).\r\n3. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n4. Optimization of trickle-timer operation for low-power and lossy IoT devices.\r\n5. Introducing 5G+ (28GHz) mmWave Campus Test-bed\r\n6. Overview of ICT Convergence Specialized Research Center in South Korea",
			"project_progress": "",
			"mnth_gls": "Finish with topic 1",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "1. Learning Deep Convolutional Network for Automatic Modulation Classification in OFDM Systems Under Channel Impairments (IEEE TCCN).\r\n2. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems.\r\n3. Densely-Accumulated Convolutional Network for Accurate LPI Radar Waveform Recognition - accepted in GLOBECOM 2021.\r\n3. Conference papers for ICT2021.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "disciple",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 리비젼 진행 중\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 및 시뮬레이션 진행\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문작성 완료, Holding 중\r\no KICS, 인공지능학술대회 2021 // 논문제출 완료",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 재출 완료, 10월 발표\r\no 인도포닥 Dr. Shrivastava // 9 - 12월 중 입국 예정\r\no Gabriel 연구원 채용 // 완료, 행정 지원\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)\r\no IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 9월 중 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Update 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-08-30 00:00:00",
			"to_dt": "2021-09-03 00:00:00",
			"paper_progress": "1. 엣지 컴퓨팅관련 논문 준비중(하드웨어 vs 소프트웨어)",
			"project_progress": "1. 이노폴리스 캠프 특화교육 신청 \r\n2. 센터 사업화 ITEM 회의\r\n3. 계약학과 강의준비",
			"mnth_gls": "1. 특허 1\r\n2. SW등록 1\r\n3. 논문진행",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 1\r\n-소프트웨어 등록 4"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-10 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문 작성 중(20%)\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- System model 부분 논문작성중\r\n\r\n* Cooperative Retransmission NOMA\r\n- Rejected (ICT express)\r\n- 수정계획 : Resource block 할당 시뮬레이션 추가",
			"project_progress": "* 프로그램 등록 1건 완료",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- 수정후 MDPI Sensors 저널 투고 계획\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- System model 및 Evaluation 부분 작성\r\n\r\n* Downlink NOMA DNN 활용 전력할당\r\n- System model 및 Evaluation 부분 작성",
			"annl_gls": "* SCIE 논문 2편 목표"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-10 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Image Processing).\r\n2. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)",
			"project_progress": "1. Submitted\r\n2. Updated",
			"mnth_gls": "Submission of 2.",
			"annl_gls": "2 SCI/SCIE."
		},
		{
			"user": "william",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-10 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 8: IEEE-ICTC International Conference 2021. [SUBMITTED]\r\nTitle 9: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 10:IEEE-WFCS, 2022 [ON-GOING]",
			"project_progress": "Title [1]-[5], and [8]: Under review process.\r\n\r\nTitle [6]: MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined on 2021/05/05.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [7], [9] & [10]:\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00502",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-10 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n3. Optimization of trickle-timer operation for low-power and lossy IoT devices.\r\n4. Overview of ICT Convergence Specialized Research Center in South Korea",
			"project_progress": "",
			"mnth_gls": "Finish with topic 1",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-10 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 리비젼 진행 중 (50%)\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 및 시뮬레이션 진행\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 접수 완료, 10월 중 결과 발표\r\no 인도포닥 Dr. Shrivastava // 9 &#8211; 12월 중 입국 예정, 입국 전까지 국제협력 진행\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no Ardey // 요청사항 지원\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)\r\no IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 9월 중 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-10 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 리비젼 진행 중 (50%)\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 및 시뮬레이션 진행\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 접수 완료, 10월 중 결과 발표\r\no 인도포닥 Dr. Shrivastava // 9 &#8211; 12월 중 입국 예정, 입국 전까지 국제협력 진행\r\no Gabriel 연구원 채용 // 채용완료, 행정지원\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no Ardey // 요청사항 지원\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)\r\no IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 9월 중 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-10 00:00:00",
			"paper_progress": "1. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)\r\n2. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Communications Letters)",
			"project_progress": "1. Update 1\r\n2. Update 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-17 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 리비젼 진행 중 (60%)\r\no Remain Useful Maintenance (RUL) 홀딩 중\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, 홀딩 중\r\no KICS, 인공지능학술대회 2021 // 논문 사전등록",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 접수 완료, 10월 중 결과 발표\r\no 인도포닥 Dr. Shrivastava // 9 &#8211; 12월 중 입국 예정, 입국 전까지 국제협력 진행\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no Ardey // 요청사항 지원\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)\r\no IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 9월 중 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-09-06 00:00:00",
			"to_dt": "2021-09-17 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 리비젼 진행 중 (60%)\r\no Remain Useful Maintenance (RUL) 홀딩 중\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, 홀딩 중\r\no KICS, 인공지능학술대회 2021 // 논문 사전등록",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 접수 완료, 10월 중 결과 발표\r\no 인도포닥 Dr. Shrivastava // 9 &#8211; 12월 중 입국 예정, 입국 전까지 국제협력 진행\r\no Gabriel 연구원 채용 // 채용완료, 행정지원\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no Ardey // 요청사항 지원\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)\r\no IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 9월 중 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-09-13 00:00:00",
			"to_dt": "2021-09-17 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문작성중 20%(Pending) -> Quality 보완 필요\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- System model 부분 논문작성중(Pending) -> Quality 보완 필요\r\n\r\n* Cooperative Retransmission NOMA\r\n- 수정중 : Resource block 할당 시뮬레이션 추가 완료",
			"project_progress": "* 특허(SNS 통합플랫폼) 작성\r\n* 강소특구 이노폴리스 창업 지원 관련 선정\r\n- 사업비 1900만원\r\n- 산학협력관 8층 공유오피스 계약완료(특구내 사업장을 내야 사업비 지원가능)\r\n- 사업자등록 신청",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- 수정후 MDPI Sensors(Q1, 게재가시 창의도전과제로 게재비 예정) 저널 투고 계획\r\n\r\n* Downlink VLC-NOMA 관련 BER 성능평가 논문\r\n- System model 및 Evaluation 부분 작성\r\n\r\n* Downlink NOMA DNN 활용 전력할당\r\n- System model 및 Evaluation 부분 작성",
			"annl_gls": "* SCIE 논문 1편 목표(2편에서 하향)"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-09-13 00:00:00",
			"to_dt": "2021-09-17 00:00:00",
			"paper_progress": "1. Comparing H.265/HEVC and VP9: Impact of High Frame Rates on the Perceptual\r\nQuality of Compressed Videos. (IEEE Transaction on Image Processing).\r\n2. 5G+ (28GHz) mmWave Campus Test-bed; Challenges and Opportunities. (IEEE Transaction on Education)\r\n3. Compressed Medical Imaging using spread Spectrum Acquisition and PDE-Based Sparsity Averagingfor Iris Images. (IEEE Access)",
			"project_progress": "(1) Submitted\r\n(2) English correction stage for final submission.\r\n(3) Submission due next week.",
			"mnth_gls": "submission of both 2 and 3.",
			"annl_gls": "3 SCI/SCIE journals\r\nSome international applications"
		},
		{
			"user": "william",
			"fr_dt": "2021-09-13 00:00:00",
			"to_dt": "2021-09-17 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 8: IEEE-ICTC International Conference 2021. [SUBMITTED]\r\nTitle 9: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 10:IEEE-WFCS, 2022 [ON-GOING]",
			"project_progress": "Title [1]-[5], and [8]: Under review process.\r\n\r\nTitle [6]: MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [7], [9] & [10]:\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-09-13 00:00:00",
			"to_dt": "2021-09-17 00:00:00",
			"paper_progress": "1. 엣지 컴퓨팅관련 논문 준비중(하드웨어 vs 소프트웨어) - 보류\r\n  \r\n2. ICTC 발표준비 (스마트에너지관련 논문)",
			"project_progress": "1. 이노폴리스 캠프 특화교육 수강\r\n2. 센터 사업화 ITEM 회의\r\n3. 맞춤형 기술파트너지원사업(문보트, 발표대기)\r\n4. 특허아이디어 (매타버스 크로스 플랫폼 특허검토 -> 거절건 1건)",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-09-23 00:00:00",
			"to_dt": "2021-09-24 00:00:00",
			"paper_progress": "1. Compressed Medical Imaging using Spread Spectrum Acquisition and BPDN-Based Sparsity Averaging for Iris Images. \r\n2. Introducing 5G+ (28GHz) mmWave Campus Test-bed",
			"project_progress": "1. Submitted\r\n2. Accepted",
			"mnth_gls": "1 Transactions submission",
			"annl_gls": "2 SCI/SCIE"
		},
		{
			"user": "william",
			"fr_dt": "2021-09-23 00:00:00",
			"to_dt": "2021-09-24 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 8: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 9: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 10:IEEE-WFCS, 2022 [ON-GOING]",
			"project_progress": "Titles [1] - [5]: UNDER REVIEW PROCESS.\r\n\r\nTitle [6]: MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [8]: IEEE-ICTC, Jeju\r\n- Publication Accepted.\r\n- Final manuscript in progress.\r\n- Conference registration and payments in progress.\r\n\r\nTitle [7] and [9]:\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n\r\nCOLLABORATIONS WITH DR. HOA:\r\n[1]. Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00502",
			"fr_dt": "2021-09-23 00:00:00",
			"to_dt": "2021-09-24 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n3. Overview of ICT Convergence Specialized Research Center in South Korea",
			"project_progress": "",
			"mnth_gls": "Finish with topic 1",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-09-27 00:00:00",
			"to_dt": "2021-10-01 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)",
			"project_progress": "Finish 1",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-09-27 00:00:00",
			"to_dt": "2021-10-01 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문작성중 20%(Pending) -> Quality 보완 필요\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- System model 부분 논문작성중(Pending) -> Quality 보완 필요\r\n\r\n* Cooperative Retransmission NOMA\r\n- 수정 : Resource block 할당 시뮬레이션 추가 완료\r\n- MDPI sensors 제출 완료",
			"project_progress": "* Grand ICT 보고서 작성\r\n* 특허(SNS 통합플랫폼) 제출\r\n* 강소특구 이노폴리스 창업 지원 관련 선정\r\n- 사업자 등록 완료\r\n- 차주 협약진행",
			"mnth_gls": "* Cooperative Retransmission scheme in NOMA\r\n- 수정후 MDPI Sensors(Q1, 게재가시 창의도전과제로 게재비 예정) 저널 투고 완료",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화"
		},
		{
			"user": "william",
			"fr_dt": "2021-09-27 00:00:00",
			"to_dt": "2021-10-01 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal] [ACCEPTED]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access] [ACCEPTED]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 8: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 9: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 10:IEEE-WCNC, 2022 [SUBMITTED]",
			"project_progress": "Titles [1] & [2]: - ACCEPTED. \r\n                  - Final manuscript submitted.\r\n                  - Publications in-progress.\r\n\r\n\r\nTitles [3], [4] & [5]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [6]: - MENTORSHIP/RESEARCH SUPERVISION\r\n           - Publication declined.\r\n           - Resubmission allowed after Major revision.\r\n           - Reworking the paper with Mr. Damian.\r\n\r\nTitle [8]: - IEEE-ICTC, Jeju (ACCEPTED)\r\n           - Conference registration and payments done.\r\n           - Conference logistics (flight, hotel & PPT slides) in progress.\r\n\r\nTitle [7] and [9]: - IN-PROGRESS\r\n                   - Worked on the system model, algorithms and block diagrams.\r\n                   - To commence works on simulation and/or testbed soon.\r\n\r\nTitles [10]: - SUBMITTED on 01/10/2021.\r\n\r\nCOLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2021-09-27 00:00:00",
			"to_dt": "2021-10-01 00:00:00",
			"paper_progress": "1. Accurate Deep CNN-based Waveform Recognition for Intelligent Radar Systems.\r\n2. Densely-Accumulated Convolutional Network for Accurate LPI Radar Waveform Recognition - accepted in GLOBECOM 2021.\r\n3. Conference papers for ICT2021.",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "B00503",
			"fr_dt": "2021-10-04 00:00:00",
			"to_dt": "2021-10-08 00:00:00",
			"paper_progress": "1. The 5G+ Networks on the 28GHz Band at Campus: Challenges and Opportunities\r\n2. Compressed Medical Imaging using Spread Spectrum Acquisition and BPDN-Based Sparsity Averaging for Iris Images.\r\n3. Introducing 5G+ (28GHz) mmWave Campus Test-bed",
			"project_progress": "1. Preparation (IEEE Transactions on Education) \r\n2. Under review\r\n3. Accepted",
			"mnth_gls": "Submission of 1",
			"annl_gls": "2 SCI/SCIE"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-10-04 00:00:00",
			"to_dt": "2021-10-08 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 리비젼 진행 중 (90%)\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 및 시뮬레이션 진행\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 접수 완료, 10월 중 결과 발표\r\no 인도포닥 Dr. Shrivastava // 9 &#8211; 12월 중 입국 예정, 입국 전까지 국제협력 진행\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no Ardey // 요청사항 지원\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)\r\no IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 9월 중 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-10-04 00:00:00",
			"to_dt": "2021-10-08 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)",
			"project_progress": "Final version of 1 (To be submitted)",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals."
		},
		{
			"user": "william",
			"fr_dt": "2021-10-04 00:00:00",
			"to_dt": "2021-10-08 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal] [ACCEPTED]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access] [ACCEPTED]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 8:\r\nResearch works on IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Letters/Short Journal]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 9: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 10: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 11:IEEE-WCNC, 2022 [SUBMITTED]",
			"project_progress": "Titles [1], [2] & [9]: - ACCEPTED.\r\n- Final manuscript submitted.\r\n- Payments and publications in-progress.\r\n- For [9], conference logistics (flight, hotel & PPT slides) in progress.\r\n\r\nTitles [3], [4], [5] & [11]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [6]: - MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [7], [8] and [10]: - IN-PROGRESS\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n\r\nCOLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-10-04 00:00:00",
			"to_dt": "2021-10-08 00:00:00",
			"paper_progress": "* NOMA-VLC system에 DNN 적용 전력할당 연구\r\n- 논문작성중 20%(Pending) -> Quality 보완 필요\r\n\r\n* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- Channel estimation error 적용하여 시뮬레이션 완료",
			"project_progress": "* 강소특구 이노폴리스 창업 지원 관련 선정\r\n- 협약완료",
			"mnth_gls": "* 특허 1건 출원",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-10-04 00:00:00",
			"to_dt": "2021-10-08 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n3. Overview of ICT Convergence Specialized Research Center in South Korea",
			"project_progress": "",
			"mnth_gls": "Final version of 1 to be submitted.",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-10-08 00:00:00",
			"to_dt": "2021-10-14 00:00:00",
			"paper_progress": "1. 엣지 컴퓨팅관련 논문 준비중(하드웨어 vs 소프트웨어) - 보류\r\n   ICTC 발표준비 (스마트에너지관련 논문)",
			"project_progress": "1. 이노폴리스 캠프 특화교육 수강\r\n2. 문토트 지원사업(미선정)\r\n3. 아두이노 센서제어 프로그램 제작중",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-10-11 00:00:00",
			"to_dt": "2021-10-15 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Towards Intelligent Distributed Cloud: A Comprehensive Survey (IEEE Communications Surveys and Tutorials)",
			"project_progress": "1. Submit 1\r\n2. Update 2",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI/E journals."
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-10-12 00:00:00",
			"to_dt": "2021-10-15 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- Channel estimation error 반영하여 작성중\r\n\r\n* Cooperative Retransmission scheme in NOMA\r\n- Under review (MDPI Sensors)",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Cooperative Retransmission scheme in NOMA - Under review\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 작성 완료 목표",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2021-10-12 00:00:00",
			"to_dt": "2021-10-15 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal] [ACCEPTED]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access] [ACCEPTED]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 8:\r\nResearch works on IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Letters/Short Journal]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 9: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 10: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 11:IEEE-WCNC, 2022 [SUBMITTED]",
			"project_progress": "Titles [1], [2] & [9]: - ACCEPTED.\r\n- Final manuscript submitted.\r\n- Payments and publications in-progress.\r\n- For [9], conference logistics (flight, hotel & PPT slides) in progress.\r\n\r\nTitles [3], [4], [5] & [11]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [6]: - MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [7], [8] and [10]: - IN-PROGRESS\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n\r\nCOLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "disciple",
			"fr_dt": "2021-10-15 00:00:00",
			"to_dt": "2021-10-21 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 제출 완료\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 및 시뮬레이션 진행\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 접수 완료, 10월 중 결과 발표\r\no 인도포닥 Dr. Shrivastava // BP 과제 제안서 진행\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no Ardey // 요청사항 지원\r\no 포닥 Pool 조사 중\r\no 센터 Grand ICT 보고서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행 (50%)\r\no IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 9월 중 재투고 완료",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-10-18 00:00:00",
			"to_dt": "2021-10-22 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- Channel estimation error 반영하여 작성중\r\n\r\n* Cooperative Retransmission scheme in NOMA\r\n- Minor Revision (MDPI Sensors) 작성 제출",
			"project_progress": "* SNS통합 플랫폼 특허 초안 수정",
			"mnth_gls": "* 특허 1건 출원\r\n* Cooperative Retransmission scheme in NOMA - Minor Revision\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 작성 완료 목표",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-10-18 00:00:00",
			"to_dt": "2021-10-22 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 제출완료\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 및 시뮬레이션, 홀딩중\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 논문 작성완료, Holding 중",
			"project_progress": "o IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행\r\no 윌리암 Beamforming 논문 특허출원 및 등록 진행\r\no NRF BP 과제 (인도포닥, Dr. Dhatchayeny) // 접수 완료, 10월 중 결과 발표\r\no 인도포닥 Dr. Shrivastava // 국제협력 진행 및 BP 과제 진행\r\no 한국-베트남 국제협력과제 // 9월 중 결과발표\r\no Ardey // 요청사항 지원\r\no 센터 Grand ICT 보고서, 차년도 계획서 작업 지원",
			"mnth_gls": "o RUL 관련 아이디어 구상 및 시뮬레이션 진행",
			"annl_gls": "o SCI/E 논문 2건 게재"
		},
		{
			"user": "william",
			"fr_dt": "2021-10-18 00:00:00",
			"to_dt": "2021-10-22 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 8:\r\nResearch works on IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Letters/Short Journal]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 9: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 10: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 11:IEEE-WCNC, 2022 [SUBMITTED]",
			"project_progress": "Titles [1], [2] & [9]: - ACCEPTED.\r\n- Final manuscript submitted.\r\n- Payments and publications in-progress.\r\n- For [9], attendance and presentation at the conference was successful.\r\n\r\nTitles [3], [4], [5] & [11]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [6]: - MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\nTitle [7], [8] and [10]: - IN-PROGRESS\r\n- Worked on the system model, algorithms and block diagrams.\r\n- To commence works on simulation and/or testbed soon.\r\n\r\nCOLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-10-25 00:00:00",
			"to_dt": "2021-10-29 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concepts, Requirements, Challenges, and Future Directions",
			"project_progress": "1. Submitted\r\n2. In preparation",
			"mnth_gls": "",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "B00503",
			"fr_dt": "2021-10-25 00:00:00",
			"to_dt": "2021-11-29 00:00:00",
			"paper_progress": "1. The 5G+ Networks on the 28GHz Band at Campus: Challenges and Opportunities\r\n2. Compressed Medical Imaging using Spread Spectrum Acquisition and BPDN-Based Sparsity Averaging for Iris Images.\r\n3. Reinforcement Learning based Resource Management for Fog Computing Environment:\r\n   Literature Review, Challenges, and Open Issues\r\n4. Introducing 5G+ (28GHz) mmWave Campus Test-bed.",
			"project_progress": "1. To be submitted soon (IEEE Transactions on Education)\r\n2. Revision completed and submitted again (Under review)\r\n3. Accepted in Journals of Communications and Networks (JCN)\r\n4. Accepted in IEEE ICTC conference.",
			"mnth_gls": "",
			"annl_gls": "2 SCI/SCIE"
		},
		{
			"user": "B00502",
			"fr_dt": "2021-10-25 00:00:00",
			"to_dt": "2021-10-29 00:00:00",
			"paper_progress": "1. Regional Innovation at ICT Convergence Specialized Research Center: Researches & Industrial Cooperation (IEEE Transaction on Education)\r\n2. Learning-based Resource Management for Low-power and Lossy IoT Networks. (IEEE Internet of Things Journal).\r\n3. Reinforcement Learning based Resource Management for Fog Computing Environment: Literature Review, Challenges, and Open Issues",
			"project_progress": "",
			"mnth_gls": "Final version of 1 to be submitted to IEEE Transactions on Education",
			"annl_gls": "2 SCI/SCIE Publications.\r\n2 International conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-10-25 00:00:00",
			"to_dt": "2021-10-29 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중\r\n\r\n* Cooperative Retransmission scheme in NOMA\r\n- Accepted",
			"project_progress": "* SNS통합 플랫폼 특허 출원 완료",
			"mnth_gls": "* 특허 1건 출원\r\n* Cooperative Retransmission scheme in NOMA - Minor Revision\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 작성 - 다음달 계속 진행",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-11-01 00:00:00",
			"to_dt": "2021-11-05 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concepts, Requirements, Challenges, and Future Directions",
			"project_progress": "1. Under review\r\n2. Update",
			"mnth_gls": "",
			"annl_gls": "Publish at least 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-11-01 00:00:00",
			"to_dt": "2021-11-05 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성\r\n* 스마트에너지플랫폼 워크숍 실시",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-11-01 00:00:00",
			"to_dt": "2021-11-05 00:00:00",
			"paper_progress": "Paper research\t\r\n1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - in revision",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2021-11-01 00:00:00",
			"to_dt": "2021-11-05 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1:\r\nSensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2:\r\nAccess-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3:\r\nTCE-2021-05-0123. [IEEE Trans. on Consumer Electronics]\r\n\r\nTitle 4:\r\nTCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5:\r\nCOM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6:\r\nAccess-2021-10959. [IEEE Access]\r\n\r\nTitle 7:\r\nSurvey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 8:\r\nResearch works on IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Letters/Short Journal]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 9: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 10: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 11:IEEE-WCNC, 2022 [SUBMITTED]",
			"project_progress": "Titles [1] & [9]: - Awaiting final publications on eXplore repository.\r\n\r\n\r\nTitle [3]: - Publication declined.\r\n            - Reworking the paper based on comments received.\r\n            - To re-submit afterwards\r\n\r\nTitles [4], [5] & [11]: - UNDER REVIEW PROCESS.\r\n\r\n\r\nTitle [7], [8] and [10]: - IN-PROGRESS\r\n                         - Worked on the system model and block diagrams.\r\n                         - Simulations and testbed works in progress.\r\n                         - To finalize and submit by end-of-Nov.\r\n\r\nTitle [6]: - MENTORSHIP/RESEARCH SUPERVISION\r\n           - Publication declined.\r\n           - Resubmission allowed after Major revision.\r\n           - Reworking the paper with Mr. Damian.\r\n\r\n***COLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-11-08 00:00:00",
			"to_dt": "2021-11-12 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concepts, Requirements, Challenges, and Future Directions (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing",
			"project_progress": "1. Under review\r\n2. Update\r\n3. Update",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-11-08 00:00:00",
			"to_dt": "2021-11-12 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성\r\n* 스마트에너지플랫폼 워크숍 실시",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "disciple",
			"fr_dt": "2021-11-08 00:00:00",
			"to_dt": "2021-11-12 00:00:00",
			"paper_progress": "o IEEE Wireless Communications Letters, “A Hybrid CNN for Automatic Modulation Classification (AMC)” // 최종본 제출완료\r\no Remain Useful Maintenance (RUL) 관련 아이어디 구상 및 시뮬레이션\r\no KICS, “image-based Automatic Modulation Classification (AMC)” // 제출완료\r\no 논문상 관련 답변 완료",
			"project_progress": "o 국제협력 관련 인수인계 완료\r\no IEEE Access 게재 논문 //국내 특허출원 및 등록 진행\r\no IEEE WCL 준비논문 // 국내 특허출원 및 등록 진행",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2021-11-08 00:00:00",
			"to_dt": "2021-11-12 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3: TCE-2021-05-0123. [REVISING]\r\n\r\nTitle 4: TCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 5: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 6: Access-2021-10959. [IEEE Access]\r\n\r\nTitle 7: Survey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 8: IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Short Journal]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 9: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 10: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 11:IEEE-WCNC, 2022 [SUBMITTED]",
			"project_progress": "Titles [1] & [9]: - Awaiting final publications on eXplore repository.\r\n\r\nTitle [3]: - REVISING\r\n- Reworking the paper based on comments received.\r\n- To re-submit afterwards\r\n\r\nTitles [4], [5] & [11]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [7], [8] and [10]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-Nov.\r\n\r\nTitle [6]: - MENTORSHIP/RESEARCH SUPERVISION\r\n- Publication declined.\r\n- Resubmission allowed after Major revision.\r\n- Reworking the paper with Mr. Damian.\r\n\r\n***COLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-11-08 00:00:00",
			"to_dt": "2021-11-12 00:00:00",
			"paper_progress": "1. 스마트에너지플랫폼 관련 확장 논문 준비중\r\n\r\n2. 엣지 컴퓨팅관련 논문 준비중(하드웨어 vs 소프트웨어) - 보류",
			"project_progress": "1. 계약학과 임베디드특론 강의 진행 (~2021,12)",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-11-15 00:00:00",
			"to_dt": "2021-11-19 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concepts, Requirements, Challenges, and Future Directions (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing",
			"project_progress": "1. Under review\r\n2. Update\r\n3. Update",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-11-15 00:00:00",
			"to_dt": "2021-11-19 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - in revision",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2021-11-15 00:00:00",
			"to_dt": "2021-11-19 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3: TCAD-2021-0394. [IEEE Trans. on CAD] [REVISED & RE-SUBMITTED]\r\n\r\nTitle 4: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 5: Access-2021-10959. [IEEE Access]\r\n\r\nTitle 6: Survey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 7: IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Short Journal]\r\n\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 8: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 9: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 10:IEEE-WCNC, 2022 [SUBMITTED]\r\n.",
			"project_progress": "Titles [1] & [8]: - Awaiting final publications on eXplore repository.\r\n\r\nTitle [3]: - Comments from reviewers was received (Minor Revision)\r\n- The paper was reworked based on comments received.\r\n- Re-submission was completed on 18-11-2021.\r\n- Currently under review.\r\n\r\nTitles [3], [4] & [10]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [6], [7] and [9]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-Nov.\r\n\r\n***COLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-11-15 00:00:00",
			"to_dt": "2021-11-19 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성\r\n* 스마트에너지플랫폼 워크숍 실시(완료)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-11-22 00:00:00",
			"to_dt": "2021-11-26 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성\r\n* 스마트에너지플랫폼 워크숍 실시(완료)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-11-22 00:00:00",
			"to_dt": "2021-11-26 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concepts, Requirements, Challenges, and Future Directions (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing",
			"project_progress": "1. Under review\r\n2. Update\r\n3. Update",
			"mnth_gls": "",
			"annl_gls": "Publish 2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2021-11-22 00:00:00",
			"to_dt": "2021-11-26 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3: TCAD-2021-0394. [IEEE Trans. on CAD] [REVISED & RE-SUBMITTED]\r\n\r\nTitle 4: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 6: IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Short Journal]\r\n\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 7: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 8: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 9:IEEE-WCNC, 2022 [SUBMITTED]\r\n.",
			"project_progress": "Titles [1] & [8]: - Awaiting final publications on eXplore repository.\r\n\r\nTitles [3], [4], & [10]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5], [6] and [8]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-Nov.\r\n\r\n***COLLABORATIONS WITH DR. HOA: Paper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2021-11-22 00:00:00",
			"to_dt": "2021-11-26 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - in revision",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Intelligent Distributed Cloud.",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-11-26 00:00:00",
			"to_dt": "2021-12-02 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Collaborative Task Offloading for Delay Reduction in the Heterogeneous Fog Computing Systems, Submitted to ICT express.\r\n2. Physical Internet in the era of digital transformation, Revised and Under review, IEEE Access.\r\n3. The future of logistics: data driven technology approach and strategic management, Under review, IETE Technical review\r\n4. Reinforcement learning based resource allocation for fog computing environment: review, challenges, and open issues, Accepted (to appear in JCN)\r\n5. On the reliability of IIoT from systematic perspectives, accepted and similarity check in IETE technical review.\r\n6. Dynamic Task Offloading algorithm for fog computing systems, submitted to ICC 2022.",
			"project_progress": "Book Planning and writing: Intelligence Computation for reliable IIoT systems.",
			"mnth_gls": "3 accepted journals.",
			"annl_gls": "4-5 Published journals"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-11-29 00:00:00",
			"to_dt": "2021-12-03 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concepts, Requirements, Challenges, and Future Directions (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. Under review\r\n2. Update\r\n3. Update",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-11-29 00:00:00",
			"to_dt": "2021-12-03 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "* 개인연구과제 신청서 작성 - 세종펠로우쉽",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2021-11-29 00:00:00",
			"to_dt": "2021-12-03 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3: TCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 4: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 6: IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Short Journal]\r\n\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 7: IEEE-ICTC International Conference 2021. [ACCEPTED]\r\nTitle 8: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 9:IEEE-WCNC, 2022 [SUBMITTED]\r\n.",
			"project_progress": "Titles [1] & [8]: - Awaiting final publications on eXplore repository.\r\n\r\nTitles [3], [4], & [10]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5], [6] and [8]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA: \r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-12-03 00:00:00",
			"to_dt": "2021-12-09 00:00:00",
			"paper_progress": "1. 스마트에너지플랫폼 관련 논문 준비중\r\n2. 엣지컴퓨팅관련 논문 - 보류",
			"project_progress": "1. 계약학과 임베디드특론 강의종강",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-12-06 00:00:00",
			"to_dt": "2021-12-10 00:00:00",
			"paper_progress": "1. 스마트에너지플랫폼 관련 논문 준비중\r\n2. 엣지컴퓨팅관련 논문 - 보류",
			"project_progress": "1. 특허아이디어 검토\r\n - MRI 영상 3D변환 (선특허 조사중)\r\n\r\n2. QT 프로그래밍 study",
			"mnth_gls": "특허출원 1건\r\n소프트웨어 등록 1건",
			"annl_gls": "-국내 및 해외논문 1편 투고\r\n-저서 1권\r\n-특허 6\r\n-소프트웨어 등록 12"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-12-06 00:00:00",
			"to_dt": "2021-12-10 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concepts, Requirements, Challenges, and Future Directions (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "",
			"mnth_gls": "Under review (1)\r\nUpdating (2,3)",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-12-06 00:00:00",
			"to_dt": "2021-12-10 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n2. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- WCNC 2022",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (under review)",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-12-06 00:00:00",
			"to_dt": "2021-12-10 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "* 개인연구과제 신청서 제출 - 세종펠로우쉽",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2021-12-06 00:00:00",
			"to_dt": "2021-12-10 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3: TCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 4: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [TARGET: IEEE AES Magazine]\r\n\r\nTitle 6: IoT-Edge Packet Compression.[ON-GOING]. [TARGET: IEEE Short Journal]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 7: IEEE-ICTC International Conference 2021. [PUBLISHED]\r\nTitle 8: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 9:IEEE-WCNC, 2022 [SUBMITTED]\r\n\r\n.",
			"project_progress": "Titles [1]: - Awaiting final publications on eXplore repository.\r\n\r\nTitles [3], [4], & [10]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5], [6] and [8]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-12-10 00:00:00",
			"to_dt": "2021-12-16 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Collaborative Task Offloading for Delay Reduction in the Heterogeneous Fog Computing Systems, Submitted to IoT Journals.\r\n2. Physical Internet in the era of digital transformation, Accepted in IEEE Access, Early Access.\r\n3. The future of logistics: data driven technology approach and strategic management, Under review, IETE Technical review\r\n4. Reinforcement learning based resource allocation for fog computing environment: review, challenges, and open issues, Accepted (to appear in JCN)\r\n5. On the reliability of IIoT from systematic perspectives, accepted in IETE technical review, Awaiting Production Checklist.\r\n6. Dynamic Task Offloading algorithm for fog computing systems, submitted to ICC 2022 (Under Review).",
			"project_progress": "Book Writing:\r\nReliability of Data-driven IIoT systems: Architecture, Algorithms, Evaluation Models, and AI based intelligence computation",
			"mnth_gls": "2 accepted paper (SCI/SCIE)",
			"annl_gls": "4 accepted paper (SCI/SCIE)"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-12-13 00:00:00",
			"to_dt": "2021-12-17 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "Under review (1)\r\nUpdating (2,3)",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2021-12-13 00:00:00",
			"to_dt": "2021-12-17 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3: TCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 4: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: IoT-Edge Packet Compression.[ON-GOING]. [Journal, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 7: IEEE-ICTC International Conference 2021. [PUBLISHED]\r\nTitle 8: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 9:IEEE-WCNC, 2022 [Revising, TBD]\r\n\r\n.",
			"project_progress": "Titles [1]: - Awaiting final publications on eXplore repository.\r\n\r\nTitles [3] & [4]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5], [6], [8] and [9]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-12-13 00:00:00",
			"to_dt": "2021-12-17 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "thienht",
			"fr_dt": "2021-12-13 00:00:00",
			"to_dt": "2021-12-17 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n2. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- WCNC 2022",
			"project_progress": "1. Research collaboration\r\n- Dr. Pham: Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (under review)",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2021-12-17 00:00:00",
			"to_dt": "2021-12-23 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Collaborative Task Offloading in Fog Computing Systems, IEEE IoT Journal (Under Review)\r\n2. A dynamic algorithms for task offloading in fog computing systems, IEEE ICC 2022 conference (Under Review)\r\n3. Matching theory application for task offloading problems, IEEE IoT Magazine (In progress)\r\n4. Collaboration and Parallelism for Task Offloading in Fog computing environment: Perspectives and Open Research Issues, IEEE Access ( In progress)",
			"project_progress": "Book Writing:\r\n1- Reliability of Data Driven Industrial IoT systems: Architecture, Evaluation Models, Success Factors- Perspectives from Future Communication Networks and Computation Intelligence",
			"mnth_gls": "1- Finish paper 3",
			"annl_gls": "Achieve 4-5 accepted SIC/E papers."
		},
		{
			"user": "B00501",
			"fr_dt": "2021-12-20 00:00:00",
			"to_dt": "2021-12-24 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "Under review (1)\r\nUpdating (2,3)",
			"mnth_gls": "2-3 SCI journals",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2021-12-20 00:00:00",
			"to_dt": "2021-12-24 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\n\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED]\r\n\r\nTitle 3: TCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 4: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: IoT-Edge Packet Compression.[ON-GOING]. [Journal, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 7: IEEE-ICTC International Conference 2021. [PUBLISHED]\r\nTitle 8: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 9:IEEE-WCNC, 2022 [Revising, TBD]\r\n\r\n.",
			"project_progress": "Titles [1]: - Awaiting final publications on eXplore repository.\r\n\r\nTitles [3] & [4]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5], [6], [8] and [9]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "[1]. At-least two (2) SCI/E Journal publications per calendar year.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2021-12-20 00:00:00",
			"to_dt": "2021-12-28 00:00:00",
			"paper_progress": "1. 스마트에너지플랫폼 관련 논문 준비중\r\n2. 엣지컴퓨팅관련 논문 - 보류\r\n3. 통신학회 동계학술발표회 논문 준비중",
			"project_progress": "12월 29 - 31 개인 휴가",
			"mnth_gls": "특허출원 1건\r\nSW등록 1건",
			"annl_gls": "저서 1권\r\n특허 6\r\nSW등록 12\r\n-국내 및 해외논문 1편 투고"
		},
		{
			"user": "B00501",
			"fr_dt": "2021-12-27 00:00:00",
			"to_dt": "2021-12-31 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "In revision (1)",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2021-12-27 00:00:00",
			"to_dt": "2021-12-31 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당\r\n- 작성중",
			"project_progress": "* VE관련 교육/자료 조사",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-01-03 00:00:00",
			"to_dt": "2022-01-05 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: IoT-Edge Packet Compression.\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 5: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 6:IEEE-WCNC, 2022 [Revising, TBD]",
			"project_progress": "Titles [1], [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-01-03 00:00:00",
			"to_dt": "2022-01-07 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n2. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- WCNC 2022 (accepted)\r\n3. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE Sensor Journal (major revision)",
			"project_progress": "Dr. Pham: Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (major revision)",
			"mnth_gls": "Preparation of the response letter (IEEE sensor journal)",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-01-03 00:00:00",
			"to_dt": "2022-01-07 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "In revision (1)\r\nUpdated (2, 3)",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-01-03 00:00:00",
			"to_dt": "2022-01-07 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 작성중(70%)",
			"project_progress": "* VE관련 교육 희망 신청",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-01-05 00:00:00",
			"to_dt": "2022-01-07 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394. [IEEE Trans. on CAD]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Trans. on Comp.].\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 5: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 6:IEEE-WCNC, 2022 [Revising]",
			"project_progress": "Titles [1], [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-01-08 00:00:00",
			"to_dt": "2022-01-14 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Collaborative Task Offloading for Delay Reduction in the Heterogeneous Fog Computing Systems, Submitted to IoT Journals (Under Review).\r\n2. Physical Internet in the era of digital transformation, Published in IEEE Access.\r\n3. The future of logistics: data driven technology approach and strategic management, Under review, IETE Technical review\r\n4. Reinforcement learning based resource allocation for fog computing environment: review, challenges, and open issues, Accepted (to appear in JCN)\r\n5. On the reliability of IIoT from systematic perspectives, accepted in IETE technical review, Awaiting Production Checklist.\r\n6. Dynamic Task Offloading algorithm for fog computing systems, submitted to ICC 2022 (Under Review).\r\n7. Matching theory for Resource Allocation in Fog Environment: Perspectives and Open Issues (IoT Journal magazine)",
			"project_progress": "Book: \r\nReliability of Industrial Internet of Things systems: Concept, Evaluation Model,",
			"mnth_gls": "-2 SCI/E accepted",
			"annl_gls": "-4-5 SIC/E accepted paper\r\n-4-5 International Conferences"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-01-10 00:00:00",
			"to_dt": "2022-01-12 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n2. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- WCNC 2022 (accepted)\r\n3. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE Sensor Journal (major revision)",
			"project_progress": "Dr. Pham: Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (major revision)",
			"mnth_gls": "Preparation of the response letter (IEEE sensor journal",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-01-10 00:00:00",
			"to_dt": "2022-01-12 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2,3. Editing",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-01-10 00:00:00",
			"to_dt": "2022-01-12 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Trans. on CAD]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Trans. on Comp].\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 5: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 6:IEEE-WCNC, 2022 [Revising]",
			"project_progress": "Titles [1], [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-01-10 00:00:00",
			"to_dt": "2022-01-12 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 작성중(80%)",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-01-12 00:00:00",
			"to_dt": "2022-01-18 00:00:00",
			"paper_progress": "1. On reliability of IIoT systems, Accepted in IETE Technical Review (In production)\r\n2. Dynamical Algorithms for Fog Computing Systems, Submitted to ICC conference 2022 (under review)\r\n3. Joint Task Scheduling and Offloading for Delay Minimization in Fog Computing, submitted to KICS Winter 2022 (Under Review)\r\n4. Matching Theory for Distributed Computation Offloading, IoT Journal Magazine (in progress)",
			"project_progress": "Book:\r\n-Reliability for Industrial Internet of Things systems (in progress, springer publisher)",
			"mnth_gls": "- Submit one journal/ month",
			"annl_gls": "-Averagely, 1 accepted (SIC/E) paper/ month"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-01-12 00:00:00",
			"to_dt": "2022-01-14 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2,3. Editing",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-01-12 00:00:00",
			"to_dt": "2022-01-14 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Trans. on CAD]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Trans. on Comp].\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 5: IEEE-ICC, 2022 [ON-GOING]\r\nTitle 6:IEEE-WCNC, 2022 [Revising]",
			"project_progress": "Titles [1], [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-DEC.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-01-12 00:00:00",
			"to_dt": "2022-01-14 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n2. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- WCNC 2022 (accepted)\r\n3. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE Sensor Journal (major revision)",
			"project_progress": "Dr. Pham: Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (major revision).",
			"mnth_gls": "Preparation of the response letter (IEEE sensor journal)",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-01-12 00:00:00",
			"to_dt": "2022-01-14 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 작성완료\r\n- 자체 검토후 수정 계획",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-01-14 00:00:00",
			"to_dt": "2022-01-20 00:00:00",
			"paper_progress": "1. IIoT Reliability, IETE technical review (Accepted & in production)\r\n2. DCTO: Dynamic Collaborative Task Offloading, IoT Journal (Under review)\r\n3. Shaping the future of logistics: technologies and strategic management, IETE Technical review (Under review)\r\n4. Distributed algorithm for task offloading in fog computing systems, ICC 2022 conference (under review)\r\n5. Matching theory for Distributed Computation Offloading in IoT-Fog-Cloud Systems, IoT Journal Magazine (In progress)",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-01-17 00:00:00",
			"to_dt": "2022-01-19 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision",
			"mnth_gls": "Submit 2",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-01-17 00:00:00",
			"to_dt": "2022-01-19 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- WCNC 2022 (accepted)\r\n\r\n2. RaComNet: High-Performance Deep Network for Waveform Recognition in Coexistence Radar-Communication Systems - ICC 2022 (accepted)\r\n\r\n3. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n\r\n4. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE Sensor Journal (major revision)",
			"project_progress": "Dr. Pham: Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (major revision).",
			"mnth_gls": "Preparation of the response letter (IEEE sensor journal)",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2022-01-17 00:00:00",
			"to_dt": "2022-01-19 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Trans. on CAD]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Trans. on Comp].\r\n\r\nTitle 4:IEEE-short paper [Revising/resubmission soon]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 6: IEEE-ICC, 2022 [ON-GOING]",
			"project_progress": "Titles [1], [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "william",
			"fr_dt": "2022-01-19 00:00:00",
			"to_dt": "2022-01-21 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Trans. on CAD]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Trans. on Comp].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\nConference Papers: IEEE-ICC 2022, IEEE-ETFA 2022, and ICTC 2022 [ON-GOING]\r\n\r\n.",
			"project_progress": "Titles [1], [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-01-19 00:00:00",
			"to_dt": "2022-01-21 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-01-20 00:00:00",
			"to_dt": "2022-01-21 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- IEEE WCNC 2022 (accepted)\r\n\r\n2. RaComNet: High-Performance Deep Network for Waveform Recognition in Coexistence Radar-Communication Systems - IEEE ICC 2022 (accepted)\r\n\r\n3. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n\r\n4. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE Sensor Journal (major revision)",
			"project_progress": "Dr. Pham: Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (major revision).",
			"mnth_gls": "Monthly goals \tPreparation of the response letter (IEEE sensor journal)",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2022-01-24 00:00:00",
			"to_dt": "2022-02-26 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [ACCEPTED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\n>>>CONFERENCE LIST [Sept. 2021 - Aug. 2022]<<<\r\nConference Papers: IEEE-ICC 2022, IEEE-ETFA 2022, and ICTC 2022 [ON-GOING]\r\n\r\n.",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Revised/worked on final manuscript and copyright transfer.\r\n- Publication in progress.\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [ACCEPTED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-01-24 00:00:00",
			"to_dt": "2022-01-26 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision",
			"mnth_gls": "Submit 2",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-01-24 00:00:00",
			"to_dt": "2022-01-26 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- IEEE WCNC 2022 (accepted)\r\n\r\n2. RaComNet: High-Performance Deep Network for Waveform Recognition in Coexistence Radar-Communication Systems - IEEE ICC 2022 (accepted)\r\n\r\n3. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n\r\n4. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)",
			"project_progress": "",
			"mnth_gls": "Preparation of the response letter (IEEE System journal)",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-01-24 00:00:00",
			"to_dt": "2022-01-26 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)\r\n- 레퍼런스 추가 중",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-01-26 00:00:00",
			"to_dt": "2022-02-28 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [ACCEPTED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ICC 2022, IEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Revised/worked on final manuscript and copyright transfer.\r\n- Publication in progress.\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [ACCEPTED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-01-27 00:00:00",
			"to_dt": "2022-01-28 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)\r\n- 레퍼런스 추가 중",
			"project_progress": "",
			"mnth_gls": "* 특허 1건 출원\r\n* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-02-03 00:00:00",
			"to_dt": "2022-02-09 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ICC 2022, IEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Published (Early access).\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ALREADY PUBLISHED [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [ACCEPTED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-07 00:00:00",
			"to_dt": "2022-02-09 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)",
			"project_progress": "",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-07 00:00:00",
			"to_dt": "2022-02-09 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)",
			"project_progress": "* BMS 회로 개발\r\n- 강소특구 이노폴리스 결과보고서 작성\r\n- 강소특구 테크페어 전시 및 발표 자료 준비",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-07 00:00:00",
			"to_dt": "2022-02-11 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2. To be submitted",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-02-07 00:00:00",
			"to_dt": "2022-02-11 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- IEEE WCNC 2022 (accepted)\r\n\r\n2. RaComNet: High-Performance Deep Network for Waveform Recognition in Coexistence Radar-Communication Systems - IEEE ICC 2022 (accepted)\r\n\r\n3. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n\r\n4. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n5. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (Major revision).",
			"project_progress": "",
			"mnth_gls": "Preparation of the response letter (IEEE System journal)",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-07 00:00:00",
			"to_dt": "2022-02-11 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)",
			"project_progress": "",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-07 00:00:00",
			"to_dt": "2022-02-11 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)",
			"project_progress": "* BMS 회로 개발\r\n- 강소특구 이노폴리스 결과보고서 작성\r\n- 강소특구 테크페어 전시 및 발표 자료 준비",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-02-11 00:00:00",
			"to_dt": "2022-02-17 00:00:00",
			"paper_progress": "1. A survey: Matching theory for distributed computational offloading, IoT Journal (in progress)\r\n2. Matching-based distributed algorithm for dynamic task offloading, IoT Journal (In progress)\r\n3. DCTO: Dynamic Collaboration Task offloading in fog computing systems, IEEE Systems Journal ( Under review)",
			"project_progress": "",
			"mnth_gls": "Submit paper 1",
			"annl_gls": "3-4 ISI paper\r\n1 Published book"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-14 00:00:00",
			"to_dt": "2022-02-16 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)",
			"project_progress": "* BMS 회로 개발\r\n- 강소특구 이노폴리스 결과보고서 제출\r\n- 강소특구 이노폴리스 테크페어 참석 및 IR 대회 발표",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-02-14 00:00:00",
			"to_dt": "2022-02-16 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Published (Early access).\r\n- Awaiting Final publications\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4], [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-14 00:00:00",
			"to_dt": "2022-02-16 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-02-14 00:00:00",
			"to_dt": "2022-02-18 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- IEEE WCNC 2022 (accepted)\r\n\r\n2. RaComNet: High-Performance Deep Network for Waveform Recognition in Coexistence Radar-Communication Systems - IEEE ICC 2022 (accepted)\r\n\r\n3. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n\r\n4. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n5. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (major revision).",
			"project_progress": "",
			"mnth_gls": "Preparation of the response letter (IEEE System journal)",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-16 00:00:00",
			"to_dt": "2022-02-18 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2. Under review",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-02-16 00:00:00",
			"to_dt": "2022-02-18 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Published (Early access).\r\n- Awaiting Final publications\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4], [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-17 00:00:00",
			"to_dt": "2022-02-18 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Introduction 수정중 (DNN 적용 VLC 기존 연구 내용 추가 중)",
			"project_progress": "* BMS 회로 개발\r\n- 충방전 시험 관련 BMS 안전기능 펌웨어 작성",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-02-23 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Published (Early access).\r\n- Awaiting Final publications\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4], [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-02-23 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 초안 작성 완료",
			"project_progress": "* BMS 회로 개발\r\n- 셀 밸런싱 펌웨어 작성",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-03-23 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2. Under review",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-03-23 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2. Under review",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-02-25 00:00:00",
			"paper_progress": "1. Automatic Modulation Classification with Low-Cost Attention Network for Impaired OFDM Signals- IEEE WCNC 2022 (accepted)\r\n\r\n2. RaComNet: High-Performance Deep Network for Waveform Recognition in Coexistence Radar-Communication Systems - IEEE ICC 2022 (accepted)\r\n\r\n3. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n\r\n4. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n5. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (major revision).",
			"project_progress": "",
			"mnth_gls": "Preparation of the response letter (IEEE System journal)",
			"annl_gls": ""
		},
		{
			"user": "william",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-02-25 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Published (Early access).\r\n- Awaiting Final publications\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4], [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-03-25 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2. Under review",
			"mnth_gls": "",
			"annl_gls": "2-3 SCI journals"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-21 00:00:00",
			"to_dt": "2022-03-25 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2. Under review",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-24 00:00:00",
			"to_dt": "2022-02-25 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 초안 작성 및 영어교정",
			"project_progress": "* BMS 회로 개발\r\n- 충방전 테스트",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-02-28 00:00:00",
			"to_dt": "2022-03-02 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision\r\n2. Under review\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-02-28 00:00:00",
			"to_dt": "2022-03-02 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Published (Early access).\r\n- Awaiting Final publications\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4], [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-02-28 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (major revision)\r\n\r\n2. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n3. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (major revision).",
			"project_progress": "",
			"mnth_gls": "Preparation of the response letter (IEEE Wireless Communications Letters)",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-02-28 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 영어교정중",
			"project_progress": "* BMS 회로 개발\r\n- Current Sensor부 펌웨어 수정",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "jwkim",
			"fr_dt": "2022-03-01 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": "1. 함정통합네트워크관련 논문 준비",
			"project_progress": "1. 임베디드 AI 관련 연구",
			"mnth_gls": "소프트웨어 등록 1건\r\n국내논문초안준비",
			"annl_gls": "1. 용역 과제진행\r\n2. 국내논문 2편\r\n3. 소프트웨어 등록,특허출원"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-02 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022\r\nTarget: IEEE Sensor Journal (Under Review).\r\n\r\nTitle 2:ICTE-D-21-00585, ICT Express (under review).\r\n\r\nTitle 3: Access-2022-03435, IEEE Access (Under Review).\r\n\r\nTitle 4: TPWRS-00183-2022, IEEE Transactions on Power Systems (Under Review).",
			"project_progress": "",
			"mnth_gls": "1. Winter Intensive Completion and Assignment of Papers to reviewers\r\n2. Submission of ICUFN 2022 paper\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n 2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals\r\n 3. Attracting and Training of skilled international graduate students\r\n 4. Attend at least one (1) International Conference\r\n 5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-03-02 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision (With Associate Editor)\r\n2. Under review\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-03-02 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": "Title 1: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 2: Vision-based Drone Surveillance System Using CNN. [TVT]",
			"project_progress": "Title 2 is under processing.",
			"mnth_gls": "Complete Section I and Section II of Title 02",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "william",
			"fr_dt": "2022-03-02 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED]\r\n\r\nTitle 2: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 3: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 4: Drone-enabled JT-CoMP Cell-edges [IEEE Trans. on Par. and Distr. Sys.]\r\n\r\nTitle 5: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 6: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1]: - ACCEPTED.\r\n- Published (Early access).\r\n- Awaiting Final publications\r\n\r\nTitles [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4], [5] & [6]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-January.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED 2021].\r\nTitle 3: IEEE-ICTC International Conference 2021.\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "nsl",
			"fr_dt": "2022-03-02 00:00:00",
			"to_dt": "2022-03-04 00:00:00",
			"paper_progress": "1- Shaping the future of logistics systems, IETE Technical Review ( IN revision)\r\n2- DCTO: Dynamic Collaborative Task Offloading, IEEE Systems Journal (Under Review)\r\n3- Matching theory for distributed computational offloading, IEEE Systems Journals (In progress)",
			"project_progress": "- Book Proposal:\r\n1- Reliability of IIoT systems: Evaluation, Models, and Factors.",
			"mnth_gls": "1- Resubmit paper 1\r\n2- Submit paper 3",
			"annl_gls": "- 3-4 SCIE papers (publish)\r\n1- One book (published)"
		},
		{
			"user": "",
			"fr_dt": "2022-03-04 00:00:00",
			"to_dt": "2022-03-10 00:00:00",
			"paper_progress": "Title 1: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 2: Multi-task Learning Framework for Drone Surveillance System [IEEE Transactions on Vehicular Technology]\r\nTitle 3: Vision-based Drone Surveillance System Using CNN [Not fixed yet]",
			"project_progress": "Title 2 is now under processing.",
			"mnth_gls": "Write Section I and Section II of the Title 2 journal.",
			"annl_gls": "1. Acceptance of 2 SCI journals.\r\n2. Participate 2 international Conference."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-03-07 00:00:00",
			"to_dt": "2022-03-09 00:00:00",
			"paper_progress": "Title 1: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 2: Vision-based Drone Surveillance System Using CNN. [TVT]",
			"project_progress": "Title 2 is under processing.\r\n- Wrote two paragraph of section I.\r\n- Review one NSL winter intensive Paper.\r\n- Continue the simulation work",
			"mnth_gls": "Complete Section I and Section II of Title 02",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-07 00:00:00",
			"to_dt": "2022-03-09 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022\r\nTarget: IEEE Sensor Journal (Under Review).\r\n\r\nTitle 2:ICTE-D-21-00585, ICT Express (under review).\r\n\r\nTitle 3: Access-2022-03435, IEEE Access (Under Review).\r\n\r\nTitle 4: TPWRS-00183-2022, IEEE Transactions on Power Systems (Under Review).\r\n\r\nTitle 5: Innovative Industry-Track Graduate Studies Systems (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project: \r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\n2. Winter-intensive: So far, 5 papers have been completed and submitted to the review committee ( 2 of them already submitted to the target journals)\r\n3. NSL Monitoring and Supervision: Weekly paper meeting and seminar going on smoothly\r\n4. Research papers in progress.",
			"mnth_gls": "1. Winter Intensive Completion \r\n2. Assignment of Papers to reviewers (On-going)\r\n3. Submission of ICUFN 2022 paper\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-03-07 00:00:00",
			"to_dt": "2022-03-11 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n3. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (major revision).",
			"project_progress": "Preparation of the response letter (IEEE Wireless Communications Letters)",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-03-07 00:00:00",
			"to_dt": "2022-03-11 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision (With Associate Editor)\r\n2. Under review\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-03-07 00:00:00",
			"to_dt": "2022-03-11 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 2: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 3: Drone-enabled JT-CoMP Cell-edges  [IEEE Trans. on Netw.]\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1] & [2]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [3], [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-March.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED Oct. 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 3: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-03-07 00:00:00",
			"to_dt": "2022-03-11 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 영어교정 완료\r\n- latex 수정",
			"project_progress": "* BMS 회로 개발\r\n- 전류 측정 충방전 테스",
			"mnth_gls": "* Downlink NOMA 시스템 DNN 활용 전력할당 논문작성(목표저널:Optics express)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-03-10 00:00:00",
			"to_dt": "2022-03-11 00:00:00",
			"paper_progress": "Title 1: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 2: Vision-based Drone Surveillance System Using CNN. [TVT]",
			"project_progress": "Title 2 is under processing.\r\n- Continue to write of section I.\r\n- Continue the simulation work",
			"mnth_gls": "Complete Section I and Section II of Title 02",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-10 00:00:00",
			"to_dt": "2022-03-11 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022\r\nTarget: IEEE Sensor Journal (Under Review).\r\n\r\nTitle 2:ICTE-D-21-00585, ICT Express (under review).\r\n\r\nTitle 3: Access-2022-03435, IEEE Access (Under Review).\r\n\r\nTitle 4: TPWRS-00183-2022, IEEE Transactions on Power Systems (Under Review).\r\n\r\nTitle 5: Innovative Industry-Track Graduate Studies Systems (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\n2. Winter-intensive: So far, 5 papers have been completed and submitted to the review committee ( 2 of them already submitted to the target journals)\r\n3. NSL Monitoring and Supervision: \r\n1.Weekly paper meeting and seminar going on smoothly\r\n2. Assigned seven (7) Winter Intensive Papers to internal reviewers\r\n3. Begin preparation for the NSL Workshop holding on 2022.03.22\r\n4. Research papers in progress.",
			"mnth_gls": "1. Winter Intensive Completion\r\n2. Assignment of Papers to reviewers (On-going)\r\n3. Submission of ICUFN 2022 paper\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n4. hold the NSL Workshop on 2022.03.22",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "william",
			"fr_dt": "2022-03-14 00:00:00",
			"to_dt": "2022-03-16 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 2: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 3: Drone-enabled JT-CoMP Cell-edges  [IEEE Trans. on Netw.]\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1] & [2]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [3], [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-March.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED Oct. 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 3: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-03-14 00:00:00",
			"to_dt": "2022-03-16 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 제출 (Peer Review)\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- 관련 연구 논문 조사중",
			"project_progress": "* BMS 회로 개발",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-03-14 00:00:00",
			"to_dt": "2022-03-18 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Network)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision (With Associate Editor)\r\n2. Under review\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-14 00:00:00",
			"to_dt": "2022-03-16 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022\r\nTarget: IEEE Sensor Journal (Under Review).\r\nTitle 2:ICTE-D-21-00585, ICT Express (under review).\r\nTitle 3: Access-2022-03435, IEEE Access (Under Review).\r\nTitle 4: TPWRS-00183-2022, IEEE Transactions on Power Systems (Under Review).\r\nTitle 5: ADHOC-D-22-00135, Ad-hoc Networks (Under Review).\r\nTitle 6: Metaverse review paper collaboration with post master researchers (awaiting submission)\r\nTitle 7: Innovative Industry-Track Graduate Studies Systems (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\n2. Winter-intensive: So far, 5 papers have been completed and submitted to the review committee ( 2 of them already submitted to the target journals)\r\n3. NSL Monitoring and Supervision:\r\n1.Weekly paper meeting and seminar going on smoothly\r\n2. Assigned seven (7) Winter Intensive Papers to internal reviewers\r\n3. Begin preparation for the NSL Workshop holding on 2022.03.22\r\n4. Research papers in progress.",
			"mnth_gls": "1. Winter Intensive Completion\r\n2. Releasing of review comments to all NSL papers deadline is 2022.03.18 (On-going)\r\n3. Submission of ICUFN 2022 paper\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n4. hold the NSL Workshop on 2022.03.22\r\n5. Secure a collaboration meeting with at least one agency",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-03-14 00:00:00",
			"to_dt": "2022-03-18 00:00:00",
			"paper_progress": "Title 01: Multi-Task Framework for UAVs Surveillance System. [IEEE IoT Journal]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]",
			"project_progress": "Title 01 is under processing.\r\n- Continue to write of section I.\r\n- Continue the simulation work\r\nReview 3 winter intensive papers.",
			"mnth_gls": "Complete Section I, Section II of Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-03-14 00:00:00",
			"to_dt": "2022-03-18 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n3. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (major revision).",
			"project_progress": "",
			"mnth_gls": "Preparation of the response letter (IEEE Wireless Communications Letters)",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-03-17 00:00:00",
			"to_dt": "2022-03-18 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 제출 (Peer Review)\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- 관련 연구 논문 조사중",
			"project_progress": "* BMS 회로 개발",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-03-17 00:00:00",
			"to_dt": "2022-03-18 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 2: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 3: Drone-enabled JT-CoMP Cell-edges  [IEEE Trans. on Netw.]\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1] & [2]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [3], [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-March.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED Oct. 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 3: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-17 00:00:00",
			"to_dt": "2022-03-18 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022\r\nTarget: IEEE Sensor Journal (Under Review).\r\nTitle 2:ICTE-D-21-00585, ICT Express (under review).\r\nTitle 3: Access-2022-03435, IEEE Access (Under Review).\r\nTitle 4: TPWRS-00183-2022, IEEE Transactions on Power Systems (Under Review).\r\nTitle 5: ADHOC-D-22-00135, Ad-hoc Networks (Under Review).\r\nTitle 6: T-ITS-22-03-0721(Awaiting AE Assignment)\r\nTitle 7  COMNET-D-22-00420 (With Editor)\r\nTitle 8: T-ITS-22-03-0723(Awaiting Admin Processing)\r\nTitle 9: Innovative Industry-Track Graduate Studies Systems (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. submitted two papers on Metaverse (Under review)\r\nd. Started receiving reply from various agencies and universities in Nigeria. \r\n2. Winter-intensive: So far, 5 papers have been completed and submitted to the review committee ( 2 of them already submitted to the target journals)\r\n3. NSL Monitoring and Supervision:\r\n1.Weekly paper meeting and seminar going on smoothly\r\n2. Assigned seven (7) Winter Intensive Papers to internal reviewers\r\n3. Begin preparation for the NSL Workshop holding on 2022.03.22\r\n4. Research papers in progress.",
			"mnth_gls": "1. Winter Intensive Completion\r\n2. Releasing of review comments to all NSL papers deadline is 2022.03.18 (On-going)\r\n3. Submission of ICUFN 2022 paper\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n4. Hold the NSL Workshop on 2022.03.22\r\n5. Secure a collaboration meeting with at least one agency",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-03-18 00:00:00",
			"to_dt": "2022-03-24 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Coolaborative Task Offloading in fog computing systems, IEEE System journals ( Under review)\r\n2. Matching theory for distributed computation offloading, IEEE System Journals (under review)\r\n3. Shaping the future of logistics: Data-drivent technology and strategic management, IETE Technical Review (in revision)",
			"project_progress": "Book proposal:\r\n- Reliability of IIOT systems: Systematic evaluation, technology, and outlooks\r\n (springer) (in progress)",
			"mnth_gls": "1 SCI accepted paper",
			"annl_gls": "3-4 SCI articles published\r\nA book published"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-21 00:00:00",
			"to_dt": "2022-03-23 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022\r\nTarget: IEEE Sensor Journal (Under Review).\r\nTitle 2:ICTE-D-21-00585, ICT Express (under review).\r\nTitle 3: Access-2022-03435, IEEE Access (Under Review).\r\nTitle 4: TPWRS-00183-2022, IEEE Transactions on Power Systems (Under Review).\r\nTitle 5: ADHOC-D-22-00135, Ad-hoc Networks (Under Review).\r\nTitle 6: T-ITS-22-03-0721(Awaiting AE Assignment)\r\nTitle 7 COMNET-D-22-00420 (With Editor)\r\nTitle 8: T-ITS-22-03-0723(Awaiting Admin Processing)\r\nTitle 9: Innovative Industry-Track Graduate Studies Systems (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. submitted two papers on Metaverse (Under review)\r\nd. Started receiving reply from various agencies and universities in Nigeria.\r\ne. Nigerian Army University replied and awaiting further discussions before MOU\r\n2. Winter-intensive and NSL Matters: \r\na. Reviewed with Dr. Rubina, a total of 11 papers for submission to various journals. \r\nb. Successfully completed the NSL 2022 Winter Intensive Workshop on 2022.03.22\r\nc. 5 papers have been completed and submitted to their target journals\r\nd. Weekly paper meeting and seminar going on smoothly",
			"mnth_gls": "1. Winter Intensive Completion\r\n2. Releasing of review comments to all NSL papers deadline is 2022.03.18 (On-going)\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n4. Hold the NSL Workshop on 2022.03.22\r\n5. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-03-21 00:00:00",
			"to_dt": "2022-03-23 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In revision (With Associate Editor)\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-03-21 00:00:00",
			"to_dt": "2022-03-23 00:00:00",
			"paper_progress": "Title 01: Multi-Task Framework for UAVs Surveillance System. [IEEE IoT Journal]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]",
			"project_progress": "Title 01 is under processing.\r\n- Continue to write of section I.\r\n- Continue the simulation work\r\nReview 3 winter intensive papers.\r\n- Conduct NSL workshop\r\n- Review three Winter intensive paper",
			"mnth_gls": "Complete Section I, Section II of Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "william",
			"fr_dt": "2022-03-21 00:00:00",
			"to_dt": "2022-03-23 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Communications]\r\n\r\nTitle 2: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\n\r\nTitle 3: Drone-enabled JT-CoMP Cell-edges  [IEEE Trans. on Netw.]\r\n\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\n\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nTITLE 6: Accurate Continuous-Discrete Unscented Kalman Filtering Model for Aircraft-turn-coordinated Radar Tracking in ATC Systems. (ABSTRACT SUBMITTED - DASC 2022).\r\n\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1], [2] & [6]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [3], [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-March.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.\r\n\r\n.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": ".\r\nJOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED Oct. 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 3: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-03-21 00:00:00",
			"to_dt": "2022-03-25 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- 제출 (Peer Review)\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- 관련 연구 논문 조사중",
			"project_progress": "* BMS 회로 개발",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-03-21 00:00:00",
			"to_dt": "2022-03-25 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n3. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-24 00:00:00",
			"to_dt": "2022-03-25 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022, IEEE Sensor Journal (Under Review).\r\nTitle 2:ICTE-D-21-00585, ICT Express (under review).\r\nTitle 3: Access-2022-03435, IEEE Access (Under Review).\r\nTitle 4: TPWRS-00183-2022, IEEE Transactions on Power Systems (Under Review).\r\nTitle 5: ADHOC-D-22-00135, Ad-hoc Networks (Under Review).\r\nTitle 6: T-ITS-22-03-0721(Awaiting AE Assignment)\r\nTitle 7 COMNET-D-22-00420 (With Editor)\r\nTitle 8: T-ITS-22-03-0723(Under Review)\r\nTitle 9: Innovative Industry-Track Graduate Studies Systems (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. submitted two papers on Metaverse (Under review)\r\nd. Started receiving reply from various agencies and universities in Nigeria.\r\ne. Nigerian Army University replied and awaiting further discussions before MOU\r\n\r\n2. Winter-intensive and NSL Matters:\r\na. Reviewed with Dr. Rubina, a total of 11 papers for submission to various journals.\r\nb. Successfully completed the NSL 2022 Winter Intensive Workshop on 2022.03.22\r\nc. 5 papers have been completed and submitted to their target journals\r\nd. Weekly paper meeting and seminar going on smoothly\r\n\r\n3. Outstanding Review Comments of Previous Authors' Papers (Former NSL or Postdoc)\r\na. IEEE IoT Journal final minor corrections completed and uploaded to the IEEE author center: (doi: 10.1109/jiot.2022.3152929)\r\nb. IET Measurement paper returned with minor revision: (deadline is April 8, 2022)",
			"mnth_gls": "1. Winter Intensive Completion\r\n2. Releasing of review comments to all NSL papers deadline is 2022.03.18 (On-going)\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n4. Hold the NSL Workshop on 2022.03.22\r\n5. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-03-24 00:00:00",
			"to_dt": "2022-03-25 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. With Associate Editor\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-03-24 00:00:00",
			"to_dt": "2022-03-25 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Communications]\r\nTitle 2: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\nTitle 3: Drone-enabled JT-CoMP Cell-edges  [IEEE Trans. on Netw.]\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nTITLE 6: Accurate Continuous-Discrete Unscented Kalman Filtering Model for Aircraft-turn-coordinated Radar Tracking in ATC Systems. (SUBMITTED - DASC 2022).\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1], [2] & [6]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [3], [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-March.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "JOURNAL/CONFERENCE STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED Oct. 2021]\r\nTitle 2: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 3: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 4: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-28 00:00:00",
			"to_dt": "2022-03-30 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022,  (Under Review).\r\nTitle 2: ICTE-D-21-00585,  (under review).\r\nTitle 3: Access-2022-03435, (Under Review).\r\nTitle 4: TPWRS-00183-2022,  (Under Review).\r\nTitle 5: ADHOC-D-22-00135, (Under Review).\r\nTitle 6: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 7: COMNET-D-22-00420,  (With Editor)\r\nTitle 8: T-ITS-22-03-0723, (Under Review)\r\nTitle 9: IoT-23106-2022,  ( Under review)\r\nTitle 10: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. submitted two papers on Metaverse (Under review)\r\nd. Started receiving reply from various agencies and universities in Nigeria.\r\ne. Nigerian Army University replied and awaiting further discussions before MOU\r\nf. Prepared and submitted metaverse project proposal (April 2022 to March 2024)\r\n2. NSL Activities: \r\na. Reviewed and reviewed 14 applications of prospective members with Dr. Rubina.\r\nb. Successfully completed the recruitment examination and assignments to all prospective members of NSL\r\nc. 5 papers have been completed and submitted to the lab for possible conference papers of new comers\r\nd. 6 Winter intensive papers submitted to their target journals\r\ne. Weekly paper meeting and seminar going on smoothly\r\n\r\n3. Outstanding Review Comments of Previous Authors' Papers (Former NSL or Postdoc)\r\na. IEEE IoT Journal (Arslan)  final minor corrections completed and uploaded to the IEEE author center: (doi: 10.1109/jiot.2022.3152929) (done)\r\nb. IET Measurement paper returned with minor revision (Bushra) : (deadline is April 8, 2022)\r\nc. IET Communications paper on edge computing (Sajjad)",
			"mnth_gls": "1. Winter Intensive Completion\r\n2. Releasing of review comments to all NSL papers deadline is 2022.03.18 (done)\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n4. Hold the NSL Workshop on 2022.03.22 (done)\r\n5. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.\r\n6. prepare and submit metaverse project proposal  (done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-03-28 00:00:00",
			"to_dt": "2022-03-30 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- 관련 연구 논문 조사중",
			"project_progress": "* BMS 회로 개발\r\n- CAN통신 테스트",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-03-28 00:00:00",
			"to_dt": "2022-04-30 00:00:00",
			"paper_progress": "Title 01: Multi-Task Framework for UAVs Surveillance System. [IEEE IoT Journal]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]",
			"project_progress": "Title 01 is under processing",
			"mnth_gls": "Complete Section I, Section II of Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "william",
			"fr_dt": "2022-03-28 00:00:00",
			"to_dt": "2022-03-30 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Communications]\r\nTitle 2: TCSI-2022-01-0010 [IEEE Transactions on Comp.].\r\nTitle 3: Drone-enabled JT-CoMP Cell-edges  [IEEE Trans. on Netw.]\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nTITLE 6: Submission ID: 3169 (DASC 2022).\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1], [2] & [6]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [3], [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-March.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "JOURNAL/CONFERENCE PUBLICATION STATUS [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-03-28 00:00:00",
			"to_dt": "2022-03-30 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. With Associate Editor\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-03-28 00:00:00",
			"to_dt": "2022-04-01 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n3. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-03-31 00:00:00",
			"to_dt": "2022-04-01 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- 관련 연구 논문 조사중",
			"project_progress": "* BMS 회로 개발",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-03-31 00:00:00",
			"to_dt": "2022-04-01 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022, (Under Review).\r\nTitle 2: ICTE-D-21-00585,    (under review).\r\nTitle 3: Access-2022-03435,  (Under Review).\r\nTitle 4: TPWRS-00183-2022,   (Under Review).\r\nTitle 5: ADHOC-D-22-00135,   (Under Review).\r\nTitle 6: T-ITS-22-03-0721,   (Awaiting AE Assignment)\r\nTitle 7: COMNET-D-22-00420,  (With Editor).\r\nTitle 8: T-ITS-22-03-0723,   (Awaiting Admin Processing)\r\nTitle 9: IoT-23106-2022,     (Under review).\r\nTitle 10: ITSM-22-03-0051,   (Under Review).\r\nTitle 11: ICTE-D-22-00143,   (With Editor).\r\nTitle 11: SMT-2022-04-0039,  (Pending Editor Assignment).\r\nTitle 12: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with post master researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. submitted two papers on Metaverse (Under review)\r\nd. Started receiving reply from various agencies and universities in Nigeria.\r\ne. Nigerian Army University replied and awaiting further discussions before MOU\r\nf. Prepared and submitted metaverse project proposal (April 2022 to March 2024)\r\n2. NSL Activities:\r\na. Reviewed and reviewed 14 applications of prospective members with Dr. Rubina.\r\nb. Successfully completed the recruitment examination and assignments to all prospective members of NSL\r\nc. 5 papers have been completed and submitted to the lab for possible conference papers of new comers\r\nd. 7 Winter intensive papers submitted to their target journals\r\ne. Weekly paper meeting and seminar going on smoothly\r\n\r\n3. Outstanding Review Comments of Previous Authors' Papers (Former NSL or Postdoc)\r\na. IEEE IoT Journal (Arslan) final minor corrections completed and uploaded to the IEEE author center: (doi: 10.1109/jiot.2022.3152929) (done)\r\nb. IET Measurement paper returned with minor revision (Bushra) : (deadline is April 8, 2022)\r\nc. IET Communications paper on edge computing (Sajjad) (in progress)",
			"mnth_gls": "1. Winter Intensive Completion (Done)\r\n2. Releasing of review comments to all NSL papers deadline is 2022.03.18 (done)\r\n3. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n4. Hold the NSL Workshop on 2022.03.22 (done)\r\n5. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.\r\n6. prepare and submit metaverse project proposal (done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training of skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-03-31 00:00:00",
			"to_dt": "2022-04-01 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. With Associate Editor\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-03-31 00:00:00",
			"to_dt": "2022-04-08 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Comm.]\r\nTitle 2: TCSI-2022-01-0010 [IEEE TC.].\r\nTitle 3: TNSM-2022-05102 [IEEE TNetw.]\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nTITLE 6: Submission ID: 3169 (DASC 2022).\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1], [2], [3] & [6]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-April.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-04-04 00:00:00",
			"to_dt": "2022-04-06 00:00:00",
			"paper_progress": "Title 01: Multi-Task Framework for UAVs Surveillance System. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: (Under Review)\r\nTitle 05: (Under Revision)\r\nTitle 06: (Under Review)",
			"project_progress": "Title 01 is under processing",
			"mnth_gls": "Complete Section III, and Section IV of Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-04-04 00:00:00",
			"to_dt": "2022-04-06 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022, (Under Review).\r\nTitle 2: ICTE-D-21-00585, (under review).\r\nTitle 3: MEASEN-D-22-00052, (With Editor).\r\nTitle 4: Access-2022-03435, (In-Revision).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Admin Processing)\r\nTitle 10: IoT-23106-2022, (Under review).\r\nTitle 11: ITSM-22-03-0051, (Under Review).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: SMT-2022-04-0039, (Pending Editor Assignment).\r\nTitle 14: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with postmaster researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. submitted two papers on Metaverse (Under review)\r\nd. Started receiving replies from various agencies and universities in Nigeria.\r\ne. Nigerian Army University and five more universities replied and awaiting further discussions before MOU\r\nf. Prepared and submitted metaverse project proposal (April 2022 to March 2024)\r\n2. NSL Activities:\r\na. Reviewed 16 applications of prospective members with Dr. Rubina.\r\nb. Successfully completed the recruitment examination and assignments to all prospective members of NSL (Shortlisted 13)\r\nc. 6 papers have been completed and submitted to the lab for possible conference papers of newcomers\r\nd. 7 Winter intensive papers submitted to their target journals\r\ne. Weekly paper meetings and seminars going on smoothly\r\n\r\n3. Outstanding Review Comments of Previous Authors' Papers (Former NSL or Postdoc)\r\na. IET Measurement paper returned with minor revision (Bushra) : (deadline is April 8, 2022)\r\nc. IET Communications paper on edge computing (Sajjad) (in progress)",
			"mnth_gls": "1. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n2. Conclude plans for the first Metaverse workshop coming up in May 2022 (done)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.\r\n4. prepare and populate content on the Creativia website (50% done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-04 00:00:00",
			"to_dt": "2022-04-06 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고 목표)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- 전력할당부 DRL 환경 작성",
			"project_progress": "* BMS 회로 개발",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-04-04 00:00:00",
			"to_dt": "2022-04-06 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. With Associate Editor\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-04-04 00:00:00",
			"to_dt": "2022-04-08 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision)\r\n\r\n3. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).",
			"project_progress": "",
			"mnth_gls": "",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-04-06 00:00:00",
			"to_dt": "2022-04-08 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Concept, Architecture, Design Principles, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. With Associate Editor\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journals"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-04-07 00:00:00",
			"to_dt": "2022-04-08 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022, (Under Review).\r\nTitle 2: ICTE-D-21-00585, (under review).\r\nTitle 3: MEASEN-D-22-00052, (With Editor).\r\nTitle 4: Access-2022-03435, (In-Revision).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Admin Processing)\r\nTitle 10: IoT-23106-2022, (Under review).\r\nTitle 11: ITSM-22-03-0051, (Under Review).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Pending Reviewer Assignment).\r\nTitle 14: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with postmaster researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. submitted two papers on Metaverse (Under review)\r\nd. Started receiving replies from various agencies and universities in Nigeria.\r\ne. Nigerian Army University and five more universities replied and awaiting further discussions before MOU\r\nf. Prepared and submitted metaverse project proposal (April 2022 to March 2024)\r\n2. NSL Activities:\r\na. Reviewed 16 applications of prospective members with Dr. Rubina.\r\nb. Successfully completed the recruitment examination and assignments to all prospective members of NSL (Shortlisted 13)\r\nc. 6 papers have been completed and submitted to the lab for possible conference papers of newcomers\r\nd. 7 Winter intensive papers submitted to their target journals\r\ne. Weekly paper meetings and seminars going on smoothly\r\n\r\n3. Outstanding Review Comments of Previous Authors' Papers (Former NSL or Postdoc)\r\na. IET Measurement (Bushra (submitted on 2022.04.06)\r\nb. IET Communications paper on edge computing (Sajjad) (in progress)",
			"mnth_gls": "1. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n2. Conclude plans for the first Metaverse workshop coming up in May 2022 (done)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.\r\n4. prepare and populate content on the Creativia website (50% done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-04-07 00:00:00",
			"to_dt": "2022-04-08 00:00:00",
			"paper_progress": "Title 01: Multi-Task Framework for UAVs Surveillance System. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: (Under Review)\r\nTitle 05: (Under Revision)\r\nTitle 06: (Under Review)",
			"project_progress": "Title 01 is under processing\r\n1.   Survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2.   Shortlist the university and software company to welcome in NSL metaverse platform.\r\n3.   Discussed one software agent about NSL metaverse, need to explore the feasibility of the NSL metaverse platform for the elaborate discussion.",
			"mnth_gls": "Complete Section III, and Section IV of Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-07 00:00:00",
			"to_dt": "2022-04-08 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- 전력할당부 DRL 환경 작성 완료\r\n- Double DQN 구현중",
			"project_progress": "* BMS 회로 개발",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-04-08 00:00:00",
			"to_dt": "2022-04-14 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Collaborative Task Offloading in Fog computing systems, IEEE System Journal (Under review)\r\n2. Matching theory for distributed computation offloading, IEEE system journal (under review)\r\n3. Shaping the future of logistics, IETE technical review (revised and under review)\r\n4. AI-based assistance system for monitoring the baby activities at home ( Journal and Patent) ( In progress)",
			"project_progress": "Book proposals:\r\n1- Reliability of Industrial IoT\r\n2- Distributed computation for fog computing systems",
			"mnth_gls": "1 accepted SCI",
			"annl_gls": "* 3-4 SCI journal published\r\n\r\n* 1 book online"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-04-11 00:00:00",
			"to_dt": "2022-04-13 00:00:00",
			"paper_progress": "Title 1: Sensors-47352-2022, (Under Review).\r\nTitle 2: ICTE-D-21-00585, (under review).\r\nTitle 3: MEASEN-D-22-00052, (With Editor).\r\nTitle 4: Access-2022-03435, (In-Revision).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Admin Processing)\r\nTitle 10: IoT-23106-2022, (Under review).\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review) Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Pending Reviewer Assignment).\r\nTitle 14: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (In progress)",
			"project_progress": "1. Nigerian Project:\r\na. Meeting with postmaster researchers and Professor\r\nb. Drafted and got approval for the March and April Targets\r\nc. Submitted two papers on Metaverse (Under review)\r\nd. Started receiving replies from various agencies and universities in Nigeria.\r\ne. Commenced the first implementation project on Virtual Assistant in the metaverse.\r\nf. Prepared and submitted metaverse project proposal (April 2022 to March 2024)\r\n2. NSL Activities:\r\na. Reviewed 16 applications of prospective members with Dr. Rubina.\r\nb. Successfully completed the recruitment examination and assignments to all prospective members of NSL (Shortlisted 13)\r\nc. 6 papers have been completed and submitted to the lab for possible conference papers of newcomers\r\nd. 7 Winter intensive papers submitted to their target journals\r\ne. Weekly paper meetings and seminars going on smoothly\r\n\r\n3. Outstanding Review Comments of Previous Authors' Papers (Former NSL or Postdoc)\r\na. IET Measurement (Bushra (submitted on 2022.04.06)\r\nb. IET Communications paper on edge computing (Sajjad) (in progress)",
			"mnth_gls": "1. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n2. Conclude plans for the first Metaverse workshop coming up in May 2022 (done)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.\r\n4. prepare and populate content on the Creativia website (50% done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-04-11 00:00:00",
			"to_dt": "2022-04-13 00:00:00",
			"paper_progress": "Title 01: Multi-Task Framework for UAVs Surveillance System. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: (Under Review)\r\nTitle 05: (Under Revision)\r\nTitle 06: (Under Review)",
			"project_progress": "Title 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Shortlist the university and software company to welcome in NSL metaverse platform.\r\n3. Discussed one software agent about NSL metaverse, need to explore the feasibility of the NSL metaverse platform for the elaborate discussion.\r\n4. Guiding the new comers for the application",
			"mnth_gls": "Complete Section III, and Section IV of Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "william",
			"fr_dt": "2022-04-11 00:00:00",
			"to_dt": "2022-04-13 00:00:00",
			"paper_progress": ">>>JOURNAL LIST [Sept. 2021 - Aug. 2022]<<<\r\n\r\nTitle 1: COM-2021-07-0270 [IET Comm.]\r\nTitle 2: TCSI-2022-01-0010 [IEEE TC.].\r\nTitle 3: TNSM-2022-05102 [IEEE TNetw.]\r\nTitle 4: Survey works on combat Avionics.[ON-GOING]. [Magazine, TBD]\r\nTitle 5: Low-Power FACTS for SVCs [ON-GOING]. [IEEE Transactions, TBD]\r\n\r\n\r\nCONFERENCE PAPERS:\r\nTITLE 6: Submission ID: 3169 (DASC 2022).\r\nIEEE-ETFA 2022, and ICTC 2022 [ON-GOING]",
			"project_progress": "Titles [1], [2], [3] & [6]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-April.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-11 00:00:00",
			"to_dt": "2022-04-13 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Double DQN 구현완료\r\n- Uplink 전력할당부 완료",
			"project_progress": "* BMS 회로 개발\r\n- 하드웨어 에러 발견 및 수정 요청",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-04-11 00:00:00",
			"to_dt": "2022-04-13 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. With Associate Editor\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "thienht",
			"fr_dt": "2022-04-11 00:00:00",
			"to_dt": "2022-04-15 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).\r\n\r\n3. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision).\r\n\r\n4. High-Performance Convolutional Network for RF-based Drone Surveillance Systems (major revision).\r\n\r\n5. Artificial Intelligence for the Metaverse: A Survey - IEEE TAI (under review).",
			"project_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (minor revision).",
			"mnth_gls": "1. IEEE WCNC 2022, Apr. 10-13, Austin, USA (virtual participation).\r\n\r\n2. IEEE ICC 2022, May. 16-20, Seoul, South Korea.",
			"annl_gls": ""
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-04-14 00:00:00",
			"to_dt": "2022-04-15 00:00:00",
			"paper_progress": "Title 1:Sensors-47352-2022, (Under Review).\r\nTitle 2:ICTE-D-22-00143, (With Editor).\r\nTitle 3:MEASEN-D-22-00052, (Under Review).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 50% in progress)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\nTitle 1: ICTE-D-21-00585, (under review).\r\nTitle 2: IoT-20662-2021. (under review).\r\nTitle 3: IoT-23106-2022, (Under review).\r\nTitle 4: IoT-23193-2022, (under review).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Admin Processing)\r\nTitle 10: Access-2022-03435, (Under review: Second Revision).\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review) Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Pending Reviewer Assignment).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Consolidating on the Nigerian Project and Clarity of Target Project.\r\n2. Conclude plans for the first Metaverse workshop coming up in May 2022 (done)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria.\r\n4. prepare and populate content on the Creativia website (60% done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-14 00:00:00",
			"to_dt": "2022-04-15 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)",
			"project_progress": "* BMS 회로 개발\r\n- 배터리모듈 수정후 BMS 적용",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-04-14 00:00:00",
			"to_dt": "2022-04-15 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)",
			"project_progress": "1. In Revision\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation",
			"mnth_gls": "",
			"annl_gls": "2 SCI journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-04-14 00:00:00",
			"to_dt": "2022-04-15 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCSI-2022-01-0010 - IEEE TC.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (ON-GOING)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (ON-GOING)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\n*IEEE-ETFA 2022, and ICTC 2022 (ON-GOING)",
			"project_progress": "Titles [1], [2] & [3]: - UNDER REVIEW PROCESS.\r\n\r\nTitle [6]: - Accepted for publication.\r\n- Revising Camera-ready manuscript.\r\n\r\nTitle [4] & [5]: - IN-PROGRESS\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-April.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-04-14 00:00:00",
			"to_dt": "2022-04-15 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Under Review)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (Under Revision)",
			"project_progress": "Title 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Shortlist the university and software company to welcome in NSL metaverse platform.\r\n3. Discussed one software agent about NSL metaverse, need to explore the feasibility of the NSL metaverse platform for the elaborate discussion.\r\n4. Guiding the new comers for the application\r\n\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "Complete Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-04-18 00:00:00",
			"to_dt": "2022-04-20 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE Journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-04-18 00:00:00",
			"to_dt": "2022-04-20 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCSI-2022-01-0010 - IEEE TC.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [2] & [3]: - (UNDER REVIEW PROCESS).\r\n\r\nTitle [1]: - (IN-REVISION).\r\n- Comments anticipating major revision was received on April 17th.\r\n- Revising manuscript for re-submission.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-April.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Revising Camera-ready manuscript.\r\n\r\nTitle [7]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\n\r\n\r\nFURTHER GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-18 00:00:00",
			"to_dt": "2022-04-20 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)",
			"project_progress": "* BMS 회로 개발\r\n- 배터리모듈 수정후 BMS 적용",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-04-18 00:00:00",
			"to_dt": "2022-04-20 00:00:00",
			"paper_progress": "Title 1:Sensors-47352-2022, (Under Review).\r\nTitle 2:ICTE-D-22-00143, (With Editor).\r\nTitle 3:MEASEN-D-22-00052, (Under Review).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\nTitle 1: ICTE-D-21-00585, (under review).\r\nTitle 2: IoT-20662-2021. (under review).\r\nTitle 3: IoT-23106-2022, (Under review).\r\nTitle 4: IoT-23193-2022, (under review).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 10: Access-2022-03435, (Under review: Second Revision).\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Pending Reviewer Assignment).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the expression of interest with three Nigerian Universities (80%).\r\n2. Conclude plans for the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (50%).\r\n4. prepare and populate content on the Creativia website (80% done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-04-18 00:00:00",
			"to_dt": "2022-04-22 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).\r\n\r\n3. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision).\r\n\r\n4. High-Performance Convolutional Network for RF-based Drone Surveillance Systems (major revision).\r\n\r\n5. Artificial Intelligence for the Metaverse: A Survey - IEEE TAI (under review).",
			"project_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (minor revision).",
			"mnth_gls": "1. IEEE WCNC 2022, Apr. 10-13, Austin, USA (virtual participation).\r\n\r\n2. IEEE ICC 2022, May. 16-20, Seoul, South Korea.",
			"annl_gls": ""
		},
		{
			"user": "20195028",
			"fr_dt": "2022-04-20 00:00:00",
			"to_dt": "2022-04-26 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Under Review)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (Under Revision)",
			"project_progress": "Title 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Shortlist the university and software company to welcome in NSL metaverse platform.\r\n3. Discussed Dynamite game software agent about NSL metaverse, need to explore the feasibility of the NSL metaverse platform for the elaborate discussion.\r\n4. Guiding the new comers for the application\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "Complete Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-04-21 00:00:00",
			"to_dt": "2022-04-22 00:00:00",
			"paper_progress": "Title 1:Sensors-47352-2022, (Under Review).\r\nTitle 2:ICTE-D-22-00143, (With Editor).\r\nTitle 3:MEASEN-D-22-00052, (Under Review).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 85% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\nTitle 1: ICTE-D-21-00585, (under review).\r\nTitle 2: IoT-20662-2021. (under review).\r\nTitle 3: IoT-23106-2022, (Under review).\r\nTitle 4: IoT-23193-2022, (under review).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 10: Access-2022-03435, (Under review: Second Revision).\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Pending Reviewer Assignment).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the expression of interest with three Nigerian Universities (85%).\r\n2. Conclude plans for the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (50%).\r\n4. prepare and populate content on the Creativia website (80% done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-04-21 00:00:00",
			"to_dt": "2022-04-22 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Revised and submit to IEEE-CEM\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE Journals"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-04-21 00:00:00",
			"to_dt": "2022-04-22 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Under Review)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (Under Revision)",
			"project_progress": "Title 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Trying to contact with the Walton company for metaverse collaboration.\r\n\r\n4. Guiding the new comers for the application\r\n\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "Complete Title 01",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-21 00:00:00",
			"to_dt": "2022-04-22 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)",
			"project_progress": "* BMS 회로 개발\r\n- BMS 샘플 회로 2개 에러 수정",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-04-21 00:00:00",
			"to_dt": "2022-04-27 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCSI-2022-01-0010 - IEEE TC.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [2] & [3]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [1]: - (IN-REVISION).\r\n- Review comments anticipating major revision was received on April 17th.\r\n- Revising manuscript according to the received review comments.\r\n- Preparing the manuscript for re-submission soon.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-April.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Revising Camera-ready manuscript.\r\n\r\nTitle [7]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 (ACCEPTED April 2022)\r\n\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-25 00:00:00",
			"to_dt": "2022-04-27 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)",
			"project_progress": "* BMS 회로 개발\r\n- BMS적용 배터리 모듈 충방전 테스트 재실시",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-04-25 00:00:00",
			"to_dt": "2022-04-27 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (Under Review).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 85% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\nTitle 1: ICTE-D-21-00585, (under review).\r\nTitle 2: IoT-20662-2021. (under review).\r\nTitle 3: IoT-23106-2022, (Under review).\r\nTitle 4: IoT-23193-2022, (under review).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 10: Access-2022-03435, (Under review: Second Revision).\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Pending Reviewer Assignment).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the expression of interest (EoI) and MOU with three Nigerian Universities (95%). (Waiting for Professors' signature) \r\n2. Conclude plans for the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. prepare and populate content on the Creativia website (90% done)",
			"annl_gls": "1. Submission of three journal articles with at least two (2) Acceptance.\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-04-25 00:00:00",
			"to_dt": "2022-04-27 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Under Review)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (Under Revision)\r\nTitle 06: Multitasking UAV Surveillance System [Conference]",
			"project_progress": "Title 06: Complete the paper\r\nTitle 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Trying to contact with the Walton company for metaverse collaboration.\r\n\r\n4. Guiding the new comers for the application\r\n\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "Complete Title 01 and 06",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-04-25 00:00:00",
			"to_dt": "2022-04-29 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).\r\n\r\n3. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision).\r\n\r\n4. High-Performance Convolutional Network for RF-based Drone Surveillance Systems (major revision).\r\n\r\n5. Artificial Intelligence for the Metaverse: A Survey - IEEE TAI (under review).",
			"project_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (minor revision).",
			"mnth_gls": "1. IEEE WCNC 2022, Apr. 10-13, Austin, USA (virtual participation).\r\n\r\n2. IEEE ICC 2022, May. 16-20, Seoul, South Korea.",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-04-25 00:00:00",
			"to_dt": "2022-04-29 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Under Review\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE Journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-04-28 00:00:00",
			"to_dt": "2022-05-29 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCSI-2022-01-0010 - IEEE TC.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [2] & [3]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [1]: - (IN-REVISION).\r\n- Review comments anticipating major revision was received on April 17th.\r\n- Revising manuscript according to the received review comments.\r\n- Preparing the manuscript for re-submission soon.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit by end-of-April.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Camera-ready manuscript is finally revised and to be submitted accordingly.\r\n- Conference registration and payment to follow.\r\n\r\n\r\nTitle [7]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 (ACCEPTED April 2022)\r\n\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-04-28 00:00:00",
			"to_dt": "2022-04-29 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)",
			"project_progress": "* BMS 회로 개발\r\n- BMS적용 배터리 모듈 충방전 테스트 재실시",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (시뮬레이션 설계)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-05-02 00:00:00",
			"to_dt": "2022-05-04 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (Under Review).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 85% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\nTitle 1: ICTE-D-21-00585, (under review).\r\nTitle 2: IoT-20662-2021. (under review).\r\nTitle 3: IoT-23106-2022, (Under review).\r\nTitle 4: IoT-23193-2022, (under review).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 10: Access-2022-03435, (Under review: Second Revision).\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Out of scope).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Professors' signature)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. prepare and populate content on the Creativia website (95% done)",
			"annl_gls": "1. Submission of three journal articles with at least one (1) Acceptance.\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-05-02 00:00:00",
			"to_dt": "2022-05-04 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Under Review\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE Journals"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-05-02 00:00:00",
			"to_dt": "2022-05-04 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Under Review)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (Under Revision)\r\nTitle 06: Multitasking UAV Surveillance System [ICUFN Conf.]",
			"project_progress": "Title 06: Completed the paper for ICUFN submission\r\nTitle 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Contacted with MBSTU and IUBAT university for the metaverse collaboration. \r\n4. Guiding the new comers for the application\r\n\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "Complete Title 01 and 06",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-05-02 00:00:00",
			"to_dt": "2022-05-04 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)",
			"project_progress": "* BMS 회로 개발\r\n- 배터리 모듈 충방전 테스트용 Slave BMS 펌웨어 수정\r\n- Master BMS 펌웨어 작성중\r\n- Slave BMS <-> Master BMS 간 CAN통신 프로토콜 정의 및 펌웨어 구현(Slave BMS)",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (논문작성)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-05-02 00:00:00",
			"to_dt": "2022-05-04 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCSI-2022-01-0010 - IEEE TC.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [2] & [3]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [1]: - (IN-REVISION).\r\n- Review comments anticipating major revision was received on April 17th.\r\n- Revising manuscript according to the received review comments.\r\n- Preparing the manuscript for re-submission soon.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit as at when required.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Camera-ready manuscript is finally revised and to be submitted accordingly.\r\n- Conference registration and payment to follow.\r\n\r\n\r\nTitle [7]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 (ACCEPTED April 2022)\r\n\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-05-05 00:00:00",
			"to_dt": "2022-05-06 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (In-Revision).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 85% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 10: Access-2022-03435, (Accepted).\r\nTitle 1: ICTE-D-21-00585, (under review).\r\nTitle 2: IoT-20662-2021. (under review).\r\nTitle 3: IoT-23106-2022, (Under review).\r\nTitle 4: IoT-23193-2022, (under review).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Out of scope).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Professors' signature)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. prepare and populate content on the Creativia website (95% done)\r\n5. Ensure Accepted Access Paper fully Published.",
			"annl_gls": "1. Submission of three journal articles with at least one (1) Acceptance.\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum) (4/18 achieved)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-05-05 00:00:00",
			"to_dt": "2022-05-06 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Under Review\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE Journals"
		},
		{
			"user": "william",
			"fr_dt": "2022-05-05 00:00:00",
			"to_dt": "2022-05-11 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCSI-2022-01-0010 - IEEE TC.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [2] & [3]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [1]: - (REVISION COMPLETED).\r\n- Manuscript has been revised and re-submitted accordingly. \r\n- Awaiting review comments.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit as at when required.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Camera-ready manuscript is finally revised and to be submitted accordingly.\r\n- Conference registration and payment to follow.\r\n\r\n\r\nTitle [7]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 (ACCEPTED April 2022)\r\n\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-05-09 00:00:00",
			"to_dt": "2022-05-11 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Under Review\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journals"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-05-09 00:00:00",
			"to_dt": "2022-05-11 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (In-Revision).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 85% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress)\r\nTitle 6: Language translation project in Metaverse (KICS version completed and submitted) Full Project continues.",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 10: Access-2022-03435, (Accepted).\r\nTitle 1: ICTE-D-21-00585, (under review).\r\nTitle 2: IoT-20662-2021. (under review).\r\nTitle 3: IoT-23106-2022, (Under review).\r\nTitle 4: IoT-23193-2022, (under review).\r\nTitle 5: TPWRS-00183-2022, (Under Review).\r\nTitle 6: ADHOC-D-22-00135, (Under Review).\r\nTitle 7: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 8: COMNET-D-22-00420, (With Editor).\r\nTitle 9: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 11: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 12: ICTE-D-22-00143, (With Editor).\r\nTitle 13: IFS-2022-04-0057, (Out of scope).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Professors' signature)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted Access Paper fully Published. (Early access now online 2022.05.09)",
			"annl_gls": "1. Submission of three journal articles with at least one (1) Acceptance.\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum) (5/18 achieved)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-05-09 00:00:00",
			"to_dt": "2022-05-11 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Under Review)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (Under Revision)\r\nTitle 06: Multitasking UAV Surveillance System [ICUFN Conf.]",
			"project_progress": "Title 06: Completed the paper and submit to the ICUFN \r\nTitle 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Received the confirmation for the research collaboration from MBSTU university. \r\n3. Did not received yet formal consent from IUBAT University.\r\n4. Newly Contacted with WALTON company for the metaverse collaboration.\r\n5. Guiding the new comers for the application\r\n6. Guiding the newcomers (Bangladeshi students) at there research work. \r\n\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "-Complete Title 01 and 02\r\n- Target 06 completed",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-05-09 00:00:00",
			"to_dt": "2022-05-13 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).\r\n\r\n3. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision).\r\n\r\n4. High-Performance Convolutional Network for RF-based Drone Surveillance Systems - IEEE Access (accepted)\r\n\r\n5. Artificial Intelligence for the Metaverse: A Survey - IEEE TAI (under review).",
			"project_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (minor revision).",
			"mnth_gls": "1. IEEE WCNC 2022, Apr. 10-13, Austin, USA (virtual participation).\r\n\r\n2. IEEE ICC 2022, May. 16-20, Seoul, South Korea.",
			"annl_gls": ""
		},
		{
			"user": "B00501",
			"fr_dt": "2022-05-11 00:00:00",
			"to_dt": "2022-05-13 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Under Review\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-05-11 00:00:00",
			"to_dt": "2022-05-13 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)\r\n- KICS 하계학술대회 논문 작성",
			"project_progress": "* BMS 회로 개발\r\n- Master BMS 펌웨어 작성중\r\n- Slave BMS <-> Master BMS 간 CAN통신 프로토콜 정의 및 펌웨어 구현(Slave BMS)",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (논문작성)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-05-12 00:00:00",
			"to_dt": "2022-05-13 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (In-Revision).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 85% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress)\r\nTitle 6: Language translation project in Metaverse (KICS version completed and submitted) Full Project continues.",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435, (Published:10.1109/ACCESS.2022.3173643).\r\nTitle 2: ICTE-D-21-00585, (Major Revision: Deadline 2022.05.27).\r\nTitle 3: ITS-2022-04-0154, (Major Revision due date: 2022.06.11)\r\n\r\n\r\nTitle 4: IoT-23106-2022, (Under review).\r\nTitle 5: IoT-23193-2022, (under review).\r\nTitle 6: TPWRS-00183-2022, (Under Review).\r\nTitle 7: ADHOC-D-22-00135, (Under Review).\r\nTitle 9: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 10: COMNET-D-22-00420, (With Editor).\r\nTitle 11: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 12: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 13: ICTE-D-22-00143, (With Editor).\r\nTitle 14: IFS-2022-04-0057, (Out of scope).\r\nTitle 15: TNSM-2022-05110, (under review)\r\nTitle 16: IoT-20662-2021. (under review).",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Professors' signature)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted Access Paper fully Published. (100%: 10.1109/ACCESS.2022.3173643 2022.05.15)",
			"annl_gls": "1. Submission of three journal articles with at least one (1) Acceptance.\r\n2. 50% increase in the number of NSL graduate students' papers accepted in SCIE journals (Acceptance target of 18 papers minimum) (6/18 achieved)\r\n3. Attracting and Training skilled international graduate students\r\n4. Attend at least one (1) International Conference\r\n5. Achieve at least one (1) International Collaboration (Africa or Nigeria) with ICTCRC."
		},
		{
			"user": "william",
			"fr_dt": "2022-05-12 00:00:00",
			"to_dt": "2022-05-20 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TNSE-2022-05-0628 - IEEE TNSE.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: 16968 (KICS 2022)\r\nTitle 8: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [1], [2], [3] & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit as at when required.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Camera-ready manuscript is finally revised and to be submitted accordingly.\r\n- Conference registration and payment to follow.\r\n\r\nTitle [8]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022]\r\n\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-05-16 00:00:00",
			"to_dt": "2022-05-18 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Reject)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (IEEE Internet of Things Journal) (Accepted)\r\nTitle 06: Multitasking UAV Surveillance System [ICUFN Conf.] (Submit)",
			"project_progress": "Title 05: Transfer final file for publication\r\nTitle 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Received the confirmation for the research collaboration from MBSTU university.\r\n3. Received yet formal consent from IUBAT University.\r\n4. Newly Contacted with WALTON company for the metaverse collaboration.\r\n5. Guiding the new comers for the application\r\n6. Guiding the newcomers (Bangladeshi students) at there research work.\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "-Complete Title 01 and 02\r\n- Target 06 completed",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-05-16 00:00:00",
			"to_dt": "2022-05-18 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (In-Revision).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 95% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress: Stopped for Revision of two journals)\r\nTitle 6: Language translation project in Metaverse (KICS version completed and submitted) Full Project continues.",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435, (Published:10.1109/ACCESS.2022.3173643).\r\nTitle 2: ICTE-D-21-00585, (Major Revision: Deadline 2022.05.27).\r\nTitle 3: ITS-2022-04-0154, (Major Revision due date: 2022.06.11)\r\n\r\n\r\nTitle 4: IoT-23106-2022, (Under review).\r\nTitle 5: IoT-23193-2022, (under review).\r\nTitle 6: TPWRS-00183-2022, (Under Review).\r\nTitle 7: ADHOC-D-22-00135, (Under Review).\r\nTitle 9: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 10: COMNET-D-22-00420, (With Editor).\r\nTitle 11: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 12: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 13: IFS-2022-04-0057, (Out of scope).\r\nTitle 14: TNSM-2022-05110, (under review)\r\nTitle 15: IoT-20662-2021. (under review).",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Professors' signature)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted Access Paper fully Published. (100%: 10.1109/ACCESS.2022.3173643 2022.05.15)",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Professors' signature)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are  fully Published. (4/6 achieved)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-05-16 00:00:00",
			"to_dt": "2022-05-20 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. In Revision\r\n2. Under Review\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journals"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-05-16 00:00:00",
			"to_dt": "2022-05-20 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)\r\n- KICS 하계학술대회 논문 작성 및 제출완료",
			"project_progress": "* BMS 회로 개발\r\n- Master BMS 펌웨어 작성 완료",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (논문작성)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-05-23 00:00:00",
			"to_dt": "2022-05-27 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. Under review (R2)\r\n2. Awaiting Reviewer Scores\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journal"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-05-23 00:00:00",
			"to_dt": "2022-05-27 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Reject)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (IEEE Internet of Things Journal) (Accepted)\r\nTitle 06: Multitasking UAV Surveillance System [ICUFN Conf.] (Submit)\r\nTitle 07: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer](Submit)",
			"project_progress": "Title 05: Transfer Proof read.\r\nTitle 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Received the confirmation for the research collaboration from MBSTU university.\r\n3. Guiding the new comers for the application\r\n4. Guiding the newcomers (Bangladeshi students) at there research work.\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "-Complete Title 01 and 02\r\n- Target 06, 07 completed",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "thienht",
			"fr_dt": "2022-05-23 00:00:00",
			"to_dt": "2022-05-27 00:00:00",
			"paper_progress": "1. MIMO-OFDM Modulation Classification Using Three-Dimensional Convolutional Network - IEEE TVT (accepted)\r\n\r\n2. RanNet: Learning Residual-Attention Structure in CNNs for Automatic Modulation Classification - IEEE Wireless Communications Letters (accepted).\r\n\r\n3. High-Performance Convolutional Network for RF-based Drone Surveillance Systems - IEEE Access (accepted)\r\n\r\n4. Efficient Convolutional Networks for Robust Automatic Modulation Classification in OFDM-Based Wireless Systems - IEEE System Journal (major revision).\r\n\r\n5. Artificial Intelligence for the Metaverse: A Survey - ACM Computing Surveys (under review).",
			"project_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach - IEEE TVT (minor revision).",
			"mnth_gls": "1. IEEE WCNC 2022, Apr. 10-13, Austin, USA (virtual participation).\r\n\r\n2. IEEE ICC 2022, May. 16-20, Seoul, South Korea",
			"annl_gls": ""
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-05-23 00:00:00",
			"to_dt": "2022-05-27 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (In-Revision).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 95% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 60% in progress: Stopped for Revision of two journals)\r\nTitle 6: Language translation project in Metaverse (KICS version completed and submitted) Full Project continues.",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643).\r\nTitle 2: ICTE-D-21-00585,       (Major Revision: Resubmitted 2022.05.20).\r\nTitle 3: ITS-2022-04-0154,      (Major Revision due date: 2022.06.11)\r\nTitle 4: IoT-20662-2021,        (Awaiting Decision).\r\n\r\nTitle 5: IoT-23106-2022, (Under review).\r\nTitle 6: IoT-23193-2022, (under review).\r\nTitle 7: TPWRS-00183-2022, (Under Review).\r\nTitle 8: ADHOC-D-22-00135, (Under Review).\r\nTitle 9: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 10: COMNET-D-22-00420, (With Editor).\r\nTitle 11: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 12: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 13: IFS-2022-04-0057, (Out of scope).\r\nTitle 14: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). ( Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted Access Paper fully Published. (100%: 10.1109/ACCESS.2022.3173643 2022.05.09)",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Professors' signature)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (5/6 achieved)"
		},
		{
			"user": "william",
			"fr_dt": "2022-05-23 00:00:00",
			"to_dt": "2022-05-27 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TNSE-2022-05-0628 - IEEE TNSE.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: 16968 (KICS 2022)\r\nTitle 8: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [1], [2], [3] & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit as at when required.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Camera-ready manuscript is finally revised and to be submitted accordingly.\r\n- Conference registration and payment to follow.\r\n\r\nTitle [8]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022]\r\n\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-05-23 00:00:00",
			"to_dt": "2022-05-27 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)",
			"project_progress": "* BMS 회로 개발\r\n- PyQT활용 모니터링 프로그램 개발중\r\n- Edge Computing 기반 BMS 관련 특허/논문 조사중",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (논문작성)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-05-30 00:00:00",
			"to_dt": "2022-06-03 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. Accepted\r\n2. Awaiting Reviewer Scores\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journal"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-05-30 00:00:00",
			"to_dt": "2022-06-03 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (With Editor).\r\nTitle 2:MEASEN-D-22-00052, (In-Revision).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 95% In progress)\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 65% in progress: Stopped for Revision of two journals)\r\nTitle 6: Language translation project in Metaverse (KICS version completed and submitted) Full Project continues.",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643).\r\nTitle 2: ICTE-D-21-00585, (Major Revision: Resubmitted 2022.05.20).\r\nTitle 3: ITS-2022-04-0154, (Major Revision due date: 2022.06.11)\r\nTitle 4: IoT-20662-2021, (Awaiting Decision).\r\n\r\nTitle 5: IoT-23106-2022, (Under review).\r\nTitle 6: IoT-23193-2022, (under review).\r\nTitle 7: TPWRS-00183-2022, (Under Review).\r\nTitle 8: ADHOC-D-22-00135, (Under Review).\r\nTitle 9: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 10: COMNET-D-22-00420, (With Editor).\r\nTitle 11: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\nTitle 12: ITSM-22-03-0051, (Awaiting Review Score).\r\nTitle 13: TNSM-2022-05110, (under review)",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). ( Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Host the first Metaverse workshop coming up in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted Access Paper fully Published. (100%: 10.1109/ACCESS.2022.3173643 2022.05.09)\r\n6. Resubmit the Major Revision Papers in June 2022",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop in May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (5/6 achieved)"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-05-30 00:00:00",
			"to_dt": "2022-06-03 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)\r\n\r\n* 하향링크 NOMA시스템에서 협력 재전송 전력할당\r\n- ICTC2022제출 위해 시뮬레이션 작성중",
			"project_progress": "* BMS 회로 개발\r\n- PyQT활용 모니터링 프로그램 개발중\r\n- Edge Computing 기반 BMS 관련 특허/논문 조사중",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (논문작성)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-05-30 00:00:00",
			"to_dt": "2022-06-03 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted)\r\nTitle 7: 16968 (KICS 2022)\r\nTitle 8: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n\r\n*IEEE-ETFA 2022, and ICTC 2022 (on-going)",
			"project_progress": "Titles [1], [2], [3] & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit as at when required.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Camera-ready manuscript is finally revised and to be submitted accordingly.\r\n- Conference registration and payment to follow.\r\n\r\nTitle [8]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within April 2022.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021]\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022]\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022]\r\n\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-06-06 00:00:00",
			"to_dt": "2022-06-10 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)",
			"project_progress": "1. Accepted (Final files submitted)\r\n2. Awaiting Reviewer Scores\r\n3. In preparation\r\n4. Draft",
			"mnth_gls": "",
			"annl_gls": "2 SCIE journal"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-06-06 00:00:00",
			"to_dt": "2022-06-10 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, (Under Review).\r\nTitle 2:MEASEN-D-22-00052, (In-Revision).\r\nTitle 3:Sensors-47352-2022, (In-Revision).\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 95% In progress) deadline is 2022.06.17\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 65% in progress: Stopped for Revision of two journals)\r\nTitle 6: Language translation project in Metaverse (KICS version completed and submitted) Full Project continues.",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643).\r\nTitle 2: ICTE-D-21-00585, (Accepted: 2022.06.07).\r\nTitle 3: ITS-2022-04-0154, (Major Revision: Resubmitted: 2022.06.10)\r\nTitle 4: IoT-20662-2021, (Awaiting Decision).\r\n\r\nTitle 5: IoT-23106-2022, (Under review).\r\nTitle 6: IoT-23193-2022, (under review).\r\nTitle 7: TPWRS-00183-2022, (Under Review).\r\nTitle 8: ADHOC-D-22-00135, (Under Review).\r\nTitle 9: T-ITS-22-03-0721, (Awaiting AE Assignment)\r\nTitle 10: COMNET-D-22-00420, (With Editor).\r\nTitle 11: T-ITS-22-03-0723, (Awaiting Reviewer Assignment)\r\n\r\nBushra:\r\n IDSMT-2021-10-0102, Accepted ( Sent final version for publication)",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). ( Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Prepare certificates for speakers and key participants to the Metaverse workshop held  in May 2022 (10%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Resubmit the Major Revision Papers in 2022.06.10\r\n5. Submit and ensure Bushra's paper is published in June 2022",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop in May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (6/7 achieved)"
		},
		{
			"user": "william",
			"fr_dt": "2022-06-06 00:00:00",
			"to_dt": "2022-06-10 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm.\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN.\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw.\r\nTitle 4: Survey works on combat Avionics - IEEE Magazine (on-going)\r\nTitle 5: Low-Power FACTS for SVCs - IEEE Trans. (on-going)\r\nTitle 6: Manuscript ID: 3169 - DASC 2022 (Accepted April 2022)\r\nTitle 7: 16968 - Summer KICS 2022 (Accepted May 2022)\r\nTitle 8: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION)\r\n\r\n\r\n*IEEE-APCC 2022 (on-going)",
			"project_progress": "Titles [1], [2], [3] & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitles [4] & [5]: - (IN-PROGRESS)\r\n- Worked on the system model and block diagrams.\r\n- Simulations and testbed works in progress.\r\n- To finalize and submit as at when required.\r\n\r\nTitle [6]: - (ACCEPTED).\r\n- Camera-ready manuscript is finally revised and to be submitted accordingly.\r\n- Conference registration and payment to follow.\r\n\r\nTitle [8]: - (PATENT APPLICATION).\r\n- Revising Camera-ready patent manuscript.\r\n- Patent application submission to be completed within July 2022.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-06-06 00:00:00",
			"to_dt": "2022-06-10 00:00:00",
			"paper_progress": "* Downlink NOMA 시스템 DNN 활용 전력할당 (Optics express 저널 투고)\r\n- Peer Review\r\n\r\n* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA 연구\r\n- Nash Equilibrium 적용 위한 관련 논문 검토(A game-theoretic Approach for NOMA-ALOHA)\r\n\r\n* 하향링크 NOMA시스템에서 협력 재전송 전력할당\r\n- ICTC2022제출 위해 시뮬레이션 작성중",
			"project_progress": "* BMS 회로 개발\r\n- PyQT활용 모니터링 프로그램 개발중\r\n- Edge Computing 기반 BMS 관련 특허/논문 조사중",
			"mnth_gls": "* URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (논문작성)",
			"annl_gls": "* SCIE 논문 1편 목표\r\n* BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-06-07 00:00:00",
			"to_dt": "2022-06-08 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Reject)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (IEEE Internet of Things Journal) (Accepted)\r\nTitle 06: Multitasking UAV Surveillance System [ICUFN Conf.] (Submit)\r\nTitle 07: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer](Submit)",
			"project_progress": "Title 06: Prepare the camera ready copy and submit the final version.\r\nTitle 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Received the confirmation for the research collaboration from MBSTU university.\r\n3. Guiding the new comers for the application\r\n4. Guiding the newcomers (Bangladeshi students) at there research work.\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "-Complete Title 01 and 02\r\n- Target 06, 07 completed",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-06-09 00:00:00",
			"to_dt": "2022-06-10 00:00:00",
			"paper_progress": "Title 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (Reject)\r\nTitle 05: IoMT-Net: Blockchain Integrated Unauthorized UAV Localization Using Lightweight Convolution Neural Network for Internet of Military Things (IEEE Internet of Things Journal) (Accepted) (IEEE IoT)\r\nTitle 06: Multitasking UAV Surveillance System [ICUFN Conf.] (Accept)\r\nTitle 07: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer](Accept)",
			"project_progress": "Title 06: Prepare the camera ready copy and submit the final version.\r\nTitle 01 is under processing\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Prepare the metaverse collaboration agreement (MOU) and submit to the Prof. Kim.\r\n3. Guiding the new comers for the application\r\n4. Guiding the newcomers (Bangladeshi students) at there research work.\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Under Review)",
			"mnth_gls": "-Complete Title 01 and 02\r\n- Target 06, 07 completed",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-06-13 00:00:00",
			"to_dt": "2022-06-17 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143, \r\nA Review of Thermal Array Sensor-Based Activity Detection in Smart Spaces, ICT Express, \r\n-(Under Review). 100%\r\n\r\nTitle 2: Language Translator Module for Metaverse Virtual Assistant, KICS Summer 2022.\r\n- Accepted.\r\n- Uploaded PPT and Video\r\n- Reservation, Registration, Flight and Bus booking. \r\n\r\nTitle 3: MEASEN-D-22-00052, \r\nModified Random Forest-based Activity Detection using Thermal Sensor Array, Elsevier Measurement journal, (In-Revision). 60%\r\n- working on the review comments to enhance the paper.\r\n- learning the algorithm to improve the performance of the classification. \r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 95% In progress) 85% \r\n~ deadline is 2022.06.30\r\n~ complete the conference version as directed by Professor Kim. \r\n\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 65% in progress: Stopped for Revision of two journals)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435, \r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643).\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585, \r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in Internet of Vehicles, (Accepted: 2022.06.07).\r\nSpecific Action: Submitted Camera ready, LaTeX file, copyright and payment. \r\n\r\nTitle 3: ITS-2022-04-0154, (Major Revision: Resubmitted: 2022.06.10)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems.\r\nSpecific action: Resubmitted revised copy.\r\n\r\nTitle 4: IoT-23106-2022, (under review).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET\r\nSpecific action: \r\n-Paper is under review. \r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102, \r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Accepted \r\nSpecific Action: Sent final version for publication",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Prepare certificates for speakers and key participants to the Metaverse workshop held in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Resubmit the Major Revision Papers in 2022.06.10\r\n5. Submit and ensure Bushra's paper is published in June 2022\r\n6. Upload KICS PPT and Video and Present KICS paper in \"Poster in Metaverse\"",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop in May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (7/8 achieved)\r\n6. First author in 1 SCI journal. Second in numerous"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-06-13 00:00:00",
			"to_dt": "2022-06-17 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n- Accepted\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n- In revision\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- Problem formulation and solution\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)\r\n- Complete draft\r\n\r\n5. KICS Summer Conference\r\n- Preparation for presentation\r\n\r\n6. ICTC Conference\r\n- In preparation",
			"project_progress": "",
			"mnth_gls": "- Complete revision for (2)\r\n- Complete and submit (6)",
			"annl_gls": "2 SCIE journal acceptance\r\n1-2 patent application"
		},
		{
			"user": "jwkim",
			"fr_dt": "2022-06-13 00:00:00",
			"to_dt": "2022-06-17 00:00:00",
			"paper_progress": "1. 함정네트워크 테스트를 위한 트래픽 송수신 SW 구현 논문 준비\r\n2. KICS Summer 논문발표준비(네트워크 시뮬레이션 Survey 주제)\r\n3. ICTC향 딥러닝 관련 논문 준비",
			"project_progress": "1. 강소특구 창업과제 \r\n - 이노폴리스 교육 참가중\r\n - 임베디드 AI 교육 키트 사업화 진행\r\n\r\n2. 특허 \r\n - MDIO 관련 특허 등록",
			"mnth_gls": "1. 컨퍼런스 논문 1편\r\n2. 구현논문 초안 작성",
			"annl_gls": "1. 용역 과제진행\r\n2. 국내논문 2편\r\n3. 소프트웨어 등록,특허출원"
		},
		{
			"user": "william",
			"fr_dt": "2022-06-13 00:00:00",
			"to_dt": "2022-06-17 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%) \r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%) \r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - under review (100%)\r\n \r\nTitle 4: Manuscript ID: 3169 - DASC 2022 (Accepted April 2022) - (100%)\r\n- Camera-ready manuscript is finally revised and submitted accordingly.\r\n- Conference registration and payment is completed.\r\n\r\nTitle 5: 16968 - Summer KICS 2022 (Accepted May 2022) - (100%)\r\n- Camera-ready manuscript is finally revised and submitted accordingly.\r\n- Conference registration and payment is completed.\r\n\r\nTitle 6: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION) - Submitted (100%)\r\n- Awaiting feedbacks on the application results.\r\n\r\nTitle 7: Radar Communication System Recalibration using ML-based Unscented Kalman Filtering Model. IEEE APCC 2022. - (95%)\r\n- Working on simulation, readability and paper formatting.\r\n\r\nTitle 8: Survey works on combat Avionics - IEEE Magazine (on-going) - 70%\r\n- Pending\r\n\r\nTitle 9: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 60%\r\n- Pending",
			"project_progress": "Titles [1], [2], & [3]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [4] & [5]: - (ACCEPTED).\r\n- Making PPT slide for KICS conference attendance next week (20%)\r\n\r\nTitle [6]: - (PATENT APPLICATION).\r\n- Final Patent application submission to be completed.\r\n\r\nTitles [7]: - (IN-PROGRESS)\r\n- Simulations and testbed works in progress (100%).\r\n- To finalize and submit end of today.\r\n\r\nTitles [8] & [9]: - (IN-PROGRESS)\r\n- Pending\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-06-13 00:00:00",
			"to_dt": "2022-06-17 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\n    o Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Preparing\r\n    - Making simulation (100%) \r\n        (i) Next week: Writing an abstract\r\n\r\n    o Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n     - Pending",
			"project_progress": "o 차주 화요일 BMS개발 관련 벡셀 미팅 참석 예정\r\n      - CAN프로토콜 등 확인",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\n    o BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-06-16 00:00:00",
			"to_dt": "2022-06-17 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Accept)\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Accept)\r\n\r\nPaper in Progress (First Author)\r\nTitle 01: Undersea Acoustic Target Detection Using CNN. [IEEE TII]\r\nTitle 02: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access]\r\nTitle 03: Vision-based Drone Surveillance System Using CNN. [TVT]\r\nTitle 04: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT)",
			"project_progress": "Paper 03: Preparing the PPT for KICS presentation.\r\nTitle 01:\r\n-Performed Three simulations and plot graphs.\r\n-Complete the proposed DL model section.\r\n-Continue to write the Simulation work and writing the Result discussion section.\r\n1. Continue the survey about the integration of deep-learning in metaverse platform. (Metaverse survey paper).\r\n2. Prepare the metaverse collaboration agreement (MOU) and communicating with the Bangladeshi two universities.\r\n3. Waiting for there response.\r\n3. Guiding the new comers in application\r\n4. Guiding the newcomers (Bangladeshi students) at there research work.\r\n\r\nCo-Author Paper:\r\nTitle 1: DNN for DDoS Attack Detection and Classification [IEE-TNSM]\r\nTitle 2: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Major revision) (IEEEIOT Journal)\r\n- Received major revision and discussed the reviewer comments to my co-author.\r\n- Try to complete first reviewer comments in this week.\r\nTitle 3:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022)\r\n- Write ML part in the introduction section",
			"mnth_gls": "-Complete Title 01 and submit to the journal (Almost 70% task complete)\r\n- Target 06, 07 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Title 3 paper and submit to the MILCOM conference",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 03 and 04\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received one acceptance from IEEE IoT journal]"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-06-17 00:00:00",
			"to_dt": "2022-06-23 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Cooperation Task offloading in fog computing system, IEEE Transaction on Parallel and Distributed System, (Under Review)\r\n2. Matching theory for distributed computation in IoT-FOg-CLoud system, IEEE transaction on Parallel and Distributed System, (Under review)\r\n3. 28 GHZ 5G Test Bed, IEEE Transaction on Education (In progress (75%).\r\n4. DISCO: Distributed computation offloading in fog networks, IEEE IoT journal, (In progress, 70%)",
			"project_progress": "",
			"mnth_gls": "- Successfully submit paper 4.\r\n-Finish paper 4\r\n-Decision result on Paper 1",
			"annl_gls": "-4 SCI/E Accepted Journals\r\n-1 Published patent"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-06-20 00:00:00",
			"to_dt": "2022-06-22 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143,\r\nA Review of Thermal Array Sensor-Based Activity Detection in Smart Spaces, ICT Express,\r\n-(Under Review). 100%\r\n\r\nTitle 2: Language Translator Module for Metaverse Virtual Assistant, KICS Summer 2022.\r\n- Accepted.\r\n- Uploaded PPT and Video\r\n- Reservation, Registration, Flight and Bus booking.\r\n- Attend and present paper at Poster in Metaverse (Gather town)\r\n\r\nTitle 3: MEASEN-D-22-00052,\r\nModified Random Forest-based Activity Detection using Thermal Sensor Array, Elsevier Measurement journal, (In-Revision). 60%\r\n- working on the review comments to enhance the paper.\r\n- learning the algorithm to improve the performance of the classification.\r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 95% In progress) 85%\r\n~ deadline is 2022.06.30\r\n~ complete the conference version as directed by Professor Kim.\r\n\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 65% in progress: Stopped for Revision of two journals)",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera ready, LaTeX file, copyright and payment.\r\n- Paper now online on 2022.06.19\r\n\r\nTitle 3: ITS-2022-04-0154, (Major Revision: Resubmitted: 2022.06.10)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted revised copy.\r\n\r\nTitle 4: IoT-23106-2022, (under review).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-Paper is under review.\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted : 2022.06.21\r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102,\r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Accepted\r\nSpecific Action: \r\n- Sent final version for publication",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Prepare certificates for speakers and key participants to the Metaverse workshop held in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Resubmit the Major Revision Papers in 2022.06.10\r\n5. Submit and ensure Bushra's paper is published in June 2022\r\n6. Upload KICS PPT and Video and Present KICS paper in \"Poster in Metaverse\"\r\n7. Ensure ICT Express accepted paper is published.",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop in May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (7/18 achieved)\r\n6. First author in 1 SCI journal. Second in numerous"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-06-20 00:00:00",
			"to_dt": "2022-06-22 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n- Accepted\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n- In revision\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- Problem formulation and solution\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)\r\n- Complete draft\r\n\r\n5. KICS Summer Conference\r\n- Preparation for presentation\r\n\r\n6. ICTC Conference\r\n- In preparation",
			"project_progress": "",
			"mnth_gls": "- Complete revision for (2)\r\n- Complete (6)",
			"annl_gls": "2 SCIE journal acceptance\r\n1-2 patent application"
		},
		{
			"user": "jwkim",
			"fr_dt": "2022-06-20 00:00:00",
			"to_dt": "2022-06-21 00:00:00",
			"paper_progress": "o 함정네트워크 테스트를 위한 트래픽 송수신 SW 구현 논문 준비\r\no KICS Summer 논문발표준비\r\no ICTC향 딥러닝 관련 논문 준비",
			"project_progress": "o 강소특구 창업과제 \r\n - 이노폴리스 교육 참가중\r\n - 임베디드 AI 교육 키트 사업화 진행\r\n\r\no 특허 \r\n - HIL 관련 특허출원 준비",
			"mnth_gls": "o 컨퍼런스 논문 1편\r\no 구현논문 논문 초안준비",
			"annl_gls": "o 용역 과제진행\r\no 국내논문 2편\r\no 소프트웨어 등록,특허출원"
		},
		{
			"user": "william",
			"fr_dt": "2022-06-20 00:00:00",
			"to_dt": "2022-06-22 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%)\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - under review (100%)\r\nTitle 4: Manuscript ID: 3169 - DASC 2022 (Accepted April 2022) - (100%)\r\n\r\nTitle 5: 16968 - Summer KICS 2022 (Accepted May 2022) - (100%)\r\n- Prepared PPT slides and video presentations for the conference.\r\n- To attend KICS conference from 2022.06.22 to 2022.06.24.\r\n\r\nTitle 6: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION) - Submitted (100%)\r\n- Awaiting feedbacks on the application results.\r\n\r\nTitle 7: Radar Communication System Recalibration using ML-based Unscented Kalman Filtering Model. IEEE APCC 2022. - (100%)\r\n- Paper was successfully submitted and is awaiting review comments.\r\n\r\nTitle 8: Survey works on combat Avionics - IEEE Magazine (on-going) - 70%\r\n- Pending\r\n\r\nTitle 9: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 60%\r\n- Pending",
			"project_progress": "Titles [1], [2], [3], & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [4] & [5]: - (ACCEPTED).\r\n- Prepared PPT slides and video presentations for KICS conference (100%).\r\n- To attend KICS conference from 2022.06.22 to 2022.06.24.\r\n\r\nTitle [6]: - (PATENT APPLICATION).\r\n- Decision is now awaited.\r\n\r\nTitles [8] & [9]: - (IN-PROGRESS)\r\n- Pended/suspended due to works on [5], [6] and [7].\r\n- To continue after attending KICS conference.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-06-20 00:00:00",
			"to_dt": "2022-06-21 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\n\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Accept) [100%]\r\n- Next week I will prepare presentation slide to attend the Conference.\r\n\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Accept) [100%]\r\n- Last week I prepared the presentation slide to attend the KICS conference.\r\n-This week preparing to attend the conference from 2022/06/22 to 2022/06/24.\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [70%] (In progress)\r\n- Last week I performed  six simulations to justify the network configuration.\r\n- Draw figure 4, 5, 6, and 7 and listed into the current manuscript.\r\n- This week, I am doing simulation to compare the performance with existing model.\r\n- Include the results into the paper.\r\n- Complete the simulation result and discussion section.\r\n\r\nPaper 05: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [90%]\r\n-After the completion of title 04, I will update this paper and submit the journal.\r\n\r\nPaper 06: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 07: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Major revision) (IEEEIOT Journal)\r\n- Two comments of the second reviewer is done.\r\n- Compiling the comments.\r\n- This week I will add more information and recheck the two comments again.\r\n \r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [50%] (In progress)\r\n- Last week write ML part in the introduction section.\r\n- This week complete the system model section.",
			"mnth_gls": "-Complete paper 04 and submit to the journal (Almost 70% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10\r\n- submit paper 10 to the MILCOM conference",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received one acceptance from IEEE IoT journal]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-06-20 00:00:00",
			"to_dt": "2022-06-21 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Preparing\r\n- Writing an abstract(100%)\r\n(i) Next week: Writing Section II, System model\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o BMS개발 관련 벡셀 미팅 참석(06.21)\r\n- 전기차 충전기용 표준 통신프로토콜 논의",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-06-27 00:00:00",
			"to_dt": "2022-06-29 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143,\r\nA Review of Thermal Array Sensor-Based Activity Detection in Smart Spaces, ICT Express.  100%\r\n-(Under Review).\r\n\r\nTitle 2: Language Translator Module for Metaverse Virtual Assistant, KICS Summer 2022. 100%\r\n- Accepted.\r\n- Uploaded PPT and Video\r\n- Reservation, Registration, Flight and Bus booking.\r\n- Attend and present paper at Poster in Metaverse (Gather town)\r\n-Submitted conference report and now waiting for publication on DBpia\r\n\r\nTitle 3: MEASEN-D-22-00052,\r\nModified Random Forest-based Activity Detection using Thermal Sensor Array, Elsevier Measurement journal, (In-Revision). 60%\r\n- working on the review comments to enhance the paper.\r\n- learning the algorithm to improve the performance of the classification.\r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 95% In progress) 85%\r\n~ deadline is 2022.06.30\r\n~ complete the conference version as directed by Professor Kim.\r\n\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 65% in progress: Stopped for Revision of two journals",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera ready, LaTeX file, copyright and payment.\r\n- Paper now online on 2022.06.19\r\n- Pre-proof on-going \r\n\r\nTitle 3: ITS-2022-04-0154, (Major Revision: Resubmitted: 2022.06.10)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted revised copy.\r\n\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to review is well articulated and ready for submission 2022.07.28.\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted : 2022.06.21\r\n-Under review\r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102,\r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Accepted\r\nSpecific Action:\r\n- Sent final version for publication\r\n- created Bushra on Willey and managing the pre-proof mails.",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Prepare certificates for speakers and key participants to the Metaverse workshop held in May 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Resubmit the IET-ITS Major Revision Paper in 2022.06.10 (100%)\r\n5. Submit and ensure Bushra's paper is published in June 2022\r\n6. Upload KICS PPT and Video and Present KICS paper in \"Poster in Metaverse\"\r\n7. Ensure ICT Express accepted paper is published.\r\n8. Ensure a resubmission of the revisions (Access and Ad-hoc papers) are resubmitted",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop in May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (8/18 achieved)\r\n6. First author in 1 SCI journal. \r\n7. Second author in numerous SCI papers of NSL."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-06-27 00:00:00",
			"to_dt": "2022-06-29 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n- Accepted\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n- In revision\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- Problem formulation and solution\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)\r\n- Complete draft\r\n\r\n5. ICTC Conference\r\n- In preparation",
			"project_progress": "",
			"mnth_gls": "- Complete revision for (2)\r\n- Complete (6)",
			"annl_gls": "2 SCIE journal acceptance\r\n1-2 patent application"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-06-27 00:00:00",
			"to_dt": "2022-06-29 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Writing (40%)\r\n- Writing a section, System Model(100%)\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 윌리엄 특허 번역 작업",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-06-27 00:00:00",
			"to_dt": "2022-06-29 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%)\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - under review (100%)\r\nTitle 4: Manuscript ID: 3169 - DASC 2022 (Accepted April 2022) - (100%)\r\n\r\nTitle 5: 16968 - Summer KICS 2022 (Accepted May 2022) - (100%)\r\n- Attended KICS conference from 2022.06.22 to 2022.06.24.\r\n- Prepared and submitted KICS reports.\r\n\r\nTitle 6: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION) - Submitted (100%)\r\n- Awaiting feedbacks on the application results.\r\n\r\nTitle 7: Radar Communication System Recalibration using ML-based Unscented Kalman Filtering Model. IEEE APCC 2022. - (100%)\r\n- Paper was successfully submitted and is awaiting review comments.\r\n\r\nTitle 8: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 70%\r\n- THIS WEEK: Problem formulation and System model.\r\n- NEXT WEEK: System model and results.\r\n\r\nTitle 9:Survey works on combat Avionics - IEEE Magazine (on-going) - 60%\r\n- Pending",
			"project_progress": "Titles [1], [2], [3], & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [4] & [5]: - (ACCEPTED).\r\n- Awaiting publications.\r\n\r\nTitle [6]: - (PATENT APPLICATION - SUBMITTED).\r\n- Awaiting decision.\r\n\r\nTitles [8]: - (IN-PROGRESS)\r\n- THIS WEEK: Problem formulation and System model.\r\n- NEXT WEEK: System model and results.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2022-06-27 00:00:00",
			"to_dt": "2022-07-01 00:00:00",
			"paper_progress": "o 함정네트워크 테스트를 위한 트래픽 송수신 SW 구현 논문 준비\r\no ICTC 논문 (딥러닝 관련 논문 -> 중복게재 위험으로 주제 변경 필요)\r\no ICMIC 논문 준비",
			"project_progress": "o 강소특구 창업과제 (사업화 과제)\r\n- 이노폴리스 교육 BM모델\r\n- 임베디드 AI 교육 키트 사업화 진행",
			"mnth_gls": "o 컨퍼런스 논문 1편\r\no 구현논문 논문 초안준비",
			"annl_gls": "o 용역 과제진행\r\no 국내논문 2편\r\no 소프트웨어 등록,특허출원"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-06-27 00:00:00",
			"to_dt": "2022-07-01 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\n\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Accept) [100%]\r\n- Next week I will prepare presentation slide to attend the Conference.\r\n\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Accept) [100%]\r\n- Last week I attend the KICS conference.\r\n-Business trip from 2022/06/22 to 2022/06/24.\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [75%] (In progress)\r\n- Last week I calculated MFLOPs for various configuration of my proposed CNN model .\r\n- Perform two more simulation works.\r\n- This week, I will complete 50% of the simulation work.\r\nPaper 05: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [90%]\r\n-After the completion of title 04, I will update this paper and submit the journal.\r\n\r\nPaper 06: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 07: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Major revision) (IEEEIOT Journal)\r\n- Two comments of the second reviewer is done.\r\n- Compiling the comments.\r\n- This week I will add more information and recheck the two comments again.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [50%] (In progress)\r\n- Last week write ML part in the introduction section.\r\n- This week complete the system model section.",
			"mnth_gls": "-Complete paper 04 and submit to the journal (Almost 70% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10\r\n- submit paper 10 to the MILCOM conference",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received one acceptance from IEEE IoT journal]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-06-29 00:00:00",
			"to_dt": "2022-07-01 00:00:00",
			"paper_progress": "1. Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing: A Game-Theoretic Approach (IEEE Transactions on Vehicular Technology)\r\n- Accepted\r\n\r\n2. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consumer Electronics Magazine)\r\n- Complete revision.\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- Problem formulation and solution\r\n\r\n4. Method of Partial Computation Offloading in Parked Vehicle-assisted Multi-access Edge Computing (Patent)\r\n- Complete draft\r\n\r\n5. ICTC Conference\r\n- Final edit and about to submit.",
			"project_progress": "",
			"mnth_gls": "- Performance evaluation for (3)\r\n- Patent application",
			"annl_gls": "2 SCIE journal acceptance\r\n1-2 patent application"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-06-30 00:00:00",
			"to_dt": "2022-07-01 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143,\r\nA Review of Thermal Array Sensor-Based Activity Detection in Smart Spaces, ICT Express. 100%\r\n-(Under Review).\r\n\r\nTitle 2: Language Translator Module for Metaverse Virtual Assistant, KICS Summer 2022. 100%\r\n- Accepted and presented paper at Poster in Metaverse (Gather town)\r\n-Submitted conference report and now waiting for publication on DBpia\r\n\r\nTitle 3: ICMIC 2022,\r\n50%\r\n- working on the review of related works and trying to identify clear objectives.\r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100% \r\n~ completed paper on 2022.06.30\r\n~ Ready to submit once approved by Professor Kim.\r\n\r\nTitle 5: Vulnerability Analysis and Detection in IIoT( 65% in progress: Stopped for Revision of three journal papers",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera ready, LaTeX file, copyright and payment.\r\n- Paper now online on 2022.06.19\r\n- Proof copy submitted 2022.07.01\r\n\r\nTitle 3: ITS-2022-04-0154, (Major Revision: Resubmitted: 2022.06.10)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted revised copy.\r\n\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to review is well articulated and ready for submission 2022.07.28.\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted : 2022.06.21\r\n-Under review\r\n\r\nTitle 6: IoT-23106-2022, (Major Revision)\r\n-To resubmit on 2022.07.22\r\n- Rerunning simulations to address review comments.\r\n- Enhancing paper readability and English errors.\r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102,\r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Accepted\r\n\r\nSpecific Action:\r\n- Sent final version for publication\r\n- created Bushra on Willey \r\n- Proof copy submitted 2022.06.30.",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n3. Submit and ensure Bushra's paper is published in July 2022\r\n4. Complete and submit ICMIC and ICTC 2022\r\n5. Ensure ICT Express accepted paper is published.\r\n6. Ensure a resubmission of the revisions (Access, IEEE IoT, and Ad-hoc Networks papers) are resubmitted 2022.07.22\r\n7. Conclude the KOREA-Israel Collaboration proposal\r\n8. Submit one Journal as first author  2022.07.29",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop in May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (8/18 achieved)\r\n6. First author in 1 SCI journal.\r\n7. Second author in numerous SCI papers of NSL.\r\n8. Secure Korea-Israel Project proposal"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-06-30 00:00:00",
			"to_dt": "2022-07-01 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Writing (60%)\r\n- Writing a section, System Model(100%), Proposed Method(100%)\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 특허작성\r\n- IoT통신을 연동한 화장실 전원 사용 여부를 통한 거동불편 독거인 상태 파악 유추 방법(작성중, 10%)\r\n\r\no BMS회로 개발 관련 차주 출장(07.06 수요일 오전 10:00~12:00)\r\n- 전기차 충방전기 연동 관련 BMS 인터페이스 협의, (장소: 대구 (주)누리기술)",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-06-30 00:00:00",
			"to_dt": "2022-07-01 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%)\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - under review (100%)\r\nTitle 4: Manuscript ID: 3169 - DASC 2022 (Accepted April 2022) - (100%)\r\n\r\nTitle 5: 16968 - Summer KICS 2022 (Accepted May 2022) - (100%)\r\n- Attended KICS conference from 2022.06.22 to 2022.06.24.\r\n- Prepared and submitted KICS reports.\r\n\r\nTitle 6: Time-Frequency based Physical Resource Block (PRB) Sensors for Indoor Radio Frequency Channel Beamforming (Q1: PATENT APPLICATION) - Submitted (100%)\r\n- Awaiting feedbacks on the application results.\r\n\r\nTitle 7: Radar Communication System Recalibration using ML-based Unscented Kalman Filtering Model. IEEE APCC 2022. - (100%)\r\n- Paper was successfully submitted and is awaiting review comments.\r\n\r\nTitle 8: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 70%\r\n THIS WEEK: \r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- readability was enhanced.\r\n NEXT WEEK: \r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\nTitle 9:Survey works on combat Avionics - IEEE Magazine (on-going) - 60%\r\n- Pending",
			"project_progress": "Titles [1], [2], [3], & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [4] & [5]: - (ACCEPTED).\r\n- Awaiting publications.\r\n\r\nTitle [6]: - (PATENT APPLICATION - SUBMITTED).\r\n- Awaiting decision.\r\n\r\nTitles [8]: - (IN-PROGRESS)\r\n- THIS WEEK: Problem formulation and System model.\r\n- NEXT WEEK: System model and results.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-04 00:00:00",
			"to_dt": "2022-07-06 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Submit Minor Revision\r\n\r\n2. Distributed Cloud Computing - A Cloud Computing and Networking Perspective (IEEE Commun. Mag.)\r\n- In-progress (40%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (40%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Co-author: \r\nArtificial Intelligence for the Metaverse: A Survey (Revised)",
			"mnth_gls": "- Decision on paper 1\r\n- Finish draft for paper 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to some conferences"
		},
		{
			"user": "william",
			"fr_dt": "2022-07-04 00:00:00",
			"to_dt": "2022-07-06 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%)\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - under review (100%)\r\nTitle 4: Manuscript ID:3169 - IEEE/AIAA DASC 2022 (Accepted April 2022) - (100%)\r\nTitle 5: Manuscript ID:16968 - Summer KICS 2022 (Accepted May 2022) - (100%)\r\nTitle 6: PATENT APPLICATION (Q1) - under review (100%)\r\nTitle 7: Manuscript ID:#63 (1570820804) IEEE APCC 2022. - under review (100%)\r\n\r\nTitle 8: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 75%\r\nTHIS WEEK:\r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK:\r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\nTitle 9:Survey works on combat Avionics - IEEE Magazine (on-going) - 60%\r\n- Pending",
			"project_progress": "Titles [1], [2], [3], & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitle [4] & [5]: - (ACCEPTED).\r\n- Awaiting online repository publications.\r\n\r\nTitle [6]: - (PATENT APPLICATION - SUBMITTED).\r\n- Awaiting decision.\r\n\r\nTitles [8]: - (IN-PROGRESS)\r\nTHIS WEEK: \r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK: \r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-07-04 00:00:00",
			"to_dt": "2022-07-06 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Writing (70%)\r\n- Writing a section, Problem Formulation (30%)\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 특허작성\r\n- IoT통신을 연동한 화장실 전원 사용 여부를 통한 거동불편 독거인 상태 파악 유추 방법(작성중, 10%)",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-07-04 00:00:00",
			"to_dt": "2022-07-08 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143,\r\nA Review of Thermal Array Sensor-Based Activity Detection in Smart Spaces, ICT Express. 100%\r\n-(Under Review).\r\n\r\nTitle 2: Language Translator Module for Metaverse Virtual Assistant, KICS Summer 2022. 100%\r\n-Submitted conference report and now waiting for publication on DBpia\r\n\r\nTitle 3: ICMIC 2022,\r\n50%\r\n- working on the review of related works and trying to identify clear objectives.\r\n- brainstorm with Professor Kim and Nigerian group. \r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ completed paper on 2022.06.30\r\n~ Ready to submit once approved by Professor Kim.\r\n\r\nTitle 5: Metafrika: Paper on Metaverse for Africa (10%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for idea and main area of direction",
			"project_progress": "Second Authored works in NSL and ICTCRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera ready, LaTeX file, copyright and payment.\r\n- Paper now online on 2022.06.19\r\n- Proof copy submitted 2022.07.01\r\n- Proff copy online 2022.07.06\r\n\r\nTitle 3: ITS-2022-04-0154, (ACCEPPTED: 2022.07.05)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted Camera-ready copy.\r\n\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to review is well articulated and ready for submission 2022.07.28.\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted : 2022.06.21\r\n-Under review\r\n\r\nTitle 6: IoT-23106-2022, (Major Revision)\r\n-To resubmit on 2022.07.22\r\n- Rerunning simulations to address review comments.\r\n- Enhancing paper readability and English errors.\r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102,\r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Accepted\r\n\r\nSpecific Action:\r\n- Sent final version for publication\r\n- created Bushra on Willey\r\n- Proof copy submitted 2022.06.30.",
			"mnth_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Benson Idahosa University and University of Ilorin Signed. Waiting for Babcock University)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n3. Submit and ensure Bushra's paper is published in July 2022\r\n4. Complete and submit ICMIC and ICTC 2022 - (50%)\r\n5. Ensure ICT Express accepted paper is published - (100%)\r\n6. Ensure a resubmission of the revisions (Access, IEEE IoT, and Ad-hoc Networks papers) are resubmitted 2022.07.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal- (60%)\r\n8. Submit one Journal as first author 2022.07.29 - (20%)\r\n9. Submit IET-Intelligent Transportation System Camera-ready copy-  (100%)",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop in May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (9/18 achieved)\r\n6. First author in 1 SCI journal.\r\n7. Second author in numerous SCI papers of NSL.\r\n8. Secure Korea-Israel Project proposal"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-06 00:00:00",
			"to_dt": "2022-07-08 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Awaiting Reviewer Scores (Minor Revision)\r\n\r\n2. Distributed Cloud Computing - A Cloud Computing and Networking Perspective (IEEE Commun. Mag.)\r\n- In-progress (45%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (40%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Co-author:\r\nArtificial Intelligence for the Metaverse: A Survey (Revised)",
			"mnth_gls": "- Decision on paper 1\r\n- Finish draft for paper 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to some conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-07-07 00:00:00",
			"to_dt": "2022-07-08 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Writing (80%)\r\n- Writing a section, Problem Formulation (100%)\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 특허작성\r\n- IoT통신을 연동한 화장실 전원 사용 여부를 통한 거동불편 독거인 상태 파악 유추 방법(작성중, 10%)",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "william",
			"fr_dt": "2022-07-07 00:00:00",
			"to_dt": "2022-07-13 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%)\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - currently under revision/re-submission (10%)\r\nTitle 4: Manuscript ID:3169 - IEEE/AIAA DASC 2022 (Accepted April 2022) - (100%)\r\nTitle 5: Manuscript ID:16968 - Summer KICS 2022 (Accepted May 2022) - (100%)\r\nTitle 6: PATENT APPLICATION (Q1) - under review (100%)\r\nTitle 7: Manuscript ID:#63 (1570820804) IEEE APCC 2022. - under review (100%)\r\n\r\nTitle 8: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 75%\r\nTHIS WEEK:\r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK:\r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\nTitle 9:Survey works on combat Avionics - IEEE Magazine (on-going) - 60%\r\n- Pending",
			"project_progress": "Titles [1], [2] & [7]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitles [3]: - (REVIEW COMMENTS RECIEVED).\r\n- Reworking manuscript according to comments (10%).\r\n\r\nTitle [4] & [5]: - (ACCEPTED).\r\n- Awaiting online repository publications.\r\n\r\nTitle [6]: - (PATENT APPLICATION - SUBMITTED).\r\n- Awaiting decision.\r\n\r\nTitles [8]: - (IN-PROGRESS)\r\nTHIS WEEK:\r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK:\r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-11 00:00:00",
			"to_dt": "2022-07-13 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Accepted - Preparing Final Files\r\n\r\n2. Distributed Cloud Computing - A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (45%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (40%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (Submitted)",
			"mnth_gls": "- Finish draft for paper 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to some conferences"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-07-11 00:00:00",
			"to_dt": "2022-07-13 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143,\r\nA Review of Thermal Array Sensor-Based Activity Detection in Smart Spaces, ICT Express. 100%\r\n-(Under Review).\r\n\r\nTitle 2: Language Translator Module for Metaverse Virtual Assistant, KICS Summer 2022. 100%\r\n-Submitted conference report and now waiting for publication on DBpia\r\n\r\nTitle 3: ICMIC 2022,\r\n50%\r\n- working on the review of related works and trying to identify clear objectives.\r\n- brainstorm with Professor Kim and the Nigerian group.\r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ completed paper on 2022.06.30\r\n~ Ready to submit once approved by Professor Kim.\r\n\r\nTitle 5: Metafrika: Paper on Metaverse for Africa (10%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for the idea and main area of direction",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in the Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera-ready, LaTeX file, copyright, and payment.\r\n- Paper now online on 2022.06.19\r\n- Proof copy submitted 2022.07.01\r\n- Proof copy online 2022.07.06\r\n\r\nTitle 3: ITS-2022-04-0154, (ACCEPTED: 2022.07.05)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted Camera-ready copy and update Professor on Wiley Author platform. 100%\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to the review is well articulated and ready for submission 2022.07.28.\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted: 2022.06.21\r\n-Under review\r\n\r\nTitle 6: IoT-23106-2022, (Major Revision)\r\n-To resubmit on 2022.07.22\r\n- Rerunning simulations to address review comments.\r\n- Enhancing paper readability and English errors.\r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102,\r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Accepted\r\n\r\nSpecific Action:\r\n- Sent final version for publication\r\n- created Bushra on Willey\r\n- Proof copy submitted 2022.06.30.\r\n- paper paid today 2022.07.13",
			"mnth_gls": "1. Conclude the MOU with Nigerian Universities (100%). (Benson Idahosa University and the University of Ilorin Signed.)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n3. Submit and ensure Bushra and Saviour's paper is published in July 2022\r\n4. Complete and submit ICMIC and ICTC 2022 - (50%)\r\n5. Ensure ICT Express accepted paper is published - (100%)\r\n6. Ensure a resubmission of the revisions (Access, IEEE IoT, and Ad-hoc Networks papers) are resubmitted 2022.07.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal- (60%)\r\n8. Submit one Journal as first author 2022.07.29 - (50%)\r\n9. Submit IET-Intelligent Transportation System Camera-ready copy- (100%)",
			"annl_gls": "1. Conclude the MOU with three Nigerian Universities (95%). (Waiting for Babcock University and Professors' signature)\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (60%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (9/18 achieved)\r\n6. First author in 1 SCI journal.\r\n7. Second author in numerous SCI papers of NSL.\r\n8. Secure Korea-Israel Project proposal"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-07-11 00:00:00",
			"to_dt": "2022-07-13 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Writing (90%)\r\n- Simulation section(100%), Conclusion(100%), Introduction(20%)\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-13 00:00:00",
			"to_dt": "2022-07-15 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Accepted - Final Files Submitted\r\n\r\n2. Distributed Cloud Computing - A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (50%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (40%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (ACM CSUR)\r\n- Under review",
			"mnth_gls": "- Finish draft for 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to some conferences"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-07-14 00:00:00",
			"to_dt": "2022-07-15 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143  ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: KICS Summer 2022. 100%\r\n-Submitted conference report and now waiting for publication on DBpia\r\n\r\nTitle 3: ICMIC 2022,\r\n50%\r\n- working on the review of related works and trying to identify clear objectives.\r\n- Brainstorm with Professor Kim and the Nigerian group.\r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ completed paper on 2022.06.30\r\n~ Enhancing readability to upload paper on EDAS 2022.08.20.\r\n\r\nTitle 5: Metafrika: Paper on Metaverse for Africa (15%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for the idea and main area of direction",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in the Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera-ready, LaTeX file, copyright, and payment.\r\n- Paper now online on 2022.06.19\r\n- Proof copy submitted 2022.07.01\r\n- Proof copy online 2022.07.06\r\n\r\nTitle 3: ITS-2022-04-0154, (ACCEPTED: 2022.07.05)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted Camera-ready copy and update Professor on Wiley Author platform. 100%\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to the review is well articulated and ready for submission 2022.07.28.\r\n- Camera-Ready copy uploaded 2022.07.12\r\n- Write a letter to Author support to resolve submission issues.\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted: 2022.06.21\r\n-Under review\r\n\r\nTitle 6: IoT-23106-2022, (Major Revision)\r\n-To resubmit on 2022.07.22\r\n- Rerunning simulations to address review comments.\r\n- Enhancing paper readability and English errors.\r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102,\r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Accepted\r\n\r\nSpecific Action:\r\n- Sent final version for publication\r\n- created Bushra on Willey\r\n- Proof copy submitted 2022.06.30.\r\n- paper paid today 2022.07.13",
			"mnth_gls": "1. Conclude the MOU with Nigerian Universities (100%). (Benson Idahosa University and the University of Ilorin Signed.)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (70%).\r\n3. Submit and ensure Bushra and Saviour's papers are published in July 2022\r\n4. Complete and submit ICMIC and ICTC 2022 - (50%)\r\n5. Ensure ICT Express accepted paper is published - (100%)\r\n6. Ensure a resubmission of the revisions (Access, IEEE IoT, and Ad-hoc Networks papers) are resubmitted 2022.07.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal- (65%)\r\n8. Submit one Journal as first author 2022.07.29 - (50%)\r\n9. Submit IET-Intelligent Transportation System Camera-ready copy- (100%)",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%). \r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (65%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (10/18 achieved)\r\n6. First author in 1 SCI journal.\r\n7. Second author in numerous SCI papers of NSL (3 Achieved).\r\n8. Secure Korea-Israel Project proposal (65%)."
		},
		{
			"user": "william",
			"fr_dt": "2022-07-14 00:00:00",
			"to_dt": "2022-07-15 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%)\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - currently under revision/re-submission (10%)\r\nTitle 4: Manuscript ID:3169 - IEEE/AIAA DASC 2022 (Accepted April 2022) - (100%)\r\nTitle 5: PATENT APPLICATION (Q1) - under review (100%)\r\nTitle 6: Manuscript ID:#63 (1570820804) IEEE APCC 2022. - under review (100%)\r\n\r\nTitle 7: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 80%\r\nTHIS WEEK:\r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK:\r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\nTitle 8:Survey works on combat Avionics - IEEE Magazine (on-going) - 60%\r\n- Pending",
			"project_progress": "Titles [1], [2] & [6]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitles [3]: - (REVIEW COMMENTS RECIEVED).\r\n- Reworking manuscript according to comments (10%).\r\n\r\nTitle [4] - (ACCEPTED).\r\n- Awaiting online repository publications.\r\n\r\nTitles [7]: - (IN-PROGRESS)\r\nTHIS WEEK:\r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK:\r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "jwkim",
			"fr_dt": "2022-07-15 00:00:00",
			"to_dt": "2022-07-21 00:00:00",
			"paper_progress": "o 함정네트워크 테스트를 위한 트래픽 송수신 SW 구현 논문 준비\r\no ICTC 논문 (딥러닝 관련 논문 -> 중복게재 위험으로 주제 변경 필요)\r\no ICMIC 논문 준비 (번역진행)",
			"project_progress": "o 강소특구 창업과제 (사업화 과제)\r\n- 이노폴리스 교육 BM모델\r\n- 임베디드 AI 교육 키트 사업화 진행\r\n\r\no 특허 \r\n - HIL 관련 특허출원 준비",
			"mnth_gls": "o 컨퍼런스 논문 1편\r\no 구현논문 초안 작성",
			"annl_gls": "o 용역 과제진행\r\no 국내논문 2편\r\no 소프트웨어 등록,특허출원"
		},
		{
			"user": "t-d-hoa",
			"fr_dt": "2022-07-15 00:00:00",
			"to_dt": "2022-07-21 00:00:00",
			"paper_progress": "1. DCTO: Dynamic Cooperation Task offloading in fog computing system, IEEE Transaction on Parallel and Distributed System, (Under Review)\r\n2. Matching theory for distributed computation in IoT-Fog-CLoud system, IEEE transaction on Parallel and Distributed System, (Under review)\r\n3. 28 GHZ 5G Test Bed, IEEE Transaction on Education (In progress (75%).\r\n4. DISCO: Distributed computation offloading in fog networks, Journal of Communications and Networks (Under review)\r\n5. Digital Twin-aided Resource Allocations in Fog/Edge-enabled IoT networks, IEEE IoT journal, (In progress, 10%)",
			"project_progress": "",
			"mnth_gls": "-Finish and submit Paper #3\r\n-50% paper #4",
			"annl_gls": "4-5 SCI accepted SCI"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-18 00:00:00",
			"to_dt": "2022-07-20 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Accepted - Final Files Submitted\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (55%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (40%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (ACM CSUR)\r\n- Under review",
			"mnth_gls": "- Finish draft for 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-07-18 00:00:00",
			"to_dt": "2022-07-20 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Under review\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Writing (100%)\r\n- Submitted\r\n\r\no ICMIC 2022 - Writing(100%)\r\n- Next step: Submission\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 출장예정 : 금주 금요일 오전10시~12시 - 83정비창 출장(서류심의위원)",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-07-18 00:00:00",
			"to_dt": "2022-07-22 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: KICS Summer 2022. 100%\r\n-Submitted conference report and now waiting for publication on DBpia\r\n\r\nTitle 3: ICMIC 2022,\r\n85%\r\n- To have final meeting with co-authors and professor on final content and submission\r\n\r\nTitle 4: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ completed paper on 2022.06.30\r\n~ Enhancing readability to upload paper on EDAS 2022.08.20.\r\n\r\nTitle 5: Metafrika: Paper on Metaverse for Africa (15%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for the idea and main area of direction\r\n- Paper writting commences on the 2022.07.25",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in the Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera-ready, LaTeX file, copyright, and payment.\r\n- Paper now online on 2022.06.19\r\n- Proof copy submitted 2022.07.01\r\n- Proof copy online 2022.07.06\r\n\r\nTitle 3: ITS-2022-04-0154, (ACCEPTED: 2022.07.05)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted Camera-ready copy and update Professor on Wiley Author platform. 100%\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to the review is well articulated and ready for submission 2022.07.28.\r\n\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted: 2022.06.21\r\n-Under review\r\n\r\nTitle 6: IoT-23106-2022, (Major Revision)\r\n-Resubmitted on 2022.07.21\r\n- Rerunning simulations to address review comments.\r\n- Enhancing paper readability and English errors.\r\n\r\n\r\nBushra:\r\nIDSMT-2021-10-0102,\r\nSmart Factory Floor Monitoring using UWB Sensor, IET Science, Measurement & Technology, Published",
			"mnth_gls": "1. Conclude the MOU with Nigerian Universities (100%). (Benson Idahosa University and the University of Ilorin Signed.)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (70%).\r\n3. Submit and ensure Bushra and Saviour's papers are published in July 2022\r\n4. Complete and submit ICMIC and ICTC 2022 - (50%)\r\n5. Ensure ICT Express accepted paper is published - (100%)\r\n6. Ensure a resubmission of the revisions (Access, IEEE IoT, and Ad-hoc Networks papers) are resubmitted 2022.07.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal- (85%)\r\n8. Submit one Journal as first author 2022.07.29 - (50%)\r\n9. Submit IET-Intelligent Transportation System Camera-ready copy- (100%)",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (75%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (10/18 achieved)\r\n6. First author in 1 SCI journal.\r\n7. Second author in numerous SCI papers of NSL (3 Achieved).\r\n8. Secure Korea-Israel Project proposal (65%)."
		},
		{
			"user": "william",
			"fr_dt": "2022-07-18 00:00:00",
			"to_dt": "2022-07-22 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TCCN-TPS-22-0132 - IEEE TCCN. - under review (100%)\r\nTitle 3: TNSM-2022-05102 - IEEE TNetw. - currently under revision/re-submission (15%).\r\nTHIS WEEK:\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\n\r\nTitle 4: Manuscript ID:3169 - IEEE/AIAA DASC 2022 (Accepted April 2022) - (100%)\r\nTitle 5: PATENT APPLICATION (Q1) - under review (100%)\r\nTitle 6: Manuscript ID:#63 (1570820804) IEEE APCC 2022. - under review (100%)\r\n\r\nTitle 7: Low-Power FACTS for SVCs - IEEE Trans. (on-going) - 80%\r\nTHIS WEEK:\r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK:\r\n- To continue system model.\r\n- To continue simulation and testbed works.\r\n\r\nTitle 8:Survey works on combat Avionics - IEEE Magazine (on-going) - 65%\r\n- Pending",
			"project_progress": "Titles [1], [2] & [6]: - (UNDER REVIEW PROCESS).\r\n- Awaiting review comments.\r\n\r\nTitles [3]: - (REVIEW COMMENTS RECIEVED).\r\n- Reworking manuscript according to comments (10%).\r\n\r\nTitle [4] - (ACCEPTED).\r\n- Awaiting online repository publications.\r\n\r\nTitles [7]: - (IN-PROGRESS)\r\nTHIS WEEK:\r\n- Problem formulation and System model.\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\nNEXT WEEK:\r\n- To continue system model.\r\n- To commence simulation and testbed works.\r\n\r\n***COLLABORATIVE RESEARCH WITH DR. T-D HOA:\r\nPaper survey works in progress.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022).\r\n\r\nFURTHER ANNUAL GOALS\r\n[1]. Two (2) SCI/E Journal publications.\r\n[2]. Submissions to numerous domestic/international conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-20 00:00:00",
			"to_dt": "2022-07-22 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Early Access\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (60%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (40%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (ACM CSUR)\r\n- Under review",
			"mnth_gls": "- Finish draft for 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-07-21 00:00:00",
			"to_dt": "2022-07-22 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Major Revision\r\n\r\no Cooperative retransmission with DDQN-based power allocation in downlink NOMA systems, ICT express, Writing (100%)\r\n- Submitted\r\n\r\no ICMIC 2022 - Writing(100%)\r\n- Next step: Submission\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 출장 : 금주 금요일 오전10시~12시 - 83정비창 출장(서류심사위원)",
			"mnth_gls": "o URLLC를 위한 Multi-agent DRL 기반 Uplink NOMA (Simulation 40%)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-07-25 00:00:00",
			"to_dt": "2022-07-27 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- To have a final meeting with co-authors on the final content and submission on 2022.07.29\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ completed paper on 2022.06.30\r\n~ Enhancing readability to upload the paper on EDAS 2022.08.20.\r\n\r\nTitle 4: Metafrika: Paper on Metaverse for Africa (15%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for the idea and main area of direction\r\n- Paper writing commences on the 2022.07.25",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nKey Wearable Device Technologies Parameters for Innovative Healthcare Delivery in B5G Network: A Review, (Published:2022.05.09, 10.1109/ACCESS.2022.3173643). 100%\r\nSpecific action: None\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nNovel Hyper-Tuned Ensemble Random Forest Algorithm for the Detection of False Basic Safety Messages in the Internet of Vehicles, (Accepted: 2022.06.07). 100%\r\nSpecific Action: Submitted Camera-ready, LaTeX file, copyright, and payment.\r\n- Paper now online on 2022.06.19\r\n- Proof copy submitted 2022.07.01\r\n- Proof copy online 2022.07.06\r\n\r\nTitle 3: ITS-2022-04-0154, (ACCEPTED: 2022.07.05)\r\nProspects and Challenges of Metaverse Application in Data-Driven Intelligent Transportation Systems. 100%\r\nSpecific action: Resubmitted Camera-ready copy and update Professor on Wiley Author platform. 100%\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision).\r\nOptimization of RBF-SVM Kernel using Grid Search Algorithm for Detecting DDoS Attack in SDN-Based VANET. 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to the review is well articulated and ready for submission 2022.07.28.\r\n\r\n\r\nTitle 5: JCN22-DIV3-040\r\nClassification and Characterization of Encoded Traffic in SCADA Network using Hybrid Deep Learning Scheme. 100%\r\n~Submitted: 2022.06.21\r\n-Major revision: to resubmit in October 2022. \r\n\r\nTitle 6: IoT-23106-2022, (Major Revision)\r\n-Resubmitted on 2022.07.21\r\n- Rerunning simulations to address review comments.\r\n- Enhancing paper readability and English errors.",
			"mnth_gls": "1. Conclude the MOU with Nigerian Universities (100%). (Benson Idahosa University and the University of Ilorin Signed.)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (70%).\r\n3. Submit and ensure Bushra and Saviour's papers are published in July 2022 (100%)\r\n4. Complete and submit ICMIC and ICTC 2022 - (50%)\r\n5. Ensure ICT Express accepted paper is published - (100%)\r\n6. Ensure a resubmission of the revisions (Access, IEEE IoT, and Ad-hoc Networks papers) are resubmitted 2022.07.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal- (85%)\r\n8. Ensure that Metaverse journal paper is published (90%)- in production.",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (75%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (11/18 achieved)\r\n6. First author in 1 SCI journal (under review).\r\n7. Second author in numerous SCI papers of NSL (3 Achieved).\r\n8. Secure Korea-Israel Project proposal (75%)."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-25 00:00:00",
			"to_dt": "2022-07-27 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Final Proof\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (65%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (45%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (ACM Computing Surveys)\r\n- Under review",
			"mnth_gls": "Finalizing draft for 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "jwkim",
			"fr_dt": "2022-07-25 00:00:00",
			"to_dt": "2022-07-29 00:00:00",
			"paper_progress": "o 함정네트워크 테스트를 위한 트래픽 모니터링SW 구현 논문 준비\r\no ICMIC 논문 제출",
			"project_progress": "o 강소특구 창업과제 (사업화 과제)\r\n- 우수창업 경진대회 사업계획서 작성",
			"mnth_gls": "o 컨퍼런스 논문 1편\r\no 구현논문 초안 작성",
			"annl_gls": "o 용역 과제진행\r\no 국내논문 2편\r\no 소프트웨어 등록,특허출원"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-07-25 00:00:00",
			"to_dt": "2022-07-29 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Major Revision\r\n- Submitted\r\n\r\no ICMIC 2022 - Writing(100%)\r\n- Submitted\r\n\r\no 상향링크 NOMA시스템에서 강화학습을 이용한 사용자쌍 전력 할당에 관한 연구, 한국통신학회 - Preparing\r\n- 하계학술대회 좌장 추천\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o LIC 슈퍼커패시터 팩 테스트 관련\r\n- 유에이썬 방문 (2022.07.28)",
			"mnth_gls": "o Optics express, revision 제출",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-07-27 00:00:00",
			"to_dt": "2022-07-29 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Final Proof\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (65%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (45%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (ACM Computing Surveys)\r\n- Under review",
			"mnth_gls": "Finalizing draft for 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-08-01 00:00:00",
			"to_dt": "2022-08-05 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- To have a final meeting with co-authors on the final content and submission on 2022.08.16\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ completed paper on 2022.06.30\r\n~ Enhancing readability to upload the paper on EDAS 2022.08.20.\r\n\r\nTitle 4: Metafrika: Paper on Metaverse for Africa (15%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for the idea and main area of direction\r\n- Paper writing commences on the 2022.07.25 to be submitted 2022.10.31",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nIn-Production: 2022.07.05, 10.1049/itr2.12252\r\n\r\nTitle 4: ADHOC-D-22-00135, (Minor Revision)  100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to the review is well articulated and ready for submission 2022.08.20.\r\n\r\n\r\nTitle 5: JCN22-DIV3-040 \r\nIn-Revision: \r\n~Submitted: 2022.06.21\r\n-Major revision: to resubmit in October 2022.\r\n\r\nTitle 6: IoT-23106-2022, (Major Revision)\r\n-Resubmitted on 2022.07.21",
			"mnth_gls": "1. Conclude the MOU with Nigerian Universities (100%). (Benson Idahosa University and the University of Ilorin Signed.)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (70%).\r\n3. Submit and ensure Judith and Goodness's papers are published in August 2022 (100%)\r\n4. Complete and submit ICMIC and ICTC 2022 - (75%)\r\n5. Ensure a resubmission of the revisions (Access, IEEE IoT, and Ad-hoc Networks papers) are resubmitted 2022.08.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal- (85%)\r\n8. Ensure that Metaverse journal paper is published (90%)- in production.",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (75%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (11/18 achieved)\r\n6. First author in 1 SCI journal (under review).\r\n7. Second author in numerous SCI papers of NSL (3 Achieved).\r\n8. Secure Korea-Israel Project proposal (85%)."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-08-01 00:00:00",
			"to_dt": "2022-08-05 00:00:00",
			"paper_progress": "1. Distributed Cloud Computing: Architecture, Enabling Technologies, and Open Challenges (IEEE Consum. Electron. Mag.)\r\n- Published\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (70%)\r\n\r\n3. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (45%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (ACM Computing Surveys)\r\n- Under review",
			"mnth_gls": "Finalizing draft for 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-08-01 00:00:00",
			"to_dt": "2022-08-03 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Major Revision\r\n- Submitted\r\n\r\no ICMIC 2022 - Writing(100%)\r\n- Submitted\r\n\r\no 상향링크 NOMA시스템에서 강화학습을 이용한 사용자쌍 전력 할당에 관한 연구, 한국통신학회 - Preparing\r\n- 하계학술대회 좌장 추천\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "- 하계휴가(2022.08.04~2022.08.05)",
			"mnth_gls": "o KICS하계 좌장 추천 논문 작성(시뮬레이션 보강, 제출일 ~9.30)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-08-01 00:00:00",
			"to_dt": "2022-08-05 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n- Last week I updated the result of MFLOPs for various configuration in the result discussion section.\r\n- Perform two more simulation works.\r\n-Next week I will complete the result discussion section.\r\nPaper 05: Drone detection Identification and recognition using Pretrained CNN Network [ICTC 2022] (In progress) [50%].\r\n- Write the Introduction section.\r\n-Next week complete the paper and submit to the conference.\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [90%]\r\n-After the completion of title 04, I will update this paper and submit the journal.\r\n\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal. \r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [10%] (Submit)",
			"mnth_gls": "-Complete paper 04, 05, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-03 00:00:00",
			"to_dt": "2022-08-09 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Under Review\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks-Under Revision- Telecommunication Systems (TELS)\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-08-08 00:00:00",
			"to_dt": "2022-08-10 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n- Last week I updated the result of MFLOPs for various configuration in the result discussion section.\r\n- Perform two more simulation works.\r\n-Next week I will complete the result discussion section.\r\nPaper 05: Drone detection Identification and recognition using Pretrained CNN Network [ICTC 2022] (In progress) [50%].\r\n- Revise the Introduction section.\r\n-Write the system model and proposed CNN model section\r\n-Next week complete the paper and submit to the conference.\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [90%]\r\n-After the completion of title 04, I will update this paper and submit the journal.\r\n\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [10%] (Submit)",
			"mnth_gls": "-Complete paper 04, 05, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-08-08 00:00:00",
			"to_dt": "2022-08-12 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- Submitted\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Submitted.\r\n\r\nTitle 4: Metafrika: Paper on Metaverse for Africa (15%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for the idea and main area of direction\r\n- Paper writing commences on the 2022.08.25 to be submitted 2022.10.31",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022, (Major Revision- Awaiting decision)\r\n-Resubmitted on 2022.07.21\r\n\r\nTitle 5: JCN22-DIV3-040   (Major Revision)\r\n\r\n~Resubmitted on 2022.08.10\r\n\r\nTitle 6: ADHOC-D-22-00135, (Minor Revision) 100%\r\nSpecific action:\r\n-responding to all review comments and trying to simulate with new datasets\r\n- Ensuring all response to the review is well articulated and ready for submission 2022.08.20.",
			"mnth_gls": "1. Conclude the MOU with Nigerian Universities (100%). (Benson Idahosa University and the University of Ilorin Signed.)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (70%).\r\n3. Submit and ensure Judith and Goodness's papers are published in August 2022 (100%)\r\n4. Complete and submit ICMIC and ICTC 2022 - (100%)\r\n5. Ensure a resubmission of the revisions (Access, IEEE IoT, JCN, and Ad-hoc Networks papers) are resubmitted 2022.08.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal- (85%)\r\n8. Ensure that Metaverse journal paper is published (100%).",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (75%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (12/18 achieved)\r\n6. First author in 1 SCI journal (under review).\r\n7. Second author in numerous SCI papers of NSL (3 Achieved).\r\n8. Secure Korea-Israel Project proposal (85%)."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-08-08 00:00:00",
			"to_dt": "2022-08-12 00:00:00",
			"paper_progress": "1. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (75%)\r\n\r\n2. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (45%)\r\n\r\n3. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (ACM Computing Surveys)\r\n- Under review",
			"mnth_gls": "Finalize 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-10 00:00:00",
			"to_dt": "2022-08-16 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Under Review\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks-Under Revision- Telecommunication Systems (TELS): 60 % Complete\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 10 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-10 00:00:00",
			"to_dt": "2022-08-12 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Under Review\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks-Under Revision- Telecommunication Systems (TELS): 70 % Complete\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 10 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-12 00:00:00",
			"to_dt": "2022-08-17 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Under Review\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks-Under Revision- Telecommunication Systems (TELS): 80 % Complete\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 10 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1.. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-08-15 00:00:00",
			"to_dt": "2022-08-19 00:00:00",
			"paper_progress": "1. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (80%)\r\n\r\n2. An Efficient QoS-Aware Service Provisioning for Multi-access edge computing (TBD)\r\n- In-progess (45%)\r\n\r\n3. ICTC-2022: Submitted",
			"project_progress": "Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\n- In revision",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-08-16 00:00:00",
			"to_dt": "2022-08-19 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Major Revision\r\n\r\no 상향링크 NOMA시스템에서 강화학습을 이용한 사용자쌍 전력 할당에 관한 연구, 한국통신학회 - Preparing\r\n- 전력할당 DRL부분 수정중\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 83정비창 딥러닝 수업준비 (08.29~09.01)",
			"mnth_gls": "o KICS하계 좌장 추천 논문 작성(시뮬레이션 보강, 제출일 ~9.30)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-17 00:00:00",
			"to_dt": "2022-08-19 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks-Under Revision- Telecommunication Systems (TELS): Complete (To be submitted)\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 20 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-19 00:00:00",
			"to_dt": "2022-08-24 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks-Under Revision- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 30 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-08-22 00:00:00",
			"to_dt": "2022-08-24 00:00:00",
			"paper_progress": "1. ICMIC2022: Submitted\r\n\r\n2. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Wirel. Commun. Lett.)\r\n- In-progess (65%)\r\n\r\n3. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (80%)\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "5. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\n- In revision",
			"mnth_gls": "Derive closed-form solution (complete), and doing simulation for (2).",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-08-22 00:00:00",
			"to_dt": "2022-08-24 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n- Last week I updated the result of MFLOPs for various configuration in the result discussion section.\r\n- Perform two more simulation works.\r\n-Next week I will complete the result discussion section.\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%].\r\n- Revise the Introduction section and the system model and proposed CNN model section.\r\n-Write result and discussion section.\r\n-Submit the paper in ICTC Conference\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [90%]\r\n-After the completion of title 04, I will update this paper and submit the journal.\r\n\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [10%] (Submit)",
			"mnth_gls": "-Complete paper 04, 05, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "jwkim",
			"fr_dt": "2022-08-22 00:00:00",
			"to_dt": "2022-09-23 00:00:00",
			"paper_progress": "o 함정네트워크 테스트를 위한 트래픽 시험SW 구현\r\no RIVF 베트남학회(12월), 논문 준비",
			"project_progress": "o 강소특구 창업과제 (사업화 과제)\r\n- 우수창업자 지원 선정(10월중 창업예정)\r\n\r\no 특허 \r\n - HIL 관련 특허출원 준비",
			"mnth_gls": "o 컨퍼런스 논문 1편\r\no 구현논문 초안 작성",
			"annl_gls": "o 용역 과제진행\r\no 국내논문 2편\r\no 소프트웨어 등록,특허출원"
		},
		{
			"user": "william",
			"fr_dt": "2022-08-22 00:00:00",
			"to_dt": "2022-08-26 00:00:00",
			"paper_progress": "Title 1: COM-2021-07-0270 - IET Comm. - under review (100%)\r\nTitle 2: TNSM-2022-05102 - IEEE TNetw. - currently under revision/re-submission (40%).\r\nTHIS WEEK:\r\n- Algorithm and Figures were added.\r\n- Readability was enhanced.\r\n\r\nTitle 3: PATENT APPLICATION (Q1) - under review (100%)\r\nTitle 4: Manuscript ID:3169 - IEEE/AIAA DASC 2022 (Accepted April 2022) - (100%)\r\nTitle 5: Manuscript ID:#63 (1570820804) IEEE APCC 2022. - (Accepted August 2022)",
			"project_progress": "Titles [1]: - (UNDER REVIEW PROCESS).\r\n- Awaiting final decision.\r\n\r\nTitle [4], [5] - (ACCEPTED).\r\n- Awaiting online repository publications.",
			"mnth_gls": "[1]. Detailing and investigating all my essential simulation and testbed working tools.\r\n[2]. Working with PostDoc colleagues and NSL Members on current R&D project works.",
			"annl_gls": "CURRENT ANNUAL ACHIEVEMENTS - [Sept. 2021 - Aug. 2022]:\r\nTitle 1: IEEE Access-2021-24847. [IEEE Access] [PUBLISHED Sept. 2021].\r\nTitle 2: IEEE-ICTC International Conference, [PUBLISHED Dec. 2021].\r\nTitle 3: IEEE TCAD-2021-0394 [IEEE Transactions on CAD] [PUBLISHED Jan. 2022].\r\nTitle 4: IEEE Sensors-38710-2021. [IEEE Sensor Journal] [PUBLISHED March 2022]\r\nTitle 5: IEEE/AIAA DASC 2022 [ACCEPTED April 2022].\r\nTitle 6: 16968 - Domestic KICS (Summer) 2022 Conference (Accepted May 2022)."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-08-22 00:00:00",
			"to_dt": "2022-08-26 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Awaiting final decision.\r\n\r\no 상향링크 NOMA시스템에서 강화학습을 이용한 사용자쌍 전력 할당에 관한 연구, 한국통신학회 - Preparing\r\n- 전력할당 DRL부분 수정중\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 83정비창 딥러닝 수업준비 (08.29~09.01)",
			"mnth_gls": "o KICS하계 좌장 추천 논문 작성(시뮬레이션 보강, 제출일 ~9.30)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-24 00:00:00",
			"to_dt": "2022-08-26 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks-Under Revision- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 40 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-08-24 00:00:00",
			"to_dt": "2022-08-26 00:00:00",
			"paper_progress": "1. ICMIC2022: Submitted\r\n\r\n2. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Wirel. Commun. Lett.)\r\n- In-progess (65%)\r\n\r\n3. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress\r\n\r\n4. ICTC-2022: Submitted",
			"project_progress": "5. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\n- In revision",
			"mnth_gls": "Derive closed-form solution (complete), and doing simulation for (2).",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-27 00:00:00",
			"to_dt": "2022-08-31 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federate Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 70 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-08-29 00:00:00",
			"to_dt": "2022-08-31 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n- Last week I updated the result of MFLOPs for various configuration in the result discussion section.\r\n- Perform two more simulation works.\r\n-Next week I will complete the result discussion section.\r\n\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%].\r\n- Revise the whole paper\r\n-Submit the paper in ICTC Conference\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [90%]\r\n-This week perform simulation using another dataset to justify the interfering signal and RF signal.\r\n-Modify the paragraph of the proposed CNN model.\r\n\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [10%] (Submit)",
			"mnth_gls": "-Complete paper 04, 05, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-08-29 00:00:00",
			"to_dt": "2022-09-02 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Awaiting final decision.\r\n\r\no 상향링크 NOMA시스템에서 강화학습을 이용한 사용자쌍 전력 할당에 관한 연구, 한국통신학회 - Preparing\r\n- 전력할당 DRL부분 수정중\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "o 83정비창 딥러닝 수업 (08.29~09.01)",
			"mnth_gls": "o KICS하계 좌장 추천 논문 작성(시뮬레이션 보강, 제출일 ~9.30)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-08-29 00:00:00",
			"to_dt": "2022-09-02 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Wirel. Commun. Lett.)\r\n- In-progess (70%)\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (80%)\r\n\r\n3. ICMIC2022: Accepted\r\n\r\n4. ICTC-2022: Accepted",
			"project_progress": "5. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\n- In revision",
			"mnth_gls": "Finish (1).",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-08-31 00:00:00",
			"to_dt": "2022-09-02 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 90 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-09-02 00:00:00",
			"to_dt": "2022-09-07 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Submitted- Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Under Revision-Transaction of Vehicular Technology: 95 % Complete",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-09-05 00:00:00",
			"to_dt": "2022-09-08 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- Accepted\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Accepted in ICTC 2022.\r\n\r\nTitle 4: Metafrika: Paper on Metaverse for Africa (15%)\r\n- Suggested by Professor Kim\r\n-Skeletal search for the idea and main area of direction\r\n- Paper writing commences on 2022.08.25 to be submitted on 2022.10.31",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022, (Major Revision- Awaiting decision)\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: JCN22-DIV3-040 (Major Revision)\r\n\r\n~Resubmitted on 2022.08.10\r\n\r\nTitle 6: ADHOC-D-22-00135, (Minor Revision) 100%\r\nSpecific action:\r\n-Resubmitted 2022.08.26.\r\n\r\nTitle 7: T-ITS-22-03-0723, (Major Revision)\r\n- To resubmit on 2022.09.29",
			"mnth_gls": "1. Conclude the MOU with Nigerian Universities (100%). (Benson Idahosa University and the University of Ilorin Signed.)\r\n2. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (70%).\r\n3. Submit and ensure Judith and Goodness's papers are published in August 2022 (100%)\r\n4. Complete and submit ICMIC and ICTC 2022 - (100%)\r\n5. Ensure a resubmission of the revisions (Access, IEEE IoT, JCN, and Ad-hoc Networks papers) are resubmitted 2022.08.22 - (50%)\r\n7. Conclude the KOREA-Israel Collaboration proposal and audit- (90%)\r\n8. Ensure that a Metaverse journal paper is published (100%).",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (75%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (13/18 achieved)\r\n6. First author in 1 SCI journal (under review).\r\n7. Second author in numerous SCI papers of NSL (4 Achieved).\r\n8. Secure Korea-Israel Project proposal (95%)."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-09-05 00:00:00",
			"to_dt": "2022-09-08 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Rereview\r\n\r\no 상향링크 NOMA시스템에서 강화학습을 이용한 사용자쌍 전력 할당에 관한 연구, 한국통신학회 - Preparing\r\n- 전력할당 DRL부분 수정중\r\n\r\no Multi-agent DRL-based Uplink NOMA system for URLLC, IEEE Wireless communications letter, preparing\r\n- Pending",
			"project_progress": "",
			"mnth_gls": "o KICS하계 좌장 추천 논문 작성(시뮬레이션 보강, 제출일 ~9.30)",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-09-08 00:00:00",
			"to_dt": "2022-09-14 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: 30 %",
			"project_progress": "",
			"mnth_gls": "Completion of paper under revision.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-09-12 00:00:00",
			"to_dt": "2022-09-16 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Wirel. Commun. Lett.)\r\n- In-progess (85%)\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (80%)",
			"project_progress": "3. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\n- In revision",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-09-13 00:00:00",
			"to_dt": "2022-09-16 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n- Last week I updated the result of MFLOPs for various configuration in the result discussion section.\r\n- Perform two more simulation works.\r\n-Next week I will complete the result discussion section.\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%].\r\n- Revise the whole paper\r\n-Submit the paper in ICTC Conference\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [100%]\r\n-Add a results table in the paper.\r\n- Add description of the result analysis.\r\n-Add content in the introduction section.\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)",
			"mnth_gls": "-Complete paper 04, 05, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "saviour",
			"fr_dt": "2022-09-14 00:00:00",
			"to_dt": "2022-09-20 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.",
			"project_progress": "Training new members\r\n\r\n1) Identifying interested candidates to join the blockchain projected team.\r\n2) Scheduling the training session and time.",
			"mnth_gls": "1) Complete hashing security model implementation.\r\n\r\n2) Start training the new member of the project team.\r\n\r\n3) Design schedule for the first commercial Pure Wallet application.",
			"annl_gls": "1) Complete the first commercial version of the Pure Wallet.\r\n\r\n2) Start the Pure Voting project."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-09-14 00:00:00",
			"to_dt": "2022-09-16 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: 40 %",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "saviour",
			"fr_dt": "2022-09-16 00:00:00",
			"to_dt": "2022-09-22 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.",
			"project_progress": "Training new members\r\n\r\n1) Started training the new members.\r\n2) Two days of training completed.",
			"mnth_gls": "1) Complete hashing security model implementation.\r\n\r\n2) Start training the new member of the project team.\r\n\r\n3) Design schedule for the first commercial Pure Wallet application.",
			"annl_gls": "1) Complete the first commercial version of the Pure Wallet.\r\n\r\n2) Start the Pure Voting project."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-09-23 00:00:00",
			"to_dt": "2022-09-29 00:00:00",
			"paper_progress": "1. C-DRN Based Modulation Classification for Beyond 5G in Multipath Fading Channels-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: 50 %",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-09-26 00:00:00",
			"to_dt": "2022-09-30 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Rejected\r\n- Updating",
			"project_progress": "ㅇ 10월 4일 연차",
			"mnth_gls": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation -> Revision",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-09-28 00:00:00",
			"to_dt": "2022-10-05 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n- Last week I updated the result of MFLOPs for various configuration in the result discussion section.\r\n- Perform two more simulation works.\r\n-Next week I will complete the result discussion section.\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%].\r\n- Revise the whole paper\r\n-Submit the paper in ICTC Conference\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE IoT) (In progress) [100%]\r\n-Add a results table in the paper.\r\n- Add description of the result analysis.\r\n-Add content in the introduction section.\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][10%] (In Progress)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)",
			"mnth_gls": "Complete paper 04, 05, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-10-03 00:00:00",
			"to_dt": "2022-10-07 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Wirel. Commun. Lett.)\r\n- Almost done (95%)\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (80%)",
			"project_progress": "3. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\n- Submit revision",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-10-07 00:00:00",
			"to_dt": "2022-10-13 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: 30%\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "1.. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-10-10 00:00:00",
			"to_dt": "2022-10-14 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n-Revise the paper.\r\n-After coming from ICTC 2022 submit the paper to the journal\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%]. (Accepted ICTC 2022)\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE) (summited) [100%]\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][100%] (complete)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)\r\n- Add contents according to the reviewer comments.",
			"mnth_gls": "Complete paper 04, 05, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-10-14 00:00:00",
			"to_dt": "2022-10-20 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: 50%\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-10-21 00:00:00",
			"to_dt": "2022-10-27 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: 70%\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "saviour",
			"fr_dt": "2022-10-24 00:00:00",
			"to_dt": "2022-10-30 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.",
			"project_progress": "Training new members\r\n\r\n1) Continue implementation training of new members.\r\n2) Learning Flutter and Solidity.",
			"mnth_gls": "1) Complete hashing security model implementation.\r\n\r\n2) Continue training the new member of the project team.\r\n\r\n3) Make data book for connection of Smart contract function and mobile application.",
			"annl_gls": "1) Complete the first commercial version of the Pure Wallet.\r\n\r\n2) Start the Pure Voting project or layer 2 solution."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-10-24 00:00:00",
			"to_dt": "2022-10-28 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Wirel. Commun. Lett.)\r\n- 100%\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress (80%)",
			"project_progress": "3. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\n- Submit revision",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-10-24 00:00:00",
			"to_dt": "2022-10-28 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Optics Express, Submitted\r\n- 수정후 제출\r\n- APC전액 면제 제안 받음",
			"project_progress": "",
			"mnth_gls": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation -> Revision",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "saviour",
			"fr_dt": "2022-10-28 00:00:00",
			"to_dt": "2022-11-03 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.",
			"project_progress": "Training new members\r\n\r\n1) Continue implementation training of new members.\r\n2) Learning Flutter and Solidity.",
			"mnth_gls": "1) Complete hashing security model implementation.\r\n\r\n2) Continue training the new member of the project team.\r\n\r\n3) Make a data book for connection of Smart contract function and mobile application.",
			"annl_gls": "1) Complete the first commercial version of the Pure Wallet.\r\n\r\n2) Start the Pure Voting project or layer 2 solutions."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-10-28 00:00:00",
			"to_dt": "2022-11-03 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: 80%\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-10-31 00:00:00",
			"to_dt": "2022-11-04 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Transactions on Emerging Topics in Computing)\r\n- 100%\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress",
			"project_progress": "3. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\nAccepted",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-10-31 00:00:00",
			"to_dt": "2022-11-02 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n-Make some modifications as needed.\r\n-Send the paper to the correction service.\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%]\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE) (summited) [100%]\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][100%] (complete)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)\r\n- Add contents according to the reviewer comments.",
			"mnth_gls": "Complete paper 04, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-11-04 00:00:00",
			"to_dt": "2022-11-10 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: 90%\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "!. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2022-11-07 00:00:00",
			"to_dt": "2022-11-11 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Transactions on Emerging Topics in Computing)\r\n- 100%\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)\r\n- In-progress",
			"project_progress": "3. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\nAccepted",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "nsl",
			"fr_dt": "2022-11-07 00:00:00",
			"to_dt": "2022-11-11 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Sensors, Major Revision\r\n- APC전액 면제 제안 받음",
			"project_progress": "",
			"mnth_gls": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation -> Revision",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "saviour",
			"fr_dt": "2022-11-11 00:00:00",
			"to_dt": "2022-11-17 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.\r\n\r\n2) Saviour Multi-Hashing (SMuHa): A Quantum Resistant Security Algorithm for Offline Transactions (ICC 2023)",
			"project_progress": "Training new members\r\n\r\n1) Continue implementation training of new members.\r\n2) Learning Flutter and Solidity.\r\n\r\n\r\nICC 2023 paper\r\n\r\n1) Making the title.\r\n2) Studied and prepared related works.\r\n3) Designed and wrote the system model.\r\n4) Implementation and result gathering.\r\n5) Wrote about the system results.\r\n6) wrote the introduction.\r\n7) Wrote abstract and conclusion.\r\n8) Checked the paper plagiarism.\r\n9) Checked paper for grammar, spelling, and typo errors to enhance readability.\r\n10) Submitted the paper to ICC 2023 (symposium paper)",
			"mnth_gls": "1) Complete hashing security model implementation.\r\n\r\n2) Continue training the new member of the project team.\r\n\r\n3) Make a data book for the connection of the Smart contract function and mobile application.\r\n\r\n4) Submit a paper to ICC 2023.",
			"annl_gls": "1) Complete the first commercial version of the Pure Wallet.\r\n\r\n2) Start the Pure Voting project or layer 2 solutions."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-11-11 00:00:00",
			"to_dt": "2022-11-17 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: to be submitted\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "20195028",
			"fr_dt": "2022-11-14 00:00:00",
			"to_dt": "2022-11-24 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n-Make some modifications as needed.\r\n-Send the paper to the correction service.\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%]\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE) (summited) [100%]\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]\r\n\r\n- Last week attend the KICS conference.\r\n-This week taking preparation to attend the MILCOM Conference.",
			"project_progress": "Co-Author Paper:\r\nPaper 08: DNN for DDoS Attack Detection and Classification [IEE-TNSM][100%] (complete)\r\nPaper 09: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\n\r\nPaper 10:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)\r\n- Preparing to attend the MILCOM conference.\r\n- Prepared the presentation Slide.",
			"mnth_gls": "Complete paper 04, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-11-18 00:00:00",
			"to_dt": "2022-11-24 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Major Revision)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Major Revision)",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revesions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences."
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-11-21 00:00:00",
			"to_dt": "2022-11-25 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Sensors, Resubmitted\r\n-수정 후 제출",
			"project_progress": "o BMS 마스터 슬레이브간 통신 펌웨어 수정",
			"mnth_gls": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation -> Resubmission",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-11-25 00:00:00",
			"to_dt": "2022-12-01 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Major Revision)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-Transaction of Vehicular Technology: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- VEHICULAR COMMUNICATIONS: Submitted (Major Revision)",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-11-28 00:00:00",
			"to_dt": "2022-12-02 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Trans. Emerg. Topics Comput.)\r\n- Under review\r\n\r\n2. MEC Computation Offloading Assisted by Parked Vehicles for Digital Twin-Enabled Metaverse (IEEE Wireless Commun. Lett.) \r\n\r\n3. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)",
			"project_progress": "3. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\nPublished",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-12-05 00:00:00",
			"to_dt": "2022-12-09 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Sensors, Published",
			"project_progress": "o BMS 마스터 슬레이브간 통신 펌웨어 수정",
			"mnth_gls": "o DQN 기반 Partial NOMA resource allocation 시뮬레이션 작성",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-12-09 00:00:00",
			"to_dt": "2022-12-15 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion \r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "B00501",
			"fr_dt": "2022-12-12 00:00:00",
			"to_dt": "2022-12-16 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Trans. Emerg. Topics Comput.)\r\n- Under review\r\n\r\n2. Distributed Cloud: A Cloud Computing and Networking Convergence Perspective (IEEE Commun. Mag.)",
			"project_progress": "3. Artificial Intelligence for the Metaverse: A Survey (Engineering Applications of Artificial Intelligence)\r\nPublished",
			"mnth_gls": "",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-12-12 00:00:00",
			"to_dt": "2022-12-16 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [85%] (In progress)\r\n-Working with this paper. Hopefully submit end of this month.\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%]\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE) (summited) [100%]\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\nPaper 9:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)\r\n\r\nPaper 10: DNN for DDoS Attack Detection and Classification [IEE-TNSM][100%] (complete)",
			"mnth_gls": "Complete paper 04, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "saviour",
			"fr_dt": "2022-12-13 00:00:00",
			"to_dt": "2022-12-19 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.\r\n\r\n2) Saviour Multi-Hashing (SMuHa): A Quantum Resistant Security Algorithm for Offline Transactions (ICC 2023) Pure Wallet",
			"project_progress": "1) Submitted the paper to ICC 2023 (symposium paper)",
			"mnth_gls": "1) Complete hashing security model implementation.\r\n\r\n2) Continue training the new member of the project team.\r\n\r\n3) Make a data book for the connection of the Smart contract function and mobile application.\r\n\r\n4) Submit a paper to ICC 2023.",
			"annl_gls": "1) Complete the first commercial version of the Pure Wallet.\r\n\r\n2) Start the Pure Voting project or layer 2 solutions."
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-12-16 00:00:00",
			"to_dt": "2022-12-22 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2022-12-19 00:00:00",
			"to_dt": "2022-12-23 00:00:00",
			"paper_progress": "o Reliability improvement in downlink VLC-NOMA systems using DNN-based power allocation, Sensors, Published\r\n\r\no Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n\r\no DQN 기반 Partial NOMA resource allocation 시뮬레이션 작성",
			"project_progress": "",
			"mnth_gls": "o DQN 기반 Partial NOMA resource allocation 시뮬레이션 작성",
			"annl_gls": "o SCIE 논문 1편 목표\r\no BMS 개발을 통한 사업화(BMS 보드 개발 완료 목표)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-12-23 00:00:00",
			"to_dt": "2022-12-29 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "20195028",
			"fr_dt": "2022-12-26 00:00:00",
			"to_dt": "2022-12-30 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [95%] (In progress)\r\n-manuscript under processing\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%]\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE) (summited) [100%]\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\nPaper 9:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)\r\n\r\nPaper 10: DNN for DDoS Attack Detection and Classification [IEE-TNSM][100%] (complete)",
			"mnth_gls": "Complete paper 04, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN and ICTC 2022 conference]"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-29 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- Accepted\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Published in ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 5: Survey with Dr. Hoa\r\n~ Submitted for English Correction\r\n\r\nTitle 6: Survey with Dr. Kim\r\n~ 20% progress",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135, \r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores \r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted with Minor Revision)\r\n- Awaiting AE Recommendation",
			"mnth_gls": "1. Submit one Survey paper by 2022.12.30 (100%).\r\n2. Continue Academic collaboration meetings with Nigerian Universities (100%).\r\n3. Submit and ensure Love and Goodness's papers are published in October 2022 (90%)\r\n4.  Ensure a resubmission of all revised papers - (100%)\r\n5. Come up with a new direction for future KOREA-Israel Collaboration proposal (50%)\r\n6. Ensure that NRF is submitted by 2022.12.30 (95%).",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (75%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (18/18 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (6 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-29 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- Accepted\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Published in ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 5: Survey with Dr. Hoa\r\n~ Submitted for English Correction\r\n\r\nTitle 6: Survey with Dr. Kim\r\n~ 20% progress",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135,\r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted with Minor Revision)\r\n- Awaiting EIC Decision\r\n\r\nTitle 8: IoT-26497-2022.R1, (Accepted with Minor Revision)\r\n-To submit the camera-ready copy 2022.12.31\r\n\r\nTitle 9: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 10: COMST-00569-2022\r\n-Under Review",
			"mnth_gls": "1. Submit one Survey paper by 2022.12.30 (100%).\r\n2. Continue Academic collaboration meetings with Nigerian Universities (100%).\r\n3. Submit and ensure Love and Goodness's papers are published in December 2022 (90%)\r\n4. Ensure a resubmission of all revised papers - (100%)\r\n5. Come up with a new direction for future KOREA-Israel Collaboration proposal (80%)\r\n6. Ensure that NRF is submitted by 2022.12.30 (95%).",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (85%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (18/18 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (6 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-30 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- Published\r\n\r\nTitle 3: Metaverse Conference paper for creativia (Dong-Seong Kim and Cosmas) \r\n~ Published ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~Accepted 2022.10.18\r\n~Camera Ready copy to be resubmitted 2022.10.22\r\n~ Attended Conference and used it for Collaboration for Imo State Government, Nigeria 2022.11.1~3\r\n\r\nTitle 5: applsci-2128497\r\n~Survey Paper in collaboration with authors from Canada and Nigeria.\r\n~Under review\r\n\r\nTitle 6: Survey paper in collaboration with Dr. Hoa and Professor Kim on \"5G+ Networks...\"\r\n~Submitted for English Correction Service 2022.12.23\r\n\r\nTitle 7: Survey paper in collaboration with Dr. Kim on \"Neuromorphic Computing\" \r\n~ 20% in progress",
			"project_progress": "1. Application for NRF ongoing.\r\nSecond Authored works in NSL and ICT-CRC\r\n\r\nPapers in 2022.03.01~2023.02.28\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135, \r\n-Published 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IoT-D-22-00330,\r\n~Accepted 2022.12.21\r\n- In-production \r\n\r\nTitle 7: T-ITS-22-03-0723, (Accept with Minor Revision)\r\n- Awaiting AE Recommendation\r\n\r\nTitle 8: JCN22-DIV3-040 (Major Revision)\r\n~Awaiting Reviewer Score \r\n\r\nTitle 9: IoT-26497-2022.R1\r\n~Awaiting Decision\r\n\r\nTitle 10: COMST-00569-2022\r\n~Under Review",
			"mnth_gls": "1. Ensure all accepted papers are published.\r\n2. Complete and Submit NRF Proposal\r\n3. Submit Survey paper with Dr. Hoa to Target Journal \r\n4. Complete phase 1 of the NSL Winter Intensive\r\n5. Establish and Consolidate \"Academic Collaboration with Nigerian Universities on Metaverse\"",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (100%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (100% done)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (7 Achieved).\r\n8. Submit at least one fund proposal (100%)"
		},
		{
			"user": "",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-30 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: ICMIC 2022,\r\n100%\r\n- Published\r\n\r\nTitle 3: Metaverse Conference paper for creativia (Dong-Seong Kim and Cosmas) \r\n~ Published ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~Accepted 2022.10.18\r\n~Camera Ready copy to be resubmitted 2022.10.22\r\n~ Attended Conference and used it for Collaboration for Imo State Government, Nigeria 2022.11.1~3\r\n\r\nTitle 5: applsci-2128497\r\n~Survey Paper in collaboration with authors from Canada and Nigeria.\r\n~Under review\r\n\r\nTitle 6: Survey paper in collaboration with Dr. Hoa and Professor Kim on \"5G+ Networks...\"\r\n~Submitted for English Correction Service 2022.12.23\r\n\r\nTitle 7: Survey paper in collaboration with Dr. Kim on \"Neuromorphic Computing\" \r\n~ 20% in progress",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135, \r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IoT-D-22-00330, (Accepted)\r\n~ Publication production 2022.12.21.\r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted)\r\n- Awaiting AE Decision\r\n\r\nTitle 8: JCN22-DIV3-055, (Major revision resubmitted)\r\n~Awating Reviewer Scores\r\n\r\nTitle 9: IoT-26497-2022.R1, (Minor Revision Resubmitted)\r\n- Awaiting Decision\r\n\r\nTitle 10: COMST-00569-20222\r\n~Under review",
			"mnth_gls": "1. Publication of all accepted papers (100%).\r\n2. Continue academic collaboration with Nigerian Universities.\r\n3. Submit paper with Dr. Hoa to target journal\r\n4. Complete the NRF proposal writing\r\n5. Follow up on new direction based on the rejected proposal of KORIL",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (100%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (100%)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (8 Achieved).\r\n8. Submit at least a research grant proposal (100%)."
		},
		{
			"user": "",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-30 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Published in ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~Accepted 2022.10.18\r\n~Camera Ready copy to be resubmitted 2022.10.22\r\n~ Awaiting publication\r\n\r\nTitle 5: applsci-2128497 (collaboration paper with Canadian and Nigerian Researchers)\r\n~Under review\r\n\r\nTitle 6: Survey with Dr. Hoa\r\n~Submitted for English correction\r\n\r\nTitle 7: Survey with Dr. Kim\r\n20% in progress",
			"project_progress": "1. Application for NRF ongoing.\r\nSecond Authored works in NSL and ICT-CRC\r\n\r\nPapers in 2022.03.01~2023.02.28\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135, \r\n-Published 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IoT-D-22-00330,\r\n~Accepted 2022.12.21\r\n- In-production \r\n\r\nTitle 7: T-ITS-22-03-0723, (Accept with Minor Revision)\r\n- Awaiting AE Recommendation\r\n\r\nTitle 8: JCN22-DIV3-040 (Major Revision)\r\n~Awaiting Reviewer Score \r\n\r\nTitle 9: IoT-26497-2022.R1\r\n~Awaiting Decision\r\n\r\nTitle 10: COMST-00569-2022\r\n~Under Review",
			"mnth_gls": "1. Ensure all accepted papers are published.\r\n2. Complete and Submit NRF Proposal\r\n3. Submit Survey paper with Dr. Hoa to Target Journal \r\n4. Complete phase 1 of the NSL Winter Intensive\r\n5. Establish and Consolidate \"Academic Collaboration with Nigerian Universities on Metaverse\"",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (100%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (100% done)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (7 Achieved).\r\n8. Submit at least one fund proposal (100%)"
		},
		{
			"user": "",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-30 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Published in ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~Accepted 2022.10.18\r\n~Camera Ready copy to be resubmitted 2022.10.22\r\n~ Awaiting publication\r\n\r\nTitle 5: applsci-2128497 (collaboration paper with Canadian and Nigerian Researchers)\r\n~Under review\r\n\r\nTitle 6: Survey with Dr. Hoa\r\n~Submitted for English correction\r\n\r\nTitle 7: Survey with Dr. Kim\r\n20% in progress",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135, \r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IoT-D-22-00330, (Accepted)\r\n~ Publication production 2022.12.21.\r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted)\r\n- Awaiting AE Decision\r\n\r\nTitle 8: JCN22-DIV3-055, (Major revision resubmitted)\r\n~Awating Reviewer Scores\r\n\r\nTitle 9: IoT-26497-2022.R1, (Minor Revision Resubmitted)\r\n- Awaiting Decision\r\n\r\nTitle 10: COMST-00569-20222\r\n~Under review",
			"mnth_gls": "1. Publication of all accepted papers (100%).\r\n2. Continue academic collaboration with Nigerian Universities.\r\n3. Submit paper with Dr. Hoa to target journal\r\n4. Complete the NRF proposal writing\r\n5. Follow up on new direction based on the rejected proposal of KORIL",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (100%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (100%)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (8 Achieved).\r\n8. Submit at least a research grant proposal (100%)."
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-30 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100%\r\n- Under Review\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Published in ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 5: Survey with Dr. Hoa\r\n~ Submitted for English Correction\r\n\r\nTitle 6: Survey with Dr. Kim\r\n~ 20% progress",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135, \r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores \r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted with Minor Revision)\r\n- Awaiting AE Recommendation",
			"mnth_gls": "1. Submit one Survey paper by 2022.12.30 (100%).\r\n2. Continue Academic collaboration meetings with Nigerian Universities (100%).\r\n3. Submit and ensure Love and Goodness's papers are published in October 2022 (90%)\r\n4.  Ensure a resubmission of all revised papers - (100%)\r\n5. Come up with a new direction for future KOREA-Israel Collaboration proposal (50%)\r\n6. Ensure that NRF is submitted by 2022.12.30 (95%).",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (75%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (18/18 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (6 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "cosmas",
			"fr_dt": "2022-12-27 00:00:00",
			"to_dt": "2022-12-30 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100%\r\n- Under Review\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Published in ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 5: Survey with Dr. Hoa\r\n~ Submitted for English Correction\r\n\r\nTitle 6: Survey with Dr. Kim\r\n~ 20% progress",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135,\r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted with Minor Revision)\r\n- Awaiting EIC Decision\r\n\r\nTitle 8: IoT-26497-2022.R1, (Accepted with Minor Revision)\r\n-To submit the camera-ready copy 2022.12.31\r\n\r\nTitle 9: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 10: COMST-00569-2022\r\n-Under Review",
			"mnth_gls": "1. Submit one Survey paper by 2022.12.30 (100%).\r\n2. Continue Academic collaboration meetings with Nigerian Universities (100%).\r\n3. Submit and ensure Love and Goodness's papers are published in December 2022 (90%)\r\n4. Ensure a resubmission of all revised papers - (100%)\r\n5. Come up with a new direction for future KOREA-Israel Collaboration proposal (80%)\r\n6. Ensure that NRF is submitted by 2022.12.30 (95%).",
			"annl_gls": "1. Conclude the MOU with Nigerian Universities (100%).\r\n2. Host the first Metaverse workshop on May 25-26 2022 (100%)\r\n3. Secure a collaboration meeting with at least one agency or arm of government in Nigeria (85%).\r\n4. Prepare and populate content on the Creativia website (100% done)\r\n5. Ensure Accepted NSL Papers are fully Published. (18/18 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (6 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2022-12-30 00:00:00",
			"to_dt": "2023-01-05 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion: Pr.\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "cosmas",
			"fr_dt": "2023-01-02 00:00:00",
			"to_dt": "2023-01-06 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100%\r\n- Under Review\r\n\r\nTitle 3: Metaverse paper for creativia (Dong-Seong Kim and Cosmas) (Conference version 100%\r\n~ Published in ICTC 2022.\r\n\r\nTitle 4: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 5: Survey with Dr. Hoa\r\n~ Submitted for English Correction\r\n\r\nTitle 6: Survey with Dr. Kim\r\n~ 20% progress\r\n~ ICUFN 2023 version to be completed this Friday 2023.01.06",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\n2022.03.01~ 2023.02.28\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135,\r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted with Minor Revision)\r\n- Awaiting EIC Decision\r\n\r\nTitle 8: IoT-26497-2022.R1, (Accepted with Minor Revision)\r\n-To submit the camera-ready copy 2022.12.31\r\n\r\nTitle 9: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 10: COMST-00569-2022\r\n-Under Review",
			"mnth_gls": "1. Submit ICUFN 2023 and one Survey paper by 2022.01.30 (50%).\r\n2. Continue Academic International collaboration meetings with Nigerian Universities (100%).\r\n3. Ensure Goodness and Love's papers are published (90%)\r\n4. Ensure a resubmission of all revised papers - (100%)\r\n5. Submit NRF proposal (80%)",
			"annl_gls": "1. Continue working with Nigerian Universities on metaverse (100%).\r\n2. Host the second Metaverse workshop on May 25-26 2023 (10%)\r\n3. Secure a collaboration meeting with at least one more university in the US or Canada (15%).\r\n4. Prepare and submit one Magazine paper based on the Creativia platform (10%)\r\n5. Ensure Accepted NSL Papers are fully Published. (3/30 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (10 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-01-02 00:00:00",
			"to_dt": "2023-01-06 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n- Irregular Repetition Slotted ALOHA 수식 파악중\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "",
			"mnth_gls": "o FBL 적용한 Irregular Repetition Slotted ALOHA 수식 구현",
			"annl_gls": "o SCIE 논문 1편, Hardware in the loop Survey 논문 작성\r\no BMS 관련 사업화"
		},
		{
			"user": "20195028",
			"fr_dt": "2023-01-02 00:00:00",
			"to_dt": "2023-01-06 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [95%] (In progress)\r\n-Performed two more simulation work\r\n-Add more graphs.\r\n-Calculate computational complexity.\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network [100%]\r\n\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE) (summited) [100%]\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Accepted) (IEEEIOT Journal)\r\n- Check the final version and submit to the journal.\r\nPaper 9:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (Accept)\r\n\r\nPaper 10: DNN for DDoS Attack Detection and Classification [IEE-TNSM][100%] (complete)",
			"mnth_gls": "Complete paper 04, and 06 and submit to the journal (Almost 85% task complete)\r\n- Target 01, 02, 03 completed\r\n- Complete ICTC paper and submit it.\r\n-Complete Paper 9 & paper 10",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n- Target journal 01, 04 and 05\r\n2. Participate 2 International Conferences.\r\n\r\n[Already received two acceptance from IEEE IoT journal, one as a first author, and another co-author ]\r\n[Participate ICUFN, ICTC 2022, MILCOM 2022 conference]"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-01-06 00:00:00",
			"to_dt": "2023-01-12 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion: Pr.\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "cosmas",
			"fr_dt": "2023-01-09 00:00:00",
			"to_dt": "2023-01-13 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100%\r\n- Major Revision: Resubmission date: 2023.01.14\r\n\r\nTitle 3: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 4: Survey with Dr. Hoa\r\n~ TE-2023-000007\r\n~ Submitted: 2023.01.09\r\n\r\nTitle 5: Survey with Dr. Kim\r\n~ 20% progress\r\n\r\nTitle 6: \r\n~ ICUFN 2023 in progress (to be completed this Friday 2023.01.20)",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\n2022.03.01~ 2023.02.28\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135,\r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted)\r\n- https://doi.org/10.1109/TITS.2022.3233536\r\n-In-production\r\n- Awaiting to pay for Over-length pages\r\n\r\nTitle 8: IoT-26497-2022.R1, (Accepted with Minor Revision)\r\n-Awaiting full Acceptance Letter\r\n\r\nTitle 9: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 10: COMST-00569-2022\r\n-Under Review",
			"mnth_gls": "1. Submit ICUFN 2023 and one Survey paper by 2022.01.23 (50%).\r\n2. Continue Academic International collaboration meetings with Nigerian Universities (100%).\r\n3. Ensure Goodness and Love's papers are published (90%)\r\n4. Ensure a resubmission of all revised papers - (100%)\r\n5. Submit NRF proposal (80%)",
			"annl_gls": "1. Continue working with Nigerian Universities on metaverse (100%).\r\n2. Host the second Metaverse workshop on May 25-26 2023 (10%)\r\n3. Secure a collaboration meeting with at least one more university in the US or Canada (15%).\r\n4. Prepare and submit one Magazine paper based on the Creativia platform (10%)\r\n5. Ensure Accepted NSL Papers are fully Published. (3/30 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (100%) (10 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-01-09 00:00:00",
			"to_dt": "2023-01-13 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n- Irregular Repetition Slotted ALOHA 수식 연구\r\n- Uplink NOMA collision rate 관련 수식 유도\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey\r\n\r\no KICS winter\r\n- Israel 과제 관련 학회 논문 작성중",
			"project_progress": "",
			"mnth_gls": "o FBL 적용한 Irregular Repetition Slotted ALOHA 수식 구현",
			"annl_gls": "o SCIE 논문 1편, Hardware in the loop Survey 논문 작성\r\no BMS 관련 사업화"
		},
		{
			"user": "saviour",
			"fr_dt": "2023-01-10 00:00:00",
			"to_dt": "2023-01-16 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.\r\n\r\n2) Saviour Multi-Hashing (SMuHa): A Quantum Resistant Security Algorithm for Offline Transactions (ICC 2023) Pure Wallet",
			"project_progress": "...",
			"mnth_gls": "1) Lab testing of the final Pure Wallet 2.0 application\r\n2) Start Medical record project\r\n3) introduce new member to layer 2 project",
			"annl_gls": "1) Complete the first commercial version of the Pure Wallet.\r\n\r\n2) Start the Pure Voting project or layer 2 solutions.\r\n\r\n3) Complete the layer 2 project."
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-01-13 00:00:00",
			"to_dt": "2023-01-19 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion: Pr.\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "",
			"fr_dt": "2023-01-16 00:00:00",
			"to_dt": "2023-01-20 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100% (Collaboration paper with Nigeria and Canada researchers)\r\n- Accepted with Minor corrections: In-Production\r\n\r\nTitle 3: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 4: Survey with Dr. Hoa\r\n~ TE-2023-000007\r\n~ Submitted: 2023.01.09\r\n\r\nTitle 5: Survey with Dr. Kim\r\n~ 20% progress\r\n\r\nTitle 6:\r\n~ ICUFN 2023 in progress (to be completed this Friday 2023.01.20)",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\n2022.03.01~ 2023.02.28\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135,\r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\nTitle 7: T-ITS-22-03-0723, (Accepted)\r\n- Published: 2023.01.09, https://doi.org/10.1109/TITS.2022.3233536\r\n\r\nTitle 8: IoT-26497-2022.R1, (Accepted)\r\n-In-Production\r\n\r\nTitle 9: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 10: COMST-00569-2022 (Love) \r\n-Under Review\r\nTitle 11: COMST-00569-2022 (Adi)\r\n-Under Review\r\nTitle 12: IoT-D-23-00023 (Vivian)\r\n-Under Review\r\nTitle 13: IoT-D-23-00055 (Love)\r\n-Under Review\r\nTitle 14: TII-23-0127\r\n-Under Review\r\nTitle 15: TE-2023-000007 (Hoa and Kim)\r\n-Under Review",
			"mnth_gls": "1. Submit ICUFN 2023 and one Survey paper by 2022.01.23 (50%).\r\n2. Continue Academic International collaboration meetings with Nigerian Universities (100%).\r\n3. Ensure Goodness and Love's papers are published (95%)\r\n4. Ensure a resubmission of all revised papers - (100%)\r\n5. Submit NRF proposal (90%)",
			"annl_gls": "1. Continue working with Nigerian Universities on metaverse (100%).\r\n2. Host the second Metaverse workshop on May 25-26 2023 (10%)\r\n3. Secure a collaboration meeting with at least one more university in the US or Canada (25%).\r\n4. Prepare and submit one Magazine paper based on the Creativia platform (10%)\r\n5. Ensure Accepted NSL Papers are fully Published. (5/30 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (100%) (13 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-01-20 00:00:00",
			"to_dt": "2023-01-26 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Fading Channels-Transaction of Parallel and Distribution: Submitted (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion: Pr.\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "cosmas",
			"fr_dt": "2023-01-25 00:00:00",
			"to_dt": "2023-01-27 00:00:00",
			"paper_progress": "Title 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100%\r\n- Published: 2023.01.17 \r\nAppl. Sci. 2023, 13(3), 1252; https://doi.org/10.3390/app13031252\r\n\r\nTitle 3: IEEE ITED-2022\r\n~In-Production\r\n\r\nTitle 4: Survey with Dr. Hoa\r\n~ TE-2023-000007\r\n~ Submitted: 2023.01.09\r\n\r\nTitle 5: Survey with Dr. Kim\r\n~ 20% progress\r\n\r\nTitle 6:\r\n~ ICUFN 2023 in progress (to be completed this Friday 2023.01.28)",
			"project_progress": "Second Authored works in NSL and ICT-CRC\r\n\r\n2022.03.01~ 2023.02.28\r\n\r\nTitle 1: Access-2022-03435,\r\nPublished:2022.05.09, 10.1109/ACCESS.2022.3173643\r\n\r\nTitle 2: ICTE-D-21-00585,\r\nPublished: 2022.06.19, https://doi.org/10.1016/j.icte.2022.06.003\r\n\r\nTitle 3: ITS-2022-04-0154\r\nPublished: 2022.08.06, https://doi.org/10.1049/itr2.12252\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: ADHOC-D-22-00135,\r\n-Published: 2022.11.24, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\nTitle 6: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\nTitle 7: T-ITS-22-03-0723, \r\n- Published: 2023.01.09, https://doi.org/10.1109/TITS.2022.3233536\r\n\r\nTitle 8: IoT-26497-2022.R1, (Accepted with Minor Revision)\r\n-Published: 2023.01.18, https://doi.org/10.1109/JIOT.2023.3237797\r\n\r\nTitle 9: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 10: COMST-00569-2022 (Love)\r\n-Under Review\r\n\r\nTitle 11: T-IV-23-01-0132 (Judith)\r\n-Under Review\r\n\r\nTitle 12: IoT-27616-2023 (Adi)\r\n-Under Review\r\n\r\nTitle 13: TII-23-0127 (Love)\r\n-Awaiting AE assignment\r\n\r\nTitle 14: IoT-D-23-00055 (Love)\r\n-Editor Invited\r\n\r\nTitle 15: IoT-D-23-00023 (Vivian)\r\n-Under Review",
			"mnth_gls": "1. Submit ICUFN 2023 and one Survey paper by 2023.01.27 (95%).\r\n2. Continue Academic International collaboration meetings with Nigerian Universities (100%).\r\n3. Ensure a resubmission of all revised papers - (100%)\r\n4. Submit NRF proposal (90%)",
			"annl_gls": "1. Continue working with Nigerian Universities on metaverse (100%).\r\n2. Host the second Metaverse workshop on May 25-26 2023 (10%)\r\n3. Secure a collaboration meeting with at least one more university in the US or Canada (15%).\r\n4. Prepare and submit one Magazine paper based on the Creativia platform (10%)\r\n5. Ensure Accepted NSL Papers are fully Published. (5/30 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (100%) (12 Achieved).\r\n8. Secure and submit NRF Proposal (90%)"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-01-27 00:00:00",
			"to_dt": "2023-02-02 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Target Journal: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTarget Journal: Transaction of Intelligent Transportaion: Pr.\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Revision\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-01-30 00:00:00",
			"to_dt": "2023-02-03 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n- Uplink NOMA collision rate 관련 수식 유도\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "",
			"mnth_gls": "o FBL 적용한 Irregular Repetition Slotted ALOHA 수식 구현",
			"annl_gls": "o SCIE 논문 1편, Hardware in the loop Survey 논문 작성\r\no BMS 관련 사업화"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-02-03 00:00:00",
			"to_dt": "2023-02-09 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Target Journal: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-02-06 00:00:00",
			"to_dt": "2023-02-10 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n- Uplink NOMA collision rate 관련 수식 유도\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey\r\n\r\no 네트워크 시뮬레이터 관련 survey 논문 작성중\r\n- 정보과학회 논문지",
			"project_progress": "ㅇ KICS 동계학술대회 발표",
			"mnth_gls": "o FBL 적용한 Irregular Repetition Slotted ALOHA 수식 구현",
			"annl_gls": "o SCIE 논문 1편, Hardware in the loop Survey 논문 작성\r\no BMS 관련 사업화"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-02-10 00:00:00",
			"to_dt": "2023-02-16 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Target Journal: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-02-17 00:00:00",
			"to_dt": "2023-02-23 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Target Journal: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications Surveys and Tutorials: Pr.",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-02-20 00:00:00",
			"to_dt": "2023-02-24 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n- Uplink NOMA collision rate 관련 수식 유도\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey\r\n\r\no 네트워크 시뮬레이터 관련 survey 논문 작성 완료\r\n- 정보과학회 논문지 작성 완료 및 제출",
			"project_progress": "o Saviour 특허 번역\r\no Sanjay 원격 근무 등록",
			"mnth_gls": "o FBL 적용한 Irregular Repetition Slotted ALOHA 수식 구현",
			"annl_gls": "o SCIE 논문 1편, Hardware in the loop Survey 논문 작성\r\no BMS 관련 사업화"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-02-24 00:00:00",
			"to_dt": "2023-03-02 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted-Minor Revision\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Survey paper with Dr. Pham- A Comprehensive Survey of Joint Radar and Communication Problem Formulation Approach- Target Journal: IEEE Communications",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-02-27 00:00:00",
			"to_dt": "2023-03-03 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n- IRSA 수식 활용 시뮬레이션 작성\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "",
			"mnth_gls": "o FBL 적용한 Irregular Repetition Slotted ALOHA 수식 구현",
			"annl_gls": "o SCIE 논문 1편, Hardware in the loop Survey 논문 작성\r\no BMS 관련 사업화"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-03-06 00:00:00",
			"to_dt": "2023-03-10 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구 Survey\r\n- IRSA-NOMA 수식 활용 시뮬레이션 작성\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "",
			"mnth_gls": "o FBL 적용한 Irregular Repetition Slotted ALOHA 수식 구현",
			"annl_gls": "o SCIE 논문 1편, Hardware in the loop Survey 논문 작성\r\no BMS 관련 사업화"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-04-03 00:00:00",
			"to_dt": "2023-04-07 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구\r\n- Markcov chain 기반 페이딩 채널 모델 구현 중\r\n\r\no Q-learning 기반 Relay-selection \r\n- FBL기반 수식 유도중\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "o 창업 디딤돌 과제 준비",
			"mnth_gls": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHAey\r\n- Markcov chain 기반 페이딩 채널 모델 구현\r\n\r\no Q-learning 기반 Relay-selection \r\n- Relay-selection 알고리즘 시뮬레이션 완료\r\n\r\no 창업 디딤돌 과제 제출",
			"annl_gls": "o SCIE 논문 1편, Deep reinforcement learning + Irregular Repetition Slotted ALOHA \r\no Hardware in the loop Survey 논문 작성\r\no KICS 논문 1편, Relay Selection using Q-learning\r\no BMS 관련 사업화"
		},
		{
			"user": "B00501",
			"fr_dt": "2023-04-03 00:00:00",
			"to_dt": "2023-04-07 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Trans. Emerg. Topics Comput.)\r\n- Under review\r\n\r\n2. Distributed Cloud Computing: From the Convergence Perspective of Cloud Computing and Networking (IEEE Commun. Mag.)\r\n- In preparation\r\n\r\n3. Study on blockchain for cloud/edge computing and IoT",
			"project_progress": "",
			"mnth_gls": "Submit 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-04-07 00:00:00",
			"to_dt": "2023-04-13 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Communications Letters",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "cosmas",
			"fr_dt": "2023-04-10 00:00:00",
			"to_dt": "2023-04-16 00:00:00",
			"paper_progress": "Paper research\t\r\nTitle 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100%\r\n- Published: 2023.01.17\r\nAppl. Sci. 2023, 13(3), 1252; https://doi.org/10.3390/app13031252\r\n\r\nTitle 3: XAI for Networked Robotic Systems for Smart Factory (Idea stage for the UK collaboration)\r\n-- Still searching for ideas.",
			"project_progress": "2023.03.01~ 2024.02.28\r\n\r\nTitle 1: https://doi.org/10.3390/app13031252 (First Author)\r\nPublished: 2023.01.17\r\n\r\nTitle 2: T-ITS-22-03-0723,\r\n- Published: 2023.04.09, https://doi.org/10.1109/TITS.2022.3233536\r\n\r\nTitle 3: ADHOC-D-22-00135,\r\n-Published: 2023.03.01, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\n\r\nTitle 6: IoT-26497-2022.R1, (Accepted with Minor Revision)\r\n-Published: 2023.01.18, https://doi.org/10.1109/JIOT.2023.3237797\r\n\r\n\r\nYet to be Published: \r\n\r\nTitle 7: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 8: IOTMAG-23-00086 (Love)\r\n-Under Review\r\n\r\nTitle 9: TII-23-0127 (Love)\r\n-Awaiting Reviewer Scores\r\n\r\nTitle 10: IoT-28533-2023 (Love)\r\n-Under Review\r\n\r\nTitle 11: IoT-D-23-00055 (Love)\r\n-Editor Invited\r\n\r\nTitle 12: IoT-D-23-00023 (Vivian)\r\n-Under Review\r\n\r\nTitle 13: KICS Journal (Vivian)\r\n-Under Review\r\n\r\nTitle 12: KICS Journal (Kim)\r\n-Under Review",
			"mnth_gls": "Monthly goals\r\n1. Submit IEEE ComGrid Conference in the UK (85%).\r\n2. Continue Academic International collaboration meetings with Nigerian Universities, TrigoPi Israel, and Horizon Project (100%).\r\n3. Ensure a resubmission of all revised papers - (100%)\r\n4. Follow up on ICT express paper under review (90%)",
			"annl_gls": "1. Continue working with Nigerian Universities on metaverse (100%).\r\n2. Host the second Metaverse workshop: (Suspended for too many workloads. )\r\n3. Secure a collaboration meeting with at least one more US or UK university (15%).\r\n4. Prepare and submit one Magazine paper based on the Creativia platform (Waiting for the NRF result first)\r\n5. Ensure Accepted NSL Papers are fully Published. (7/30 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (100%) (12 Achieved).\r\n8. Secure and submit NRF Proposal (100%)"
		},
		{
			"user": "20195028",
			"fr_dt": "2023-04-10 00:00:00",
			"to_dt": "2023-04-16 00:00:00",
			"paper_progress": "Accepted Journal:\r\nPaper 01: IoMT-Net, IEEE Internet Things of Journal, (Early Access), May 2022, doi: 10.1109/JIOT.2022.3176310 [100%]\r\nPaper 02: Multitasking UAV Surveillance System [ICUFN Conf.] (Published) [100%]\r\nPaper 03: Convolution Neural Network Inspired Mine Recognition for USS. [KICS summer, 2022](Published) [100%]\r\n\r\nPaper in Progress (First Author)\r\nPaper 04: Undersea Acoustic Target Detection Using CNN. [IEEE TII] [95%] (In progress)\r\n-Work in result discussion section\r\nPaper 05: RF Signal-Based Multipurpose UAV Surveillance System Using Deep Neural Network \r\n--> Writing introduction section\r\nPaper 06: Low-Complexity Convolution Neural Network for Drone Detection- Sensing RF Signal (IEEE) (summited) [100%]\r\nPaper 07: Anti-Drone Design Techniques and Technology- A Survey [IEEE Access] (In progress)[10%]\r\nPaper 08: Vision-based Drone Surveillance System Using CNN. [TVT] (In progress)[10%]",
			"project_progress": "Co-Author Paper:\r\nPaper 08: An Efficient Hybrid-DNN for DDoS Detection and Classification in Software-Defined IIoT Networks (Published) (IEEEIOT Journal)\r\nPaper 9:\r\nBlockchain Inspired Intruder UAV Localization Using Lightweight CNN for Internet of Battlefield Things (MILCOM-2022) [100%] (published)\r\n\r\nPaper 10: DNN for DDoS Attack Detection and Classification [IEE-TNSM][100%] (Major revision)\r\nPaper 11: Blockchain-Enabled Federated Intrusion Detection with Client Selection for Industrial CPS Networks. (In progress)\r\nPaper 12: Artificial Intelligence for Human Safety in Indoor Environment: A Survey .(In progress)\r\n\r\nPaper 13: A Survey on Quantum Computing Toward Advanced Technologies: Metaverse, Web 3.0, and Artificial Intelligence. (In progress)",
			"mnth_gls": "--Submit : Paper 4, and paper 5 in the journal.\r\n\r\n--> Learn advanced machine learning algorithms.\r\n\r\n--> Learn blockchain",
			"annl_gls": "1. Acceptance from 2 SCI Journals.\r\n\r\n2. Participate 2 International Conferences."
		},
		{
			"user": "B00501",
			"fr_dt": "2023-04-10 00:00:00",
			"to_dt": "2023-04-14 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Trans. Emerg. Topics Comput.)\r\n- Under review\r\n\r\n2. Distributed Cloud Computing: From the Convergence Perspective of Cloud Computing and Networking (IEEE Commun. Mag.)\r\n- In preparation\r\n\r\n3. Study on blockchain for cloud/edge computing and IoT",
			"project_progress": "",
			"mnth_gls": "Submit 2",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-04-10 00:00:00",
			"to_dt": "2023-04-14 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구\r\n- Markcov chain 기반 페이딩 채널 모델 구현 중\r\n\r\no Q-learning 기반 Relay-selection\r\n- FBL기반 수식 유도중\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "o 창업 디딤돌 과제 준비\r\n- 사업계획서 작성중",
			"mnth_gls": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHAey\r\n- Markcov chain 기반 페이딩 채널 모델 구현\r\n\r\no Q-learning 기반 Relay-selection\r\n- Relay-selection 알고리즘 시뮬레이션 완료\r\n\r\no 창업 디딤돌 과제 제출",
			"annl_gls": "o SCIE 논문 1편, Deep reinforcement learning + Irregular Repetition Slotted ALOHA\r\no Hardware in the loop Survey 논문 작성\r\no KICS 논문 1편, Relay Selection using Q-learning\r\no BMS 관련 사업화"
		},
		{
			"user": "saviour",
			"fr_dt": "2023-04-11 00:00:00",
			"to_dt": "2023-04-17 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.\r\n\r\n2) Saviour Multi-Hashing (SMuHa): A Quantum Resistant Security Algorithm for Offline Transactions (ICC 2023). Rejected.",
			"project_progress": "- Training of the new blockchain members\r\n- completed blockchain theory introduction.\r\n- will soon start implementation of blockchain network.",
			"mnth_gls": "- Complete PoA2 implementation, debugging and testing.\r\n- Complete the implementation of the medical record Smart contract, debugging and testing.",
			"annl_gls": "- Complete PoA2 implementation, debugging and testing.\r\n- Complete the implementation of the medical record Smart contract, debugging and testing."
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-04-14 00:00:00",
			"to_dt": "2023-04-20 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Submitted (Under Review)\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Communications Letters: In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "B00501",
			"fr_dt": "2023-04-17 00:00:00",
			"to_dt": "2023-04-21 00:00:00",
			"paper_progress": "1. Joint Partial Offloading and Resource Allocation for Parked Vehicle-assisted Multi-access Edge Computing (IEEE Trans. Emerg. Topics Comput.)\r\n- Under review\r\n\r\n2. Distributed Cloud Computing: From the Convergence Perspective of Cloud Computing and Networking (IEEE Commun. Mag.)\r\n- In preparation\r\n\r\n3. Study on blockchain for cloud/edge computing and IoT",
			"project_progress": "",
			"mnth_gls": "Finish (2)",
			"annl_gls": "- 2 SCI journals\r\n- Submission to numerous conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-04-17 00:00:00",
			"to_dt": "2023-04-21 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구\r\n- Markcov chain 기반 페이딩 채널 모델 구현 중\r\n\r\no Q-learning 기반 Relay-selection\r\n- FBL기반 수식 유도중\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "o 창업 디딤돌 과제 준비\r\n- 사업계획서 작성중\r\n\r\no 서울 COEX출장 4.19~4.20",
			"mnth_gls": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHAey\r\n- Markcov chain 기반 페이딩 채널 모델 구현\r\n\r\no Q-learning 기반 Relay-selection\r\n- Relay-selection 알고리즘 시뮬레이션 완료\r\n\r\no 창업 디딤돌 과제 제출",
			"annl_gls": "o SCIE 논문 1편, Deep reinforcement learning + Irregular Repetition Slotted ALOHA\r\no Hardware in the loop Survey 논문 작성\r\no KICS 논문 1편, Relay Selection using Q-learning\r\no BMS 관련 사업화"
		},
		{
			"user": "cosmas",
			"fr_dt": "2023-04-18 00:00:00",
			"to_dt": "2023-04-24 00:00:00",
			"paper_progress": "Cosmas\r\nReports from 2023.03.01~\r\nPaper research\tPaper research\r\n\r\nTitle 1:ICTE-D-22-00143 ~~ 100%\r\n-(Under Review).\r\n\r\nTitle 2: applsci-2128497, ~~100%\r\n- Published: 2023.01.17\r\nAppl. Sci. 2023, 13(3), 1252; https://doi.org/10.3390/app13031252\r\n\r\nTitle 3: XAI for Networked Robotic Systems for Smart Factory (Idea stage for the UK collaboration)\r\n-- Still searching for ideas.",
			"project_progress": "2023.03.01~ 2024.02.28\r\n\r\nTitle 1: https://doi.org/10.3390/app13031252 (First Author)\r\nPublished: 2023.01.17\r\n\r\nTitle 2: T-ITS-22-03-0723,\r\n- Published: 2023.04.09, https://doi.org/10.1109/TITS.2022.3233536\r\n\r\nTitle 3: ADHOC-D-22-00135,\r\n-Published: 2023.03.01, https://doi.org/10.1016/j.adhoc.2022.103026\r\n\r\n\r\nTitle 4: IoT-23106-2022,\r\n-Published: 2022.08.18, https://doi.org/10.1109/JIOT.2022.3199712\r\n\r\nTitle 5: IOT-D-22-00330R1,\r\n-Published: 2022.12.27, https://doi.org/10.1016/j.iot.2022.100676\r\n\r\n\r\nTitle 6: IoT-26497-2022.R1, (Accepted with Minor Revision)\r\n-Published: 2023.01.18, https://doi.org/10.1109/JIOT.2023.3237797\r\n\r\n\r\nYet to be Published:\r\n\r\nTitle 7: JCN22-DIV3-055 (Major Revision)\r\n~Awaiting Reviewer Scores\r\n\r\nTitle 8: IOTMAG-23-00086 (Love)\r\n-Under Review\r\n\r\nTitle 9: TII-23-0127 (Love)\r\n-Awaiting Reviewer Scores\r\n\r\nTitle 10: IoT-28533-2023 (Love)\r\n-Under Review\r\n\r\nTitle 11: IoT-D-23-00055 (Love)\r\n-Editor Invited\r\n\r\nTitle 12: IoT-D-23-00023 (Vivian)\r\n-Under Review\r\n\r\nTitle 13: KICS Journal (Vivian)\r\n-Under Review\r\n\r\nTitle 12: KICS Journal (Kim)\r\n-Under Review",
			"mnth_gls": "1. Submit IEEE ComGrid Conference in the UK (85%).\r\n2. Continue Academic International collaboration meetings with Nigerian Universities, TrigoPi Israel, and Horizon Project (100%).\r\n3. Ensure a resubmission of all revised papers - (100%)\r\n4. Follow up on ICT express paper under review (now with the editor)",
			"annl_gls": "1. Continue working with Nigerian Universities on metaverse (100%).\r\n2. Host the second Metaverse workshop: (Suspended for too many workloads. )\r\n3. Secure a collaboration meeting with at least one more US or UK university (15%).\r\n4. Prepare and submit one Magazine paper based on the Creativia platform (Waiting for the NRF result first)\r\n5. Ensure Accepted NSL Papers are fully Published. (7/30 achieved)\r\n6. First author in 1 SCI journal (100%).\r\n7. Second author in numerous SCI papers of NSL (100%) (12 Achieved).\r\n8. Secure and submit NRF Proposal (100%)"
		},
		{
			"user": "saviour",
			"fr_dt": "2023-04-18 00:00:00",
			"to_dt": "2023-04-24 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.\r\n\r\n2) Saviour Multi-Hashing (SMuHa): A Quantum Resistant Security Algorithm for Offline Transactions (ICC 2023). Rejected.",
			"project_progress": "- Training of the new blockchain members\r\n- completed blockchain theory introduction.\r\n- started implementation of blockchain network.",
			"mnth_gls": "- Completed PoA2 implementation, debugging and testing.\r\n- Completed the implementation of the medical record Smart contract, debugging and testing.",
			"annl_gls": "- Build the Pure Chain Ecosystem"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-04-21 00:00:00",
			"to_dt": "2023-04-27 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Submitted (Under Review)\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Communications Letters: In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-04-24 00:00:00",
			"to_dt": "2023-04-28 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구\r\n- Markcov chain 기반 페이딩 채널 모델 구현 중\r\n\r\no Q-learning 기반 Relay-selection\r\n- FBL기반 수식 유도중\r\n\r\no Writing KICS summer conference paper\r\n0 Repetition optimization in IRSA using PSO\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "o 창업 디딤돌 과제 준비\r\n- 사업계획서 제출완료",
			"mnth_gls": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHAey\r\n- Markcov chain 기반 페이딩 채널 모델 구현\r\n\r\no Q-learning 기반 Relay-selection\r\n- Relay-selection 알고리즘 시뮬레이션 완료\r\n\r\no 창업 디딤돌 과제 제출",
			"annl_gls": "o SCIE 논문 1편, Deep reinforcement learning + Irregular Repetition Slotted ALOHA\r\no Hardware in the loop Survey 논문 작성\r\no KICS 논문 1편, Relay Selection using Q-learning\r\no BMS 관련 사업화"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-05-05 00:00:00",
			"to_dt": "2023-05-11 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Minor Revision\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Communications Letters: Submitted",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-05-08 00:00:00",
			"to_dt": "2023-05-12 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구\r\n- Markcov chain 기반 페이딩 채널 모델 구현 중\r\n\r\no Q-learning 기반 Relay-selection\r\n- FBL기반 수식 유도중\r\n\r\no Writing KICS summer conference paper\r\n- Repetition optimization in IRSA using PSO (Submitted)\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "o 창업 디딤돌 과제 준비\r\n- 대면평가 완료(05.12)",
			"mnth_gls": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHAey\r\n- Markcov chain 기반 페이딩 채널 모델 구현\r\n\r\no Q-learning 기반 Relay-selection\r\n- Relay-selection 알고리즘 시뮬레이션 완료\r\n\r\no 창업 디딤돌 과제 제출",
			"annl_gls": "o SCIE 논문 1편, Deep reinforcement learning + Irregular Repetition Slotted ALOHA\r\no Hardware in the loop Survey 논문 작성\r\no KICS 논문 1편, Relay Selection using Q-learning\r\no BMS 관련 사업화"
		},
		{
			"user": "saviour",
			"fr_dt": "2023-05-09 00:00:00",
			"to_dt": "2023-05-15 00:00:00",
			"paper_progress": "1) Pure Voting (PV): An Offline Voting Algorithm (APCC 2022) Accepted.\r\n\r\n2) Saviour Multi-Hashing (SMuHa): A Quantum Resistant Security Algorithm for Offline Transactions (KICS 2023). P.",
			"project_progress": "- Continue implementation of blockchain network.",
			"mnth_gls": "- Complete documentation of the Pure Chain Ecosystem.\r\n- Start deployment of public layer 1 network.",
			"annl_gls": "- Build the Pure Chain Ecosystem"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-05-15 00:00:00",
			"to_dt": "2023-05-19 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구\r\n- Markcov chain 기반 페이딩 채널 모델 구현 중\r\n\r\no Q-learning 기반 Relay-selection\r\n- FBL기반 수식 유도중\r\n\r\no Writing KICS summer conference paper\r\n- Repetition optimization in IRSA using PSO (Submitted)\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "o 창업 디딤돌 과제 준비\r\n- 대면평가 미선정\r\n- 강소특구 시제품 제작사업 지원예정",
			"mnth_gls": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHAey\r\n- Markcov chain 기반 페이딩 채널 모델 구현\r\n\r\no Q-learning 기반 Relay-selection\r\n- Relay-selection 알고리즘 시뮬레이션 완료\r\n\r\no 강소특구 시제품 제작사업 지원",
			"annl_gls": "o SCIE 논문 1편, Deep reinforcement learning + Irregular Repetition Slotted ALOHA\r\no Hardware in the loop Survey 논문 작성\r\no KICS 논문 1편, Relay Selection using Q-learning\r\no BMS 관련 사업화"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-05-19 00:00:00",
			"to_dt": "2023-05-25 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Minor Revision\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Communications Letters: Submitted",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "wj0828",
			"fr_dt": "2023-05-22 00:00:00",
			"to_dt": "2023-05-26 00:00:00",
			"paper_progress": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHA 관련 연구\r\n- Markcov chain 기반 페이딩 채널 모델 구현 중\r\n\r\no Q-learning 기반 Relay-selection\r\n- FBL기반 수식 유도중\r\n\r\no Writing KICS summer conference paper\r\n- Repetition optimization in IRSA using PSO (Submitted)\r\n\r\no Writing ICMIC 2023\r\n- Making simulation\r\n\r\no Metaverse를 활용한 Hardware-in-the-loop Survey",
			"project_progress": "o 창업 디딤돌 과제 준비\r\n- 대면평가 미선정\r\n- 강소특구 시제품 제작사업 지원예정",
			"mnth_gls": "o Deep reinforcement learning + Irregular Repetition Slotted ALOHAey\r\n- Markcov chain 기반 페이딩 채널 모델 구현\r\n\r\no Q-learning 기반 Relay-selection\r\n- Relay-selection 알고리즘 시뮬레이션 완료\r\n\r\no 강소특구 시제품 제작사업 지원",
			"annl_gls": "o SCIE 논문 1편, Deep reinforcement learning + Irregular Repetition Slotted ALOHA\r\no Hardware in the loop Survey 논문 작성\r\no KICS 논문 1편, Relay Selection using Q-learning\r\no BMS 관련 사업화"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-05-26 00:00:00",
			"to_dt": "2023-06-01 00:00:00",
			"paper_progress": "1. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n2. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Communications Letters: Submitted",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-06-02 00:00:00",
			"to_dt": "2023-06-08 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n4. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Wireless Communications Letters: Revision-In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-06-09 00:00:00",
			"to_dt": "2023-06-15 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n4. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Wireless Communications Letters: Revision-In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-06-16 00:00:00",
			"to_dt": "2023-06-22 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Modulation Classification for Multipath Channels-Submitted: IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING (Under Review)\r\n\r\n4. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Wireless Communications Letters: Revision-In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-06-23 00:00:00",
			"to_dt": "2023-06-29 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-Submitted-In Progress \r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Target Journal: IEEE Wireless Communications Letters: Revision-In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-06-30 00:00:00",
			"to_dt": "2023-07-06 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Journal: IEEE Wireless Communications Letters: Revision-In Progress\r\n\r\n6. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-07-14 00:00:00",
			"to_dt": "2023-07-20 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Journal: IEEE Wireless Communications Letters: Submitted\r\n\r\n6. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-07-21 00:00:00",
			"to_dt": "2023-07-27 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Journal: IEEE Wireless Communications Letters: Submitted (Under Review)\r\n\r\n6. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: Submitted",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-07-28 00:00:00",
			"to_dt": "2023-08-03 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-\r\nTarget Journal: Physical Communications (In Progress)\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Journal: IEEE Wireless Communications Letters: (Under Review)\r\n\r\n6. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision:  (Submitted)",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-08-04 00:00:00",
			"to_dt": "2023-08-10 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-\r\nTarget Journal: Physical Communications (In Progress)\r\n\r\n5. Federated Learning-Based Joint Radar-Communication mmWave Beamtracking for V2X Communications- Journal: IEEE Wireless Communications Letters: (Under Review)\r\n\r\n6. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering: Under Review",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-08-11 00:00:00",
			"to_dt": "2023-08-17 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-08-18 00:00:00",
			"to_dt": "2023-08-24 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-08-25 00:00:00",
			"to_dt": "2023-08-31 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: Submitted",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-09-01 00:00:00",
			"to_dt": "2023-09-07 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision:",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-09-15 00:00:00",
			"to_dt": "2023-09-21 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: In Progress",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-09-22 00:00:00",
			"to_dt": "2023-09-28 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision: Submitted",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		},
		{
			"user": "sanjay",
			"fr_dt": "2023-10-13 00:00:00",
			"to_dt": "2023-10-19 00:00:00",
			"paper_progress": "1. Deep Q-Learning Based SCMA for URLLC in Industrial Wireless Networks- Telecommunication Systems (TELS): Accepted\r\n\r\n2. Backscatter-Enabled CR-NOMA Based Cooperative V2X Communication with Imperfect CSI- Vehicular Communications: Accepted\r\n\r\n3. Federated Learning Based Resource Allocation for V2X Communication-\r\nTransaction of Intelligent Transportaion: Submitted (Under Review)\r\n\r\n4. Federated Learning Based Modulation Classification for Multipath Channels-In Progress\r\n\r\n5. Dragonfly Interaction Algorithm for Optimization of Queuing Delay in Industrial Wireless Networks- Journal: Bionic Engineering, Minor Revision:",
			"project_progress": "",
			"mnth_gls": "Completion of paper and major revisions.",
			"annl_gls": "1. 2 Sci Journals\r\n2. Submission to conferences"
		}
	]
}

def populate():
    for row in data['rows']:
        PostDocReport.objects.create(**row)

if __name__ == '__main__':
    populate()
    print("working again")