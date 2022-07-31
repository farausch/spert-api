# spert-api

The SpERT API receives text from German financial statements and returns financial entities, financial values and their relationship if they form a pair.

## Setup

This repository contains a Dockerfile for deploying the service. A ready-to-use deployment is also available (see example usage).

## Example Usage
`curl -G "https://spert-api-mtvfo2xgia-ey.a.run.app/fs-predict" --data-urlencode "text=Das Umlaufvermögen beläuft sich zum Ende des Geschäftsjahres auf TEUR 10000, wovon TEUR 255 auf Guthaben bei Kreditinstituten entfallen."`

## Acknowledgements

This repository is a fork of the original [SpERT repository](https://github.com/lavis-nlp/spert) extending it by a REST service.
