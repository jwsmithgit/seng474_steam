import sys
import json

print( "usage python .\\6removekeyauto.py data.json outfile.json" )

with open(sys.argv[1], 'r') as json_data:
    data = json.load(json_data)

keys = ["steam_appid",
        "achievements",
        "price_overview",
        "platforms",
        "detailed_description",
        "required_age",
        "metacritic",
        "about_the_game",
        "short_description",
        "developers",
        "type",
        "supported_languages",
        "website",
        "publishers",
        "pc_requirements",
        "recommendations",
        "is_free",
        "packages",
        "support_info",
        "package_groups",
        "release_date",
        "linux_requirements",
        "mac_requirements",
        "developer",
        "publisher",
        "score_rank",
        "owners",
        "owners_variance",
        "players_forever",
        "players_forever_variance",
        "players_2weeks",
        "players_2weeks_variance",
        "average_forever",
        "average_2weeks",
        "median_forever",
        "median_2weeks",
        "ccu",
        "price",
        "positive",
        "negative",
        "dlc",
        "demos",
        "movies",
        "controller_support",
        "reviews",
        "legal_notice",
        "drm_notice",
        "ext_user_account_notice",
        "fullgame"
        ]

for item in data:
    for key in keys:
        if key in data[item]:
            data[item].pop(key)

with open(sys.argv[2], 'w') as outfile:
    json.dump(data, outfile, separators=(',', ':'))
