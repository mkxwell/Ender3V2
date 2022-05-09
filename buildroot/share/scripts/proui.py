# ------------------------------------------------------------------------------
# VSCode script for the Professional Firmware
# URL: https://github.com/mriscoc/Marlin_Ender3v2/releases
# Version: 1.2
# Date: 2022/04/30
# Author: Miguel Risco-Castillo
# ------------------------------------------------------------------------------

import shutil

libpath = "Marlin/lib/proui/"

Import("env")

print("Processing Professional Firmware requirements")

def _GetMarlinEnv(marlinEnv, feature):
    if not marlinEnv: return None
    return 1 if feature in marlinEnv else None

# Get Marlin evironment vars
MarlinEnv = env['MARLIN_FEATURES']
marlin_manualmesh = _GetMarlinEnv(MarlinEnv, 'MESH_BED_LEVELING')
marlin_abl = _GetMarlinEnv(MarlinEnv, 'AUTO_BED_LEVELING_BILINEAR')
marlin_ubl = _GetMarlinEnv(MarlinEnv, 'AUTO_BED_LEVELING_UBL')
stm32f1 = _GetMarlinEnv(MarlinEnv, 'MCU_STM32F103RC') or _GetMarlinEnv(MarlinEnv, 'MCU_STM32F103RE')
stm32f4 = _GetMarlinEnv(MarlinEnv, 'MCU_STM32F401RC') or _GetMarlinEnv(MarlinEnv, 'MCU_STM32F401RE')

if (stm32f1):
   arch = 'stm32f1/'
   print ('STM32F1 Architecture detected')
elif (stm32f4):
   arch = 'stm32f4/'
   print ('STM32F4 Architecture detected')
else:
   print("Error: can't detect the correct architecture")
   exit()

if (marlin_manualmesh):
   print("Manual Mesh Bed Leveling detected")
   shutil.copy(libpath+arch+'libproui_mbl.a', libpath+'libproui.a')

if(marlin_abl):
   print("Auto Mesh Bed Leveling detected")
   shutil.copy(libpath+arch+'libproui_abl.a', libpath+'libproui.a')

if(marlin_ubl):
   print("Unified Mesh Bed Leveling detected")
   shutil.copy(libpath+arch+'libproui_ubl.a', libpath+'libproui.a')

