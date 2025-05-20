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

<ul>

<details>
<summary>coefficients.py</summary>
<ul>
<details>
<summary>atribūti</summary>
<ul>
<em>Komandas statistikas koeficienti (kopā 5), visi atribūti ir saraksti, inicializēti kā [1.0,1.0]:</em>

<li>gold_per_minute_or_gold_lead</li>

<li>kills_per_game</li>

<li>avg_tower_difference</li>

<li>dragons_per_game</li>

<li>nashor_per_game</li>
<p></p>
<em> Spēlētāju specifiskie koeficienti katrai lomai (kopā 5), visi atribūti ir saraksti, inicializēti kā [1.0,1.0]: </em>
<li>_kda</li>

<li>_csm</li>

<li>_dmg</li>

<li>vspm</li>

</ul>
</details>

</ul>
<ul>
<details>
<summary>funkcionalitāte</summary>
<ul>
Tiek izmantota lai sekotu līdzi komandu un spēlētāju atsevišķu datu ietekmes līmenim mača iznākumam.
</ul>
</details>
</ul>
<ul>
<details>
<summary>metodes</summary>
<ul>
<details>
<summary>evaluate_coefficients</summary>
<ul>
<details>
<summary>parametri</summary>
<ul>
<li>self</li>
</ul>
<ul>
<li>winning_team:Team</li>
</ul>
<ul>
<li>losing_team:Team</li>
</ul>
</details>
</ul>
<ul>
<details>
<summary>funkcionalitāte</summary>
<ul>
Salīdzināt iedoto komandu datus, kuriem var izveidot koeficientus, un atjaunina koeficentus,sekojot algoritmam:
1. Higher value on winning_team -> values coefficient[0]+=1
2.Higher value on losing_team -> values coefficient[1]+=1
</ul>
</details>
</ul>
<ul>
<details>
<summary>izvade</summary>
<ul>
---
</ul>
</details>
</ul>
</details>
</ul>
</details>
</ul>
</ul>



</details>
</details>
</details>

<summary>services</summary>

</details>
<details>
<summary>controllers</summary>

</details>



## *Iespējamās programmas kļūmes*
* Saitu [[season](season-S15/split-Spring/tournament-ALL/), [teams_list_address](https://gol.gg/teams/list/),[teams_stats_address](https://gol.gg/teams/),[tournament_list_address](https://gol.gg/tournament/ajax.trlist.php),[tournament_address](https://gol.gg/tournament/tournament-matchlist/),[golgg_address](https://gol.gg/),[leaguepedia_address](https://lol.fandom.com/wiki/League_of_Legends_Esports_Wiki)] nobrukšana, slēgšanās ciet, datu privatizēšana, datu atrašanās vietas un etiķetes izmainīšana, kā arī datu novecošana.

## Potenciālie programmas uzlabojumi
* `MatchController` klases `self.history` atribūta pievienošana komandu izvērtēšanas procesā.
* `Player` klases komandas biedru un pretinieku vēstures izveidošana un pievienošana `MatchController` komandu izvērtēšanas procesā.
* Tiešraides mača komandu izanalizēšana, salīdzīnot mača stāvokli ar komandu datiem, klasēs `Team` un `Player`, kā arī izveidot jaunus koeficientus klasē `Coefficients`.