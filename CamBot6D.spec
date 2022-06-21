# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['CamBot6D.py'],
    pathex=[],
    binaries=[],
    datas=[('./images', 'images'),('./icons', 'icons'),('./fonts', 'fonts')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

splash = Splash('images/logo-01.png',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=(10,457),
                text_size=8,
                text_color='grey')

exe = EXE(
    pyz,
    a.scripts,
    splash,
    splash.binaries,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CamBot6D',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)

