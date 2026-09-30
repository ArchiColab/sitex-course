#@title <font color=#1B7192> Draw the site (optional -- default 2x2km box shown in yellow) </font>  { display-mode: "form" }
import json
import uuid

from IPython.display import display

# --- default 2 x 2 km box around the site centre (SITE_CENTER_LAT / SITE_CENTER_LON) ---
from pyproj import Transformer

_zone = int((SITE_CENTER_LON + 180) // 6) + 1
_utm = f"EPSG:{(32600 if SITE_CENTER_LAT >= 0 else 32700) + _zone}"
_to_utm = Transformer.from_crs("EPSG:4326", _utm, always_xy=True)
_to_ll = Transformer.from_crs(_utm, "EPSG:4326", always_xy=True)
_x, _y = _to_utm.transform(SITE_CENTER_LON, SITE_CENTER_LAT)
_west, _south = _to_ll.transform(_x - 1000, _y - 1000)
_east, _north = _to_ll.transform(_x + 1000, _y + 1000)
_default_site_bbox = (_west, _south, _east, _north)

_HTML = r"""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.css"/>
<div id="__ID__status" style="font:14px sans-serif;margin:4px 0"><i>Click two opposite corners to draw a custom site. Yellow shows the default box, kept if you draw nothing.</i></div>
<div id="__ID__" style="height:480px;width:100%;cursor:crosshair"></div>
<script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
(function () {
  var cfg = __CONFIG__;
  var statusEl = document.getElementById("__ID__status");
  function report() {
    var args = Array.prototype.slice.call(arguments);
    try { google.colab.kernel.invokeFunction(cfg.callback, args, {}); }
    catch (err) { statusEl.innerHTML = "<b>Could not reach Python: " + err + "</b>"; }
  }
  var map = L.map("__ID__", {scrollWheelZoom: true}).setView(cfg.center, cfg.zoom);
  L.tileLayer(cfg.tiles, {attribution: cfg.attribution, maxZoom: 19}).addTo(map);
  var d = cfg.defaultBbox;
  L.rectangle([[d[1], d[0]], [d[3], d[2]]], {color: "#FFFF00", weight: 2, fillOpacity: 0.08}).addTo(map);
  var first = null, dots = [], preview = null, drawn = null;
  function clear() {
    dots.forEach(function (x) { map.removeLayer(x); }); dots = [];
    if (preview) { map.removeLayer(preview); preview = null; }
    if (drawn) { map.removeLayer(drawn); drawn = null; }
  }
  map.on("mousemove", function (e) {
    if (!first) return;
    var b = [[first.lat, first.lng], [e.latlng.lat, e.latlng.lng]];
    if (preview) preview.setBounds(b);
    else preview = L.rectangle(b, {color: "#6bc2e5", weight: 2, fillOpacity: 0.1}).addTo(map);
  });
  map.on("click", function (e) {
    if (!first) {
      clear();
      first = e.latlng;
      dots.push(L.circleMarker(first, {radius: 4, color: "red"}).addTo(map));
      report();
      statusEl.innerHTML = "<i>Click 1/2 - click the opposite corner</i>";
      return;
    }
    var a = first, b = e.latlng;
    first = null;
    clear();
    var w = Math.min(a.lng, b.lng), s = Math.min(a.lat, b.lat);
    var ee = Math.max(a.lng, b.lng), n = Math.max(a.lat, b.lat);
    drawn = L.rectangle([[s, w], [n, ee]], {color: "red", weight: 2, fillOpacity: 0.15}).addTo(map);
    report(w, s, ee, n);
    statusEl.innerHTML = "<i>Site drawn (" + w.toFixed(5) + ", " + s.toFixed(5) + ", " + ee.toFixed(5) + ", " + n.toFixed(5) + "). Click again to redraw, or run the next cell to confirm.</i>";
  });
})();
</script>
"""

_drawn = {"value": None}


def _on_draw(*args):
    _drawn["value"] = tuple(float(v) for v in args) if len(args) == 4 else None


class _SiteMap:
    """Read back by sitex.data.aoi.resolve_aoi_from_map in the next cell."""

    def __init__(self, html, drawn):
        self._html = html
        self._sitex_drawn_bbox = drawn

    def _repr_html_(self):
        return self._html


if IN_COLAB:
    # Colab does not reliably show ipyleaflet widgets, so the map is a plain Leaflet page
    # and the two clicks reach Python through Colab's own callback.
    from google.colab import output

    _uid = uuid.uuid4().hex[:8]
    _callback = f"site_draw_{_uid}"
    output.register_callback(_callback, _on_draw)
    _config = json.dumps({
        "callback": _callback,
        "center": [SITE_CENTER_LAT, SITE_CENTER_LON],
        "zoom": 16,
        "tiles": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        "attribution": "Tiles &copy; Esri",
        "defaultBbox": list(_default_site_bbox),
    })
    site_map = _SiteMap(_HTML.replace("__CONFIG__", _config).replace("__ID__", f"site_map_{_uid}"), _drawn)
else:
    site_map, _default_site_bbox = aoi_lib.build_aoi_map(SITE_CENTER_LAT, SITE_CENTER_LON, dist_m=1000, zoom=16)

print("Draw a rectangle over the exact site, or leave it and keep the default 2x2km "
      "box. Run the next cell to confirm.")

display(site_map)
