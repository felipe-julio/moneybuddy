# Money Buddy

Web application that helps you see how you are spending your money. The front-end for this project is being developed in a separate [repository](https://github.com/samuelgrigolato/moneybuddy-front).

## Features

None, yet.

## Roadmap

* Account tree management.
* Manual transaction management.
* OFX import.
* Reports.
* Dashboard.
* Budget.

## Technologies

- Python
- Flask

## How to Develop

```
python -m venv <venv_dir>
source <venv_dir>/bin/activate
(venv_dir) pip install -r requirements.txt
(venv_dir) FLASK_ENV=development FLASK_APP=api flask run
```

Note that you can use whichever virtual environment tool you prefer, or even none at all (not recommended).

Although not being strictly necessary, you may find it useful to spawn a front-end development server as well, specially if you're developing an entire new feature. Refer to the [front-end repository](https://github.com/samuelgrigolato/moneybuddy-front) for details.

## How to Deploy

This project has everything needed to be deployed on Heroku (see the `Procfile`).

## Important Design Principles

* There should be support for multiple currencies, everywhere, with historical exchange rates.
* The application should try to be feature complete and easy to use at the same time, providing guidelines for people that don't have a clue on how to check where their money is going.

## Double-entry system

See the [Wikipedia entry](https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system) for details. This is the same system used by tools like GnuCash.

## Transaction

Each transaction has a collection of operations (usually two). Each operation has a value (can be positive or negative) and a target/source account. Any given transaction should have a balance of zero to be considered valid. Examples:

* Simple transaction with two operations:

|Op. #|Account|Amount|
|---|---|---|
|1|Expenses > Bakery|+50|
|2|Assets > Bank Account 1|-50|

* A little more complex transaction with multiple sources:

|Op. #|Account|Amount|
|---|---|---|
|1|Expenses > Entertainment|+100|
|2|Liabilities > Credit Card 1|-90|
|3|Assets > Wallet|-10|
