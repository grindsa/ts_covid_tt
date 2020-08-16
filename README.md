<!-- markdownlint-disable  MD013 -->
# ts_covid_tt

`ts_covid_tt` is a small python script which parses the [COVID19 - newsticker from Tagesspiegel](https://www.tagesspiegel.de/berlin/25605226.html) and

- puts the articles into a JSON file
- sends new articles via WhatsApp by using the `wa_hack` library

```bash
root@pdo:/usr/local/ts_covid_tt/data# head -n 50 tsbln.json
{
    "urn:newsml:localhost:2020-03-15T13:51:09.953087:b6cb97ac-18a3-486a-bf70-f09c09478536": {
        "headline": "Restauranteröffnung trotz Shutdown",
        "text": "Ungünstiger hätte der Termin kaum liegen können: Am Sonntagmittag um 12 Uhr hat Zihir Khan in Berlin-Moabit sein Restaurant Ajwa eröffnet, berichtet unsere Autorin Ingrid Müller. Pakistanische und indische Spezialitäten will der Mann anbieten, der aus Gujarat in Pakistan stammt. Doch erst einmal sitzt der 35-Jährige allein mit zwei Bekannten im Lokal. „Ich muss wenigstens einmal aufmachen”, sagt Khan. Schließlich habe er das auf die Flyer geschrieben, die er überall im Viertel verteilt hat. Wie es in den nächsten Tagen sein wird? Er weiß es nicht. „Ich glaube nicht, dass in Berlin die Geschäfte zu bleiben.” Er sagt aber auch: „Ich glaube nicht, dass heute jemand kommt.” Dann wird er den Tag mit ein paar Freunden feiern. Heute hat er sich nach 21 Jahren als Kellner in Berlin selbständig gemacht."
    },
    "urn:newsml:localhost:2020-03-15T13:40:48.859080:6b06f65d-72b2-4070-ae24-475caefcd953": {
        "headline": "Sonntagmittag und keine Schlange vor dem Berghain",
        "text": "Ausnahmsweise keinerlei Schlange, nur ein paar Dealer streifen umher, das beobachtet unsere Autorin Julia Prosinger. Eine junge Frau lässt sich vor dem verrammelten Gebäude fotografieren und sagt zu ihrem Freund: \"Ausgerechnet wenn ich ein einziges Mal ausgehen will, hat es zu\". Ein anderer Feierwilliger hat sich mit einer Bluethoothbox auf einem Stein aufgebaut und tanzt allein in der Sonne."
    },
    "urn:newsml:localhost:2020-03-15T13:04:51.828260:2f0ffc7c-fcf0-41ee-b839-6685563efe71": {
        "headline": "Falschmeldungen über Supermarkt-Schließungen",
        "text": " In den Sozialen Medien kursieren derzeit Falschmeldungen, dass die Lebensmittelläden ab Montag geschlossen seien. Über die Messengerdienste Whatsapp und Telegram werden Nachrichten verschickt, dass große Supermarktketten wie Rewe oder Edeka ab Montag schließen oder nur noch zwei Stunden pro Tag geöffnet haben sollen. Derzeit gibt es keine Hinweise auf eine solche Maßnahme. Auch in Italien und Österreich sind die Supermärkte noch geöffnet. Hier wurde lediglich der Zugang zu den Geschäften eingeschränkt, damit sich nicht zu viele Menschen auf einmal im Markt aufhalten."
    },
    "urn:newsml:localhost:2020-03-15T13:03:32.451903:6367f753-55e6-495b-9308-32b2cd0fe9e2": {
        "headline": "So gehen Berliner Cafés mit der Abstandsregel um",
        "text": null
    },
    "urn:newsml:localhost:2020-03-15T12:49:56.342318:c4cda934-4f8f-4cbd-880d-0dd3f83fe594": {
        "headline": "Zehlendorf-Mitte sorgt vor, Friedenau bleibt gelassen",
        "text": "Unsere Kollegin Heike Jahberg war heute in zwei Bäckereien und meldet: \"In Zehlendorf-Mitte ist Brot ausverkauft.\" Nur Brötchen seien noch zu bekommen. Beide Filialen hätten sonntags normalerweise so viel Brot, dass es bis nachmittags hält - nicht jede Sorte, aber irgendwas ist immer da. Die Gründe können vielfältig sein, womöglich sorgen Leute vor oder haben auch einfach einen größeren Bedarf, wenn sie nun mehr zu Hause sind. Ein anderes Bild in Friedenau, von dort schreibt unser Kollege Ingo Bach: \"War alles da wie immer. Kuchen, Brötchen, Brot.\" So oder so - wir wünschen guten Appetit. Und Gelassenheit."
    },
    "urn:newsml:localhost:2020-03-15T11:38:27.343481:4b32ba34-e8e2-44ee-8c92-ae28f8ca0102": {
        "headline": "Hier noch mal die Überlegungen zu den Folgen der Senatsverordnung für den Fußball aus dem Blog von gestern Abend als eigener Artikel.",
        "text": null
    },
    "urn:newsml:localhost:2020-03-15T11:23:27.645333:af19f7ce-b3a3-47c4-88d0-c7d295643089": {
        "headline": "Wenn das Nachtleben endet: Streifzüge am Samstagabend",
        "text": "Das Ende kam plötzlich: Am späten Samstagnachmittag verkündete der Berliner Senat die vorgezogene Schließung von Clubs, Bars und Kneipen - nicht erst ab Dienstag, sondern ab sofort, unverzüglich, bereits ab Samstag. Einige Läden hatten schon in den Tagen zuvor von sich aus den Betrieb eingestellt, für die anderen kam die Anordnung dann schneller als gedacht. Und schneller, als sie davon erfahren konnten. Die Polizei war am Abend mit zwei Hundertschaften und weiteren zivilen Beamten im Einsatz, um die Schließung durchzusetzen - nicht brachial, sondern im Gespräch. Und sie berichtete auch von verständnisvollen Reaktionen. Hier ein paar Eindrücke von Tagesspiegel-Kolleg*innen."
    }
```

## License

This project is licensed under the GPLv3 - see the [LICENSE.md](https://github.com/grindsa/ts_covid_tt/blob/master/LICENSE) file for details
