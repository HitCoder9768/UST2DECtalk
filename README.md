# UST2DECtalk
This project is a WIP / experiment. the calculation for note lengths is currently incorrect. Feel free to push any fixes and i will approve them upon inspection.

## Prerequisites
This script requires [pyUtau by UtaUtaUtau](https://github.com/UtaUtaUtau/pyUtau/blob/master/pyutau.py)

## Usage
pass a UST file as an argument to ust2dectalk.py. for example:
`python .\ust2dectalk.py 'h:\VocalSynth\VSQ-UST-ETCs\butterfly.ust'`
the ust should be formatted to use dectalk phonemes. Currently [R] (rest) notes are not automatically replaced with [_] so this will have to be done manually for now.

## Dectalk phonemes compared to arpasing
![Phonemes](https://cdn.discordapp.com/attachments/880307911585312779/885630527607046144/unknown.png)

## Known issues
- A singular [あ] note is parsed and added to the end of the outputted dectalk scripts, which has to currently be manually removed
- [R] (rest) notes are not currently converted to [_] for dectalk scripts