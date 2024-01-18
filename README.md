
# ExcelHelper

## Projekta process

### Ideja

Mūsu ideja ir izveidot tīmekļa vietni ar nosaukumu "ExcelHelper", lai cilvēkiem būtu vieglāk izsekot savus ienākumus un izmaksas. Mūsu tīmekļa vietnē lietotājs var ierakstīt savus ienākumus (Your income) ailītē un izmaksas (Your expense) ailītē. Nospiežot uz pogu "Get excel file" lietotājs saņem uz datoru excel failu, kurā ir divas lapas. Pirmajā lapā "Incomes" lietotājs saņem tabulu ar ienākumiem un kopējo ienākumu summu(Total), otrajā lapā "Expenses" par izmaksām.

### Komunikācija un darba sadalīšana

Tā kā mēs strādājām komandā, mums bija jāapmainās ar kodiem. Lai to izpildītu mēs izveidojām github repozitoriju un strādājām caur GitHub vietni. Projekta gaitnē mēs iepazināmies ar tādām funkcijām kā "git push", "git pull", "git branch" u.c.

Lai izveidotu mūsu tīmekļa vietni, bija jāiztaisa Backend un Frontend, tāpēc sadalījām mūsu pienākumus, ka Evelīna strādāja ar Backend daļu, savukārt Agne ar Frontend.

### Backend

Galvenā problēma bija savienot Backend daļu, kas rakstīta python valodā, ar Frontend. Šim pienākumam izmantojām Django programmatūru un DWF (Django Web Framework). Vispirms izveidojām myapi ar DWF palīdzību un definējām serializers un viewsets, lai nodrošinātu datu izmaiņas un lasīšanu caur API. '[urls.py](https://urls.py/ "https://urls.py")' fails izmantojās, lai sasaistītu mūsu API punktus ar attiecīgajiem viewsets.

Vislielāko darba laiku aizņēma fails '[views.py](https://views.py/ "https://views.py")'. Šajā failā mums ļoti palīdzēja openpyxl bibliotēka. Klasē ExcelManager pārbauda, vai Excel fails jau eksistē, un ja nē, tad to izveido. Ja fails jau eksistē, tad tiek atvērts un iegūta norādītā lapa. Ja fails nepastāv, tiek izveidots jauns fails ar norādīto lapu. Klase IncExpApi  apstrādā POST pieprasījumus uz /api/incexp. Ja pieprasījumā ir dati par ienākumiem (incomeItems), tad tiek izveidoti jauni dati no šiem ienākumiem, un šie dati tiek ierakstīti Excel failā lapā 'Incomes'. Ja ir dati par izmaksām (expenseItems), tad šie dati tiek ierakstīti Excel faila lapā 'Expenses'. Kā arī gan Incomes, gan Expenses lapās ir kolonna, kur ir saskaitīta kopējā ienākumu vai izmaksu summa.

### Frontend

Tā kā mūsu projekta galvenā ideja bija nodrošināt lietotājiem skaistu saskarni darbam ar Excel, vietnei bija jāatbilst mūsdienu dizaina un ātruma standartiem.

Mēs izmantojām React, lai izveidotu klienta pusi un pārvaldītu dažādas vietnes daļas kā komponentu. Turklāt nākotnē mēs varēsim ērti mainīt programmas izskatu, pateicoties tam, ka React komponentus var ērti atkārtoti izmantot, pārdalīt utt. React komponenti tika rakstīti TypeScript, lai piešķirtu tipus datiem, kas nāk no servera un tiek nosūtīti uz to. Pieprasījumus apstrādājām ar axios bibliotēkas palīdzību, jo mums jau bija pieredze ar to, skaistai vizualizācijai izmantojām chakra ui un bootstrap bibliotēkas.

### Start the project

Instalējiet atkarības:

Projekta front mapē palaidiet atkarību instalēšanas komandu:

npm install

Palaidiet React izstrādes serveri:

npm start

Tādējādi tiks palaists vietējais React izstrādes serveris, un jūs varēsiet apskatīt savu projektu pārlūkprogrammā http://localhost:3000.

Iestatiet un palaidiet Django lietojumprogrammu:

Pārliecinieties, ka jums ir instalēts Python un Django. Ja tā nav, instalējiet tos:

pip install django
Pārejiet uz mapi, kurā atrodas jūsu Django lietojumprogramma (backend).

Palaidiet migrāciju:

python manage.py migrate

Palaidiet Django serveri:

python manage.py runserver


### Paraugs

[![Dotajā video Jūs varat redzēt, kā strādā mūsu tīmekļa vietne](https://img.youtube.com/vi/2ctMnX51UTQ/0.jpg)](https://www.youtube.com/watch?v=2ctMnX51UTQ)

