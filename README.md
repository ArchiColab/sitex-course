# SiteX Course

![SiteX banner](https://github.com/ArchiColab/sitex/blob/main/images/banner.png?raw=1)

Teaching notebooks for a site-analysis workshop in **data-scarce contexts**, for e.g.
secondary cities with no municipal GIS portal, no cadastral layer, no official DTM. The
notebooks use only open data and the [`sitex`](https://github.com/ArchiColab/sitex)
library. They were built for Pleiku, Gia Lai, Vietnam, and work for any geocodable place.

The library holds the code; this repository holds the notebooks that teach with it.

## Context of this work

These notebooks were developed by Chau Nguyen as part of the master's thesis *SITEX: An
AI-Assisted Notebook Library for Computational Site Analysis in Data-Scarce Contexts*, at
Metropolia University of Applied Sciences, in the Computing in Construction programme. The
thesis is a design-based research study in Vietnam. It asks how an AI-assisted,
notebook-based library can support architecture students and practitioners in
computational site analysis under data scarcity. Together with the `sitex` library, this
course is the artefact that the thesis designs, tests and evaluates.

### Development approach: AI-assisted, with a human in the loop

Agentic AI systems range from a chat assistant that answers one prompt at a time to
software in which a large language model is given a goal and tools (here: reading and
editing files, running Python and GIS code) and decides its own next steps. The
development of this library sits at the low-agency end of that range.

The AI tool used was Claude Code (Anthropic). The author defined the research questions,
the analytical methods and the data sources, reviewed and ran the AI's output, corrected
it, and decided what entered the notebooks. Claude was a tool in this process and is not
an author of the work. Responsibility for the code, methods and results rests with the
author. The thesis compares this human-in-the-loop way of working with agentic execution on
the same batch tests, and reports the method, its limits and its evaluation.

## How to run the notebooks: Google Colab

The notebooks are written for **[Google Colab](https://colab.research.google.com/)**. It
runs in the browser, so nothing needs to be installed and a laptop with limited computing
power is enough. You only need a Google account and about 1 GB of free space in Google Drive.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course)

1. **Open a notebook in Colab.** Click the *Open in Colab* badge next to it in the tables
   below.
2. **Copy the reference tables to your Google Drive** (see *Where the files are*), once.
3. **Run the first code cell.** It connects Google Drive (Colab asks for your permission)
   and installs the `sitex` library, which takes a couple of minutes. Then run the
   notebook from top to bottom.

## Where the files are: Colab and your own computer

The notebooks keep three kinds of files apart: the **notebooks** (this repository), the
**input data** (what they download, and the reference tables), and the **results**. The
data and the results are not part of this repository.

| Kind of file | In Google Drive (Colab) | On your computer | Content |
|---|---|---|---|
| Input data | `My Drive/Colab_Outputs/` | `data/` | What the acquisition notebooks download. Every notebook reads from here. |
| Reference tables | `My Drive/Colab_Outputs/reference/` | `data/reference/` | The Overture place classification files (`overture_place_classification.csv` and `.json`, `overture_category_crosswalk.csv`). The notebooks read them from the data folder. |
| Results | `My Drive/SiteX_Outputs/` | `outputs/` | What the notebooks produce: maps, GeoPackages, CAD files. |

**On your own computer** the notebooks detect that they are not in Colab and use the paths
`../data` and `../outputs`. These are relative to the folder that holds the notebook, so
`data/` and `outputs/` must sit **next to** the folder of this repository, not inside it:

```
my-project/
├── sitex-course/     this repository: notebooks, README, reference/
├── data/             input data, same subfolders as Colab_Outputs (dem, osm, overture, reference, ...)
└── outputs/          results
```

If a notebook cannot find a file, check that `data/` and `outputs/` are in the folder above
the notebooks. The repository also contains its own `reference/` folder with the same
tables and their edit history (`reference/history/`). That copy is the master version: copy
its files into `data/reference/` (or `Colab_Outputs/reference/`) when you set up your data,
because the notebooks do not read the repository copy.

For the conda environment, see the
[install instructions in the `sitex` repository](https://github.com/ArchiColab/sitex#install).

## Example places and data

Data acquisition has no sample data to copy. Everybody runs `00-Data-Acquisition` for an
**example place** (or for their own area) and builds their own `data/` folder. The only
files you need before you start are the **reference tables** (`reference/`, copied to
`data/reference/`, see above). All the open datasets are streamed or downloaded from their
providers when you run the notebook (streets from one Geofabrik country file of about 330 MB).

The example places are small wards with a compact street network, so that the street and
place steps run in about a minute (measured for these two steps only, in a test run on a
laptop; the imagery, terrain and building downloads were not timed):

| Place | OSM ID | Area | Streets | Places in Overture | Why this one |
|---|---|---|---|---|---|
| Phường Bình Quới, Ho Chi Minh City | `R19260957` | 6.4 km² | 125 km | about 1,000 | The smallest street network: a river peninsula with green and water. Few places are tagged in OSM, so Overture matters most here. |
| Lê Chân, Hải Phòng | `R19262156` | 5.6 km² | 312 km | about 5,700 | Dense, well-mapped ward: many places for the POI, Gehl and accessibility notebooks. |
| Phường Châu Đốc, An Giang | `R13836928` | 40.7 km² | 290 km | about 1,500 | Flat Mekong delta town, the place of the flood notebook. Long Xuyên (`R13566853`, 440 km of streets, about 4,500 places) is a larger alternative. |

Give the OSM ID as `PLACE` in Section 3 of `00-Data-Acquisition` (a name search can match
several boundaries). The choice is still open: these three were picked from a test on 38
Vietnamese places, and the full run of every notebook on them has not been done yet.
Pleiku, the case the notebooks were built on, works the same way but is a bigger and
sparser ward.

**What you need:**

1. `data/reference/`: the files from the `reference/` folder of this repository.
2. A free account on the [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)
   for the Sentinel-2 step (Section 5; the first run opens a browser tab for the login).
   All other sources need no account or key. Without Sentinel-2, the Urban Change Detection
   notebook cannot run.
3. About 1 GB of free space in Google Drive (Colab) or on your disk.

**The VIZ notebooks** (`04-VIZ-`) are optional samples and are not run in the workshop. They
read the results of the earlier notebooks, so for your own place they work after you have run
those. Set `PLACE` and `SLUG` at the top of each to the values you used in `00-Data-Acquisition`. If you only want to open them, a Pleiku data set can be provided: **[to be decided]**.
The data and the licences of the downloaded datasets are described under
[Data sources and licences](#data-sources-and-licences).

## The logic of the workshop

The notebooks follow one story: **model the form of the city, sense the environment, read
how the city is used, test on the ground, then design and test again.** The sensing and
reading phases produce predictions, the field trip checks them, and the design phase feeds
proposals back into the same tools.

| Phase | Question | Notebooks |
|---|---|---|
| **0. Acquire** | What data exists? | `00-Data-Acquisition` (building heights are its Section 12, switched off until you turn them on) |
| **1. Model the city** | What is its form? | Building Morphology → DEM Contour → Site 3D Model. You choose the 2 × 2 km site here and can come back to choose again. |
| **2. Sense the city** | What does the city look like from a satellite? | UHI, Urban Change *(field trip)*; Terrain and NDWI flood *(site risk, desk only)* |
| **3. Read the city** | How is it used and moved through? | **Space Syntax** (movement the model predicts) → **POIs / Gehl** (what life is actually there) → **Accessibility** (which services you can reach: NA03–NA05, green NA06) |
| **4. Test on the ground** | Was the model right? | The field trip. There is no notebook: the "check on the ground" sections of the notebooks become your worksheet. |
| **5. Understand → design** | What should change, and does it help? | Scenario tests: a new street (NA01), a new facility or street link (NA04, NA05). The VIZ notebooks produce the layouts. |

## How the files are named

Each file name starts with a number and a short code. The number gives the running order,
the code gives the theme.

| Prefix | Theme | Phase |
|---|---|---|
| `00-` | Data acquisition | 0. Acquire |
| `01-ARCH-` | Buildings and ground, city/ward scale | 1. Model the city |
| `01-SITE-` | The 2 × 2 km site, CAD/BIM export | 1. Model the city |
| `02-ENV-` | Environment from satellite and terrain data | 2. Sense the city |
| `03-NA01` … `03-NA06` | Network analysis: streets, places, accessibility | 3. Read the city |
| `04-VIZ-` | Visualization only, optional | 4. Design (layouts) |

```
sitex-course/
├── 00-Data-Acquisition.ipynb
├── 00-Data-Add_Missing_Streets.ipynb
├── 00- Overture - Activities Classifier.ipynb   (pre-workshop, not for participants)
├── 01-ARCH-Building_Morphology.ipynb
├── 01-ARCH-DEM_Contour.ipynb
├── 01-SITE-3D_Model.ipynb
├── 02-ENV-UHI_Analysis.ipynb
├── 02-ENV-Urban_Change_Detection.ipynb
├── 02-ENV-DEM_Terrain.ipynb
├── 02-ENV-Flood_Risk_NDWI.ipynb
├── 03-NA01-SpaceSyntax.ipynb
├── 03-NA01-SpaceSyntax_FieldTripIntro.ipynb
├── 03-NA02-POIs_Gehl.ipynb
├── 03-NA03-Amenity_Isochrones.ipynb
├── 03-NA04-Simple_Isochrone.ipynb
├── 03-NA05-Simple_Service_Area.ipynb
├── 03-NA06-Green_Accessibility.ipynb
├── 04-VIZ-Building_UHI_Overlays.ipynb
├── 04-VIZ-Interactive_Webmap.ipynb
├── 04-VIZ-POIsHeatmaps.ipynb
└── 04-VIZ-Workshop_3Layer_Diagram.ipynb
```

## Phase 0 — Acquire: what data exists?

Everybody runs this phase first, for an example place or their own area (see
[Example places and data](#example-places-and-data)). Every later notebook reads the files it
downloads into `Colab_Outputs`.

| Notebook | What it does | Main output | Colab |
|---|---|---|---|
| [`00-Data-Acquisition`](00-Data-Acquisition.ipynb) | Downloads the open datasets for the area of interest: terrain (GEDTM30), Sentinel-2 and Landsat 8/9 imagery, ESA WorldCover land cover, tree canopy height, OSM streets (Geofabrik extract), and Overture buildings, places, land use and water. Section 12 adds building heights from Google Open Buildings 2.5D Temporal and the Global Building Atlas; it is switched off until you set `RUN_BUILDING_HEIGHTS = True`, and Building Morphology needs its files. | The `Colab_Outputs` folder | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/00-Data-Acquisition.ipynb) |
| [`00-Data-Add_Missing_Streets`](00-Data-Add_Missing_Streets.ipynb) | Adds streets that are missing from OpenStreetMap, from a sketch you draw in QGIS. | Updated street network files | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/00-Data-Add_Missing_Streets.ipynb) |

**Pre-workshop only:** [`00- Overture - Activities Classifier`](00-%20Overture%20-%20Activities%20Classifier.ipynb)
prepares the classification lookup used by `03-NA02-POIs_Gehl`. Participants don't need to
run it: the finished lookup is part of the workshop data.

## Phase 1 — Model the city: what is its form?

Run in this order. The site is chosen in the last notebook, and you can come back to it
and choose again.

| Notebook | What it does | Main output | Colab |
|---|---|---|---|
| [`01-ARCH-Building_Morphology`](01-ARCH-Building_Morphology.ipynb) | Gives every building footprint one reconciled height, a function class (residential / mixed / industrial / civic) and its ground elevation. City/ward scale, LOD 200. | `buildings_enriched.gpkg` for QGIS | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/01-ARCH-Building_Morphology.ipynb) |
| [`01-ARCH-DEM_Contour`](01-ARCH-DEM_Contour.ipynb) | Turns the terrain model into contour lines. | Shapefile for QGIS, optional DXF for Rhino/Revit | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/01-ARCH-DEM_Contour.ipynb) |
| [`01-SITE-3D_Model`](01-SITE-3D_Model.ipynb) | **You choose the 2 × 2 km site here.** Clips the attributed buildings to the site and exports CAD/BIM-ready geometry: buildings, terrain, land cover, land use, water and contours. LOD 200. | DXF and OBJ files of the site | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/01-SITE-3D_Model.ipynb) |

## Phase 2 — Sense the city: what does it look like from a satellite?

Four independent notebooks. Two give predictions you check on the field trip; two are
desk-based site analysis.

| Notebook | The question | Use | Colab |
|---|---|---|---|
| [`02-ENV-UHI_Analysis`](02-ENV-UHI_Analysis.ipynb) | Which parts of the ward will be hardest to walk through at ten in the morning, and is it the asphalt or the missing trees? | Field trip | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/02-ENV-UHI_Analysis.ipynb) |
| [`02-ENV-Urban_Change_Detection`](02-ENV-Urban_Change_Detection.ipynb) | What has this place become, and what did it replace? | Field trip | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/02-ENV-Urban_Change_Detection.ipynb) |
| [`02-ENV-DEM_Terrain`](02-ENV-DEM_Terrain.ipynb) | Where would water go on this site? | Site risk, desk only | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/02-ENV-DEM_Terrain.ipynb) |
| [`02-ENV-Flood_Risk_NDWI`](02-ENV-Flood_Risk_NDWI.ipynb) | Which land goes under water every flood season, and what has been built on it? (Case study: Châu Đốc, Mekong Delta) | Site risk, desk only | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/02-ENV-Flood_Risk_NDWI.ipynb) |

