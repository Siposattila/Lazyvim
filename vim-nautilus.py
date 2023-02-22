# Nvim Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to nvim
NVIM = 'nvim'

# what name do you want to see in the context menu?
NVIMNAME = 'Nvim'

class VimExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_nvim(self, menu, files):
        safepaths = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

        call(NVIM + ' ' + safepaths, shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='NvimOpen',
            label='Open in ' + NVIMNAME,
            tip='Opens the selected files with Vim'
        )
        item.connect('activate', self.launch_nvim, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='NvimOpenBackground',
            label='Open in ' + NVIMNAME,
            tip='Opens the current directory in Nvim'
        )
        item.connect('activate', self.launch_nvim, [file_])

        return [item]

