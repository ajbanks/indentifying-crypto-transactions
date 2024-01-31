# indentifying-crypto-transactions

Bitcoin transactions can have multiple inputs and multiple outputs. It is common for Bitcoin
transactions to have one input and two outputs; one of the outputs is likely to be the
“change” amount that is returned to an address owned by the sender (example here:
ff411dc27ed066813beeba43c0d0c2a9f483c2db3db9570895fe8d6b1b4307d6). It is also
possible for a sender to contribute multiple inputs to a particular transaction (example here:
930513410594a0b1e0b2cd7403c7ab241e265ceb37b1e7d03e1105b106f826fb).

When trying to make Bitcoin funds hard to track, one method is to construct a transaction
with multiple other Bitcoin users. We are interested in identifying transactions created with
this intent.

These multi-party transactions are called CoinJoin transactions. They were first proposed by
Gregory Maxwell in a Bitcointalk forum post. In his own words: “When you want to make a
payment, find someone else who also wants to make a payment and make a joint payment
together”.

Here is an example of a potential 2-party Coinjoin transaction:
  ● c38aac9910f327700e0f199972eed8ea7c6b1920e965f9cb48a92973e7325046

There are several distinct implementations of the CoinJoin idea. A very early one that was
used was called Shared Coin.

The Dataset
Here you can download a file containing some stats on a sample of Bitcoin transactions from
the early days of bitcoin (2009) to 2016: dataset.tar.gz (398M / 112M compressed)

Data description:
  1. time_info.csv
  Id - just an id
  Time - unix timestamp in seconds
  2. tx_info.csv
  Id - just an id
  fee - fee that was offered to the miner (units: satoshis)
  inAds - number of addresses from which coins were spent (number of distinct input addresses)
  outAds - number of addresses this transaction spends to
  Invol - incoming volume to the TX (units: satoshis)
  outvol - volume spent in the TX (units: satoshis)

Explorations

    ● Can you think of a simple “heuristic” (two/three rules) that could be used to identify
    SharedCoin transactions?
    ● Can you implement the above rules (in Python preferably, but any language is ok) to
    filter the data down to a list of potential SharedCoin transactions?
    ● Again using code, can you plot the detected SharedCoin transactions over time?
    (The time_info.csv file will help).
    ● SharedCoin ceased to exist several years ago. Other implementations of CoinJoin
    transactions remain. Another implementation (let’s call it ‘Implementation XYZ’) has
    produced the below:
    c3fb2163c4768ac82ef8a16351610d0c52614d39d29d67dbb375fd1c23c8b305
    5b579ae5c2d4d559b2dc29d2b13fd25f81b9e3354529195857383b067e740a99
    3e426e2bacf76dbe4cab73036d80789138d4132094856f69e12a798afc77f13c
    From studying the above three transactions, can you write down some practical rules
    that could be used to detect further ‘Implementation XYZ’ transactions? (note: this
    type of transaction doesn’t appear in the dataset).
    ● Can you think of ways that ground truth / true positives / false positives can
    be evaluated for?
    Guidelines
    ● We expect this should take you around 2 hours. It is ok to submit partial answers,
    with the steps you would take to complete the answer. We are interested in how you
    chose to spend your time and what you would have done given more time.
    ● In the interests of time, focus on properties of single transactions, do not attempt
    graph related exploration.
    ● You may use any freely accessible tooling and any information on the web
