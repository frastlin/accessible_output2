from builtins import str
import os
import platform

from accessible_output2.platform_utils import paths
from accessible_output2.libloader import load_library
from .base import Output

class NVDA(Output):
 """Supports The NVDA screen reader"""
 name = "NVDA"
 lib32 = 'nvdaControllerClient32.dll'
 lib64 = 'nvdaControllerClient64.dll'

 def is_active(self):
  try:
   return self.lib.nvdaController_testIfRunning() == 0
  except:
   return False

 def braille(self, text, **options):
  self.lib.nvdaController_brailleMessage(str(text))

 def speak(self, text, interrupt=False):
  if interrupt:
   self.silence()
  self.lib.nvdaController_speakText(str(text))

 def silence(self):
  self.lib.nvdaController_cancelSpeech()

output_class = NVDA
