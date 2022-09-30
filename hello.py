#!/usr/bin/env python3

import os, json

# env = {}

# for env_key, env_value in os.environ.items():
#     env[env_key] = env_value

# print("Content-Type: applucation/json")
# print()

# print(json.dumps(env))

print("Content-Type: text/html")
print()
print(f"<p>USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")