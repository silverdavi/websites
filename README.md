# Websites Workspace

Parent repository containing all website projects as submodules.

## Sites

| Site | URL | Repo |
|------|-----|------|
| dhsilver.me | https://dhsilver.me | [dhsilver-site](https://github.com/silverdavi/dhsilver-site) |
| embino.com | https://embino.com | [embino-site](https://github.com/silverdavi/embino-site) |
| kernel-keys.com | https://kernel-keys.com | [kernel-keys-site](https://github.com/silverdavi/kernel-keys-site) |
| unpop.info | https://unpop.info | [unpop-site](https://github.com/silverdavi/unpop-site) |
| vax.ninja | https://vax.ninja | [vax-ninja-site](https://github.com/silverdavi/vax-ninja-site) |
| freshsilver.net | https://freshsilver.net | [freshsilver-site](https://github.com/silverdavi/freshsilver-site) |
| theinvariant.org | https://theinvariant.org | [theinvariant-site](https://github.com/silverdavi/theinvariant-site) |

## Setup

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/silverdavi/websites.git
```

Or if already cloned:

```bash
git submodule update --init --recursive
```

## Working with Submodules

Each site is an independent git repo. Changes to a site:

```bash
cd dhsilver-site
# make changes
git add . && git commit -m "..."
git push origin main
```

Then update the parent to track the new commit:

```bash
cd ..
git add dhsilver-site
git commit -m "Update dhsilver-site submodule"
git push
```

## Shared Resources

The `shared/` folder contains:
- Design tokens and standards
- Data files (profile.json, etc.)
- Scripts and utilities

See `shared/STATUS.md` for full documentation.
