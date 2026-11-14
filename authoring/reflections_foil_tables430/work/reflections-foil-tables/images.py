"""Fit a rotated original inside a200px set-table cell despite site image width rules."""
import math
def rotated(filename,title,alt,info):
    scale=info['width']/info['height'];height=math.ceil(200*scale)
    return f'<div style="position:relative;width:200px;height:{height}px;"><div style="position:absolute;left:0;top:0;width:200px;transform:translateY({height}px) rotate(-90deg) scale({scale:.8f});transform-origin:0 0;">[[File:{filename}|200px|link={title}|alt={alt}]]</div></div>'
