#!/usr/bin/env python
#
#
"""
A hopefully simple CLI app for directly printing stuff to a FreeX
wifi printer.  This is for making labels used mostly on containers and
boxes to indicate what is in them (and to enumerate them)

NOTE: If the env. var "FREEX_PRINTER" is defined this script will
      attempting to connect to that address (at port 9100). This can
      be overriden by using the `--printer` option.

Usage:
    freex_cli.py [--printer=<printer>] <label text>

Options:
  --version
  -h, --help           Show this text and exit
  --printer=<printer>  The ip address or hostname for the FreeX label printer.
                       This will override the envvar "FREEZ_PRINTER"
"""
# system imports
#
import dataclasses


####################################################################
#
@dataclasses.dataclass
class Image:
    """
    A bitmap image where the data is already in the format to
    directly send to the FreeX printer (as TSPL)
    """
    width: int
    height: int
    data: bytes


####################################################################
#
def image2tspl(image, labelwidth_mm: int=100, labelheight_mm: int=150, dpi: float=203.2, ):
    """
    Convert the image into TSPL code (using the IMAGE operator)
    """
    labelwidth = int(round(labelwidth_mm / 25.4 * dpi))
    labelheight = int(round(labelheight_mm / 25.4 * dpi))
