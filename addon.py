import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "SNART ONLINE!"
line2 = "HD MUSIC"
line3 = "Darkzide inc!"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
