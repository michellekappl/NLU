# Natural Language Understanding for multiple Languages

## File Structure
### *Rasa*
- new implementation of Rasa complete with the integration of XLM
- new custom component "CorrectSpelling" in german and english for spelling correction and lemmatization
### *Dataset*
- BoRis dataset german/english
- shortened dataset for initial testing
- script used to help with annotation
### *Results*
- midterm results
- final results

---
## How to train the model
### *Prerequisites:*
 - [Rasa](https://rasa.com/docs/rasa/installation/)
 - [Poetry](https://python-poetry.org/docs/)

### *Different configurations:*
Use one of the following commands to run our rasa pipeline:


<details><summary><em>Base</em></summary>
<p>

  - german: 
```bash 
rasa test nlu --nlu data/germanNLU.yml --config configs/config-base-german.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/base
```
- german with lemmatizer and spellchecker:
```bash
rasa test nlu --nlu data/germanNLU.yml --config configs/config-base-german-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/base-lem-spell
```
  - english:
```bash  
rasa test nlu --nlu data/englishNLU.yml --config configs/config-base-english.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/base
```
- english with lemmatizer and spellchecker:
```bash
rasa test nlu --nlu data/germanNLU.yml --config configs/config-base-german-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/base-lem-spell
```
  - multilingual:
```bash
rasa test nlu --config configs/config-base-mult.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/mult/base
```
  
</p>
</details>

<details><summary><em>Bert</em></summary>
<p>

  - german: 
```bash 
rasa test nlu --nlu data/germanNLU.yml --config configs/config-bert-german.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/bert
```
- german with lemmatizer and spellchecker:
```bash
rasa test nlu --nlu data/germanNLU.yml --config configs/config-bert-german-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/bert-lem-spell
```
  - english:
```bash 
rasa test nlu --nlu data/englishNLU.yml --config configs/config-bert-english.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/bert
```
- english with lemmatizer and spellchecker:
```bash
rasa test nlu --nlu data/englishNLU.yml --config configs/config-bert-english-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/bert-lem-spell
```
  - multilingual:
```bash
rasa test nlu --config configs/config-bert-mult.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/mult/bert
```
  
</p>
</details>

<details><summary><em>XLM</em></summary>
<p>

  - german: 
```bash 
rasa test nlu --nlu data/germanNLU.yml --config configs/config-xlm-german.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/xlm
```
- german with lemmatizer and spellchecker:
```bash
rasa test nlu --nlu data/germanNLU.yml --config configs/config-xlm-german-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/german/xlm-lem-spell
```
  - english:
```bash
rasa test nlu --nlu data/englishNLU.yml --config configs/config-xlm-english.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/xlm
```
- english with lemmatizer and spellchecker:
```bash
rasa test nlu --nlu data/englishNLU.yml --config configs/config-xlm-english-lem-spell.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/english/xlm-lem-spell
```
  - multilingual:
```bash
rasa test nlu --config configs/config-xlm-mult.yml --cross-validation --runs 1 --folds 5 --out ../gridresults/mult/xlm
```

</p>
</details>

Alternatively you can test all models using the script
```bash
./run-all.sh

