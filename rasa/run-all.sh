#!/bin/bash

rasa test nlu --nlu data/germanNLU.yml --config configs/config-bert-german.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/bert
rasa test nlu --nlu data/germanNLU.yml --config configs/config-base-german.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/base
rasa test nlu --nlu data/germanNLU.yml --config configs/config-xlm-german.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/xlm

rasa test nlu --nlu data/germanNLU.yml --config configs/config-base-german-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/base-lem-spell
rasa test nlu --nlu data/germanNLU.yml --config configs/config-bert-german-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/bert-lem-spell
rasa test nlu --nlu data/germanNLU.yml --config configs/config-xlm-german-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/xlm-lem-spell


rasa test nlu --nlu data/englishNLU.yml --config configs/config-bert-english.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/bert
rasa test nlu --nlu data/englishNLU.yml --config configs/config-base-english.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/base
rasa test nlu --nlu data/englishNLU.yml --config configs/config-xlm-english.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/xlm

rasa test nlu --nlu data/englishNLU.yml --config configs/config-base-english-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/base-lem-spell
rasa test nlu --nlu data/englishNLU.yml --config configs/config-bert-english-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/bert-lem-spell
rasa test nlu --nlu data/englishNLU.yml --config configs/config-xlm-english-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/xlm-lem-spell

rasa test nlu --config configs/config-bert-mult.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/mult/bert
rasa test nlu --config configs/config-base-mult.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/mult/base
rasa test nlu --config configs/config-xlm-mult.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/mult/xlm
