#!/bin/bash

rasa test nlu --nlu data/germanNLU.yml --config configs/config-base-german.yml configs/config-base-german-lem-spell.yml --out ../gridresults/german/base
rasa test nlu --nlu data/germanNLU.yml --config configs/config-bert-german.yml configs/config-bert-german-lem-spell.yml --out ../gridresults/german/bert

rasa test nlu --nlu data/englishNLU.yml --config configs/config-base-english.yml configs/config-base-english-lem-spell.yml --out ../gridresults/english/base
rasa test nlu --nlu data/englishNLU.yml --config configs/config-bert-english.yml configs/config-bert-english-lem-spell.yml --out ../gridresults/english/bert

