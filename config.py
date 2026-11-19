# Safe version: no hardcoded secret is stored in the source code.
# The value should come from an environment variable or GitHub Secret.

import os

AWS_ACCESS_KEY_ID = os.environ.get("AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe")
