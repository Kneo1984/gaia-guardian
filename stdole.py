# -*- coding: utf-8 -*-
from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    OLE_XPOS_CONTAINER, VgaColor, DISPPARAMS, IPicture, FontEvents,
    typelib_path, OLE_OPTEXCLUSIVE, OLE_YPOS_HIMETRIC,
    FONTSTRIKETHROUGH, OLE_YSIZE_PIXELS, IFontDisp, IFontEventsDisp,
    Unchecked, Checked, IPictureDisp, FONTUNDERSCORE,
    OLE_XSIZE_PIXELS, FONTITALIC, OLE_XSIZE_CONTAINER, IFont, StdFont,
    Picture, StdPicture, HRESULT, dispid, OLE_YPOS_CONTAINER,
    IUnknown, OLE_XSIZE_HIMETRIC, EXCEPINFO, Library, FONTBOLD,
    FONTNAME, OLE_COLOR, Gray, _check_version, Color, BSTR,
    OLE_CANCELBOOL, IDispatch, OLE_XPOS_HIMETRIC, DISPMETHOD, Font,
    CoClass, IEnumVARIANT, VARIANT_BOOL, OLE_YSIZE_HIMETRIC,
    OLE_XPOS_PIXELS, GUID, Monochrome, _lcid, FONTSIZE,
    OLE_ENABLEDEFAULTBOOL, OLE_HANDLE, COMMETHOD, DISPPROPERTY,
    OLE_YPOS_PIXELS, OLE_YSIZE_CONTAINER, Default
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'OLE_XPOS_CONTAINER', 'VgaColor', 'OLE_XSIZE_HIMETRIC',
    'IPicture', 'Library', 'FontEvents', 'FONTNAME', 'OLE_COLOR',
    'Gray', 'typelib_path', 'Color', 'OLE_OPTEXCLUSIVE',
    'OLE_CANCELBOOL', 'OLE_YPOS_HIMETRIC', 'FONTSTRIKETHROUGH',
    'OLE_YSIZE_PIXELS', 'OLE_XPOS_HIMETRIC', 'IFontDisp',
    'IFontEventsDisp', 'Unchecked', 'Font', 'Default', 'Checked',
    'IPictureDisp', 'OLE_YSIZE_HIMETRIC', 'OLE_XPOS_PIXELS',
    'Monochrome', 'FONTUNDERSCORE', 'FONTSIZE', 'FONTITALIC',
    'OLE_XSIZE_CONTAINER', 'OLE_XSIZE_PIXELS', 'IFont', 'StdFont',
    'OLE_ENABLEDEFAULTBOOL', 'Picture', 'OLE_HANDLE',
    'LoadPictureConstants', 'StdPicture', 'OLE_YPOS_PIXELS',
    'OLE_YSIZE_CONTAINER', 'FONTBOLD', 'OLE_TRISTATE',
    'OLE_YPOS_CONTAINER'
]

