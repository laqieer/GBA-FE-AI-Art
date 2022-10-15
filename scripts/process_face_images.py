#!/usr/bin/env python

import os
import json
import numpy as np
from PIL import Image

with open('../../FE-Mod-Face-Search/refMap.json') as f:
    for v in json.load(f).values():
        for x in v:
            im = Image.open(os.path.join('../../FE-Mod-Face-Search', x))
            im = im.convert('RGBA')
            data = np.array(im)
            transparent = [0,0,0,0]
            backdrop = list(im.getpixel((0, 0)))
            if backdrop != transparent:
                # just use the rgb values for comparison
                rgb = data[:,:,:3]
                mask = np.all(rgb == backdrop[:3], axis = -1)
                data[mask] = transparent
            new_im = Image.new('RGBA', (128, 128), tuple(transparent))
            new_im.paste(Image.fromarray(data), (64 - im.width // 2, 128 - im.height))
            new_im.save(os.path.join('../datasets/portraits', os.path.basename(x)))