## Phase 3 — Read the city: how is it used and moved through?

Run in this order. Space Syntax predicts movement from the street network alone, the POIs
show what life is actually there, and the accessibility notebooks measure which services
you can reach.

| Step | Notebook | The question | Colab |
|---|---|---|---|
| **Movement** | [`03-NA01-SpaceSyntax_FieldTripIntro`](03-NA01-SpaceSyntax_FieldTripIntro.ipynb) | A short introduction with three measures (Integration, Choice, Reach), and the field-trip assignment. Start here. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/03-NA01-SpaceSyntax_FieldTripIntro.ipynb) |
| | [`03-NA01-SpaceSyntax`](03-NA01-SpaceSyntax.ipynb) | The full method: how is every street connected to all the others, and what does that predict about movement and centrality? | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/03-NA01-SpaceSyntax.ipynb) |
| **Public life** | [`03-NA02-POIs_Gehl`](03-NA02-POIs_Gehl.ipynb) | Where does public life happen? Places sorted into necessary, optional and social activities (Gehl, 2010). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/03-NA02-POIs_Gehl.ipynb) |
| **Accessibility** | [`03-NA03-Amenity_Isochrones`](03-NA03-Amenity_Isochrones.ipynb) | From here, can you walk or cycle to the school, the health station and the market? (The 15-minute city.) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/03-NA03-Amenity_Isochrones.ipynb) |
| | [`03-NA04-Simple_Isochrone`](03-NA04-Simple_Isochrone.ipynb) | How far can people walk or cycle from one kind of facility? | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/03-NA04-Simple_Isochrone.ipynb) |
| | [`03-NA05-Simple_Service_Area`](03-NA05-Simple_Service_Area.ipynb) | Which school or health station is "yours", and how many homes does it serve? | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/03-NA05-Simple_Service_Area.ipynb) |
| **Green** | [`03-NA06-Green_Accessibility`](03-NA06-Green_Accessibility.ipynb) | Where can you sit under a tree within a short walk from home, and are you allowed to? | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/03-NA06-Green_Accessibility.ipynb) |

