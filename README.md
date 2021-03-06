# easytime

The simplest python time library ever written.


## Why a Time Library?

Handling times in python is painful. This library makes it not painful. That is
the reason.

I know there are plenty of ways to handle this sort of thing, but this is my
way, and I enjoy it.

Maybe you will too.


## Install

The simplest way to install `easytime` is via `pip`, the python package manager:

```bash
$ pip install easytime
```

If you'd like to upgrade `easytime` to the latest release, you can do so at any
time by running:

```bash
$ pip install -U easytime
```


## Usage

Using `easytime` is, well, ... *easy*. There are only a couple things you need
to know:

1. Always use UTC when handling time in your program. The best way to do this
   is via the `easytime.utcnow()` method, for instance:

   ```python
   >>> from easytime import easytime
   >>> now = easytime.utcnow()
   >>> now
   easytime(2012, 11, 18, 16, 53, 30, 316026)
   ```

2. **Only use timezones to display time data to users!** This means that you
   should keep your time in UTC always, until the very last second when you have
   to display time to your user. To do this, you can use the
   `easytime.convert()` method:

   ```python
   >>> from easytime import easytime
   >>> now = easytime.utcnow()
   >>> now
   easytime(2012, 11, 19, 0, 56, 30, 847490)
   >>> now.convert('America/Los_Angeles')   # Convert the time to LA time.
   datetime.datetime(2012, 11, 18, 16, 56, 30, 847490, tzinfo=<DstTzInfo 'America/Los_Angeles' PST-1 day, 16:00:00 STD>)
   >>> now.convert('Europe/Berlin') # Convert the time to Berlin time.
   datetime.datetime(2012, 11, 19, 1, 56, 30, 847490, tzinfo=<DstTzInfo 'Europe/Berlin' CET+1:00:00 STD>)
   ```

**If you follow the above two rules, you will no longer hate your life each
time you need to use timezones.**


## Details

`easytime` is really nothing more than a simple wrapper around python's built-in
`datetime.datetime` type. Every `easytime` object is a `datetime` object, with
two exceptions:

- You have access to a new method, `convert`, which allows you to specify a
    timezone (the full list is available here:
    http://en.wikipedia.org/wiki/List_of_tz_database_time_zones) to convert your
    datetime into. This is how you can display the time in different local
    timezones.

- You are forced to use UTC. Even if you try to generate a local time, eg:
  `datetime.datetime.now()`, you'll get back UTC, because `easytime` overrides
  it.

You can do anything with `easytime` that you can do with a normal
`datetime.datetime` object, so be sure to read the official [Python
datetime](http://docs.python.org/2/library/datetime.html) documentation if you
need to do anything more advanced.
