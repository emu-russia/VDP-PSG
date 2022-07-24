# VDP PSG

This is a small project to rebuild the VDP PSG circuit.

## History

Not so long ago we received a VDP of a Sega for analysis. The chip was damaged during the opening, but by some magical coincidence the broken off piece clearly contains the whole PSG. This is destiny!

![vdp-damaged-chip](/imgstore/vdp-damaged-chip.png)

## Introduction

Sega chips are basically designed with standard cell technology. 2 layers of metal. That is the typical approach of the mid-90s.

EDIT: VDP (and PSG) is built with CMOS technology, 1 layer of metal.

The project promises to be uncomplicated and interesting.

The broken off piece has already been photographed at 40x, the first thing to do is stitch the slides together:

![vdp-slides](/imgstore/vdp-slides.png)

And then the standard Workflow for learning about chips:
- Trace the wires
- Remove the top layers of metal
- Examine the standard cells that are found in this area of the chip
- Add cells and connect all ports
- Make a schematic in Logisim
- Examine the pins (bonus)

Note on the English version: the translation was done with the service [DeepL.com](http://DeepL.com), so it may seem awkward somewhere for native speakers. You are free to contribute your own edits to make it "human".
