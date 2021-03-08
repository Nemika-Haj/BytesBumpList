"""
MIT License

Copyright (c) 2021 Nemika

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from flask import Flask, render_template, redirect, url_for

import humanfriendly

from PyJS import JSON
from PyJS.modules import fs

from core import discordAPI
from core.database import Servers
from core.routes import route_for

app = Flask(__name__)

settings = JSON.parse(fs.createReadStream('settings.json'))
settings["len"] = len
settings["human"] = humanfriendly

@app.errorhandler(404)
def _404Err(err):
    return redirect(url_for('index'))

@app.route("/")
def index():
    return render_template('index.html', servers=Servers.get_all(),**settings)

@app.route(**route_for('view_server_default'), defaults={"serverID": None})
@app.route(**route_for('view_server'))
def view_server(serverID):
    if not serverID:
        redirect(url_for('index'))

    server = Servers.get_one(_id=int(serverID))

    _data = discordAPI.get_guild(serverID)

    inv = discordAPI.get_invite(server['invite']).json()

    _data["invite"]= f"https://discord.gg/{inv['code']}"

    return render_template('view_server.html', server=server, discord=_data, **settings)

app.run(debug=True)