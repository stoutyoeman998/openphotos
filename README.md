# openphotos

A dead-simple command-line tool to download your full iCloud Photos library
to your computer. No flags to remember, no config files - just run it and
answer two questions.

It's a thin wrapper around the excellent
[icloudpd](https://github.com/icloud-photos-downloader/icloud_photos_downloader)
project, which does all the actual work of talking to iCloud.

## Install

```bash
pipx install git+https://github.com/stoutyoeman998/openphotos.git
```

(Don't have `pipx`? `sudo apt install pipx` on Debian/Ubuntu, then run
`pipx ensurepath` and open a new terminal. `pipx` is preferred over plain
`pip install` because it keeps the tool and its dependencies in their own
isolated environment, so it won't ever conflict with other Python projects
on your machine.)

Plain pip works too, if you'd rather:

```bash
pip install git+https://github.com/stoutyoeman998/openphotos.git
```

## Use

```bash
openphotos
```

You'll be asked for:

1. Your iCloud email
2. A folder name to save photos into (defaults to `icloud_photos` in your
   home directory)

Then it downloads your library. iCloud may ask for your password and a 2FA
code interactively - that's normal, and it's Apple's own login flow, not
anything openphotos stores or sees.

Run it again anytime - it skips photos it's already downloaded, so it
doubles as an easy way to keep a local backup up to date.


## A couple of notes

- This tool doesn't touch your Apple ID password - it's passed directly to
  Apple's own servers by `icloudpd`, the same way Apple's own apps do it.
- Downloaded originals are full resolution, regardless of your device's
  "Optimize Storage" setting - this is a benefit of going through iCloud
  directly rather than pulling photos off a phone over USB.

## License

MIT - do whatever you'd like with it.
