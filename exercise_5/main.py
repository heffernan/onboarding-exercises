# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
import requests

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    response = requests.get("https://api.chucknorris.io/jokes/random")
    joke = response.json()['value']
    res = {}
    res['joke'] = joke
    res['char_count'] = get_letter_count(joke)
    return res

def get_letter_count(s):
    arr = [0] * 26
    for c in s.lower():
        if 'a' <= c <= 'z':
            arr[ord(c)-97] += 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_count = dict(zip(alphabet, arr))
    return char_count


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]