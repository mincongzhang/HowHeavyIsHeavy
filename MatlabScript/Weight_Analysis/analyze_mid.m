function  analyze_mid()
%mid
mid1=[62	61	60	59	57	57	54	54	54	52	47	46	44	43	40	40	37	37	36	36	35	35	34	34	33	32	31	31	26	26	26	26	25	25	24	24	24	23	22	22	21	20	20	20	18	17	16	15	14	13	13	8	8	8	6	6	6	6	4	4	4	4	4	3	3	3	3	3	2	2	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
mid3=[57	55	54	47	47	44	38	37	34	33	33	27	21	20	20	20	20	20	19	19	17	17	17	12	10	10	8	6	5	5	5	5	4	4	3	3	3	3	3	3	3	3	3	2	2	2	2	1	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
mid5=[54	47	46	42	41	41	35	35	34	33	26	21	21	21	17	17	17	17	14	13	13	12	9	8	8	8	8	8	6	6	6	6	6	5	5	5	5	4	3	3	2	2	1	1	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
mid7=[54	49	48	47	38	38	33	30	29	26	26	25	25	24	21	20	20	20	20	19	19	15	15	13	13	13	10	9	8	8	8	8	6	6	6	6	5	4	3	3	3	3	3	2	2	2	2	2	2	2	2	1	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
mid9=[58	56	54	54	53	52	51	50	45	44	44	41	41	40	40	39	35	35	35	35	34	34	33	32	32	32	29	28	25	24	24	21	21	21	19	19	19	19	17	17	14	13	12	11	8	7	6	6	6	6	6	6	5	4	4	4	4	3	3	3	3	3	2	2	2	2	2	2	2	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
];
midbox1=mid1;
midbox3=mid3;
midbox5=mid5;
midbox7=mid7;
midbox9=mid9;
weight0=find(midbox1==0);
midbox1(weight0)=[NaN]; 
weight0=find(midbox3==0);
midbox3(weight0)=[NaN]; 
weight0=find(midbox5==0);
midbox5(weight0)=[NaN]; 
weight0=find(midbox7==0);
midbox7(weight0)=[NaN]; 
weight0=find(midbox9==0);
midbox9(weight0)=[NaN]; 
boxplot([midbox1' midbox3' midbox5' midbox7' midbox9'],'plotstyle','compact')
hold on;
weight0=find(mid1==0);
mid1(weight0)=[]; 
weight0=find(mid3==0);
mid3(weight0)=[]; 
weight0=find(mid5==0);
mid5(weight0)=[]; 
weight0=find(mid7==0);
mid7(weight0)=[]; 
weight0=find(mid9==0);
mid9(weight0)=[]; 
medianx=[1:5];
mediany=[median(mid1),median(mid3),median(mid5),median(mid7),median(mid9)];
plot(medianx,mediany,':');
set(gca,'XTick',1:5);
set(gca,'XTickLabel',{'0.1','0.3','0.5','0.7','0.9'});
title('Mid');

end

