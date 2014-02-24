function analyze_bass(  )
%bass
bass1=[51	43	41	40	37	36	36	35	34	28	26	26	26	25	22	21	21	20	20	20	20	19	19	18	17	17	17	17	13	9	9	8	7	6	6	6	6	6	6	5	5	4	3	3	3	3	3	3	3	2	2	2	2	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
bass3=[46	35	35	34	30	25	22	21	21	21	19	13	10	8	6	6	6	6	6	5	4	4	3	3	3	3	3	2	2	2	2	2	2	2	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
bass5=[39	35	32	32	31	27	24	24	23	21	21	20	20	20	20	17	17	17	15	14	13	13	12	12	11	10	8	8	8	6	6	6	5	5	5	5	4	4	3	3	3	3	3	3	2	2	2	2	1	1	1	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
bass7=[54	49	45	44	40	40	38	37	35	34	34	33	33	33	31	29	29	25	24	24	24	21	20	20	19	19	19	19	17	16	14	14	13	13	13	12	10	8	8	8	8	6	6	6	6	5	5	4	4	4	4	3	3	3	3	3	3	2	2	2	2	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
bass9=[62	61	60	59	58	57	57	57	56	55	54	54	54	54	54	54	54	53	52	52	50	48	47	47	47	47	47	46	44	44	44	42	41	41	41	40	38	38	37	35	35	35	34	34	33	33	33	32	32	26	26	26	26	25	25	24	21	20	20	19	17	17	15	15	13	8	8	8	8	8	6	6	5	4	4	4	4	3	3	2	2	2	2	1	1	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0
];

bassbox1=bass1;
bassbox3=bass3;
bassbox5=bass5;
bassbox7=bass7;
bassbox9=bass9;
weight0=find(bassbox1==0);
bassbox1(weight0)=[NaN]; 
weight0=find(bassbox3==0);
bassbox3(weight0)=[NaN]; 
weight0=find(bassbox5==0);
bassbox5(weight0)=[NaN]; 
weight0=find(bassbox7==0);
bassbox7(weight0)=[NaN]; 
weight0=find(bassbox9==0);
bassbox9(weight0)=[NaN]; 
boxplot([bassbox1' bassbox3' bassbox5' bassbox7' bassbox9'],'plotstyle','compact')
hold on;
weight0=find(bass1==0);
bass1(weight0)=[]; 
weight0=find(bass3==0);
bass3(weight0)=[]; 
weight0=find(bass5==0);
bass5(weight0)=[]; 
weight0=find(bass7==0);
bass7(weight0)=[]; 
weight0=find(bass9==0);
bass9(weight0)=[]; 
medianx=[1:5];
mediany=[median(bass1),median(bass3),median(bass5),median(bass7),median(bass9)];
plot(medianx,mediany,':');
set(gca,'XTick',1:5);
set(gca,'XTickLabel',{'0.1','0.3','0.5','0.7','0.9'});
title('Bass');


end

