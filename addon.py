import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "SNART ONLINE!"
line2 = "HD MUSIC"
line3 = "Darkzide inc!"
swfUrl = "http://hdstream.one.by/jw/jwplayer.flash.swf" 
pageUrl = "http://hdstream.one.by"

xbmcgui.Dialog().ok(addonname, line1, line2, line3, pageUrl, swfUrl)
