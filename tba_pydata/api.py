import requests
import pandas

from tba_pydata import constants

TBA = 'https://www.thebluealliance.com/api/v3'
HEADER = {'X-TBA-Auth_Key': 'SfIaTaudX9MLcouEO0NbEktueyhKcNJ8PlBlrHuw4yXWx1D30fVQxtLHERg7QZVG'}
YEAR = 2018


def tba_fetch(path):
    resp = requests.get(TBA + path, headers=HEADER)
    print(TBA + path, resp.status_code)
    return resp.json()


def status():
    res = tba_fetch('/status')
    return pandas.Series(res)


def teams(page=-1, year=None):
    def get_team_page(page, year):
        if year is None:
            return tba_fetch('/teams/' + str(page))
        else:
            return tba_fetch('/teams/%d/%d' % (year, page))

    if page != -1:
        res = get_team_page(page, year)
        if len(res) == 0:
            return None
        else:
            data = pandas.DataFrame(res)
    else:
        teamlist = []
        i = 0
        reslen = -1
        while reslen != 0:
            res = get_team_page(i, year)
            reslen = len(res)
            if reslen > 0:
                teamlist += res
            i += 1
        data = pandas.DataFrame(teamlist)

    champs_year = '2018' if (year is None or year < 2017) else str(year)
    data['home_championship'] = data.home_championship.apply(lambda val: val[champs_year] if val is not None else None)
    data['state_prov'] = data.state_prov.apply(lambda loc: constants.STATE_PROV_NORMALIZATION[loc])
    data.index = data['key']

    return data


print(teams(year=2018).groupby('state_prov').size())
