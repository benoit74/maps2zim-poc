from zimscraperlib.zim import Creator
from pathlib import Path
from zimscraperlib.zim import metadata
from zimscraperlib.types import get_mime_for_name

OL_APP_DIST = Path("ol-app/dist")

creator = Creator(Path("tests_maps2zim_switzerland.zim"), "home").config_metadata(
    std_metadata=metadata.DEFAULT_DEV_ZIM_METADATA
)

creator.start()

creator.add_item_for("home", "Main Page", fpath=OL_APP_DIST / "index.html", mimetype="text/html", is_front=True )

for fpath in (OL_APP_DIST / "assets").glob("*"):
    creator.add_item_for(str(fpath.relative_to(OL_APP_DIST)), fpath=fpath, mimetype=get_mime_for_name(fpath))

creator.finish()