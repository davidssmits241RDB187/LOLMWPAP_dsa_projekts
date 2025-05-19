# Datu struktūras un algoritmi(1) Noslēguma projekts "League of Legends match winner probability analysis program" (LOLMWPAP)

## **Programmas funkcionalitātes apraksts**

### Programmas uzdevums ###
```
Programma 'LOLMWPAP' veic publiski pieejamo 'League of Legends (Riot Game 2009)' elektroniskā sporta turnīru maču un komandu datu analīzi un nolasa tuvāko maču komandu saturu lai noteiktu katras komandas iespējas uzvarēt vienai pret otru.
```
### Izmantotās bibliotēkas
* dataclasses
* os.path
* json
* requests
* unicodedata
* ast
* datetime
* timedelta
* BeautifulSoup
* Tag

## **Programmas izmantošanas ceļvedis**
```

```

## Programmas struktūras un koda apraksts
Programma ir strukturizēta 3 pamatpgrupās:
<details>
<summary>classes</summary>
<details>
<summary>coefficients.py</summary>

</details>
</details>
<details>
<summary>services</summary>

</details>
<details>
<summary>controllers</summary>

</details>



## *Iespējamās programmas kļūmes*
* Saitu [[season](season-S15/split-Spring/tournament-ALL/), [teams_list_address](https://gol.gg/teams/list/),[teams_stats_address](https://gol.gg/teams/),[tournament_list_address](https://gol.gg/tournament/ajax.trlist.php),[tournament_address](https://gol.gg/tournament/tournament-matchlist/),[golgg_address](https://gol.gg/),[leaguepedia_address](https://lol.fandom.com/wiki/League_of_Legends_Esports_Wiki)] nobrukšana, slēgšanās ciet, datu privatizēšana, datu atrašanās vietas un etiķetes izmainīšana.

## Potenciālie programmas uzlabojumi
* `MatchController` klases `self.history` atribūta pievienošana komandu izvērtēšanas procesā.
* `Player` klases komandas biedru un pretinieku vēstures izveidošana un pievienošana `MatchController` komandu izvērtēšanas procesā.
* Tiešraides mača komandu izanalizēšana, salīdzīnot mača stāvokli ar komandu datiem, klasēs `Team` un `Player`, kā arī izveidot jaunus koeficientus klasē `Coefficients`.