import pandas as pd
survival_unemp = pd.read_csv("C:/My Files/Excelr/08 - Survival Analysis/PythonCodes/survival_unemployment1.csv")
survival_unemp.head()
survival_unemp.describe()

survival_unemp["spell"].describe()
T = survival_unemp.spell

from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(T,event_observed=survival_unemp.event)
kmf.plot()

survival_unemp.ui.value_counts()
kmf.fit(T[survival_unemp.ui==1], survival_unemp.event[survival_unemp.ui==1], label='1')
ax = kmf.plot()
kmf.fit(T[survival_unemp.ui==0], survival_unemp.event[survival_unemp.ui==0], label='0')
kmf.plot(ax=ax)
