function analyze_treble()

%treble
treble1=[57	57	54	53	52	50	48	47	47	47	44	44	44	43	42	41	38	35	35	35	34	34	34	33	32	31	29	26	26	25	24	24	22	21	21	20	20	20	20	13	13	13	13	10	9	8	8	8	8	7	6	6	6	6	5	5	4	4	4	4	3	3	3	3	3	3	2	2	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
treble3=[58	54	44	33	33	26	26	26	25	25	24	24	19	19	17	17	14	13	13	13	12	11	8	8	8	6	6	5	5	4	4	4	4	4	3	3	3	3	3	2	2	2	2	2	2	2	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
treble5=[54	49	47	41	33	33	28	21	20	20	19	19	19	14	14	13	12	10	8	8	6	6	5	4	3	3	3	3	3	3	3	3	3	3	2	2	2	2	2	2	2	2	1	1	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
treble7=[54	54	54	46	41	40	39	38	37	35	35	35	34	34	33	32	30	27	24	23	21	20	20	20	20	20	19	19	18	17	17	17	17	15	15	12	8	8	6	6	6	6	6	5	5	4	4	4	3	3	3	2	2	2	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
treble9=[62	61	60	59	57	56	55	54	54	52	51	47	46	45	41	40	40	40	38	37	37	36	36	35	35	34	32	32	31	29	26	26	25	25	24	22	21	21	21	21	21	20	19	17	17	17	17	16	15	10	9	8	8	8	6	6	6	6	6	6	6	5	5	5	3	3	2	2	2	1	1	1	1	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
treblebox1=treble1;
treblebox3=treble3;
treblebox5=treble5;
treblebox7=treble7;
treblebox9=treble9;
weight0=find(treblebox1==0);
treblebox1(weight0)=[NaN]; 
weight0=find(treblebox3==0);
treblebox3(weight0)=[NaN]; 
weight0=find(treblebox5==0);
treblebox5(weight0)=[NaN]; 
weight0=find(treblebox7==0);
treblebox7(weight0)=[NaN]; 
weight0=find(treblebox9==0);
treblebox9(weight0)=[NaN]; 
boxplot([treblebox1' treblebox3' treblebox5' treblebox7' treblebox9'],'plotstyle','compact')
hold on;
weight0=find(treble1==0);
treble1(weight0)=[]; 
weight0=find(treble3==0);
treble3(weight0)=[]; 
weight0=find(treble5==0);
treble5(weight0)=[]; 
weight0=find(treble7==0);
treble7(weight0)=[]; 
weight0=find(treble9==0);
treble9(weight0)=[]; 
medianx=[1:5];
mediany=[median(treble1),median(treble3),median(treble5),median(treble7),median(treble9)];
plot(medianx,mediany,':');
set(gca,'XTick',1:5);
set(gca,'XTickLabel',{'0.1','0.3','0.5','0.7','0.9'});
title('Treble');


end

