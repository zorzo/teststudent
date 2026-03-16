"""
Fáze 1: Základní informace o operačním systému
- Využívá pouze vestavěný modul 'platform'.
- Zjišťuje název OS, verzi a architekturu (bez nutnosti cokoliv instalovat).
"""
import platform

print("=== Fáze 1: Základní informace o OS a hardware ===")
print(f"Operační systém: {platform.system()} {platform.release()}")
print(f"Verze OS: {platform.version()}")
print(f"Architektura: {platform.machine()}")
print(f"Procesor (obecně): {platform.processor()}")

