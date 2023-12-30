import pandas as pd
import random
import self as self
from clickhouse_driver import Client

client = Client(host='localhost', port=9000, settings={'use_numpy': True})

create_query = """
create table dbtdb.mouse_movements(
id UInt32,
x UInt16,
y UInt16,
deltaX UInt16,
deltaY UInt16,
clientTimeStamp Float32,
button Int8,
target String
) Engine = MergeTree() ORDER BY id;
"""
client.execute(create_query)

x = [random.randint(a=1, b=1500) for i in range(10000)]
y = [random.randint(a=1, b=1500) for i in range(10000)]
deltaX = [x[i] - x[i-1] if i != 0 else 0 for i in range(0, len(x))]
deltaY = [y[i] - x[i-1] if i != 0 else 0 for i in range(0, len(x))]
clientTimeStamp = [random.uniform(a=0.0005, b=800) for i in range(10000)]
button = [random.randint(a=1, b=200) for i in range(10000)]
targets = ['Google Chrome',
           'Microsoft Word',
           'Adobe Photoshop',
           'Visual Studio Code',
           'Slack',
           'Microsoft Excel',
           'Safari',
           'iTunes',
           'Final Cut Pro',
           'Adobe Illustrator',
           'Zoom',
           'Logic Pro',
           'Adobe Premiere Pro',
           'Xcode',
           'Microsoft PowerPoint',
           'WhatsApp',
           'Skype',
           'Zoom',
           'Photos',
           'Spotify']
target = [random.choice(targets) for i in range(10000)]
df = pd.DataFrame({'id': [i for i in range(10000)], 'x': x, 'y': y, 'deltaX': deltaX,
                   'deltaY': deltaY, 'clientTimeStamp': clientTimeStamp, 'button': button, 'target': target})
client.insert_dataframe('INSERT INTO dbtdb.mouse_movements VALUES', df)
