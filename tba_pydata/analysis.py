"""
Created on Wed Feb 14 19:21:30 2018

@author: wes
"""
import pandas
import statsmodels.api as sm


def get_opr_matrices(df):
    df = df[['key', 'red_score', 'blue_score', 'red1', 'red2', 'red3', 'blue1', 'blue2', 'blue3']]
    melted = pandas.melt(df, ['key', 'red_score', 'blue_score']).sort_values('value')
    teams = melted.value.unique()
    scores = pandas.melt(df[['key', 'red_score', 'blue_score']], ['key']).sort_values('key')
    scores.index = scores.key + '_' + scores.variable
    oprmat = pandas.DataFrame(0, index=scores.key + '_' + scores.variable, columns=teams)

    for (i, record) in melted.iterrows():
        if record.variable.startswith('blue'): oprmat.loc[record.key + '_blue_score', record.value] = 1
        if record.variable.startswith('red'): oprmat.loc[record.key + '_red_score', record.value] = 1

    return oprmat, teams, scores


def get_opr_model(df, fit=True):
    oprmat, teams, scores = get_opr_matrices(df)
    reg = sm.OLS(scores.value, oprmat)

    if fit:
        return reg.fit()
    else:
        return reg