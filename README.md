# SiteX Course

![SiteX banner](https://github.com/ArchiColab/sitex/blob/main/images/banner.png?raw=1)

Teaching notebooks for a site-analysis workshop in **data-scarce contexts**, for e.g.
secondary cities with no municipal GIS portal, no cadastral layer, no official DTM. The
notebooks use only open data and the [`sitex`](https://github.com/ArchiColab/sitex)
library. They were built for Pleiku, Gia Lai, Vietnam, and work for any geocodable place.

The library holds the code; this repository holds the notebooks that teach with it.

## Context of this work

These notebooks were developed by Chau Nguyen as part of a master's thesis at Metropolia
University of Applied Sciences, in the Computing in Construction programme. Together with
the `sitex` library they form the experimental case of the thesis: an **agentic system
for spatial analysis**.

### Development approach: an agentic system with a human in the loop

In this thesis, an *agentic system* is a software system in which a large language model
is given a goal and a set of tools (here: reading and editing files, running Python and
GIS code) and decides its own next steps in a loop of acting, observing the result and
adjusting, instead of answering one prompt at a time.

The agent used here was Claude Code (Anthropic). It worked with a human in the loop: the
author defined the research questions, the workshop design, the analytical methods and
the data sources, reviewed and ran the agent's output, corrected it, and decided what
entered the notebooks. Claude was a tool in this process and is not an author of the work.
Responsibility for the code, methods and results rests with the author. The method, its
limits and its evaluation are reported in the thesis.

## Setup

The notebooks need the `sitex` library and a geospatial stack (GDAL, PROJ). Follow the
[install instructions in the `sitex` repository](https://github.com/ArchiColab/sitex#install),
which create a conda environment called `sitex`. Then:

```bash
git clone https://github.com/ArchiColab/sitex-course.git
cd sitex-course
conda activate sitex
jupyter lab
```

Run `00-Data-Acquisition` first. It downloads the data for your area of interest, and
every later notebook reads the files it saves.

## The logic of the workshop

The notebooks follow one story: **model the form of the city, sense the environment, read
how the city is used, test on the ground, then design and test again.** The sensing and
reading phases produce predictions, the field trip checks them, and the design phase feeds
proposals back into the same tools.

| Phase | Question | Notebooks |
|---|---|---|
| **0. Acquire** | What data exists? | `00-Data-Acquisition`, `00-Data-Acquisition_BuildingHeights` |
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
├── 00-Data-Acquisition_BuildingHeights.ipynb
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

Run these first. Every later notebook reads the files they download.

| Notebook | What it does | Main output |
|---|---|---|
| [`00-Data-Acquisition`](00-Data-Acquisition.ipynb) | Downloads the open datasets for the area of interest: terrain (NASADEM, AW3D30), Sentinel-2 and Landsat 8/9 imagery, ESA WorldCover land cover, tree canopy height, OSM streets, and Overture buildings, places, land use and water. | The `data/` folder |
| [`00-Data-Acquisition_BuildingHeights`](00-Data-Acquisition_BuildingHeights.ipynb) | Downloads building heights from Google Open Buildings 2.5D Temporal and the Global Building Atlas, for the same area. | Height data for Building Morphology |
| [`00-Data-Add_Missing_Streets`](00-Data-Add_Missing_Streets.ipynb) | Adds streets that are missing from OpenStreetMap, from a sketch you draw in QGIS. | Updated street network files |

**Pre-workshop only:** [`00- Overture - Activities Classifier`](00-%20Overture%20-%20Activities%20Classifier.ipynb)
prepares the classification lookup used by `03-NA02-POIs_Gehl`. Participants don't need to
run it: the finished lookup is part of the workshop data.

## Phase 1 — Model the city: what is its form?

Run in this order. The site is chosen in the last notebook, and you can come back to it
and choose again.

| Notebook | What it does | Main output |
|---|---|---|
| [`01-ARCH-Building_Morphology`](01-ARCH-Building_Morphology.ipynb) | Gives every building footprint one reconciled height, a function class (residential / mixed / industrial / civic) and its ground elevation. City/ward scale, LOD 100–200. | `buildings_enriched.gpkg` for QGIS |
| [`01-ARCH-DEM_Contour`](01-ARCH-DEM_Contour.ipynb) | Turns the terrain model into contour lines. | Shapefile for QGIS, optional DXF for Rhino/Revit |
| [`01-SITE-3D_Model`](01-SITE-3D_Model.ipynb) | **You choose the 2 × 2 km site here.** Clips the attributed buildings to the site and exports CAD/BIM-ready geometry: buildings, terrain, land cover, land use, water and contours. LOD 300+. | DXF and OBJ files of the site |

## Phase 2 — Sense the city: what does it look like from a satellite?

Four independent notebooks. Two give predictions you check on the field trip; two are
desk-based site analysis.

| Notebook | The question | Use |
|---|---|---|
| [`02-ENV-UHI_Analysis`](02-ENV-UHI_Analysis.ipynb) | Which parts of the ward will be hardest to walk through at ten in the morning, and is it the asphalt or the missing trees? | Field trip |
| [`02-ENV-Urban_Change_Detection`](02-ENV-Urban_Change_Detection.ipynb) | What has this place become, and what did it replace? | Field trip |
| [`02-ENV-DEM_Terrain`](02-ENV-DEM_Terrain.ipynb) | Where would water go on this site? | Site risk, desk only |
| [`02-ENV-Flood_Risk_NDWI`](02-ENV-Flood_Risk_NDWI.ipynb) | Which land goes under water every flood season, and what has been built on it? (Case study: Châu Đốc, Mekong Delta) | Site risk, desk only |

## Phase 3 — Read the city: how is it used and moved through?

Run in this order. Space Syntax predicts movement from the street network alone, the POIs
show what life is actually there, and the accessibility notebooks measure which services
you can reach.

| Step | Notebook | The question |
|---|---|---|
| **Movement** | [`03-NA01-SpaceSyntax_FieldTripIntro`](03-NA01-SpaceSyntax_FieldTripIntro.ipynb) | A short introduction with three measures (Integration, Choice, Reach), and the field-trip assignment. Start here. |
| | [`03-NA01-SpaceSyntax`](03-NA01-SpaceSyntax.ipynb) | The full method: how is every street connected to all the others, and what does that predict about movement and centrality? |
| **Public life** | [`03-NA02-POIs_Gehl`](03-NA02-POIs_Gehl.ipynb) | Where does public life happen? Places sorted into necessary, optional and social activities (Gehl, 2010). |
| **Accessibility** | [`03-NA03-Amenity_Isochrones`](03-NA03-Amenity_Isochrones.ipynb) | From here, can you walk or cycle to the school, the health station and the market? (The 15-minute city.) |
| | [`03-NA04-Simple_Isochrone`](03-NA04-Simple_Isochrone.ipynb) | How far can people walk or cycle from one kind of facility? |
| | [`03-NA05-Simple_Service_Area`](03-NA05-Simple_Service_Area.ipynb) | Which school or health station is "yours", and how many homes does it serve? |
| **Green** | [`03-NA06-Green_Accessibility`](03-NA06-Green_Accessibility.ipynb) | Where can you sit under a tree within a short walk from home, and are you allowed to? |

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

| Notebook | What it draws |
|---|---|
| [`04-VIZ-Building_UHI_Overlays`](04-VIZ-Building_UHI_Overlays.ipynb) | Building outlines on top of the heat and change maps |
| [`04-VIZ-Interactive_Webmap`](04-VIZ-Interactive_Webmap.ipynb) | The five heat and change maps as layers of one web map |
| [`04-VIZ-POIsHeatmaps`](04-VIZ-POIsHeatmaps.ipynb) | Density heatmaps of the Gehl activities and of third spaces |
| [`04-VIZ-Workshop_3Layer_Diagram`](04-VIZ-Workshop_3Layer_Diagram.ipynb) | Exploded data stacks next to the 3D site model |

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

> Nguyen, C. (2026). *[Thesis title]*. Master's thesis, Metropolia University of Applied
> Sciences, Computing in Construction.