## Phase 4 — Test on the ground: was the model right?

This is the field trip. There is no notebook for it. The notebooks of phases 2 and 3 each
end with the same three parts, and together these are your worksheet:

1. **A check section** ("Field check" or "Reading the result for your site"): the pattern
   on the map, what the model predicts, what to check and survey on site, and an example
   record.
2. **When the model is wrong:** what it means when the street does not match the map.
3. **Where to go next:** the following notebook, and how the result feeds the design phase.

| Notebook | Check section |
|---|---|
| `02-ENV-UHI_Analysis` | 9. Field check: reading the heat on the ground |
| `02-ENV-Urban_Change_Detection` | 9. Field check: what replaced the green? |
| `03-NA01-SpaceSyntax_FieldTripIntro` | 7. Field-trip assignment |
| `03-NA02-POIs_Gehl` | 8. Field check: does the network predict the places? |
| `03-NA03-Amenity_Isochrones` | 7. Field check: a 15-minute neighbourhood? |
| `03-NA04-Simple_Isochrone` | 7. Discussion & field check: testing a proposal |
| `03-NA05-Simple_Service_Area` | 6. Field check: who comes, and how? |
| `03-NA06-Green_Accessibility` | 9. Field check: what is this green? |

`02-ENV-DEM_Terrain` (Section 6) and `02-ENV-Flood_Risk_NDWI` (Section 11) are read at the
desk, not on the field trip: "Reading the result for your site".

