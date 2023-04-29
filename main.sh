#!/bin/bash

curl -i "https://api.waqi.info/feed/@10118/?token=91951b6471f2e8a4c9eee810000d54582cccfbaf" | grep -o '{.*}' | sed 's/\\r//g' > data.json