
# ExcelHelper

## Projekta process

### Ideja

Mūsu ideja ir izveidot tīmekļa vietni ar nosaukumu "ExcelHelper", lai cilvēkiem būtu vieglāk izsekot savus ienākumus un izmaksas. Mūsu tīmekļa vietnē lietotājs var ierakstīt savus ienākumus (Your income) ailītē un izmaksas (Your expense) ailītē. Nospiežot uz pogu "Get excel file" lietotājs saņem uz datoru excel failu, kurā ir divas lapas. Pirmajā lapā "Incomes" lietotājs saņem tabulu ar ienākumiem, otrajā lapā "Expenses" par izmaksām.

### Komunikācija un darba sadalīšana

Tā kā mēs strādājām komandā, mums bija jāapmainās ar kodiem. Lai to izpildītu mēs izveidojām github repozitoriju un strādājām caur GitHub vietni. Projekta gaitnē mēs iepazināmies ar tādām funkcijām kā "git push", "git pull", "git branch" u.c.

Lai izveidotu mūsu tīmekļa vietni, bija jāiztaisa Backend un Frontend, tāpēc sadalījām mūsu pienākumus, ka Evelīna strādāja ar Backend daļu, savukārt Agne ar Frontend.

## Backend

Galvenā problēma bija savienot Backend daļu, kas rakstīta python valodā, ar Frontend. Šim pienākumam izmantojām Django programmatūru un DWF (Django Web Framework). Vispirms izveidoju myapi ar DWF palīdzību un definēju serializers un viewsets, lai nodrošinātu datu izmaiņas un lasīšanu caur API. '[urls.py](https://urls.py/ "https://urls.py")' fails izmantojās, lai sasaistītu mūsu API punktus ar attiecīgajiem viewsets.

Vislielāko darba laiku aizņēma fails '[views.py](https://views.py/ "https://views.py")'. Šajā failā mums ļoti palīdzēja openpyxl bibliotēka. Klasē ExcelManager pārbauda, vai Excel fails jau eksistē, un ja nē, tad to izveido. Ja fails jau eksistē, tad tiek atvērts un iegūta norādītā lapa. Ja fails nepastāv, tiek izveidots jauns fails ar norādīto lapu. Klase IncExpApi  apstrādā POST pieprasījumus uz /api/incexp. Ja pieprasījumā ir dati par ienākumiem (incomeItems), tad tiek izveidoti jauni dati no šiem ienākumiem, un šie dati tiek ierakstīti Excel failā lapā 'Incomes'. Ja ir dati par izmaksām (expenseItems), tad šie dati tiek ierakstīti Excel faila lapā 'Expenses'.
