# maps2zim-poc
PoC on having a ZIM with maps inside

## How it was built

Create a Node.JS Vite app with ol package:

```
npm create ol-app ol-app
```

Tweak few things:
- adjust CSS + HTML to display a title with the map
- adjust JS to load tiles locally instead of OSM online tile server
- adjust `vite.config.js` to specify base directory

## Python setup

Check python version (3.13 expected).

```bash
python --version
```

Create your venv and install requirements

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements
```

## Usage

Build Vite app:

```
cd ol-app
npm run build
cd ..
```

Create the ZIM

```bash
python create-zim.py
```