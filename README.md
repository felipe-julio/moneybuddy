# Money Buddy

Web application that helps you see how you are spending your money.

## Features

None, yet.

## Roadmap

* Account tree management.
* Manual transaction management.
* OFX import.
* Reports.
* Dashboard.
* Budget.

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