## Phase 5 — Understand → design: what should change, and does it help?

There are no new analysis notebooks in this phase. You go back to the notebooks of phase 3
and test a proposal against the situation today.

| Proposal | Where to test it |
|---|---|
| A new street | [`03-NA01-SpaceSyntax`](03-NA01-SpaceSyntax.ipynb), Sections 10–11: scenario testing and the impact map |
| A new facility or a new street link | [`03-NA04-Simple_Isochrone`](03-NA04-Simple_Isochrone.ipynb), Section 7 |
| A new service | [`03-NA05-Simple_Service_Area`](03-NA05-Simple_Service_Area.ipynb), Section 7 |

The `04-VIZ` notebooks produce the layouts. They are optional and do no analysis: they only
draw what the earlier notebooks have already calculated. You can make the same maps in QGIS,
which is usually more convenient for a layout.

| Notebook | What it draws | Colab |
|---|---|---|
| [`04-VIZ-Building_UHI_Overlays`](04-VIZ-Building_UHI_Overlays.ipynb) | Building outlines on top of the heat and change maps | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/04-VIZ-Building_UHI_Overlays.ipynb) |
| [`04-VIZ-Interactive_Webmap`](04-VIZ-Interactive_Webmap.ipynb) | The five heat and change maps as layers of one web map | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/04-VIZ-Interactive_Webmap.ipynb) |
| [`04-VIZ-POIsHeatmaps`](04-VIZ-POIsHeatmaps.ipynb) | Density heatmaps of the Gehl activities and of third spaces | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/04-VIZ-POIsHeatmaps.ipynb) |
| [`04-VIZ-Workshop_3Layer_Diagram`](04-VIZ-Workshop_3Layer_Diagram.ipynb) | Exploded data stacks next to the 3D site model | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ArchiColab/sitex-course/blob/main/04-VIZ-Workshop_3Layer_Diagram.ipynb) |

## Data sources and licences

The MIT licence of this repository covers the **notebooks only**. The notebooks download
open datasets at run time (OpenStreetMap, Overture Maps, Sentinel-2, Landsat, ESA
WorldCover, terrain models, building datasets), and each dataset keeps its own licence
and attribution rule. The
[table in the `sitex` README](https://github.com/ArchiColab/sitex#data-sources-and-licences)
lists them. Check the terms before you publish or reuse a result.

## Licence

Notebooks: MIT, see [LICENSE](LICENSE).

## Citation

If you use these notebooks, please cite the thesis they belong to:

> Nguyen, C. (2026). *SITEX: An AI-Assisted Notebook Library for Computational Site
> Analysis in Data-Scarce Contexts: A Design-Based Research Study in Vietnam*. Master's
> thesis, Metropolia University of Applied Sciences, Computing in Construction.

## References

Ho, Y.-F., Grohmann, C. H., Lindsay, J., Reuter, H. I., Parente, L., Witjes, M., & Hengl, T.
(2025). GEDTM30: Global ensemble digital terrain model at 30 m and derived multiscale
terrain variables. *PeerJ*, *13*, e19673. https://doi.org/10.7717/peerj.19673
