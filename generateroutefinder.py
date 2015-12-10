import sqlite3, os

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect(os.path.expanduser('~/eve.db'))

con.row_factory = dict_factory

c = con.cursor()

c.execute("select solarSystemID, solarSystemName from mapSolarSystems;")

results = c.fetchall()

systemIds = {}
systemNames = {}
for res in results:
    res["solarSystemName"] = res["solarSystemName"].lower()
    systemIds[res["solarSystemName"]] = res["solarSystemID"]
    systemNames[res["solarSystemID"]] = res["solarSystemName"]

c.execute("select fromSolarSystemID, toSolarSystemID from mapSolarSystemJumps;")

results = c.fetchall()

for result in results:
    f = result["fromSolarSystemID"]
    t = result["toSolarSystemID"]
    fromName = systemNames[f]
    toName = systemNames[t]
    print "connected_by_gate(%s, %s)." % (f, t)
